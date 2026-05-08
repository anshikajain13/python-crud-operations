#PROJECT - CRUD operations
from pathlib import Path
import os #operating system
try:
       def readfileandfolder():
        p = Path('')
        items = list(p.rglob('*'))  #ALL THE FILE WILL BE COLLECTED IN A LIST WITH THE HELP OF rglob.
        for index, file in enumerate(items):
            print(f'{index+1} - {file}')
except Exception as e:
        print(e)
        
def create_file():
    try:
        readfileandfolder()
        file_name = input('enter name of your file: ')
        p = Path(file_name)
        if p.exists():
            print('FILE ALREADY EXIST')
        else:
            with open(file_name,'w') as file:
                content = input("enter your file's content: ")
                file.write(content)
                print('FILE ADDED!')
    except Exception as e:
        print(e)
            
def read_file():
    try:
        readfileandfolder()
        file_name = input('enter name of your file: ')
        p = Path(file_name)
        if p.exists():
            with open(file_name,'r') as file:
                print(file.read())
        else:
            print('FILE NOT FOUND!')
    except Exception as e:
        print(e)
        
def update_file():
     try:
        readfileandfolder()
        file_name = input('enter name of your file: ')
        p = Path(file_name)
        if p.exists():
            print('press 1 to overwrite the content')
            print('press 2 to append the content')
            
            option = int(input('Enter your choice for updating a file:'))
            if option == 1:
                with open(file_name,'w') as file :
                    content = input('Enter your content: ')
                    file.write(content)
                    print('CONTENT CHANGED..')
            elif option == 2:
                 with open(file_name,'a') as file :
                    content = input('Enter your content: ')
                    file.write(content)
                    print('CONTENT CHANGED..')
            else:
                print('INVALID INPUT')
        else: 
            print('FILE DOES NOT EXISTS!')
            
     except Exception as e:
         print(e)
         
def delete_file():
     readfileandfolder()
     file_name = input('enter name of your file: ')
     p = Path(file_name)
     if p.exists():
         os.remove(p) #os is removing path of that file completely from the system
         print('FILE DELETED')
     else:
         print('FILE DOES NOT EXISTS')
    
        
while True:   
    print("press 1 for creating a file")
    print("press 2 for reading a file")
    print("press 3 for updating a file ")
    print("press 4 for deleting a file")
    print("press 5 for exiting..")

    option = int(input("ENTER YOUR CHOICE: "))
    if option == 1:
        create_file()
    if option == 2:
        read_file()
    if option == 3:
        update_file()
    if option == 4:
        delete_file()
    if option == 0:
        break
    
#Q 16 to 27 in iterative -  4 questions
#and also some questions of loops