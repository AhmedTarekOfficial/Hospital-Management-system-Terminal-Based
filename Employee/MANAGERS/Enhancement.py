import json 
import os 
import time 

class Enhancement :
    def __init__(self):
        pass
    
    def Update_employee_information(self) :
        with open("Employees_information.json","r") as Employee_Details :
            employee_Details = json.load(Employee_Details)
            
            for  Dict_index , Dict_elements in enumerate(employee_Details)  :

               parent_dict_keys = list(Dict_elements.keys())[Dict_index]
               for keys in Dict_elements[parent_dict_keys][Dict_index] :
                Sub_dict_values = list((Dict_elements[parent_dict_keys][Dict_index]).values())[Dict_index][Dict_index]
                Search_employee = input("Enter the employee you want to update it's information ")
                if Search_employee == keys : 
                        os.system("clear")
                        Manager_choice = input("please choose which information you want to update\n1-Full_name\n2-Hiring_Date\n3-Employess_Salary\n4-Job_id\n\n")
                        if Manager_choice == "1" :
                            NEW_NAME = input("Please write the new name :  ")
                            Sub_dict_values["FUll_name"] = NEW_NAME
                            os.system("clear")
                            print("ARE YOU SURE YOU WANT TO REPLACE THE CURRENT NAME "+f"{Sub_dict_values["FUll_name"]} with {NEW_NAME} ? (Y,N)\n")
                            user_choice = input()
                            if user_choice == "Y" : 
                                print("Update in progress..")
                                time.sleep(2)
                                with open("Employees_information.json" , "w") as Employee_Details :
                                    json.dump(employee_Details , Employee_Details , indent=3)
                                    os.system("clear")
                                    print("Update Successfully")
                                
                                Another_choice = input("DO YOU WAN'T TO UPDATE ANOTHER INFORAMTION ? (Y,N)")
                                if Another_choice == "N" :
                                    break 
                                else :
                                  Manager_choice = input("please choose which information you want to update\n1-Hiring_Date\n2-Employess_Salary\n3-Job_id\n\n")
                                  if Manager_choice == "1" : 
                                      New_HIRE_DATE = input("Please Write the new hire date (YEAR-MONTH-DAY)\n\n: ")
                                      Sub_dict_values["Hiring_Date"] = New_HIRE_DATE  
                                      print("Update in Progress...")
                                      time.sleep(1)  
                                      with open("Employees_information.json" , "w") as Employee_Details :
                                        json.dump(employee_Details , Employee_Details , indent=3)
                                        os.system("clear")
                                        print("Update Successfully")
                                        Employee_Details.close()
                                        
                                  elif Manager_choice == "2" :
                                      New_salary = int(input("Please enter the new salary of the employee : "))
                                      Sub_dict_values["Employee_Salary"] = New_salary 
                                      os.system("clear")
                                      print("update in progress...")
                                      time.sleep(1)
                                      with open("Employees_information.json" , "w") as Employee_Details :
                                        json.dump(employee_Details , Employee_Details , indent=3)
                                        os.system("clear")
                                        print("Update Successfully")
                                        Employee_Details.close()
                                      
                                      
                                  elif Manager_choice == "3" :
                                      NEW_JOB_ID = input("Please enter the new job id : ")
                                      Sub_dict_values["Job_id"] = NEW_JOB_ID
                                      os.system("clear")
                                      print("update in progress ..")
                                      time.sleep(1)
                                      with open("Employees_information.json" , "w") as Employee_Details :
                                        json.dump(employee_Details , Employee_Details , indent=3)
                                        os.system("clear")
                                        print("Update Successfully")
                                        Employee_Details.close()
                        elif Manager_choice == "2" :
                            newhiredate = input("Please enter the new Hire Date (YEAR-MONTH-DAY)\n\n")
                            Sub_dict_values["Hiring_Date"] = newhiredate
                            os.system("clear")
                            
                            Ensure = input("Are you sure you want to replace "+f'{Sub_dict_values["Hiring_Date"]} with {newhiredate} ? (Y , N)')
                            while Ensure !=None or Ensure != "" :
                                if Ensure == "Y" : 
                                    print("Updating in progress .. ")
                                    time.sleep(1)
                                    with open("Employees_information.json" , "w") as Employee_Details :
                                        json.dump(employee_Details , Employee_Details , indent=3)
                                        os.system("clear")
                                        print("Updating sucessfully")
                                        break 
                                else :
                                    another_time = input("do you want to rewrite new Hire date ? (Y,N) \n\n")
                                    if another_time == "N" :
                                        break
                                    else :
                                        New_hiredate = input("Please enter the new Hire Date (YEAR-MONTH-DAY)\n\n")
                                        Sub_dict_values["Hiring_Date"] = New_hiredate
                                        os.system("clear")
                                        print("Updating in progress...")
                                        time.sleep(1)
                                        with open("Employees_information.json" , "w") as Employee_Details :
                                            json.dump(employee_Details , Employee_Details , indent=3)
                                            os.system("clear")
                                            print("Updating sucessfully")
                                        break 
                        elif Manager_choice == "3" :
                            Employee_new_salary = int(input("Please enter new salary"))
                                        
                                        
                                    
                                
                                            

                                    
                        
                    
                        
                else :
                    os.system("clear")
                    print("Soory we counter an issue while searching fore the employee could you please RECHECK THE EMPLOYEE ID AND TRY AGAIN ")
                
cc = Enhancement()
cc.Update_employee_information()