# SCRUM TEAM DEVELOPMENT TICKET TRACKING APPLICATION

This website tracks a list of tickets within a sprint to enable scrum teams to track and manage their workload within a
dedicated sprint. Furthermore, the kanban board clearly highlights the priority and urgency and tracks their progress to
completion.

# PROJECT DESCRIPTION
The scrum team development ticket tracking application is a platform which has been created for the My Aviva hub scrum
web development teams. Through the use of the website, scrum teams will be able to track the development progress of
tickets through a Kanban board as well as identify the priority of each ticket. As a result, the website can be used to
streamline daily scrum huddles as tickets can be assigned to team members, providing a visual aid to the team when
discussing progress.

Anyone is able to view the Kanban board, but, you need to be logged in as either a manager or an employee to see the full
details of the ticket. This can be done through the login page, which is also where new employees or managers can register
an account. A user can see the full ticket details through clicking on the title of the ticket. When looking at the ticket
details employees can assign the ticket to them, but they are not able to edit the details of the ticket or delete the
ticket like a manager (admin) can.

An employee (user) and manger (admin) have their own dashboards, where employees can see the tickets assigned to them.
They are then able to update the current status of the ticket, they are also able to view the full details of the
ticket through clicking on the title of the ticket in the table. Furthermore, there is also a button at the bottom of
the page that allows employees to create a new ticket. On the manager dashboard, the managers (admins) can view all
the tickets in the current sprint (database). However, managers have the privilege to delete tickets from the dashboard
or when view the full details of the ticket. When managers view the full details of the ticket they will be able to edit
all teh details of an existing ticket, allowing them to perform CRUD (Create, Read, Update, Delete) operations to the ticket
database. All users are able to view their account and edit their username and password.


# TECHNOLOGIES USED
- Flask
- SQLAlchemy
- Bootstrap (as well as custom css)
- Jinja2
- JavaScript
- Dependencies can be found in requirements.txt
- Production database - postgres

# SCOPE OF THE APPLICATION 

# PROMBLEM STATEMENT 
Scrum team within the My Aviva hub function need a reliable platform to track sprint tickets on a Kanban board. This aims to increase the efficency of tracking tickets, to ensure they are completed within the sprint. The iniative came from higher management within Aviva as the end of year reports identified that there has been high carry over of tickets from sprint to sprint, leading to a decrease in sprint volocity. The new scrum team developement ticket tracking applicaiton will provide scrum masters (manager/admins) with a portal to view how the current tickets are progressing. Furthermore, it provides developers (user/employees) with the technology to pick up tickets, tasks, or bugs that have not yet been assigned, resulting in greater efficeny as they is not a wait for scrum huddle calls. The web applicaiton also provides a visual aid within scrum huddle calls, ensuring everyone within the team is aware of the current sprint progress. As a result, it highlight the risk of which tickets may not make sprint cut, providing easy communication with stakeholders such as product owners. Furhtermore, with all team members being able to view sprint work, developers are able to understand the full requirements of a ticket. This results in easy collaboration as developers are able to co-develope on a ticket with another developer as they are able to view the ticket details and requirements, leading to a reduction in loss of communication and production bugs. 

# GOALS OF PROJECT 
- reduce amount of bug in production at the end of a 2 week sprint cycle
- reduce the number of tickets that are carried over from one sprint to the next at the end of a 2 week cycle
- reduce scrum huddle calls to the appropriate 15 minuets after using the new web applicaiton for 2 sprints
- see an increase of the customer satifaction score by 0.1% after using the web applicaiton for a fiscal quater

  # KEY FEATURES
- User login, logout, and register: users can securely log in and register an account.

- Account management: users are able to edit their username and password.

- Manager controls: managers are able to preform CRUD operations on both the tickets and users. this means they are able to edit all the deatils of tickets, delete tickets, update status of tickets, and view all the tickets in a sprint. They are also able to add users, delete users, update user roles, and view all the users that are using the web applicaiton. 

- Update the status of tickets: employees are able to update the status of tickets that are assigned to them, resulting
in them moving columns on the kanban board.

- Employee controls: employees are able to create new tickets, assign ticket to them, and update the status of tickets allowing them to move across the board. employees are also able to reset their password with a new password and register a new user.

- Simple navigation: users are able to simply navigate through to different pages through the user of the navigation bar
and buttons on pages.

- Validation: the website uses a combination of flash notification and JavaScript the validate user inputs.

# INSTALLATION STEPS
When running the applciaiton locally, in the config.py file uncomment line 8 and comment out line 5. Once you have followed the steps below, you should be able to run the applicaiton locally and access it in your web browser at http://localhost:5000 or http://127.0.0.1:5000

1. Clone the repository:
   
       git clone https://github.com/abxrd/Software-engineering-project-1.git cd your-repo
   
2. Create virtual environment:
   
       python -m venv venv
   
3. Activate virtual environment:

       env\Scripts\activate

4. Install dependencies:

       pip install -r requirements.txt

# USER LOGIN 
There are 3 users already set up for log in, two employees and one manager:

Manager:
- Username: manager1
- Password: MangerPassword!

Employee one:
- Username: employee1
- Password: PasswordEmployee!

Employee two:
- Username: employee2
- Password: EmployeePassword!

# CODE REFRENCES AND LEARNINGS 
- [GeeksforGeeks Flask App Routing](https://www.geeksforgeeks.org/flask-app-routing/)
- [GeeksforGeeks Flask - Message Flashing](https://www.geeksforgeeks.org/flask-message-flashing/)
- [PythonProgramming.net - Password Hashing with Flask Tutorial](https://pythonprogramming.net/password-hashing-flask-tutorial/)
- [w3schools - JavaScript Forms](https://www.w3schools.com/js/js_validation.asp)
- [Deploying Application to Vercel](https://www.youtube.com/watch?v=sbnU0VRRUqg)
