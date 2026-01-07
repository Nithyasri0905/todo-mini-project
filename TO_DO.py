print("TASKS FOR THE DAY!!")
add_tasks = []
task = " "

while task != "exit":
    task = input("enter tasks: ")

    if task.lower() == "exit":
        break
    else:
        add_tasks.append(task)
        print("current tasks: ",add_tasks)

print("ALL TASKS: ", add_tasks)













