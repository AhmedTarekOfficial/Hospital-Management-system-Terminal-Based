import json 
import os
import time

class Removeemployee :
    def __init__(self):
        pass
    
    
    
    def Delete_employee_information(self) :
        employee_id = input("could you please enter the employee id : ")
        
        with open("Employees_information.json","r") as employee_data :
            Data = json.load(employee_data)
            for elements_index , elements_Data in enumerate(Data) :
                Employee_keys = list(elements_Data.keys())[elements_index]
                employee_idd = elements_Data[Employee_keys][elements_index]
                employee_idd = list(employee_idd.keys())[elements_index]
                if employee_id == employee_idd :
                    print("Removing in progress ...")
                    time.sleep(1)
                    print("Successfully deleted the Employee information ")
                    del Data[elements_index]
                    with open("Employees_information.json" , "w") as employee_data :
                        json.dump(Data , employee_data , indent=3)
               
               

re = Removeemployee()
re.Delete_employee_information()
                
                