def student_record_management_system():
    database={}
    
    while True:
        print("________________________________")
        print("Student Record Management System")
        print("________________________________")
        print("1.Add Student")
        print("2.View All Students")
        print("3.Search student by Roll Number")
        print("4.Update Student Information")
        print("5.Delete Student")
        print("6.Exit System")
        print("________________________________")
        
        
        Total_Students=0
        for i in database:
            Total_Students+=1
        print("Total Students Registered:",Total_Students)    
        print("________________________________")
        
        option=input("Enter your choce from 1-6:")
        print("________________________________")
        
        if option=="1":
            print("Add New Student")
            
            roll_no=input("Enter Student Roll Number: ")
            if roll_no=="":
                print("Invalid Input!")
                continue
            
            exists=False
            for i in database:
                if i==roll_no:
                    exists=True
                    break
                
            if exists:
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
            print("Student Added Successfully!")
                
        elif option=="2": 
            print("All Registered Students")
            
            Total_Students=0
            for r in database:
                Total_Students+=1
                
            if Total_Students==0:
                print("No Students Registered.")
            else:
                for rollNum, data in database.items():
                    print ("Roll Number:",rollNum)
                    print("Name:",data["Name"])
                    print("Age:",data["Age"])
                    print("Course:",data["Course"])
                    
        elif option=="3":               
            print("Search Student")
            search=input("Enter Roll Number to search: ")
            
            match=False
            for rollNum,data in database.items():
                if rollNum==search:
                    print("\nStudent Found:")
                    print("Roll Number",rollNum)
                    print("Name:",data["Name"])
                    print("Age:",data["Age"])
                    print("Course:",data["Course"])
                    match=True
                    break
                
            if not match:
                print("No Student found with this Roll Number!",search)
                
                
        elif option=="4":
            print("Update Student Information")
            update=input("Enter Roll Number to Update: ")
            
            match=False
            for rollNum in database:
                if rollNum==update:
                    match=True
                    break
               
            if match:
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
                
                print("Student Information Upated Successfully.")
            else:
                print("Studnet Roll Number Not Found!")
                
        
        elif option=="5":
            print("Delete Student Record")
            delete=input("Enter Roll Number to delete: ")
            
            if delete in database:
                database.pop(delete)
                print("Studnet Record Deleted Successfully!")
            else:
                print("Student Number Not Found!")
                
        elif option=="6":
            print("Exited System. Goodbye!")
            break
        
        else:            
            print("Invalid Input! Choose from 1-6.")


student_record_management_system()
    
    
    