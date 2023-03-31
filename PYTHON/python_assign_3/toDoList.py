tasks = []  #intailize empty list
try:
    with open('todo.txt', "r") as f:
        tasks = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    pass

# Main loop -> infinite
while True:
    print("To-Do List\n")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")
    print("\nMenu:")
    print("1. Add a task")
    print("2. Update a task")
    print("3. Delete a task")
    print("4. Open a file")
    print("5. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        task = input("Enter a new task: ")   # Add a new task
        tasks.append(task)
        with open('todo.txt', "a") as f:    # Write the tasks to the file
            f.write(task + "\n")
    elif choice == "2":
        index = int(input("Enter the index of the task to update: ")) - 1 # Update an existing task
        task = input("Enter the new task: ")
        tasks[index] = task
       
        with open('todo.txt', "w") as f:
            for task in tasks:
                f.write(task + "\n")
    elif choice == "3":
        # Delete an existing task
        index = int(input("Enter the index of the task to delete: ")) - 1
        tasks.pop(index)
        # Write the tasks to the file
        with open('todo.txt', "w") as f:
            for task in tasks:
                f.write(task + "\n")
    elif choice=="4":
        file = open('todo.txt', 'r')
        content = file.read()
        print(content)
    elif choice == "5":
        # Exit the program
        break
