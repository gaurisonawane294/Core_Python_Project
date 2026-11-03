
from database import database_con

def student_register():

    con, cur = database_con()

    print("\n************* STUDENT REGISTRATION **************")

    name = input("Enter Student Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    mobile = input("Enter Mobile: ")

    query = """
    INSERT INTO students
    (student_name, email, password, mobile)
    VALUES (%s, %s, %s, %s)
    """

    values = (name, email, password, mobile)

    cur.execute(query, values)
    con.commit()

    student_id = cur.lastrowid

    print("\nRegistration Successful!")
    print("Your Student ID is:", student_id)

    cur.close()
    con.close()


# STUDENT LOGIN
def student_login():

    con, cur = database_con()

    print("\n************* STUDENT LOGIN **************")

    email = input("Enter Email: ")
    password = input("Enter Password: ")

    query = """
    SELECT * FROM students
    WHERE email = %s AND password = %s
    """

    cur.execute(query, (email, password))

    data = cur.fetchone()

    if data:

        print("\nLogin Successful!")
        print("Welcome", data[1])

        student_id = data[0]

        cur.close()
        con.close()

        student_dashboard(student_id)

    else:

        print("\nInvalid Email or Password!")

        cur.close()
        con.close()


# STUDENT DASHBOARD
def student_dashboard(student_id):

    while True:

        print("\n************* STUDENT DASHBOARD **************")

        print("1. View Available Courses")
        print("2. Enroll in Course")
        print("3. View My Courses")
        print("4. View My Payment Details")
        print("5. Logout")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            view_available_courses()

        elif choice == 2:
            enroll_course(student_id)

        elif choice == 3:
            view_my_courses(student_id)

        elif choice == 4:
            view_my_payments(student_id)

        elif choice == 5:
            print("Student Logged Out Successfully!")
            break

        else:
            print("Invalid Choice!")


# VIEW AVAILABLE COURSES
def view_available_courses():

    con, cur = database_con()

    cur.execute("SELECT * FROM courses")

    data = cur.fetchall()

    print("\n************* AVAILABLE COURSES **************")

    if data:

        for row in data:
            print("--------------------------------")
            print("Course ID:", row[0])
            print("Course Name:", row[1])
            print("Course Fee:", row[2])
            print("Duration:", row[3])

    else:
        print("No Courses Available!")

    cur.close()
    con.close()


# ENROLL IN COURSE
def enroll_course(student_id):

    con, cur = database_con()

    print("\n************* COURSE ENROLLMENT **************")

    cur.execute("SELECT * FROM courses")

    data = cur.fetchall()

    if not data:
        print("No Courses Available!")
        cur.close()
        con.close()
        return

    for row in data:
        print("--------------------------------")
        print("Course ID:", row[0])
        print("Course Name:", row[1])
        print("Course Fee:", row[2])

    course_id = int(input("\nEnter Course ID to Enroll: "))

    # Check whether course exists
    cur.execute(
        "SELECT course_name, course_fee FROM courses WHERE course_id=%s",
        (course_id,)
    )

    course = cur.fetchone()

    if course is None:
        print("Invalid Course ID!")
        cur.close()
        con.close()
        return

    # Check whether student already enrolled
    cur.execute(
        "SELECT enrollment_id FROM enrollments WHERE student_id=%s AND course_id=%s",
        (student_id, course_id)
    )

    existing = cur.fetchone()

    if existing:
        print("You are already enrolled in this course!")
        cur.close()
        con.close()
        return

    course_name = course[0]
    course_fee = course[1]

    print("\nSelected Course:", course_name)
    print("Course Fee:", course_fee)

    print("\n1. Pay Now")
    print("2. Pay Later")

    payment_choice = int(input("Enter your choice: "))

    if payment_choice == 1:

        payment_status = "Paid"
        print("\nDummy Payment Successful!")

    elif payment_choice == 2:

        payment_status = "Pending"
        print("\nPayment Pending!")

    else:

        print("Invalid Payment Choice!")
        cur.close()
        con.close()
        return

    query = """
    INSERT INTO enrollments
    (student_id, course_id, enrollment_date,
     payment_amount, payment_status)
    VALUES (%s, %s, CURDATE(), %s, %s)
    """

    values = (student_id, course_id, course_fee, payment_status)

    cur.execute(query, values)

    con.commit()

    print("\nEnrollment Successful!")
    print("Course Name:", course_name)
    print("Payment Status:", payment_status)

    cur.close()
    con.close()


# VIEW MY COURSES
def view_my_courses(student_id):

    con, cur = database_con()

    query = """
    SELECT e.enrollment_id, c.course_id,
           c.course_name, c.duration,
           e.enrollment_date, e.payment_status
    FROM enrollments e
    JOIN courses c ON e.course_id = c.course_id
    WHERE e.student_id = %s
    """

    cur.execute(query, (student_id,))

    data = cur.fetchall()

    print("\n************* MY COURSES **************")

    if data:

        for row in data:
            print("--------------------------------")
            print("Enrollment ID:", row[0])
            print("Course ID:", row[1])
            print("Course Name:", row[2])
            print("Duration:", row[3])
            print("Enrollment Date:", row[4])
            print("Payment Status:", row[5])

    else:
        print("You have not enrolled in any course!")

    cur.close()
    con.close()


# VIEW MY PAYMENT DETAILS
def view_my_payments(student_id):

    con, cur = database_con()

    query = """
    SELECT e.enrollment_id, c.course_name,
           e.payment_amount, e.payment_status
    FROM enrollments e
    JOIN courses c ON e.course_id = c.course_id
    WHERE e.student_id = %s
    """

    cur.execute(query, (student_id,))

    data = cur.fetchall()

    print("\n************* MY PAYMENT DETAILS **************")

    if data:

        for row in data:
            print("--------------------------------")
            print("Enrollment ID:", row[0])
            print("Course Name:", row[1])
            print("Payment Amount:", row[2])
            print("Payment Status:", row[3])

    else:
        print("No Payment Records Found!")

    cur.close()
    con.close()
