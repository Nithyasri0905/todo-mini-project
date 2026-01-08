print("TASKS FOR THE DAY!!")
add_tasks = []
task =" "


def main_menu():
    while True:
        print("1.Add a new task")
        print("2.view all tasks")
        print("3.mark a task as completed")
        print("4.delete tasks")
        print("5.exit")

        choice = input("what you wanna do?: ")

        if choice == "1":
            task = input("enter tasks: ")
            add_tasks.append({"Task" : task , "Status" : "pending" })
            print(add_tasks)
            

        elif choice == "2":
            if not add_tasks:
                print("no task added yet!")

            else:
                count = 1
                for task in add_tasks:
                    print(f"{count}.{task['Task']} - {task['Status']}")
                    count += 1


        elif choice == "3":
            if not add_tasks:
                print("no tasks!!")
            else:
                count = 1
                for task in add_tasks:
                    print(f"{count}.{task['Task']} - {task['Status']}")
                    count += 1

            status_update = int(input("Enter the task number to mark completed: "))
            status_update -= 1
            add_tasks[status_update]["Status"] = "completed"
            print(f"the task  {add_tasks[status_update]['Task']} is marked as completed")


        elif choice == "4":
            if not add_tasks:
                print("No tasks")
            else:
                count = 1
                for task in add_tasks:
                    print(f"{count}.{task['Task']} - {task['Status']}")
                    count += 1
                
            delete_task = int(input("enter the task number to be deleted: "))
            delete_task -= 1
            deleted_task = add_tasks.pop(delete_task)
            print(f"the task {deleted_task['Task']} is deleted")


        elif choice == "5":
            print("Exiting...")
            exit()

        else:
            print("Invalid choice. Try again")

        



 


           

                

                    
                    




           


    






main_menu()







