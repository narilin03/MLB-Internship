#List Practice:
def get_list():
    list_input=input("Enter numbers with space in between:")
    words=list_input.split()

    numbers=[]
    for i in words:
        numbers.append(int(i))
    return numbers

def first_largest(numbers):
    if len(numbers)==0:
        print("List is empty.") 
        return None 
    
    largest=numbers[0]
    for num in numbers:
        if num>largest:
            largest=num
    print("Largest number:", largest)
    return largest
    
def second_largest(numbers): 
    if len(numbers)<2:
        print("Insufficient elements!") 
        return    
    
    firstMax=numbers[0]
    for num in numbers:
        if num>firstMax:
            firstMax=num
    
    secondMax=None
    for num in numbers:
        if num==firstMax:
            continue
      
        if secondMax is None or num>secondMax:
            secondMax=num
            
    if secondMax is None:
        print("No Second Largest Number.")
    else:
        print("Second Largest Number:",secondMax)        
              
def remove_duplicate(numbers):
    unique_values=[]
    removed_duplicates=[]
    
    for i in numbers:
        duplicate=False
        for unique_i in unique_values:
            if i==unique_i:
                duplicate=True 
                break  
            
        if duplicate:
            tracked=False
            for x in removed_duplicates:
                if i==x:
                    tracked=True
                    break
            if not tracked:
                removed_duplicates.append(i)             
        else:
            unique_values.append(i)  
    
    if len(removed_duplicates)==0:
        print("Unique List:", unique_values)
        print("No duplicates were present.")
    else:  
        print("Unique List:", unique_values)          
        print("List without Duplicates:",removed_duplicates) 
    
def reverse_list(numbers):
    stack=list(numbers)     
    reversed_list=[]
    
    while len(stack)>0:
        last_num=stack.pop() 
        reversed_list.append(last_num) 
        
    print("Reversed List:", reversed_list)
    
def common_elements(list1,list2):
    common_elements=[]
    
    for num in list1:
        if num in list2:
            if num not in common_elements:
                common_elements.append(num)
                
    if len(common_elements)==0:
        print("No common elements.") 
    else:
        print("Common elements:", common_elements) 
                       

print("_____List Implementation_____") 
myList=get_list()

first_largest(myList)
second_largest(myList)
remove_duplicate(myList)
reverse_list(myList)

print("\nNow enter a second list for Comparison:")
myList2=get_list()
common_elements(myList,myList2)

                           