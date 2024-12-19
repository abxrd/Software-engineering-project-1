*SCRUM TEAM DEVELOPMENT TICKET TRACKING APPLICATION*

This website tracks a list of tickets within a sprint to enable scrum teams to track and manage their workload within a
dedicated sprint. Furthermore, the kanban board clearly highlights the priority and urgency and tracks their progress to
completion.

*PROJECT DESCRIPTION*
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

*KEY FEATURES*
- User login, logout, and register: users can securely log in and register an account.

- Account management: users are able to edit their username and password.

- Manager controls: managers are able to preform CRUD operations on both the tickets and users.

- Update the status of tickets: employees are able to update the status of tickets that are assigned to them, resulting
in them moving columns on the kanban board.

- Simple navigation: users are able to simply navigate through to different pages through the user of the navigation bar
and buttons on pages.

- Validation: the website uses a combination of flash notification and JavaScript the validate user inputs.


*TECHNOLOGIES USED*
- Flask
- SQLAlchemy
- Bootstrap (as well as custom css)
- Jinja2
- JavaScript
- Dependencies can be found in requirements.txt

*

