import time
import os

from file_funcs import *
from parameter_bringer import *

from Immersive_Products_api_service import *
from Jobs_API_service import *
from News_api_service import *
from Nutrition_Information_api_service import * 
from Popular_Destinations_api_service import *
from courses_API_service import *

class main:
    def __init__(self,param_taker_func , domain_setter_func , data_writter_func):
        self.param_taker_func = param_taker_func
        self.data_writter_func = data_writter_func
        self.domain_setter_func = domain_setter_func

    def panel(self):
        panel_questions = "1-Immersive Products API service \n2-Jobs API service \n3-News API service\n4-Nutrition Information API service\n5-Popular Destinations API service\n6-Courses API service\nWhich api service do you want(Enter 'q' if you want to quit the app) "
        choice = str(self.param_taker_func(questions=[panel_questions])[-1])

        if choice == "q":
            print("QUİTİNG THE APP")

        elif choice not in [str(i) for i in list(range(1,7)) ]:
            with open("error.txt","w",encoding="utf-8") as file:
                file.write("PLEASE ENTER YOUR CHOİCE CORRECTLY")
            os.system("error.txt")
            self.panel()

        elif choice == "1":
            self.Immersive_Products()
        elif choice == "2":
            self.Jobs()
        elif choice == "3":
            self.News()
        elif choice == "4":
            self.Nutrition_Information()
        elif choice == "5":
            self.Popular_Destinations()
        elif choice == "6":
            self.Courses()

        

    def Immersive_Products(self):
        params = Immersive_Products_param_taker(self.param_taker_func , self.domain_setter_func)
     
        obje = Immersive_Products_API(parameters=params)
        obje.url_maker()
        obje.data_taker()
     
        datas = obje.clear_data_maker()
        self.data_writter_func(datas=datas,params=obje.params)
        
        time.sleep(3)

        self.panel()
    
    
    def Jobs(self):
        params = Jobs_param_taker(self.param_taker_func , self.domain_setter_func)
        count_of_job = job_count(self.param_taker_func)
       
        obje = Jobs_apı(params=params,job_count=count_of_job)
        obje.url_maker()
        obje.data_taker()
        obje.data_count_controller()
       
        datas = obje.clear_data_maker()
        self.data_writter_func(datas=datas,params=obje.params)
        
        time.sleep(3)
        
        self.panel()
    
    
    def News(self):
        params = News_param_taker(self.param_taker_func , self.domain_setter_func)
        
        obje = news_api(params=params)
        obje.url_maker()
        obje.data_taker()
        
        datas = obje.clear_data_maker()
        self.data_writter_func(datas=datas,params=obje.params)
        
        time.sleep(3)
                
        self.panel()
    
    
    def Nutrition_Information(self):
        params = Nutrition_Information_param_taker(self.param_taker_func , self.domain_setter_func)
        
        obje = Nutrition_Information_api(params=params)
        obje.url_maker()
        obje.datas_taker()
        
        datas = obje.clear_data_maker()
        self.data_writter_func(datas=datas,params=obje.params)     
        
        time.sleep(3)
        
        self.panel()
    
    
    def Popular_Destinations(self):
        params = Popular_Destinations_parameters(self.param_taker_func , self.domain_setter_func)
        destination_count = count_Destination(param_taker=self.param_taker_func)
        
        obje = Popular_Destinations_api(params=params,destination_count=destination_count)
        obje.url_maker()
        obje.data_taker()
        obje.data_count()
        
        datas = obje.clear_data_maker()
        self.data_writter_func(datas=datas,params=obje.params)
        
        time.sleep(3)
        
        self.panel()


    def Courses(self):
        params = Courses_param_taker(self.param_taker_func , self.domain_setter_func)
        count_of_course = course_count(param_taker=self.param_taker_func)
        
        obje = courses_api(params=params,course_count=count_of_course)
        obje.url_maker()
        obje.data_taker()
        obje.count_controller()
        
        datas = obje.clear_data_maker()
        self.data_writter_func(datas=datas,params=obje.params)
        
        time.sleep(3)
        
        self.panel()

x = main(param_taker_func=param_taker , domain_setter_func= domain_setter , data_writter_func= data_writer)
x.panel()

