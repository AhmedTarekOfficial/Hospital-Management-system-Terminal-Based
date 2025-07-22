import os 
import json 
from Employees.Managers.Register_employee import Register_employee
from Authintcation import authontication
class Control_Permissions :
    def __init__(self):
        pass
    
    
    
    def checkpermistions (self) :
        
    
             with open ("Employees_information.json" , "r") as permission_information :
              Data = json.load(permission_information) 
              if Data == "" or Data is None :
                  print("We can't find data to read")
              else :
                    
                for  array_index , array_elements in enumerate(Data) : 
                    for dict_keys in array_elements : 
                        for dict_value in array_elements[dict_keys] :
                            for implicit_dict_values in dict_value :
                                for implicitivalues_keys in dict_value[implicit_dict_values] :
                                    if authontication.Login(self) == implicit_dict_values :
                                     job_id = implicitivalues_keys["Job_id"]
                                     if job_id == "1" : 
                                            Register_employee.Add_Employee(self)
                                            return 
                    
                                
            
     
                        
                          
                        
                     
                    
                        
                    
                
con = Control_Permissions()
print(con.checkpermistions())