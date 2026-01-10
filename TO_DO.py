#class 

class TODO_list:
    def __init__(self):
            self.add_tasks = []

            try: 
                 with open("to_do.txt", "r") as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue

                        if "|" in line:
                            task_name, status = line.split("|")
                            task = {
                                'Task' : task_name,
                                'Status' : status
                            }

                            self.add_tasks.append(task)

                        else:
                            print(f"skipping invalid line: {line}")

            except FileNotFoundError :
                pass 
        

    def add(self):

        task_input = input("enter tasks: ")
        task = {
            "Task": task_input,
            "Status": "pending"
        }
        self.add_tasks.append(task)

        try :
            with open("to_do.txt", "a") as f:
                f.write(f"{task_input}|pending\n")

        except PermissionError:
            print("Error: You do not have permission to write to this file")



    def view(self):
        if not self.add_tasks:
            print("no tasks added yet!")

        else:
            count = 1
            for task in self.add_tasks:
                print(f"{count}.{task['Task']} - {task['Status']}")
                count += 1

        

    def mark(self):
        self.view()

        status_update = int(input("enter the number of the task to mark as completed: "))
        status_update -= 1
        self.add_tasks[status_update]['Status'] = "completed"
        
        try:
            with open("to_do.txt", "w") as f:
                for task in self.add_tasks:
                    f.write(f"{task['Task']}|{task['Status']}\n")

        except PermissionError:
            print("Error: You do not have permission to write to this file")

        print(f"the task {self.add_tasks[status_update]['Task']} is marked as completed. ")

    def delete(self):
        self.view()
       
        delete_task = int(input("enter the task number to be deleted: "))
        delete_task -= 1
        deleted_task = self.add_tasks.pop(delete_task)

        try:
            with open("to_do.txt", "w") as f:
                for task in self.add_tasks:
                    f.write(f"{task['Task']}|{task['Status']}\n")

        except PermissionError:
            print("Error: You do not have permission to write to this file")


        print(f"the task {deleted_task['Task']} is deleted")


t1 = TODO_list()

while True:

    

    print("MAIN MENU")
    print("1.add tasks")
    print("2.view tasks")
    print("3.mark task as completed")
    print("4.delete tasks")
    print("5.exit")

    choice = int(input("what you wanna do? "))

    if choice == 1:
        t1.add()

    elif choice == 2:
        t1.view()

    elif choice == 3:
        t1.mark()

    elif choice == 4:
        t1.delete()

    elif choice == 5:
        print("Exiting..")
        break
    
    else:
        print("invalid choice. Try again!")

