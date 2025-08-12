import os
import pygetwindow 
import time
import json as js

def domain(code:str):
    with open("google-domains.json","r+",encoding="utf-8") as file:
        countrys = js.load(file)
    for country in countrys:
        if code == country["country_code"]:
            return country["domain"]

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

countrys = "https://serpapi.com/google-domains"
    
def Immersive_Products_parameters() -> dict:
    questions = ["What do you want to search ",f"Which country will be use(country codes-dont write dot-;{countrys}) "]
    answers = param_taker(questions=questions)
    params = {
        "q":"+".join(answers[0].split(" ")),
        "google_domain":domain(answers[1].lower()),
        "engine":"google",
        "safe":"active",
        "device":"desktop"
        }
    return params

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



def Jobs_parameters() -> dict:
    questions = ["Which job do you want to search ",f"Which country will be use(countrys codes-dont write dot-;{countrys}) "]
    answers = param_taker(questions=questions)
    params = {
        "q":"+".join(answers[0].split(" ")),
        "google_domain":domain(answers[1].lower()),
        "engine":"google_jobs",
        "safe":"active",
        "device":"desktop"
        }
    return params


def Grammar_Check_parameters() -> dict:
    questions = ["What grammer do you want to check",f"Which country will be use(countrys codes-dont write dot-;{countrys})"]
    answers = param_taker(questions=questions)
    params = {
        "q": "+".join(answers[0].split(" ")) +".+grammar+check",
        "google_domain":domain(answers[1].lower()),
        "engine":"google",
        "device":"desktop"
        }
    return params


def Nutrition_Information_parameters() -> dict:
    questions = ["What do you want to search",f"Which country will be use(countrys codes-dont write dot-;{countrys})"]
    answers = param_taker(questions=questions)
    params = {
        "q": "+".join(answers[0].split(" ")),
        "google_domain":domain(answers[1].lower()),
        "engine":"google",
        "safe":"active",
        "device":"desktop"
        }
    return params



def Popular_Destinations_parameters() -> dict:
    questions = ["What do you want to search",f"Which country will be use(countrys codes-dont write dot-;{countrys})"]
    answers = param_taker(questions=questions)
    params = {
        "q": "+".join(answers[0].split(" ")) +"+Destinations",
        "google_domain":domain(answers[1].lower()),
        "engine":"google",
        "safe":"active",
        "device":"desktop"
        }
    return params
#t destination parametreleri ve soruları ayarlanıcak

def Courses_parameters() -> dict:
    questions = ["What do you want to search",f"Which country will be use(countrys codes-dont write dot-;{countrys})"]
    answers = param_taker(questions=questions)
    params = {
        "q":answers[0],
        "google_domain":answers[1].lower()
        }
    return params

#t kullanıcının girdiği ülke verisi uygunmu diye control edilecek
