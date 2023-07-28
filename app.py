import streamlit as st
import joblib
import pandas as pd


import functions
import model

 

# Стили для результа кластеризации 
cluster_message_style_blue = """
        background-color: white;
        color: blue;
        font-weight: bold;
        padding: 8px 16px;
        border-radius: 5px;
        text-align: center;
    """
cluster_message_style_red = """
        background-color: white;
        color: red;
        font-weight: bold;
        padding: 8px 16px;
        border-radius: 5px;
        text-align: center;
    """

 

html = """
    <h2> Инструкция по работе с системой </h2>
    В выпадающем меню выберите:
    <ul>
        <li>страну</li>
        <li>канал продвижения</li>
        <li>тип платформы</li>
    </ul>
    И нажмите кнопку "Предсказать".
    """
st.write(html,unsafe_allow_html=True)
 




st.write("<h1>Предсказание сегмента пользоватля</h1>",unsafe_allow_html=True) # Вывод заголовка страницы

st.write("Введите данные ")

country = st.selectbox("Select country ",functions.get_country_list()) #select страна 
channel = st.selectbox("Select channel ",functions.get_channel_list()) #select канад продвижения
device	 = st.selectbox("Select device ",functions.get_device_list()) #select устрйоство




if st.button('Предсказать*', key="p"):
     with st.spinner("Классификация в процессе..."): # показываем прелоадер

        df = model.make_df_for_segment(channel=channel, region = country, device=device) # получаем данные из полей и формируем датафрейм
        predicted_segment = model.make_predict_segment(df = df) #  делаем предсказание
        st.write("<h2>Прогноз<h2> ",unsafe_allow_html=True)
        if  predicted_segment[0]== 0: # если выдало перввый кластер

            st.write("<div style='" + cluster_message_style_red+ "'> Высокая стоимость привлечения органических пользователей</div>",unsafe_allow_html=True)
        else:
            st.write("<div style='" + cluster_message_style_blue + "'> Низкая стоимость привлечения органических пользователей</div>" ,unsafe_allow_html=True)

st.write("<h2>Для получния прогноза по новым данным в реальном времени измените поля и нажмите кнопку 'Предсказать'<h2> ",unsafe_allow_html=True)  
     

st.write('<small> * так как сегменты определены неккоретно, не ждите хороших результатов </small>',unsafe_allow_html=True)