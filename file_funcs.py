import os 
import pygetwindow
import json as js
import time

#* A function that determines the country the user will use and makes it a parameter
def domain_setter(code:str,only_country=False) -> str:
    with open("jsons/google-domains.json","r+",encoding="utf-8") as file:
        countrys = js.load(file)

    for country in countrys:
        if code == country["country_code"] :
          if only_country:
                return country["country_code"]
          else:
                return country["domain"]
              


#* Purpose of this function: to take the incoming question list, get the answers through a file, and make them parameters.
def param_taker(questions:list) -> list:
    
    #* The incoming question list is organized.
    questions = [ques + ":" for ques in questions]

    #* The organized questions are written into the "questions.txt" file.
    with open("questions.txt","w",encoding="utf-8") as file:
        for question in questions:
            file.write(question+"\n")
        
        file.write("\nPlease write your filters correctly and dont forget save and close the file.\nAlso don't change any line in this file  except filter lines.")
        #* This note is very important for the code to work.

    
    #* Working logic of the "data_taker" function: it checks at very short intervals whether the file named "questions.txt" is closed.
    #*  If the file has been closed, it takes the answers from each question line and outputs them.
    def data_taker():
        while True:
            windows:str = pygetwindow.getActiveWindowTitle()
            windows = windows.split(" - ")
            if "questions.txt" in windows or "● questions.txt" in windows:
                time.sleep(0.25)
            else:
                break

        with open("questions.txt" ,"r+" , encoding="Utf-8") as file:
            question_lines = file.readlines()[:-3]
            
        return question_lines
    
    
    os.system("questions.txt")
    
    #* The output data is converted into parameters.
    question_lines = data_taker()
    question_lines = [line.split(":")[-1] for line in question_lines]
    question_lines = [line[:-1] for line in question_lines]
    question_lines = [line.lower() for line in question_lines]
    question_lines = [line.strip(" ") for line in question_lines]
    question_lines = [line if line != "" else None for line in question_lines ]
    
    #* Since the "questions.txt" file is unnecessary, it is deleted, but if it does not exist in that folder, the error is skipped.
    try:
        os.remove("questions.txt")
    except FileNotFoundError:
        pass

    return question_lines


#* Purpose of this function: to save the received data (outputs of the service functions) into a file and present it to the user.
def data_writer(datas:str, params:dict) -> None:
    
    #* The parameters entered by the user are saved at the beginning of the file as "bot".
    str_params = [f"Searched topic = {params['q']}"]
    if "google_domain" in params.keys():
        str_params.append(f"Location = {params['google_domain']}")
    else:
        str_params.append(f"Location = {params['gl']}")
    message = "*"*20 +"\n"+"PARAMS"+"\n"+"\n".join(str_params) +"\n"+ "*"*20 +"\n\n" 

    #* A file named "temp_file.txt" is created, and the received data is saved into it.
    with open("temp_file.txt","w",encoding="utf-8") as file:
        file.write(message)
        file.write(datas)
    os.system("temp_file.txt")
    #!NOTE: THE REASON THIS FUNCTION WRITES THE RECEIVED DATA DIRECTLY IS THAT THE SERVICE FUNCTIONS ALREADY FORMAT AND OUTPUT THE DATA.  



