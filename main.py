from Immersive_Products import *
from file_funcs import *
from parameter_bringer import *



params = Immersive_Products_parameters(param_taker=param_taker , domain_setter= domain_setter)
obje = Immersive_Products(parameters=params) 
obje.url_maker()
obje.data_taker()
datas = obje.clear_data_maker()
data_writer(datas=datas)


