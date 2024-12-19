from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Ticket
from .extentions import db

app_routes = Blueprint('routes', __name__)

@app_routes.route('/')
def index():
    # Fetch tickets grouped by status
    to_do_tickets = Ticket.query.filter_by(status='To Do').all()
    in_progress_tickets = Ticket.query.filter_by(status='In Progress').all()
    done_tickets = Ticket.query.filter_by(status='Done').all()

    # Pass tickets to the template
    return render_template(
        'kanban_board.html',
        to_do_tickets=to_do_tickets,
        in_progress_tickets=in_progress_tickets,
        done_tickets=done_tickets
    )

@app_routes.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.dashboard'))  # Redirect if already logged in

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query user by username
        user = User.query.filter_by(username=username).first()

        # Check if user exists and password is correct
        if user and user.check_password(password):
            login_user(user)  # Log the user in
            flash('You are now logged in.', 'success')  # Success message
            return redirect(url_for('routes.dashboard'))

        flash('Invalid username or password.', 'danger')  # Error message if login fails

    return render_template('login.html')

@app_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different username.', 'danger')
            return redirect(url_for('routes.register'))

        # Create the new user
        user = User(username=username, role=role)
        user.set_password(password)  # Hash the password before storing

        # Add the user to the database
        db.session.add(user)
        db.session.commit()

        flash('Account successfully created! You can now log in.', 'success')
        return redirect(url_for('routes.login'))  # Redirect to login page after successful registration

    return render_template('register.html')

@app_routes.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'manager': # Check the role of the current user
        tickets = Ticket.query.all()
        return render_template('manager_dashboard.html', tickets=tickets)
    elif current_user.role == 'employee':
        tickets = Ticket.query.filter_by(assigned_to=current_user.id).all()
        return render_template('employee_dashboard.html', tickets=tickets)

@app_routes.route('/tickets/<int:id>/details')
@login_required
def ticket_details(id):
    ticket = Ticket.query.get(id)
    return render_template('ticket_details.html', ticket=ticket) # Redirect to the details view and pass the selected ticket from ID

@app_routes.route('/tickets/create', methods = ['GET', 'POST'])
@login_required
def create_ticket():
    # Post for the form submission in the ticket form view
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        type_of_ticket = request.form['type_of_ticket']
        start_date_str = request.form['start_date']
        end_date_str = request.form['end_date']
        status = request.form['status']
        priority_level = request.form['priority_level']

        # change data type back to python data for SQLALchemy
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

        ticket = Ticket(title=title, description=description, type_of_ticket=type_of_ticket, start_date=start_date, end_date=end_date,
                        status=status, priority_level=priority_level)

        # Add the ticket to the database
        db.session.add(ticket)
        db.session.commit()
        return redirect(url_for('routes.dashboard'))

    return render_template('tickets_form.html')

@app_routes.route('/tickets/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_ticket(id):
    # Retrieve the ticket by ID
    ticket = Ticket.query.get(id)

    # Ensure only managers can access this route
    if current_user.role != 'manager':
        flash("You do not have permission to edit tickets.", "danger")
        return redirect(url_for('routes.ticket_details', id=id))

    if request.method == 'POST':
        # Get updated data from the form
        ticket.title = request.form.get('title')
        ticket.description = request.form.get('description')
        ticket.type_of_ticket = request.form.get('type_of_ticket')
        ticket.priority_level = request.form.get('priority_level')
        ticket.start_date = request.form.get('start_date')
        ticket.end_date = request.form.get('end_date')
        ticket.status = request.form.get('status')
        ticket.assigned_to = request.form.get('assigned_to') or None

        # Commit the changes to the database
        db.session.commit()
        flash("Ticket updated successfully.", "success")
        return redirect(url_for('routes.ticket_details', id=ticket.id))

    # Render the edit form with the current ticket details
    return render_template('edit_ticket.html', ticket=ticket)

@app_routes.route('/tickets/<int:id>/update', methods = ['POST'])
@login_required
def update_ticket(id):
    # Retrieve the ticket by ID
    ticket = Ticket.query.get(id)

    # Employees can only update tickets assigned to them
    if not ticket or (current_user.role == 'employee' and ticket.assigned_to != current_user.id):
        flash('You are not allowed to update tickets', 'danger')
        return redirect(url_for('routes.dashboard'))

    ticket.status = request.form['status']
    db.session.commit()
    return redirect(url_for('routes.dashboard'))

@app_routes.route('/tickets/<int:id>/assign', methods = ['POST'])
@login_required
def assign_ticket(id):
    # Retrieve the ticket by ID
    ticket = Ticket.query.get(id)

    ticket.assigned_to = current_user.id
    db.session.commit()
    return redirect(url_for('routes.ticket_details', id=id))

@app_routes.route('/tickets/<int:id>/delete', methods = ['POST'])
@login_required
def delete_ticket(id):
    if current_user.role == 'employee':
        flash('You are not allowed to delete tickets', 'danger')
        return redirect(url_for('routes.index'))

    ticket = Ticket.query.get(id)
    db.session.delete(ticket)
    db.session.commit()
    return redirect(url_for('routes.dashboard'))

@app_routes.route('/retrieve_users')
@login_required
def retrieve_users():
    if current_user.role == 'manager': # Check the role of the current user
        users = User.query.all()
        return render_template('user_management.html', users=users)

@app_routes.route('/users/<int:id>/delete', methods = ['POST'])
@login_required
def delete_user(id):

    # Retrieve user by ID, delete, then commit changes to the database
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return render_template('user_management.html')

@app_routes.route('/user/<int:id>/update', methods = ['POST'])
@login_required
def update_user_role(id):
    # Retrieve the user by ID
    user = User.query.get(id)

    user.role = request.form['role']
    db.session.commit()
    return redirect(url_for('routes.dashboard'))

@app_routes.route('/user/<int:id>/details')
@login_required
def account_details(id):
    user = User.query.get(id)
    return render_template('account.html', user=user)

@app_routes.route('/account')
@login_required
def account():
    user = User.query.get(current_user.id)
    return render_template('account.html', user=user)

@app_routes.route('/reset/password/<int:id>', methods=['GET', 'POST'])
@login_required
def reset_password(id):
    # Retrieve the user by ID
    user = User.query.get(id)

    if request.method == 'POST':
        # Get updated data from the form
        user.password = request.form.get('password')

        # Commit the changes to the database
        db.session.commit()
        flash("Password reset successfully.", "success")
        return redirect(url_for('routes.account', id=user.id))


    return render_template('reset_password.html', user=user)

@app_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.login'))