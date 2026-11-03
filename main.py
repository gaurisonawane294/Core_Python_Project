
from admin_panel import admin_login
from student import student_login,student_register


while True:

    print("************* WELCOME TO OUR ONLINE COURSE MANAGEMENT SYSTEM ***********\n")


    print("1. Admin Login")
    print("2. Student Login")
    print("3. Student Registration")
    print("4. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
       admin_login()

    elif choice == 2:
        student_login()

    elif choice == 3:
        student_register()	

    elif choice == 4:
        print("Thank you for using our application!")
        break

    else:
        print("Invalid Choice! Please enter a valid choice.")
