def get_tuple():
    tuple_input=input("Enter elemenets for tuple with space in between:\n")
    words=tuple_input.split()
    
    elements=[]
    for i in words:
        elements.append(i)
    return tuple(elements)    

def total_occurences(elements):
    if len(elements)==0:
        print("Tuple is empty!")
        return
    
    target=input("Enter the number you want a count of occurence for:\n")
    
    count=0
    for item in elements:
        if item==target:
            count+=1
            
    print("The element",target,"occured",count,"times.") 
    
def convertTuple_to_list_viceversa(elements):
    print("Tuple:\n",elements) 
    
    to_list=[]
    for i in elements:
        to_list.append(i)
    print("Converted to list:\n",to_list)
    
    backTo_tuple=tuple(to_list) 
    print("Converted back to Tuple:\n",backTo_tuple)
    
    
print("____Tuple Implementation____")  
myTuple=get_tuple()

total_occurences(myTuple)
print()
convertTuple_to_list_viceversa(myTuple)  
                
            
        