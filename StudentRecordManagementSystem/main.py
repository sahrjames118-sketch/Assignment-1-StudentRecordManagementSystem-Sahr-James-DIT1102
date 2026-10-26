class Student:
    def __init__(self, student_id, full_name, department, level):
        self.student_id = student_id
        self.full_name = full_name
        self.department = department
        self.level = level

    def display_info(self):
        print("\nStudent Information")
        print("-------------------")
        print(f"Student ID: {self.student_id}")
        print(f"Full Name: {self.full_name}")
        print(f"Department: {self.department}")
        print(f"Level: {self.level}")


class StudentManagementSystem:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        # Prevent duplicate student IDs
        if self.search_student(student.student_id):
            print("Error: This student ID already exists!")
            return False

        self.students.append(student)
        print("Student registered successfully!")
        return True

    def display_students(self):
        if not self.students:
            print("No student records found.")
            return

        print("\n===== REGISTERED STUDENTS =====")

        for student in self.students:
            student.display_info()

    @classmethod
    def get_system_name(cls):
        return "Student Record Management System"

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id.lower() == student_id.lower():
                return student

        return None

    def update_student(self, student_id):
        student = self.search_student(student_id)

        if student is None:
            print("Student not found.")
            return

        print("\nEnter the new information.")
        print("Press Enter to keep the existing value.")

        new_name = input("Full Name: ").strip()
        new_department = input("Department: ").strip()
        new_level = input("Level: ").strip()

        if new_name:
            student.full_name = new_name

        if new_department:
            student.department = new_department

        if new_level:
            student.level = new_level

        print("Student information updated successfully!")

    def delete_student(self, student_id):
        student = self.search_student(student_id)

        if student is None:
            print("Student not found.")
            return

        self.students.remove(student)
        print("Student record deleted successfully!")

    def count_students(self):
        return len(self.students)


def main():

    system = StudentManagementSystem()

    while True:
        print("\n===================================")
        print("  STUDENT RECORD MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Register Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Count Students")
        print("7. Exit")
        print("===================================")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            print("\n--- Register Student ---")

            student_id = input("Student ID: ").strip()
            full_name = input("Full Name: ").strip()
            department = input("Department: ").strip()
            level = input("Level: ").strip()

            if not all([student_id, full_name, department, level]):
                print("Error: All fields are required.")
                continue

            student = Student(
                student_id,
                full_name,
                department,
                level
            )

            system.add_student(student)

        elif choice == "2":
            system.display_students()

        elif choice == "3":
            student_id = input("Enter Student ID: ").strip()
            student = system.search_student(student_id)

            if student:
                student.display_info()
            else:
                print("Student not found.")

        elif choice == "4":
            student_id = input(
                "Enter the Student ID to update: "
            ).strip()

            system.update_student(student_id)

        elif choice == "5":
            student_id = input(
                "Enter the Student ID to delete: "
            ).strip()

            system.delete_student(student_id)

        elif choice == "6":
            print(
                "Total registered students:",
                system.count_students()
            )

        elif choice == "7":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()



