task=[]
print("To-Do List using Python")
print("Enter 1 to add a task, 2 to view tasks, 3 to delete a task or 4 to quit.")
while True:
    taskask = input("enter the code(1, 2, 3 or 4): ")
    
    if taskask=="1":
        taskname = input("Enter your task: ")
        task.append(taskname)

    elif taskask=="2":
        print("Your tasks are:")
        for i, taskname in enumerate(task, start=1):
            print(i, ".", taskname)
    
    elif taskask=="3":
        print("Your tasks are:")
        for i, taskname in enumerate(task, start=1):
            print(i, ".", taskname)
        
        delete= int(input("Enter task number to delete: "))
        task.pop(delete - 1)
        print("Task deleted!")

    elif taskask == "4":
        print("Ending.")
        break

    else:
        print("Invalid")
