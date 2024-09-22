# daily_reminder.py

# Prompt the user to enter the task, priority, and time sensitivity
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using match case
# Process the task based on priority using match case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = "Invalid priority. Please enter high, medium, or low."
        print(reminder)
        exit()  # Exit the program if the priority is invalid

# Modify the reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
elif time_bound == "no":
    reminder += " Consider completing it when you have free time."
else:
    reminder = "Invalid input for time sensitivity. Please enter yes or no."
    print(reminder)
    exit()  # Exit the program if the time-bound input is invalid

# Print the customized reminder
print(f"Reminder: {reminder}")
