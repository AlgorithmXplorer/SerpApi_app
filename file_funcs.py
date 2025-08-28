import os 
import pygetwindow
import json as js
import time


def domain_setter(code:str,only_country=False):
    with open("google-domains.json","r+",encoding="utf-8") as file:
        countrys = js.load(file)

    for country in countrys:
        if code == country["country_code"] :
          if only_country:
                return country["country_code"]
          else:
                return country["domain"]
              



def param_taker(questions:list):
    #* the question file creating and writing of questions
    questions = [ques + ":" for ques in questions]

    with open("questions.txt","w",encoding="utf-8") as file:
        for question in questions:
            file.write(question+"\n")
        
        file.write("\nPlease write your filters correctly and dont forget save and close the file.\nAlso don't change any line in this file  except filter lines.")
    
    def data_taker():
        while True:
            windows:str = pygetwindow.getActiveWindowTitle()
            windows = windows.split(" - ")
            if "questions.txt" in windows or "● questions.txt" in windows:
                time.sleep(0.25)
            else:
                break

        with open("questions.txt" ,"r+" , encoding="Utf-8") as file:
            question_lines = file.readlines()[:len(questions)]
            
        return question_lines
    
    os.system("questions.txt")
    
    #* data clearing
    question_lines = data_taker()
    os.remove("questions.txt")
    question_lines = [line.split(":")[-1] for line in question_lines]
    question_lines = [line[:-1] for line in question_lines]
    question_lines = [line.lower() for line in question_lines]
    question_lines = [line.strip(" ") for line in question_lines]
    question_lines = [line if line != "" else None for line in question_lines ]
    return question_lines



def data_writer(datas:str, params:dict):
    #* gelen dataları oluşturulan dosyaya yazdırıcak
    str_params = [f"Searched topic = {params['q']}"]
    if "google_domain" in params.keys():
        str_params.append(f"Location = {params['google_domain']}")
    else:
        str_params.append(f"Location = {params['gl']}")
    message = "*"*20 +"\n"+"PARAMS"+"\n"+"\n".join(str_params) +"\n"+ "*"*20 +"\n\n" 

    with open("temp_file.txt","w",encoding="utf-8") as file:
        file.write(message)
        file.write(datas)
    



