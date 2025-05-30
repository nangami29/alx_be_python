task=input("Enter task:")
priority=input("Priority (high/medium/low):")
time_bound=input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        if time_bound=="yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
             print("Reminder: {task} is a high priority task. Consider completing it when you have free time.")

    
    case "medium":
        if time_bound=="yes":
            print("Reminder: {task} is medium priority task that requires immediate attention today!")
        else:
             print("Reminder: {task} is a medium priority task. Consider completing it when you have free time.")

    case "low":
        if time_bound=="yes":
            print("Reminder: {task} is low priority task that requires immediate attention today!")
        else:
            print("Reminder: {task} is a low priority task. Consider completing it when you have free time.")
