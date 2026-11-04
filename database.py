
import mysql.connector as m
# def database_con():
#  conn = m.connect(
#       host="localhost",
#       user="root",
#       password="gauri123",
#       database="online_course_management"
#     )
#     cur = conn.cursor()
#     return conn, cur

# conn,cur = database_con()

def database_con():

    conn = m.connect(
        host="localhost",
        user="root",
        password="gauri123",
        database="online_course_management"
    )

    cur = conn.cursor()

    return conn, cur


# Calling function
conn, cur = database_con()


cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INT PRIMARY KEY AUTO_INCREMENT,
        student_name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        mobile VARCHAR(15)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS admins (
        admin_id INT PRIMARY KEY AUTO_INCREMENT,
        admin_name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")

print("Admins Table Created!")

cur.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INT PRIMARY KEY AUTO_INCREMENT,
        course_name VARCHAR(100) NOT NULL,
        course_fee DECIMAL(10,2) NOT NULL,
        duration VARCHAR(50)
    )
""")

print("Courses Table Created!")

cur.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
        student_id INT NOT NULL,
        course_id INT NOT NULL,
        enrollment_date DATE,
        payment_amount DECIMAL(10,2),
        payment_status ENUM('Paid','Pending') DEFAULT 'Pending',

        FOREIGN KEY (student_id)
        REFERENCES students(student_id),

        FOREIGN KEY (course_id)
        REFERENCES courses(course_id),

        UNIQUE (student_id, course_id)
    )
""")


# cur.execute("INSERT INTO admins (admin_name, email, password) VALUES ('Admin', 'admin@gmail.com', 'admin123')")
# conn.commit()

cur.execute("SELECT * FROM admins WHERE email = %s", ("admin@gmail.com",))

data = cur.fetchone()

if data is None:

    cur.execute("""
        INSERT INTO admins (admin_name, email, password)
        VALUES (%s, %s, %s)
    """, ("Admin", "admin@gmail.com", "admin123"))

    conn.commit()
    print("Default Admin Created!")

else:
    print("Admin Already Exists!")