import json
import os 
import time

class authontication :
    def __init__(self):
        pass
    
    
    def Login(self) :
       Employee_id = input("ENter you'r carrer id please : ")
       with open ("Employees_information.json" , "r") as CheckEmployee_information :
            Data = json.load(CheckEmployee_information) 
            for  array_index , array_elements in enumerate(Data) : 
                for dict_keys in array_elements : 
                    for dict_value in array_elements[dict_keys] :
                        for implicit_dict_values in dict_value :
                            if implicit_dict_values == Employee_id : 
                                print("Please wait until checking you'r information")
                                time.sleep(2)
                                print("Successfully Login ")
                                return Employee_id 
                            else :
                                print("Soory but We have faced some issues while Trying to login please Rechecking  you'r information and try again later")
                                
