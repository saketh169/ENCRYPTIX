todo_list=[]

def show_tasks():
    if len(todo_list)==0:
        print("No Tasks to show")
        print("    ")
        
    else:
        i=0
        for item in todo_list:
            i=i+1
            print(i,item)
            
        print("    ")
    
    
def add_task():
    str=input("ENTER THE NEW TASK :")
    todo_list.append(str)
    print("    ")
    
    
    
    
def delete_task():
    if len(todo_list)==0:
        print("NO TASKS TO DELETE")
        print("    ")
    else:
        
         num=int(input("ENTER THE TASK NUMBER TO DELETE:"))
         del todo_list[num-1]
    
def main():
    while True:
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


main()
