import os
import json 
import time 

class Register_employee :
    
    def __init__(self):
        pass
    
    
    
    
    def Add_Employee(self) : 
        employee_id = 0 
        Employee_name = input("Could you please enter Employee name : ")
        Employee_Date = input("Could you please enter Employee Hiring_date : ")
        Employee_Salary = int(input("Could you please Enter Employee salary : "))
        Employee_Job = input("Could you please Enter the Employee Job : ")
        
        
        
        
        with open("jobs.json" , "r") as Job_information : 
            Jobs_data = json.load(Job_information)
            
            """
            First we Loop over array elements the array data is 
            dict so the element's we loop over it is dict 
            this dict contains neasted dict 
            عشان كدا بعد ما نلف علي الديكشنري 
            بنمسك المفاتيح بتاعتها وبنجيب قيم كل مفتاح
            ولو كانت القيم ديه عباره عن فهارس برضو بنلف عليها وبنجيب
            المفاتيح وهكذا عشان نوصل في الاخر للي احنا عايزينه
            """
            for array_dict_elements in Jobs_data : 
                for outer_dict_keys in array_dict_elements  :
                    for outer_dict_keys_value in array_dict_elements[outer_dict_keys] :
                        for inner_dict_keys in outer_dict_keys_value :
                            job_info= outer_dict_keys_value[inner_dict_keys]
                            job_title = job_info["Job_Title"]
                            if job_title == Employee_Job :
                                if outer_dict_keys_value[inner_dict_keys]["Job_Title"] == job_title  :
                                    Employee_Job = inner_dict_keys                                
                                               
                
        Employee_information = [
            
            {
                
                "Employee_id" : [
                    
                    {
                        
                        f"{employee_id}" : [
                            
                    {
                        "FUll_name" : Employee_name , 
                        "Hiring_Date" : Employee_Date  , 
                        "Employee_Salary" : Employee_Salary  , 
                        "Job_id" :  Employee_Job 
                        
                        
                    }
                            
                        ]
                        
                        
                    }
                    
                    
                ]
                
                
            }
            
            
        ] 
        
        with open("Employees_information.json","w") as employee_details :
            json.dump(Employee_information,employee_details , indent=3)
            print("Successfully Registerd Employee")
            return
        
        
        
        
        
    
re = Register_employee()
re.Add_Employee()
 