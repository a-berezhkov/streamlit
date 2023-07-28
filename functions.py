import pandas as pd
import model


# Если необходимы другие датасеты подулючить, поменять пути
PATH_TO_VISITS_CSV_FILE = "csv/visits.csv"

label_encoder = model.load_encoder_model()

def get_country_list()->list:
    '''
    Получаем список уникальных стран
    '''
    visits = pd.read_csv(PATH_TO_VISITS_CSV_FILE)
    return visits["Region"].unique() 


    return 


def get_device_list()->list:
    '''
    Получаем список уникальных устройства
    '''
    visits = pd.read_csv(PATH_TO_VISITS_CSV_FILE)
    return visits["Device"].unique() 

def get_channel_list()->list:
    '''
    Получаем список каналов продвижения
    '''
    visits = pd.read_csv(PATH_TO_VISITS_CSV_FILE)
    return visits["Channel"].unique() 

 