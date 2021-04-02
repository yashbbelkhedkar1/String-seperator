import main
import backend as bd

print("*"*20,"Name and address database system","*"*20,"\n\n")

bd.connect()

while(1) :
    option = input("Press 1 :\tEnter the data ?\nPress 2 :\tView all the database?\nPress 3 :\tExit\n\n")
    if option == "1" :
        res = main.func()
        bd.insert(res[0],res[1])
        print("Data Inserted Successfully")
    elif option == "2" :
        bd.view()
    elif option == "3":
        break
    else :
        print("Please Enter the number between 1 to  3 \n\n")
    print("\n\n")

bd.drop()
