import statistics
lst=[]
sam=[]
def menu():
    print("1. Sort Ascending")
    print("2. Sort Descending")
    print("3. Sum of elements")
    print("4. Mean of elements")
    print("5. Standard deviation of elements")
    print("6. Variance of elements")
    print("7. Enter a new list of values")
    print("8. Exit menu")

def asc():
    sam.sort()
    print("Ascending order of elements is: ")
    print(sam)

def desc():
    sam.sort(reverse=True)
    print("Descending order of elements is: ")
    print(sam)

def app():
    
    num=int(input("Enter the number of elements of new list: "))
    print("Enter the elements: ")
    for i in range(0, num): 
        ele = int(input()) 
        lst.append(ele)
    
    print(lst)
    
num=int(input("Enter the number of elements of list: "))
print("Enter the elements: ")
for i in range(0, num): 
    ele = int(input()) 
    lst.append(ele)

sam=lst.copy()
menu() 
choice = int(input("Enter your choice. "))
    
while choice!=8:    
    if choice == 1:
        asc()
          
    elif choice == 2:
        desc()
            
    elif choice == 3:
        print("Sum of elements is: "+str(sum(sam)))
            
    elif choice == 4:
        print("Mean of elements is: "+str(statistics.mean(sam)))
            
    elif choice == 5:
        print("Standard Deviation of elements is: "+str(round(statistics.stdev(sam),2)))
            
    elif choice == 6:
        print("Variance of elements is: "+str(round(statistics.variance(sam),2)) )
            
    elif choice == 7:
        app()
            
    else: #validate selection
        print("That is not a valid selection, please type the correct number\n")
        
    menu()
    choice = int(input("Enter your choice. "))
    
