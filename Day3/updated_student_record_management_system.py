import json 
import os 

def student_record_system():
    script_dir=os.path.dirname(os.path.abspath(__file__))
    json_file=os.path.join(script_dir,"students.json")
    
    try:
        with open(json_file, "r") as f1:
            database=json.load(f1)
    except(FileNotFoundError,json.JSONDecodeError):      
        database={}  
        
    while True:
        print("________________________________")
        print("Student Record Management System")
        print("________________________________")
        print("1.Add Student")
        print("2.View All Students")
        print("3.Search Student by Roll Number")
        print("4.Update Student Information")
        print("5.Delete Student")
        print("6.Exit System")
        print("________________________________") 
        
        
        print("Total Students Registered:",len(database))    
        print("________________________________")
                
        option=input("Enter your choce from 1-6:")
        print("________________________________")
                
        if option=="1":
            print("Add New Student")
                    
            roll_no=input("Enter Student Roll Number: ")
            if roll_no=="":
                print("Invalid Input!")
                continue
                    
                        
            if roll_no in database:
                print("This Roll Number is taken.")
                continue
                    
            student_name=input("Enter Student Name: ")
            if student_name=="": 
                print("Invalid Input!")
                continue  
                    
            student_age=input("Enter Student Age: ")
            if student_age=="" or not student_age.isdigit(): 
                print("Invalid Input!")
                continue 
                    
            age=int(student_age)
            if age<=0:
                print("Invalid Input! Age must be a positive Number")
                continue   
                    
            course=input("Enter course:")
            if course=="":
                print("Invalid Input!")
                continue  
                    
            student_Data={"Name":student_name, "Age":age,"Course":course}
            database[roll_no]=student_Data
            
            with open(json_file,"w") as f1:
                json.dump(database,f1,indent=4)
                
            print("Student Added Successfully!")
                        
        elif option=="2": 
            print("All Registered Students")
                    
            if len(database)==0:
                print("No Students Registered.")
            else:
                for rollNum, data in database.items():
                    print ("Roll Number:",rollNum)
                    print("Name:",data["Name"])
                    print("Age:",data["Age"])
                    print("Course:",data["Course"])
                    print("---")
                    
                            
        elif option=="3":               
            print("Search Student")
            search=input("Enter Roll Number to search: ")
                     
            if search in database:
                    print("\nStudent Found:")
                    print("Roll Number",search)
                    print("Name:",database[search]["Name"])
                    print("Age:",database[search]["Age"])
                    print("Course:",database[search]["Course"])    
            else:
                print("No Student found with this Roll Number!",search)
                        
                        
        elif option=="4":
            print("Update Student Information")
            update=input("Enter Roll Number to Update: ")
                    
            if update in database:
                print("Press Enter to keep current data unchanged.")
                New_name=input("Enter New Student Name: ")
                New_age=input("Enter New Student Age:")
                New_course=input("Enter New Course: ")
                        
                if New_name!="":
                    database[update]["Name"]=New_name
                            
                if New_age!="":
                    if New_age.isdigit():
                        New_age=int(New_age)
                        if New_age>0:
                            database[update]["Age"]=New_age
                    else:
                        print("Invalid Age! No change in age.")
                                        
                if New_course!="":
                    database[update]["Course"]=New_course
                
                with open(json_file,"w") as f1:
                    json.dump(database,f1,indent=4)        
                
                print("Student Information Upated Successfully.")
            else:
                print("Studnet Roll Number Not Found!")
                        
                
        elif option=="5":
            print("Delete Student Record")
            delete=input("Enter Roll Number to delete: ")
                    
            if delete in database:
                database.pop(delete)
                
                with open(json_file,"w") as f1:
                    json.dump(database,f1,indent=4)
                
                print("Studnet Record Deleted Successfully!")
            else:
                print("Student Number Not Found!")
                        
        elif option=="6":
            print("Exited System. Goodbye!")
            break
                
        else:            
           print("Invalid Input! Choose from 1-6.")
        
student_record_system()
            
            