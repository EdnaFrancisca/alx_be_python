# daily_reminder.py

# Prompt the user for task details
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high/medium/low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

# Start building the reminder message
reminder = f"Reminder: '{task}' is a {priority} priority task"

# Use match-case to handle different priority levels
match priority:
    case "high":
        reminder += " — make sure to address it as soon as possible."
    case "medium":
        reminder += " — try to complete it during the day."
    case "low":
        reminder += " — complete it when you have spare time."
    case _:
        reminder = f"Reminder: '{task}' — unknown priority level specified."

# Add time-sensitivity note if applicable
if time_bound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"

# Print the final customized reminder
print(reminder)
