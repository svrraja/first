def get_tasks():
    tasks = []
    print("Enter your tasks for today (type 'done' when finished):")
    while True:
        task = input("Task: ")
        if task.lower() == 'done':
            break
        if task.strip():
            tasks.append(task.strip())
    return tasks

def review_tasks(tasks):
    completed_tasks = []
    incomplete_tasks = []
    print("\nReview your tasks. For each task, enter 'y' if completed, or 'n' if not completed.")
    for task in tasks:
        status = input(f"Did you complete '{task}'? (y/n): ").lower()
        if status == 'y':
            completed_tasks.append(task)
        else:
            incomplete_tasks.append(task)
    return completed_tasks, incomplete_tasks

def main():
    tasks = get_tasks()
    if not tasks:
        print("No tasks entered.")
        return

    completed_tasks, incomplete_tasks = review_tasks(tasks)

    print("\nEnd of Day Review:")
    print("Completed Tasks:")
    for task in completed_tasks:
        print(f"- {task}")
    print("\nIncomplete Tasks:")
    for task in incomplete_tasks:
        print(f"- {task}")

if __name__ == "__main__":
    main()