import joblib
import pandas as pd

def load_encoder_model(path = "models/label_encoder.pkl"):
    '''
    Загрузка модели для декодинга 
    :param str path: Путь к модели классификации, по-умолчанию  "models/label_encoder.pkl"
    '''
    return joblib.load(path)

def make_df_for_segment(channel = "organic", device = "PC", region = "France", month = 0, payer = True):
    """
    Фцнкция создает фрейм  для определения сегмента
    :param str channel: Название канала продвижения 
    :param str device: Название устройства
    :param str region: Название страны
    :param int  month: Месяц (от 1 до 12)
    :param bool  payer: Признак платящих пользователей
    """
    return  pd.DataFrame({
        "channel" : channel,
        "device" : device,
        "region" : region,
        "month" : month, 
        "payer" : payer

    }, index=[0])

def make_predict_segment(model_path = "models/segment_classificator.pkl", df = pd.DataFrame({}))->list:
    '''
    Функция предсказывает кластер для новых данных 
    :param str model_path: Путь к модели классификации, по-умолчанию  "models/segment_classificator.pkl"
    :param DataFrame df: датафрейм с даннными для классификации
        Пример данных:
         pd.DataFrame({
                "channel" : channel,
                "device" : device,
                "region" : region,
                "month" : month, 
                "payer" : payer
    }, index=[0])
    :return: list Номера кластеров
    '''
    model = joblib.load(model_path) # доступ к модели классификации для прогнозирования
    columns_to_encode = ['channel', 'device', 'region', 'payer']
    for column in columns_to_encode:
        encoder = load_encoder_model()
        print(encoder['channel'].classes_)
        print(encoder)
        df[column] = encoder[column].transform(df[column])
    predict = model.predict(df)
    return predict