import csv  
    
filename = "details.csv"
fields = ['Name', 'Age', 'Address']  

print('Welcome to the user details Manager !!!')
# add user details
def addUser():
    name = input('Enter the name: ')
    age  = input('Enter the age: ')
    address = input('Enter the address: ')

    newrow =[name, age, address]
    if rows != "":
        rows.append(newrow)  
    with open(filename, 'w') as csvfile:
        
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(fields)          
        csvwriter.writerows(rows)


# get the user listing
def userList():
    with open(filename, mode ='r') as file: 
    
        fileReader = csv.reader(file)
        for lines in fileReader: 
            print(lines)    


# create a empty list
rows = []

# the program is execute 11 times
for i in range(10):
   
    print('''Enter 1 to Add a user in list !!
Enter 2 to Get the list of users !!
Enter 3 to Exit the program !! ''')
    option = int(input('Select your option : '))

    if option == 1:
        addUser()
    elif option == 2:
        userList()
    else :
        print('Exit the program !')
        break

