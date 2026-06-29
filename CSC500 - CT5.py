"""
CSC500 - CT5: Average Rainfall (Iteration and Selection, Week 5)
Uses nested loops to collect monthly rainfall over a number of years
and reports the total months, total inches, and average rainfall per month.
Python 3.14.5
"""

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]


def get_number_of_years():
    """Prompt for the number of years, accepting only positive whole numbers."""
    while True:
        years = int(input("Enter the number of years: "))
        if years > 0:
            return years
        print("Please enter a number greater than zero.")


def get_monthly_rainfall(year_label, month_name):
    """Prompt for one month's rainfall, accepting only non-negative numbers."""
    while True:
        inches = float(input(f"  {year_label}, {month_name}: enter inches of rainfall: "))
        if inches >= 0:
            return inches
        print("  Rainfall cannot be negative. Please try again.")


def main():
    print("Average Rainfall Calculator")
    print("---------------------------")

    years = get_number_of_years()

    total_months = 0
    total_rainfall = 0.0

    # Outer loop: one iteration per year.
    for year in range(1, years + 1):
        print(f"\nYear {year}")
        # Inner loop: one iteration per month.
        for month_name in MONTHS:
            total_rainfall += get_monthly_rainfall(f"Year {year}", month_name)
            total_months += 1

    average_rainfall = total_rainfall / total_months

    print("\nRainfall Summary")
    print("----------------")
    print(f"Number of months:        {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall/month:   {average_rainfall:.2f}")


if __name__ == "__main__":
    main()
