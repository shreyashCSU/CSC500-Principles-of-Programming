# This program calculates total and average rainfall over a specified number of years.

def get_positive_int(prompt): # Helper function to get a positive integer from user
    while True:
        try:
            val = int(input(prompt))
            if val > 0:
                return val
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Enter an integer.")


def get_non_negative_float(prompt): # Helper function to get a non-negative float from user
    while True:
        try:
            v = float(input(prompt))
            if v >= 0:
                return v
            print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Enter a number.")


def main(): # Main function to calculate rainfall statistics
    years = get_positive_int("Enter the number of years: ")
    total_inches = 0.0
    months = 0

    for year in range(1, years + 1): # Loop through each year
        print(f"Year {year}:")
        for month in range(1, 13): # Loop through each month
            inches = get_non_negative_float(f"  Month {month} rainfall (in inches): ")
            total_inches += inches
            months += 1

    average = total_inches / months if months else 0.0
    print()
    print(f"Number of months: {months}")
    print(f"Total rainfall: {total_inches:.2f} inches")
    print(f"Average monthly rainfall: {average:.2f} inches")


if __name__ == "__main__":
    main()