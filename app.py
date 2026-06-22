import streamlit as st
import mysql.connector
import pandas as pd

# ------------------------------
# Database Connection
# ------------------------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="engineeringcollege"
)

cursor = db.cursor()

st.set_page_config(
    page_title="Ace Edu Track",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Ace Edu Track - Admin Dashboard")

# ------------------------------
# Register Student Form
# ------------------------------
st.header("Register New Student")

with st.form("student_form"):

    roll_no = st.text_input("Roll Number")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")

    col1, col2, col3 = st.columns(3)

    with col1:
        branch = st.selectbox(
            "Branch",
            ["CSE", "CSM", "AIML", "ECE", "EEE", "MECH"]
        )

    with col2:
        year = st.selectbox(
            "Year",
            [1, 2, 3, 4]
        )

    with col3:
        section = st.selectbox(
            "Section",
            ["A", "B", "C"]
        )

    submitted = st.form_submit_button(
        "➕ Add Student"
    )

    if submitted:

        try:

            sql = """
            INSERT INTO students
            (roll_no,
             first_name,
             last_name,
             branch,
             year_of_study,
             section)
            VALUES (%s,%s,%s,%s,%s,%s)
            """

            values = (
                roll_no,
                first_name,
                last_name,
                branch,
                year,
                section
            )

            cursor.execute(sql, values)
            db.commit()

            st.success(
                "Student added successfully!"
            )

        except Exception as e:
            st.error(f"Error: {e}")

# ------------------------------
# Display Student Roster
# ------------------------------
st.header("📋 Student Roster")

cursor.execute("""
SELECT
roll_no,
first_name,
last_name,
branch,
year_of_study,
section
FROM students
""")

rows = cursor.fetchall()

df = pd.DataFrame(
    rows,
    columns=[
        "Roll No",
        "First Name",
        "Last Name",
        "Branch",
        "Year",
        "Section"
    ]
)

st.dataframe(
    df,
    use_container_width=True
)

# ------------------------------
# Dashboard Metrics
# ------------------------------
st.header("📊 Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Students",
        len(df)
    )

with col2:
    st.metric(
        "Branches",
        df["Branch"].nunique()
        if not df.empty else 0
    )

with col3:
    st.metric(
        "Sections",
        df["Section"].nunique()
        if not df.empty else 0
    )