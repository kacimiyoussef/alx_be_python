from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    # Prompt the user to enter the number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Get the current date
    current_date = datetime.now()
    # Calculate the future date
    future_date = current_date + timedelta(days=days_to_add)
    # Print the future date in "YYYY-MM-DD" format
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

# Main function to execute the above parts
def main():
    display_current_datetime()  # Display current date and time
    calculate_future_date()      # Calculate and display future date

if __name__ == "__main__":
    main()
