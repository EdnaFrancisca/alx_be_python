#!/usr/bin/env python3
"""
Daily Reminder Script
A simple task reminder system that uses conditional statements, Match Case, and loops
to provide customized reminders based on task priority and time sensitivity.
"""

def get_valid_priority():
    """Get a valid priority input from the user using a loop."""
    valid_priorities = ['high', 'medium', 'low']
    
    while True:
        priority = input("Enter task priority (high/medium/low): ").lower().strip()
        if priority in valid_priorities:
            return priority
        else:
            print("Invalid priority! Please enter 'high', 'medium', or 'low'.")

def get_valid_time_bound():
    """Get a valid time-bound input from the user using a loop."""
    valid_responses = ['yes', 'no', 'y', 'n']
    
    while True:
        time_bound = input("Is this task time-bound? (yes/no): ").lower().strip()
        if time_bound in valid_responses:
            return time_bound in ['yes', 'y']
        else:
            print("Invalid response! Please enter 'yes' or 'no'.")

def main():
    print("=== Daily Task Reminder System ===")
    print("Let's set up your priority task for today!\n")
    
    # Step 1: Prompt for a single task
    task = input("Enter your task description: ").strip()
    
    # Validate that task is not empty
    while not task:
        print("Task description cannot be empty!")
        task = input("Enter your task description: ").strip()
    
    # Get priority and time sensitivity with validation loops
    priority = get_valid_priority()
    time_bound = get_valid_time_bound()
    
    print("\n" + "="*50)
    print("DAILY TASK REMINDER")
    print("="*50)
    
    # Step 2: Process the task using Match Case based on priority
    match priority:
        case 'high':
            base_message = f"🔴 HIGH PRIORITY: {task}"
            urgency_note = "This is your top priority for today!"
            
        case 'medium':
            base_message = f"🟡 MEDIUM PRIORITY: {task}"
            urgency_note = "Make sure to complete this when you have time."
            
        case 'low':
            base_message = f"🟢 LOW PRIORITY: {task}"
            urgency_note = "Complete this if you have extra time today."
            
        case _:
            # This shouldn't happen due to validation, but good practice
            base_message = f"📝 TASK: {task}"
            urgency_note = "Please complete this task today."
    
    # Step 3: Provide customized reminder
    print(base_message)
    print(urgency_note)
    
    # Use conditional statement to modify reminder if time-bound
    if time_bound:
        print("⏰ URGENT: This task that requires immediate attention today!")
        print("Don't delay - tackle this first!")
    else:
        print("📅 You can work on this at your own pace today.")
    
    print("="*50)
    print("Have a productive day! 🚀")

if __name__ == "__main__":
    main()
