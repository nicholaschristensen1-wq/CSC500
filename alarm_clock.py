# 24-Hour Clock Alarm
# Asks the user for the current time and how many hours to wait,
# then uses the modulo operator to find the time the alarm will go
# off on a 24-hour clock (0 = midnight, 23 = 11 p.m.).


def get_int(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if minimum <= value <= maximum:
            return value
        print(f"Please enter a whole number between {minimum} and {maximum}.")


def main():
    print("24-Hour Clock Alarm")
    print("-------------------")

    current_time = get_int("Enter the current time in hours (0-23): ", 0, 23)
    wait_hours = get_int("Enter the number of hours to wait: ", 0, 1000)

    alarm_time = (current_time + wait_hours) % 24

    print("\nResults:")
    print(f"Current time:   {current_time}:00")
    print(f"Hours to wait:  {wait_hours}")
    print(f"Alarm goes off: {alarm_time}:00")


if __name__ == "__main__":
    main()
