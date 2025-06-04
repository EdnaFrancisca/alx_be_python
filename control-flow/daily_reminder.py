# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Build the reminder message
reminder = f"Reminder: '{task}' is a {priority} priority task"

# Use match-case to customize based on priority
match priority:
    case "high":
        reminder += " — make sure to address it as soon as possible."
    case "medium":
        reminder += " — try to complete it during the day."
    case "low":
        reminder += " — complete it when you have spare time."
    case _:
        reminder = f"Reminder: '{task}' — unknown priority level specified."

# Add time-bound warning
if time_bound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"

# Final output
print(reminder)
