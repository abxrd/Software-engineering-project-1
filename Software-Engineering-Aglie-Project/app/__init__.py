from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from .models import User, Ticket
from .extentions import db, bcrypt
from datetime import date

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'
    app.config.from_object('Config')

    login_manager.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager.login_view = 'routes.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes import app_routes
    app.register_blueprint(app_routes)

    with app.app_context():
        db.create_all()
        seed_data()


    return app

def seed_data():
    if not User.query.first():
        manager = User(id=1, username="manager1", role="manager")
        manager.set_password("MangerPassword!")
        employee_one = User(id=2, username="employee1", role="employee")
        employee_one.set_password("PasswordEmployee!")
        employee_two = User(id=3, username="employee2", role="employee")
        employee_two.set_password("EmployeePassword!")

        db.session.add(manager)
        db.session.add(employee_one)
        db.session.add(employee_two)

        db.session.commit()

    if not Ticket.query.first():
        ticket1 = Ticket(
            id=1,
            title="Fix logout",
            type_of_ticket="Bug",
            priority_level="Medium",
            start_date=date(2024, 12, 18),
            end_date=date(2025, 1, 18),
            status="Done",
            description="Users are unable to logout of the session, when to logout button is selected.",
            assigned_to='2'
        )

        ticket2 = Ticket(
            id=2,
            title="Fix login",
            type_of_ticket="Bug",
            priority_level="High",
            start_date=date(2024, 12, 17),
            end_date=date(2025, 1, 18),
            status="In Progress",
            description="Users are unable to login of the session, when to login button is selected.",
            assigned_to='3'
        )

        ticket3 = Ticket(
            id=3,
            title="Investigate manager ticket creation",
            type_of_ticket="Task",
            priority_level="Low",
            start_date=date(2024, 12, 15),
            end_date=date(2025, 1, 16),
            status="To Do",
            description="Investigate how the manager role will be able to create tickets.",
            assigned_to='3'
        )

        ticket4 = Ticket(
            id=4,
            title="Create navigation bar",
            type_of_ticket="Story",
            priority_level="Medium",
            start_date=date(2024, 12, 10),
            end_date=date(2024, 12, 30),
            status="Done",
            description="Create the navigation bar so users are able to navigate around the application.",
            assigned_to='2'
        )

        ticket5 = Ticket(
            id=5,
            title="Fix employee role",
            type_of_ticket="Bug",
            priority_level="Medium",
            start_date=date(2024, 10, 18),
            end_date=date(2025, 1, 10),
            status="In Progress",
            description="Make the correct role assignment to tasks, tickets, and bugs.",
            assigned_to='2'
        )

        ticket6 = Ticket(
            id=6,
            title="Create user registration",
            type_of_ticket="Story",
            priority_level="High",
            start_date=date(2024, 12, 18),
            end_date=date(2025, 1, 18),
            status="In Progress",
            description="Create functionality to allow new user to register.",
            assigned_to='3'
        )

        ticket7 = Ticket(
            id=7,
            title="Employee dashboard formatting",
            type_of_ticket="Task",
            priority_level="Low",
            start_date=date(2024, 12, 1),
            end_date=date(2025, 1, 16),
            status="To Do",
            description="Investigate the different ways of formatting the employee dashboard.",
            assigned_to='2'
        )

        ticket8 = Ticket(
            id=8,
            title="Set-up locally debugging",
            type_of_ticket="Story",
            priority_level="High",
            start_date=date(2024, 9, 18),
            end_date=date(2024, 11, 18),
            status="To Do",
            description="Create a development environment to test new project.",
            assigned_to='2'
        )

        ticket9 = Ticket(
            id=9,
            title="Fix database seeding",
            type_of_ticket="Bug",
            priority_level="High",
            start_date=date(2024, 11, 18),
            end_date=date(2025, 1, 18),
            status="Done",
            description="The database does not currently seed data, this needs to be fixed so tickets can be tracked.",
            assigned_to='3'
        )

        ticket10 = Ticket(
            id=10,
            title="Set-up production environment for the application.",
            type_of_ticket="Task",
            priority_level="Low",
            start_date=date(2024, 12, 18),
            end_date=date(2025, 1, 18),
            status="In Progress",
            description="Investigate how the new application will be hosted in a production environment.",
            assigned_to='3'
        )

        db.session.add(ticket1)
        db.session.add(ticket2)
        db.session.add(ticket3)
        db.session.add(ticket4)
        db.session.add(ticket5)
        db.session.add(ticket6)
        db.session.add(ticket7)
        db.session.add(ticket8)
        db.session.add(ticket9)
        db.session.add(ticket10)
        db.session.commit()