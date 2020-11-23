import csv  
    
# options
print('Welcome to the user details Manager !!!)')

filename = "input_user/details.csv"
fields = ['Name', 'Age', 'Address']  


# user input
name = input('Enter the name: ')
age  = input('Enter the age: ')
address = input('Enter the address:')

rows = [[name, age, address]]  
    
    
with open(filename, 'w') as csvfile:  

    csvwriter = csv.writer(csvfile)  
        
    csvwriter.writerow(fields)          

    csvwriter.writerows(rows)

with open(filename, mode ='r') as file: 
    
    fileReader = csv.reader(file)

    for lines in fileReader: 
            print(lines)