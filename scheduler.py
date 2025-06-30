# scheduler.py

exam_list = []  

def show_menu():
    print("\n      SMART SCHEDULER MENU      ")
    print("1. Add a new exam")
    print("2. View all exams")
    print("3. Edit an exam entry")
    print("4. Delete an exam entry")
    print("5. Exit")

def add_exam():
    name = input("Enter exam name: ")
    date = input("Enter exam date (year/month/day) ")
    time = input("Enter exam time: ")
    room = input("Enter assigned room: ")

    exam = {
        "name": name,
        "date": date,
        "time": time,
        "room": room
    }

    exam_list.append(exam)
    print("Exam added successfully!")

def view_exams():
    if not exam_list:
        print("No exams scheduled.")
        return

    print("\nScheduled Exams:")
    for i, exam in enumerate(exam_list):
        print(f"{i+1}. {exam['name']} - {exam['date']} at {exam['time']} in Room {exam['room']}")

def edit_exam():
    view_exams()
    try:
        index = int(input("Enter the exam number to edit: ")) - 1
        if 0 <= index < len(exam_list):
            print("Leave blank to keep the current value.")
            name = input(f"New exam name (current: {exam_list[index]['name']}): ") or exam_list[index]['name']
            date = input(f"New date (current: {exam_list[index]['date']}): ") or exam_list[index]['date']
            time = input(f"New time (current: {exam_list[index]['time']}): ") or exam_list[index]['time']
            room = input(f"New room (current: {exam_list[index]['room']}): ") or exam_list[index]['room']

            exam_list[index] = {"name": name, "date": date, "time": time, "room": room}
            print("Exam updated successfully!")
        else:
            print("Invalid exam number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_exam():
    view_exams()
    try:
        index = int(input("Enter the exam number to delete: ")) - 1
        if 0 <= index < len(exam_list):
            deleted = exam_list.pop(index)
            print(f"Deleted exam: {deleted['name']}")
        else:
            print("Invalid exam number.")
    except ValueError:
        print("Please enter a valid number.")


while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_exam()
    elif choice == "2":
        view_exams()
    elif choice == "3":
        edit_exam()
    elif choice == "4":
        delete_exam()
    elif choice == "5":
        print("Succesfully exited Smart Scheduler")
        break
    else:
        print("Invalid choice. Please try again.")
