from file_funcs import domain_setter
from file_funcs import param_taker
countrys_url = "https://serpapi.com/google-domains"
    

def Immersive_Products_parameters() -> dict:
    questions = ["What do you want to search ",f"Which country will be use(country codes-dont write dot-;{countrys_url}) "]
    answers = param_taker(questions=questions)
    params = {
        "q":"+".join(answers[0].split(" ")),
        "google_domain":domain_setter(answers[1].lower()),
        "engine":"google",
        "safe":"active",
        "device":"desktop"
        }
    return params

def Jobs_parameters() -> dict:
    questions = ["Which job do you want to search ",f"Which country will be use(countrys codes-dont write dot-;{countrys_url}) "]
    answers = param_taker(questions=questions)
    params = {
        "q":"+".join(answers[0].split(" ")),
        "google_domain":domain_setter(answers[1].lower()),
        "engine":"google_jobs",
        "safe":"active",
        "device":"desktop"
        }
    return params


def Grammar_Check_parameters() -> dict:
    questions = ["What grammer do you want to check",f"Which country will be use(countrys codes-dont write dot-;{countrys_url})"]
    answers = param_taker(questions=questions)
    params = {
        "q": "+".join(answers[0].split(" ")) +".+grammar+check",
        "google_domain":domain_setter(answers[1].lower()),
        "engine":"google",
        "device":"desktop"
        }
    return params


def Nutrition_Information_parameters() -> dict:
    questions = ["What do you want to search for subject matter",f"Which country will be use(countrys codes-dont write dot-;{countrys_url})"]
    answers = param_taker(questions=questions)
    params = {
        "q": "+".join(answers[0].split(" ")),
        "google_domain":domain_setter(answers[1].lower()),
        "engine":"google",
        "safe":"active",
        "device":"desktop"
        }
    return params



def Popular_Destinations_parameters() -> dict:
    questions = ["What do you want to search for a trip",f"Which country will be use(countrys codes-dont write dot-;{countrys_url})"]
    answers = param_taker(questions=questions)
    params = {
        "q": "+".join(answers[0].split(" ")) +"+Destinations",
        "google_domain":domain_setter(answers[1].lower()),
        "engine":"google",
        "safe":"active",
        "device":"desktop"
        }
    return params



def Courses_parameters() -> dict:
    questions = ["What course do you want to search ",f"Which country will be use(countrys codes-dont write dot-;{countrys_url})"]
    answers = param_taker(questions=questions)
    params = {
        "q": "+".join(answers[0].split(" ")) +"+course",
        "google_domain":domain_setter(answers[1].lower()),
        "engine":"google",
        "safe":"active",
        "device":"desktop"
        }
    return params


