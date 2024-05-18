def exam_registration():
    # Ask the user how many students are registering
    num_students = int(input("How many students are registering?"))

    # Create a loop for the specified number of students
    for i in range(num_students):
        # Ask the user to enter the next student ID number
        student_id = input("Enter the next student ID number:")

        # Write each student ID to a text file called "reg_form.txt"
        with open("reg_form.txt", "a") as file:
            file.write(student_id + "\n")

    print("Registration forms have been created.")

# Call the function to execute the program
exam_registration()
