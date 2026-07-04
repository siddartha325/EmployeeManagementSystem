# 👨‍💼 Employee Management System

A modern Employee Management System built using **Django** that allows organizations to manage employee records efficiently. The application provides secure authentication, employee profile management, search functionality, dashboard statistics, and an admin panel for complete control.

---

## 📌 Project Overview

The Employee Management System is a web-based application developed using the Django framework. It helps administrators manage employee information in a centralized system. Only authenticated administrators can add, edit, or delete employee records, while users can securely view employee information.

---

## ✨ Features

### Authentication
- Secure Login
- Secure Logout
- Authentication required for protected pages
- Admin-only access for managing employee records

### Dashboard
- Total Employees
- Male Employees Count
- Female Employees Count
- Total Departments
- Latest Employee Records

### Employee Management
- Add Employee
- View Employee Details
- Edit Employee Information
- Delete Employee
- Upload Employee Photo
- Default Profile Image
- Search Employees
- Pagination

### User Interface
- Responsive Design
- Bootstrap 5
- Sidebar Navigation
- Dashboard Cards
- Dark Mode / Light Mode
- Attractive Tables
- Profile Images

### Admin Panel
- Django Admin Integration
- Secure Employee Management

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Programming |
| Django | Web Framework |
| HTML5 | Frontend |
| CSS3 | Styling |
| Bootstrap 5 | Responsive UI |
| JavaScript | Dark Mode |
| SQLite | Database |
| Gunicorn | Production Server |
| WhiteNoise | Static Files |
| Render | Deployment |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```
EmployeeManagementSystem/
│
├── employee_management/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── employees/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── dashboard.html
│   │   ├── employee_list.html
│   │   ├── employee_detail.html
│   │   ├── employee_form.html
│   │   ├── confirm_delete.html
│   │   └── login.html
│   │
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── requirements.txt
├── build.sh
├── render.yaml
├── manage.py
└── README.md
```

---

# 🗄 Database

The project uses **SQLite3** as the default database.

Main Employee Fields:

- Employee ID
- Name
- Email
- Phone Number
- Gender
- Department
- Designation
- Salary
- Address
- Joining Date
- Employee Photo

---

# 🔐 Authentication Flow

```
User
   │
   ▼
Login Page
   │
Authentication
   │
   ▼
Dashboard
   │
   ├── Employees
   ├── Employee Details
   ├── Search
   ├── Pagination
   └── Logout
```

Only authenticated users can access the dashboard. Employee creation, editing, and deletion are restricted to administrators.

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/siddartha325/EmployeeManagementSystem.git
```

Move into the project

```bash
cd EmployeeManagementSystem
```

Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Create Superuser

```bash
python manage.py createsuperuser
```

Run the server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000
```

---

# 📸 Application Screens

- Home Page
- Login Page
- Dashboard
- Employee List
- Employee Details
- Add Employee
- Edit Employee
- Delete Employee
- Django Admin Panel

---

# 🌐 Deployment

This project is deployed on **Render**.

Deployment includes:

- Gunicorn
- WhiteNoise
- Build Script
- Render YAML
- Environment Variables

---

# 🔍 Search Functionality

Employees can be searched using their name.

Example:

```
John
```

Returns all employees whose names contain **John**.

---

# 📄 Pagination

Employee records are displayed with pagination to improve performance and readability.

---

# 🌙 Dark Mode

The application includes a Dark Mode / Light Mode switch using JavaScript and CSS variables.

---

# 👨‍💻 Admin Privileges

Only administrators can:

- Add Employees
- Edit Employees
- Delete Employees

Normal users have read-only access.

---

# 📈 Future Enhancements

- PostgreSQL Database
- Email Notifications
- Employee Attendance
- Payroll Management
- Leave Management
- Department Reports
- Charts and Analytics
- REST API
- Export to PDF & Excel
- Employee Role Management

---

# 📚 Learning Outcomes

This project demonstrates:

- Django Models
- Django Views
- URL Routing
- Django Templates
- Forms
- Authentication
- CRUD Operations
- Static & Media Files
- File Upload
- Search
- Pagination
- Responsive UI
- Deployment using Render
- Git & GitHub Workflow

---

# 👤 Author

**Siddartha Ravuri**

- GitHub: https://github.com/siddartha325

---

# 📄 License

This project is created for educational purposes and learning Django web development.
