import os

print("""
=========== Directory Manager ===========
[1] View 
[2] Create 
[3] Delete 
[4] Rename
[5] Exit
=========================================
""")



while True:
    user_inp = int(input("Option: "))
    if user_inp == 1:
        x = os.getcwd()
        print(x)

    elif user_inp == 2:
        dir_name = input("Folder Name: ")
        os.mkdir(dir_name)

    elif user_inp == 3:
        try:
            dir_name = input("Folder Name: ")
            os.rmdir(dir_name)
        except FileNotFoundError:
            print("File Not Found!")


    elif user_inp == 4:
        try:
            old_name = input("Old Name: ")
            new_name = input("New Name: ")
            os.rename(old_name, new_name)
        except FileNotFoundError:
            print("File Not Found!")
  
    elif user_inp == 5:
        break

    else:
        break                





    

