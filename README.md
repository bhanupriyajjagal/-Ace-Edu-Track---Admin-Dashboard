# 🎓 Ace Edu Track - Engineering College Management System

Ace Edu Track is a simple Engineering College Management System developed using **Python, Streamlit, MySQL, HTML, CSS, and JavaScript**. The application allows administrators to register students, manage student records, and view dashboard statistics through an interactive interface.

---

## 🚀 Features

### 👨‍🎓 Student Management
- Register new students
- Store student details in MySQL database
- View all registered students
- Display student roster in tabular format

### 📊 Dashboard Analytics
- Total number of students
- Total branches available
- Total sections available
- Real-time metrics using Streamlit

### 🌐 Web Interface
- Responsive HTML and CSS frontend
- JavaScript integration for fetching and displaying student data
- Form submission using REST API calls

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| Streamlit | Interactive Dashboard |
| MySQL | Database Management |
| HTML5 | Frontend Structure |
| CSS3 | Styling |
| JavaScript | Dynamic Data Fetching |
| Flask | REST API Development |
| Flask-CORS | Cross-Origin Requests |

---

## 📂 Project Structure

```bash
Ace-Edu-Track/
│
├── app.py               # Streamlit application
├── database.sql         # Database schema and tables
├── index.html           # Frontend page
├── style.css            # Styling file
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/Ace-Edu-Track.git
cd Ace-Edu-Track
```

### Step 2: Create Virtual Environment

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4: Configure MySQL Database

Create a database:

```sql
CREATE DATABASE engineeringcollege;
```

Import the SQL file:

```bash
mysql -u root -p engineeringcollege < database.sql
```

---

### Step 5: Update Database Credentials

In `app.py`, modify:

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="engineeringcollege"
)
```

---

## ▶️ Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser:

```
http://localhost:8501
```

---

## 📸 Dashboard Modules

### Register New Student
- Roll Number
- First Name
- Last Name
- Branch
- Year of Study
- Section

### Student Roster
Displays all registered students in a table.

### Dashboard Metrics
- Total Students
- Number of Branches
- Number of Sections

---

## 🔮 Future Enhancements

- Faculty Management System
- Attendance Tracking
- Marks Management
- Parent Portal
- Student Login Authentication
- Role-Based Access Control
- Data Visualization Dashboard
- Report Generation (PDF/Excel)
- Cloud Deployment

---

## 🎯 Learning Outcomes

This project demonstrates:

- Database connectivity using MySQL
- CRUD operations in Python
- Streamlit dashboard development
- Frontend development using HTML, CSS, and JavaScript
- API integration concepts
- Full Stack Development fundamentals

---

## 👩‍💻 Author

**Bhanu Priya Ajjagal**

B.Tech in Artificial Intelligence & Machine Learning  
Aspiring Data Analyst | AI Enthusiast | Full Stack Developer

---

## ⭐ Support

If you found this project useful, please consider:

⭐ Star this repository  
🍴 Fork this repository  
📢 Share with others

---
