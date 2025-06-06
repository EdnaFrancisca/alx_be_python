#!/usr/bin/env python3

def main():
    # Prompt for a single task
    task = input("Enter your task: ").strip()
    if not task:
        print("Error: Task description cannot be empty.")
        return

    # Prompt for priority
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority not in ['high', 'medium', 'low']:
        print("Error: Priority must be 'high', 'medium', or 'low'.")
        return

    # Prompt for time-bound status
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound not in ['yes', 'no']:
        print("Error: Time-bound must be 'yes' or 'no'.")
        return

    # Process the task based on priority and time sensitivity
    message = ""
    
    # Match case for priority
    match priority:
        case 'high':
            message = f"'{task}' is a high priority task"
            if time_bound == 'yes':
                message += " that requires immediate attention today!"
            else:
                message += ". You should address this soon."
        case 'medium':
            message = f"Note: '{task}' is a medium priority task"
            if time_bound == 'yes':
                message += " that should be completed by the end of the day."
            else:
                message += ". Plan to complete it this week."
        case 'low':
            message = f"Note: '{task}' is a low priority task"
            if time_bound == 'yes':
                message += ". Try to get to it when you can today."
            else:
                message += ". Consider completing it when you have free time."
    
    # Print the customized reminder with exact "Reminder: " prefix
    print(f"Reminder: {message}")

if __name__ == "__main__":
    main()
