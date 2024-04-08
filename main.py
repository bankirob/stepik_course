#C:\Users\Администратор\PycharmProjects\stepik.org-course-194633
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Загрузка данных с учетом строк с комментариями и указанием заголовков
df = pd.read_csv("venv\\food_prices_ind.csv", comment='#')

# Переименование столбцов, чтобы использовать корректные названия
df.columns = ['date', 'admin1', 'admin2', 'market', 'latitude', 'longitude', 'category', 'commodity', 'unit', 'priceflag', 'pricetype', 'currency', 'price', 'usdprice']


# Отфильтрованные данные
#df = df.query('commodity == "Rice"')
selected_category = st.radio("Выберите категорию", df['category'].unique())
if selected_category == 'cereals and tubers':
    df = df.query('category == "cereals and tubers"')

elif selected_category == 'miscellaneous food':
    df = df.query('category == "miscellaneous food"')
elif selected_category == 'oil and fats':
    df = df.query('category == "oil and fats"')
elif selected_category == 'vegetables and fruits':
    df = df.query('category == "vegetables and fruits"')
elif selected_category == 'pulses and nuts':
    df = df.query('category == "pulses and nuts"')
elif selected_category == 'milk and dairy':
    df = df.query('category == "milk and dairy"')

selected_regions = st.multiselect("Выберите регионы", df['admin2'].unique())

df = df.query('price > 1000')



clicked = st.button('Цена от 1000 рупий')
if clicked:
    df = df.query('price > 2000')


option = st.selectbox('Выберите регион', ['Delhi', 'Mumbai city', 'Chennai', 'Patna'])
if option == 'Delhi':
    df = df.query('admin2 =="Delhi"')
elif option == 'Chennai':
    df = df.query('admin2 =="Chennai"')
elif option == 'Mumbai city':
    df = df.query('admin2 =="Mumbai city"')
elif option == 'Patna':
    df = df.query('admin2 =="Patna"')
#else:
price_threshold = st.slider("Выберите пороговую цену", min_value=0, max_value=5000, value=5000)
df = df.query('price < @price_threshold')


# Построение гистограммы
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df['price'], bins=30, color='skyblue', edgecolor='black')



#df = df.query('price > 1000')


# Отображение графика и отфильтрованных данных
st.pyplot(fig)
st.write("Значения таблицы:", df)
