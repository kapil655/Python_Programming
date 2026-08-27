def add_task(tasks):
    print("Welcome! You can add your important tasks.")
    c_task = int(input("How many tasks do you want to input: "))
    for i in range(c_task):
        task = input("Enter the task you want to add: ").strip()
        tasks.append(task)
    print(tasks, "\n")

def remove_task(tasks):
    print("Remove task")
    r_task = int(input("Enter how many tasks you want to remove: "))
    for i in range(r_task):
        remove_t = input("Enter the task you want to remove: ").strip()
        if remove_t in tasks:
            tasks.remove(remove_t)
        else:
            print(f"'{remove_t}' not found in the list.")
    print(tasks, "\n")

def main():
    tasks = []
    while True:
        opt = input("Enter the option you want (1: add, 2: remove, 3: quit): ").strip()
        if opt == "1":
            add_task(tasks)
        elif opt == "2":
            remove_task(tasks)
        elif opt == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()