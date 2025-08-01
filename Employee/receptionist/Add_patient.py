import json 
import os 
import sys
import time 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import Data

class add_patient :
    def __init__(self):
        pass
    
    
    def Registerpatient(self) :
        patientinformation = []
        guilds_name = []
        os.system("clear")
        patient_name = input("please Wri""te patient name : ")
        os.system("clear")
        patient_gender = input("select patient gender\n1-Male\n2-Female\n")
        if patient_gender == "1" :
            patient_gender = "Male"
        else :
            patient_gender = "Female"
        os.system("clear")
        patient_address = input("enter patient address : ") 
        os.system("clear")
        Patient_Guild = input("is he have guild ? (yes , no)\n\n")
        if Patient_Guild == "yes" : 
            with open("../../Data/guilds.json" , "r") as guilds_information :
                Guild_Data = json.load(guilds_information)
                Data = Guild_Data["Guilds_id"]
                for dataindex , dataelement in enumerate(Data) :
                    for element in dataelement :
                        guilds_name.append(dataelement[element]["name"])
                        number = 1 
                        print(f"{number}"+"-"+dataelement[element]["name"]+"\n")

            patient_guild = int(input("please choose you'r guild : "))-1
            if guilds_name[patient_guild] : 
                print("guild information loading in progress ...")
                time.sleep(1)
                os.system("clear")
                print("guild information found successfully !")
                patient_guild = guilds_name[patient_guild] 
            else :
                print("Sorry but maybe our hospital Not approve this guild ")
            
            patientinformation.append(
                
                {
                    
                    "patient_name":patient_name , 
                    "patient_gender":patient_gender,
                    "patient_address": patient_address , 
                    "patient_guild" : patient_guild
                    
                    
                }
                
                
                
            )
            os.system("clear")
            print("Register patient information in progress ....")
            time.sleep(2)
            os.system("clear")
            with open("../../Data/Patient_information.json" , "w") as patientinfor : 
                json.dump(patientinformation , patientinfor , indent=3)
                print("Register patient information successfully !! ")
            
                
                
             
            
                   
                    
                    

                    
                    
                    
r = add_patient()
r.Registerpatient()
        
        
        
        
        
        
        