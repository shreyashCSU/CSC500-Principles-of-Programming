# Dictionary mapping course numbers to their room numbers
room_num={
    "CSC101":3004,
    "CSC102":4501,
    "CSC103":6755,
    "NET110":1244,
    "COM241":1411
    }

# Dictionary mapping course numbers to their instructor names
instructors={
    "CSC101":"Haynes",
    "CSC102":"Alvarado",
    "CSC103":"Rich",
    "NET110":"Burke",
    "COM241":"Lee"
    }

# Dictionary mapping course numbers to their meeting times
meeting_time = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Prompt user to enter a course number
course = input("Enter the course number: ") 

# Check if the entered course number exists in the room_num dictionary
if course in room_num:
    # Display course information if the course is found
    print(f"Course: {course}")
    print(f"Instructor: {instructors[course]}")
    print(f"Room number: {room_num[course]}")
    print(f"Meeting time: {meeting_time[course]}")
else:
    # Display error message if the course is not found
    print("Course not found.")