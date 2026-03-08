class AttendanceSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        name = input("Enter student name: ")
        if name not in self.students:
            self.students[name] = []
            print("Student added successfully.")
        else:
            print("Student already exists.")

    def mark_attendance(self):
        name = input("Enter student name: ")
        if name in self.students:
            status = input("Enter attendance (P/A): ")
            self.students[name].append(status.upper())
            print("Attendance marked.")
        else:
            print("Student not found.")

    def view_attendance(self):
        print("\nAttendance Report")
        for student, records in self.students.items():
            print(student, ":", records)

def main():
    system = AttendanceSystem()

    while True:
        print("\n--- Attendance System ---")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.mark_attendance()
        elif choice == "3":
            system.view_attendance()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()