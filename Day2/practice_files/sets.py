def get_set():
     set_input=input("Enter numbers with space in between:")
     words=set_input.split()

     unique_list=[]
     for i in words:
         if i not in unique_list:
             unique_list.append(i)
     return unique_list
 
def set_operations(setA,setB):
    print("Set A values:",setA)
    print("Set B values:",setB)
    
    #Union:
    union=[]
    for i in setA:
        union.append(i)
    for i in setB:
        if i not in union:
            union.append(i)    
    print("Union:",set(union))
   
   #Intersection:
    intersection=[]
    for i in setA:
        if i in setB:
            intersection.append(i)
            
    if len(intersection)==0:  
        print("Intersection:\n No common values found!") 
    else:
        print("Intersection:", set(intersection))    
    

print("____Sets Implementation____")  
print("SetA:")
set1=get_set()

print("SetB:")
set2=get_set()

set_operations(set1,set2) 
    