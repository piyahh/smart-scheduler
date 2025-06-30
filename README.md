This Python program allows users to schedule exams by performing basic CRUD (Create, Read, Update, Delete) operations using a text-based menu. Users can add new exams, view scheduled ones, edit existing details, and delete exams.

Features Implemented:
1. Add a New Exam
-Users can input exam name, date, time, and room.
-The program saves this information in a list of dictionaries.

2. View All Exams
-Displays all saved exam schedules in a numbered list.
-Shows exam name, date, time, and room.

3. Edit an Exam Entry
-Lets the user pick which exam to update using its number.
-User can then modify any detail (name, date, time, or room).

4. Delete an Exam Entry
-Lets the user delete a specific exam by selecting its number.
-Removes the exam from the schedule list.

5. Looping Menu System
-After every action, the menu appears again.
-Program only ends when the user chooses Exit.


How It Works (Step-by-Step)
1. The program starts by defining an empty list called exams which stores all exam schedules.
2. A while loop is used to show the menu again and again until the user exits.
3. Depending on the user’s input, the program performs one of the four main CRUD actions:

Option 1: Calls add_exam() function to collect details and save them.

Option 2: Calls view_exams() to display current data.

Option 3: Calls edit_exam() where the user can choose an exam and update its info.

Option 4: Calls delete_exam() to remove an entry.
Option 5: Exits the program.

4. Each CRUD function uses Python dictionaries to store structured data for every exam.
5. Input validation and clear prompts are used to make the program beginner-friendly and readable.


**Project Files**

scheduler.py - the main Python program
README.md - this guide with instructions



Created by:

Obanil, Pia Abigail 

Astillero, Christine 

Ocenar, Geline

Japag, Dave
