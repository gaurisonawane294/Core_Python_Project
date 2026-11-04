from database import database_con

import mysql.connector



# ADMIN LOGIN
def admin_login():

    # conn = database_con()
    # cur = conn.cursor()
    conn, cur=database_con()

    print("\n************* WELCOM ETO OUR ADMIN LOGIN PANEL *************\n")

    email = input("Enter Admin Email: ")
    password = input("Enter Password: ")

    query = "SELECT * FROM admins WHERE email=%s AND password=%s"

    cur.execute(query, (email, password))

    data = cur.fetchone()

    if data:
        print("\nLogin Successful!")
        print("Welcome", data[1])

        cur.close()
        conn.close()

        admin_dashboard()

    else:
        print("\nInvalid Email or Password!")

        cur.close()
        conn.close()


# ADMIN DASHBOARD
def admin_dashboard():

    while True:

        print("\n========== ADMIN DASHBOARD ==========")

        print("1. Add Course")
        print("2. View Courses")
        print("3. Update Course")
        print("4. Delete Course")
        print("5. View Students")
        print("6. View Enrollments")
        print("7. View Payment Details")
        print("8. Logout")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            add_course()

        elif choice == 2:
            view_courses()

        elif choice == 3:
            update_course()

        elif choice == 4:
            delete_course()

        elif choice == 5:
            view_students()

        elif choice == 6:
            view_enrollments()

        elif choice == 7:
            view_payments()

        elif choice == 8:
            print("Admin Logged Out Successfully!")
            break

        else:
            print("Invalid Choice!")


# ADD COURSE
def add_course():

    # conn = database_con()
    # cur = conn.cursor()
    conn, cur=database_con()

    print("\n************** ADD COURSE *************\n")

    name = input("Enter Course Name: ")
    fee = float(input("Enter Course Fee: "))
    duration = input("Enter Course Duration: ")

    query = """
    INSERT INTO courses (course_name, course_fee, duration)
    VALUES (%s, %s, %s)
    """

    cur.execute(query, (name, fee, duration))
    conn.commit()

    print("Course Added Successfully!")

    cur.close()
    conn.close()


# VIEW COURSES
# def view_courses():

#     conn, cur=database_con()

#     cur.execute("SELECT * FROM courses")

#     data = cur.fetchall()

#     print("\n***************** AVAILABLE COURSES *****************")

#     for row in data:
#         print(row)

#     cur.close()
#     conn.close()

def view_courses():

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


# UPDATE COURSE
def update_course():

    conn, cur=database_con()

    print("\n***************** UPDATE COURSE *****************")

    course_id = int(input("Enter Course ID: "))

    name = input("Enter New Course Name: ")
    fee = float(input("Enter New Course Fee: "))
    duration = input("Enter New Duration: ")

    query = """
    UPDATE courses
    SET course_name=%s, course_fee=%s, duration=%s
    WHERE course_id=%s
    """

    cur.execute(query, (name, fee, duration, course_id))
    conn.commit()

    if cur.rowcount > 0:
        print("Course Updated Successfully!")
    else:
        print("Course ID Not Found!")

    cur.close()
    conn.close()


# DELETE COURSE
def delete_course():

    conn, cur=database_con()

    print("\n************** DELETE COURSE *************")

    course_id = int(input("Enter Course ID: "))

    query = "DELETE FROM courses WHERE course_id=%s"

    cur.execute(query, (course_id,))
    conn.commit()

    if cur.rowcount > 0:
        print("Course Deleted Successfully!")
    else:
        print("Course ID Not Found!")

    cur.close()
    conn.close()


# VIEW STUDENTS
# def view_students():

#     conn = database_con()
#     cur = conn.cursor()

#     cur.execute("SELECT student_id, student_name, email, mobile FROM students")

#     data = cur.fetchall()

#     print("\n***************** STUDENT DETAILS *****************")
#     if  data:
#        for row in data:
#           print("--------------------------------")
#                 print("Course ID:", row[0])
#                     print("Course Name:", row[1])
#                     print("Course Fee:", row[2])
#                     print("Duration:", row[3])
        

#     cur.close()
#     conn.close()



# f data:

#         for row in data:
#             print("--------------------------------")
#             print("Course ID:", row[0])
#             print("Course Name:", row[1])
#             print("Course Fee:", row[2])
#             print("Duration:", row[3])

#     else:
#         print("No Courses Available!")

def view_students():

    conn, cur = database_con()

    cur.execute("SELECT student_id, student_name, email, mobile FROM students")

    data = cur.fetchall()

    print("\n***************** STUDENT DETAILS *****************")

    if data:

        for row in data:
            print("--------------------------------")
            print("Student ID:", row[0])
            print("Student Name:", row[1])
            print("Email:", row[2])
            print("Mobile:", row[3])

    else:
        print("No Students Registered!")

    cur.close()
    conn.close()

# VIEW ENROLLMENTS
def view_enrollments():

    conn, cur=database_con()

    query = """
    SELECT e.enrollment_id, s.student_name,
           c.course_name, e.enrollment_date,
           e.payment_amount, e.payment_status
    FROM enrollments e
    JOIN students s ON e.student_id = s.student_id
    JOIN courses c ON e.course_id = c.course_id
    """

    cur.execute(query)

    data = cur.fetchall()

    print("\n***************** ENROLLMENT DETAILS *****************")

    for row in data:
        print(row)

    cur.close()
    conn.close()


# VIEW PAYMENT DETAILS
def view_payments():

    conn, cur=database_con()

    query = """
    SELECT s.student_id, s.student_name,
           c.course_name, e.payment_amount,
           e.payment_status
    FROM enrollments e
    JOIN students s ON e.student_id = s.student_id
    JOIN courses c ON e.course_id = c.course_id
    """

    cur.execute(query)

    data = cur.fetchall()

    print("\n***************** PAYMENT DETAILS *****************")

    for row in data:
        print(row)

    cur.close()
    conn.close()
