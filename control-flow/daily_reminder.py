task = input("Enter your task: ")
is_time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
priority = input("Priority (high/medium/low): ").strip().lower()

# Determine the urgency message using match-case (Python 3.10+)
match is_time_bound:
    case "yes":
        urgency = "Immediate action is required!"
    case "no":
        urgency = "No immediate action needed."
    case _:
        urgency = "Time sensitivity not specified."

# Print customized reminder
print(f"\n🔔 Reminder:")
print(f"Task: {task}")
print(f"Priority: {priority.capitalize()}")
print(f"{urgency}")
