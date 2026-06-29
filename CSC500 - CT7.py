"""
CSC500 - CT7: Robust Function Development - Course Information System
Looks up a course's room number, instructor, and meeting time from three
dictionaries keyed by the course number, using try/except for robust,
crash-proof handling of unknown courses.
Python 3.13
"""

# Three separate dictionaries, each using the Course Number as the key.
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411",
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}

meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m.",
}


def get_course_info(course_number):
    """Return a formatted report for the given course number.

    A missing course raises KeyError, which is caught with try/except and
    turned into a friendly message so the program never crashes.
    """
    try:
        room = room_numbers[course_number]
        instructor = instructors[course_number]
        meeting_time = meeting_times[course_number]
    except KeyError:
        return f"Sorry, '{course_number}' is not a valid course number."

    return (f"Course Number: {course_number}\n"
            f"Room Number:   {room}\n"
            f"Instructor:    {instructor}\n"
            f"Meeting Time:  {meeting_time}")


def main():
    print("Course Information System")
    print("Available courses: CSC101, CSC102, CSC103, NET110, COM241\n")

    # Normalize the input so "csc101 " still matches the "CSC101" key.
    course_number = input("Enter a course number: ").strip().upper()

    print()
    print(get_course_info(course_number))


if __name__ == "__main__":
    main()
