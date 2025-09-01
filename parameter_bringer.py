
countrys_url = "https://serpapi.com/google-domains"
    

def Immersive_Products_parameters(param_taker , domain_setter) -> dict:
    questions = ["What product do you want to search ",f"Which country will be use(country codes-dont write dot-;{countrys_url}) "]
    answers = param_taker(questions=questions)
    params = {
        "q":"+".join(answers[0].split(" ")),
        "google_domain":domain_setter(answers[1].lower()),
        "engine":"google",
        "start":"20",
        "safe":"active",
        "device":"desktop"
        }
    return params



def Jobs_parameters(param_taker , domain_setter ) -> dict:
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
def job_count(param_taker):
    questions = ["How many jobs do you want to recive "]
    answer = param_taker(questions=questions)
    return int(answer[0])



def News_parameters(param_taker , domain_setter ) -> dict:
    questions = ["What do you want to search to news ",f"Which country will be use(countrys codes-dont write dot-;{countrys_url})"]
    answers = param_taker(questions=questions)
    params = {
        "q":"+".join(answers[0].split(" ")),
        "gl":domain_setter(answers[1].lower(),only_country=True),
        "engine":"google_news",
        }
    return params



def Nutrition_Information_parameters(param_taker , domain_setter ) -> dict:
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




def Popular_Destinations_parameters(param_taker , domain_setter ) -> dict:
    questions = ["What do you want to search for a trip",f"Which country will be use(countrys codes-dont write dot-;{countrys_url})"]
    answers = param_taker(questions=questions)
    params = {
        "q": "+".join(answers[0].split(" ")) +"+Destinations",
        "google_domain":domain_setter(answers[1].lower()),
        "engine":"google",
        "safe":"active",
        "start":"20",
        "device":"desktop"
        }
    return params




def Courses_parameters(param_taker, domain_setter ) -> dict:
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
def course_count(param_taker):
    answer = param_taker(questions = ["How many course do you want "])
    return int(answer[0])


