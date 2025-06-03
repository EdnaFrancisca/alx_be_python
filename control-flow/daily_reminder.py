# daily_reminder.py

def get_task_details():
    """Get task details from user input with validation."""
    task = input("Enter the task description: ").strip()
    
    # Validate task input
    if not task:
        print("Error: Task description cannot be empty.")
        return None, None, None
    
    # Get priority with validation
    while True:
        priority = input("Enter the task's priority (high/medium/low): ").strip().lower()
        if priority in ["high", "medium", "low"]:
            break
        print("Error: Priority must be 'high', 'medium', or 'low'. Please try again.")
    
    # Get time-bound status with validation
    while True:
        time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()
        if time_bound in ["yes", "no"]:
            break
        print("Error: Please enter 'yes' or 'no' for time-bound status.")
    
    return task, priority, time_bound

def create_customized_reminder(task, priority, time_bound):
    """Create a customized reminder message based on task details."""
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
            # This case should not occur due to input validation, but included for completeness
            reminder = f"Reminder: '{task}' — unknown priority level specified."
    
    # Add time-sensitivity note if applicable
    if time_bound == "yes":
        reminder += " This is a time-sensitive task that requires immediate attention today!"
    
    return reminder

def print_task_reminder(reminder):
    """Print the final customized reminder with formatting."""
    print("\n" + "="*50)
    print(reminder)
    print("="*50)

def main():
    """Main function to run the daily reminder program."""
    print("Daily Task Reminder Generator")
    print("-" * 30)
    
    # Get task details from user
    task, priority, time_bound = get_task_details()
    
    # Check if task details were successfully obtained
    if task is None:
        print("Failed to get valid task details. Exiting program.")
        return
    
    # Create customized reminder
    reminder = create_customized_reminder(task, priority, time_bound)
    
    # Print the final reminder
    print_task_reminder(reminder)

# Run the program
if __name__ == "__main__":
    main()
    
