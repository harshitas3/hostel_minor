class Hostel:
    def __init__(self, name, address, capacity):
        self.name = name
        self.address = address
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            print(f"{student.name} has been added to {self.name}")
        else:
            print(f"{self.name} is full. Cannot add {student.name}")

    def __str__(self):
        return f"{self.name} - {self.address} (Capacity: {self.capacity})"


class Student:
    def __init__(self, name, roll_number, room_number):
        self.name = name
        self.roll_number = roll_number
        self.room_number = room_number

    def __str__(self):
        return f"{self.name} (Roll Number: {self.roll_number}, Room Number: {self.room_number})"


def main():
    hostels = []

    while True:
        print("\nHostel/PG Tracking System")
        print("1. Add Hostel/PG")
        print("2. Add Student")
        print("3. View Hostels/PGs")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Hostel/PG Name: ")
            address = input("Enter Address: ")
            capacity = int(input("Enter Capacity: "))
            hostel = Hostel(name, address, capacity)
            hostels.append(hostel)
            print(f"{name} has been added to the system.")

        elif choice == '2':
            name = input("Enter Student Name: ")
            roll_number = input("Enter Roll Number: ")
            room_number = input("Enter Room Number: ")

            print("Select a Hostel/PG to add the student:")
            for i, hostel in enumerate(hostels):
                print(f"{i+1}. {hostel}")
            hostel_choice = int(input("Enter the hostel/PG number: ")) - 1

            if 0 <= hostel_choice < len(hostels):
                student = Student(name, roll_number, room_number)
                hostels[hostel_choice].add_student(student)
            else:
                print("Invalid hostel/PG choice.")

        elif choice == '3':
            print("\nList of Hostels/PGs:")
            for i, hostel in enumerate(hostels):
                print(f"{i+1}. {hostel}")
                for student in hostel.students:
                    print(f"   - {student}")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
