Task=[]
def addtask():
    n_task=int(input("enter the number of task you want to add:"))
    for i in range(n_task):
        t=input("enter the task:")
        Task.append(t)
    print("All the task has been added successfully")
def removetask():
    t=input("enter the task you want to remove from the to do list:")
    Task.remove(t)
    print("The task hs been deleted successfully")
def updatetask():
    print("Here is your To Do List, Which Task would you like to delete?")
    for i in Task:
        print(i)
    a=input("Enter the Task that you want to update: ")
    Task.remove(a)
    b=input("Enter the New Task that you want to add: ")
    Task.append(b)
    print("The Task was updated successfully")    
def showtasks():
    print("\n======TO-DO LIST======")
    for i in Task:
        print(i)
    
while True:
    print("1.ADD A TASK")
    print("2.DELETE A TASK")
    print("3.UPDATE TASK")
    print("4.SHOW ALL THE TASKS")
    print("5.EXIT THE MENU")
    ch=int(input("enter your choice from the following:"))
    if(ch==1):
        addtask()
    elif(ch==2):
        removetask()
    elif(ch==3):
        updatetask()
    elif(ch==4):
        showtasks()
    elif(ch==5):
        print("Exiting the Menu")
        break
    else:
        print("Enter the Correct Choice")
