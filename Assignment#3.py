import psycopg2
from psycopg2 import Error

DB_NAME = "test_db"  
DB_USER = "postgres"  
DB_PASSWORD = "postgres"
DB_HOST = "localhost"  
DB_PORT = "5432"   

# Function to establish a connection to the PostgreSQL database
def establish_connection():
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Connected to the database.")
        return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")

# Function to retrieve and display all records from the students table
def get_all_students(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students;")
        students = cursor.fetchall()
        for student in students:
            print(student)
    except Error as e:
        print(f"Error fetching students: {e}")

# Function to insert a new student record into the students table
def add_student(connection, first_name, last_name, email, enrollment_date):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                       (first_name, last_name, email, enrollment_date))
        connection.commit()
        print("Student added successfully.")
    except Error as e:
        print(f"Error adding student: {e}")

# Function to update the email address for a student with the specified student_id
def update_student_email(connection, student_id, new_email):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET email = %s WHERE student_id = %s;",
                       (new_email, student_id))
        connection.commit()
        print("Student email updated successfully.")
    except Error as e:
        print(f"Error updating student email: {e}")

# Function to delete the record of the student with the specified student_id
def delete_student(connection, student_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
        connection.commit()
        print("Student deleted successfully.")
    except Error as e:
        print(f"Error deleting student: {e}")

# Main function
def main():
    # Connect to the database
    connection = establish_connection()

    # Perform CRUD operations based on user input
    while True:
        print("\nOptions:")
        print("1. Get all students")
        print("2. Add a new student")
        print("3. Update student email")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            get_all_students(connection)
        elif choice == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            add_student(connection, first_name, last_name, email, enrollment_date)
        elif choice == "3":
            student_id = input("Enter student ID: ")
            new_email = input("Enter new email: ")
            update_student_email(connection, student_id, new_email)
        elif choice == "4":
            student_id = input("Enter student ID to delete: ")
            delete_student(connection, student_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    # Close the database connection
    connection.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()
