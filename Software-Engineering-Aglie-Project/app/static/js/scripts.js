// Validate the task creation form
function validateTaskForm() {
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;

    if (!title.trim()) {
        alert('Ticket title is required.');
        return false;
    }

    if (title.length > 100) {
        alert('Ticket title cannot exceed 100 characters.');
        return false;
    }

    if (description.length > 500) {
        alert('Description cannot exceed 500 characters.');
        return false;
    }

    return true;
}

// Validate the registration form
function validateRegistrationForm() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    const specialCharacterRegex = /[!@#$%^&*(),.?":{}|<>]/;
    const uppercaseLetterRegex = /[A-Z]/;

    if (!username.trim()) {
        alert('Username is required.');
        return false;
    }

    if (username.length > 50) {
        alert('Username cannot exceed 50 characters.');
        return false;
    }

    if (!password.trim()) {
        alert('Password is required.');
        return false;
    }

    if (!specialCharacterRegex.test(password)) {
        alert('Password must contain at least one special character.');
        return false;
    }

    if (!uppercaseLetterRegex.test(password)) {
        alert('Password must contain at least one uppercase letter.');
        return false;
    }

    if (password.length < 8) {
        alert('Password must be at least 8 characters long.');
        return false;
    }

    if (password !== confirmPassword) {
        alert('Passwords do not match.');
        return false;
    }

    return true;
}

// Delete confirmation for tasks
function confirmDelete(ticketId) {
    if (confirm('Are you sure you want to delete this ticket?')) {
        document.getElementById(`delete-ticket-${ticketId}`).submit();
    }
}

//Delete User
function confirmDeleteUser(userId) {
    if (confirm('Are you sure you want to delete this user?')) {
        document.getElementById(`delete-ticket-${userId}`).submit();
    }
}
