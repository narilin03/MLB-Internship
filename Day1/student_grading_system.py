def input_data():
    student_name= input("Studnet Name: ")
    student_class= input ("Student Class: ")
    
    student_subjects= []
    print("Enter Subjects and Marks: ")
    while True:
        subject=input("Subject Name: ") 
        if subject == "":
            break
        
        marks=float(input("Enter Marks(0-100): "))
        student_subjects.append((subject,marks))
    return student_name,student_class,student_subjects

def grade(average):
    if average>=80:
        return "A"
    elif average>=70:
        return "B"
    elif average>=60:    
        return "C"
    else:
        return "D" 
            
def calculate(student_name, studnet_class, student_subjects):
    if len(student_subjects)==0:
        print("No Subject Found!")
        return
    
    total=0
    for subject, marks in student_subjects:
        total+=marks
        
    average=total/len(student_subjects)
    grade_by_average=grade(average)
    
    print("\n____Grade Report____")
    print("Studnet Name:",student_name)
    print("Studnet Class:",studnet_class)
    print("Student Subjects and Marks: ")
    for subj, mark in student_subjects:
        subject_grade=grade(mark)
        print(" ",subj,":",mark,"(Grade:",subject_grade,")") 
      
    print("Overall Average:",average)
    print("Overall Grade:", grade_by_average)
      
student_name,student_class,student_subjects=input_data()
calculate(student_name,student_class,student_subjects)        
      
        
        
    
    
               
        
          
           