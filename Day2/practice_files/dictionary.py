def student_record():
    total_students=int(input("Total Number of Students:\n"))
    studentRecord={}
    
    for i in range(total_students):
        student_name=input("Enter Student Name:")
        marks=input("Enter marks obtained separated by space:")
        words=marks.split()
        
        marks_list=[]
        for num in words:
            marks_list.append(float(num))
            
        studentRecord[student_name]=marks_list 
        
    print("Student Database:",studentRecord)
    
    print("Student Average Report") 
    for student,numbers in studentRecord.items():
        total_numbers=0
        count=0
        
        for score in numbers:
            total_numbers+=score
            count+=1
        
        if count==0:
            average=0
        else:
            average=total_numbers/count
        
        print(student, "Average Marks:",average) 
    
def word_frequency():
    print("Frequency of a word in a sentence\n")
    sentence=input("Enter a Sentence:")
    words=sentence.lower().split()
    
    frequency={}
    for i in words:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
                
    print("Word Frequencies in a sentence:", frequency)     
    
    
    
print("____Dictionary Implementation____")
student_record()
word_frequency()
  
              