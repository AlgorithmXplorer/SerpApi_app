import os
import pygetwindow 
import time

def param_taker(questions:list):
    #* the question file creating and writing of questions
    questions = [ques + ":" for ques in questions]
    with open("questions.txt","a",encoding="utf-8") as file:
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
    question_lines = [line.split(":")[-1] for line in question_lines]
    question_lines = [line[:-1] for line in question_lines]
    question_lines = [line.strip(" ") for line in question_lines]
    question_lines = [line if line != "" else None for line in question_lines ]
    os.remove("questions.txt")
    return question_lines

    
def Immersive_Products_parameters() -> dict:
    questions = ["What do you want to search","Which country will be use(countrys codes-dont write dot-;https://serpapi.com/google-domains)"]
    answers = param_taker(questions=questions)
    params = {
        "q":answers[0],
        "google_domain":answers[1],
        }
    return params

x = Immersive_Products_parameters()
print(x)
"""
default:
-engine
-device
-safe
-api_key

optional
-q
-google_domain ( normally i will use gl and hl parameters but google domain is more simple)
"""



