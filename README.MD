# Описание проекта

Интрумент предоставлят возможность осущетсвлять различные предскзаания и визуализацию.
Всегда можно доработать - доки тут - https://docs.streamlit.io/library/api-reference

Важно! Иногда проект может немного долго грузитья 

### Струтктура

```

app.py - приложение на основе streamlit
functions.py - API  в виде фцнкций с методами для выборки данных
model.py - API для использования итоговой модели в виде фцнкций с методами для классификации и загрузки моделей
/csv - файлы с исходными данными
/models - модель классификатора и моджель кодировщика
/ml - jupyter notebook + исходные данные

```

# Запуск проекта

## Установите зависимости, если онм не установлены

```
pip install joblib
pip install streamlit
pip install pandas 
 

```


## Запустите flask API

## Запустите основное приложение из диретории проекта

```

streamlit run app.py

```

После запуска будет показана ссылка по которой необходимо перейти

```

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://172.25.221.108:8501

  ```

  В выпадающем меню выберите:

  - страну

  - канал продвижения

  - тип платформы

  И нажмите кнопку "Предсказать".
 
