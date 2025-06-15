import pandas as pd
import pickle
import cloudpickle
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
try:
    st.title('Калькулятор запасов - Таганское, запад')
    u = st.checkbox('Задать участок')
    if u:
        num444 = 1
        st.image("west_n.png", caption="Западный участок ТМ")

        left = st.slider('left', 14716000, 14717400)
        top = st.slider('top', 5267300, 5267900)
        right = st.slider('right', 14717400, 14716000)
        bottom = st.slider('bottom', 5267900, 5267300)

        L = round((left - 14715755.24)/1.426, 0)
        R = round((right - 14715755.24)/1.426, 0)
        T = round((top - 5267188.06)/1.41, 0)
        B = round((bottom - 5267188.06)/1.41, 0)


    ##    L = round((14716000 - 14715755.24)/1.426, 0)
    ##    R = round((14717400 - 14715755.24)/1.426, 0)
    ##    T = round((5267300 - 5267188.06)/1.41, 0)
    ##    B = round((5267900 - 5267188.06)/1.41, 0)

        aa = [(L,T), (R,T), (R,B), (L,B)]
        bb = [(R,T), (R,B), (L,B), (L,T)]

        if st.button('Создать'):
        #st.image("C:\\west\\west_n.png", caption="Sunrise by the mountains")
            ima = Image.open("west_n.png")
            img = ima.crop((L, T, R, B))  
            st.image(img)
    else:
        num444 = 0
        L = round((14716000 - 14715755.24)/1.426, 0)
        R = round((14717400 - 14715755.24)/1.426, 0)
        T = round((5267300 - 5267188.06)/1.41, 0)
        B = round((5267900 - 5267188.06)/1.41, 0)

        aa = [(L,T), (R,T), (R,B), (L,B)]
        bb = [(R,T), (R,B), (L,B), (L,T)]
        
    s = st.checkbox('Классификация сырья')
    if s:
        num666 = 1
        rates = {'ГНБ':'G', 'Литейка':'L', 'OCMA':'O', 'Гидроизоляция':'I','ГОК':'K'}
        R_ = st.selectbox('Цель классификации', list(rates))
        R = [rates[R_]]
        print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        print(R)
        sw = st.number_input('Точность', min_value = 0.0, max_value = 1.0, value = 0.5, step = 0.05)
    else:
        num666 = 0
        sw = 0.5
    num555 = 0
    n = st.checkbox('Полные данные')
    if n:
        num777 = 1
    else:
        num777 = 0
    n1 = st.checkbox('Выбрать горизонт_1')
    if n1:
        num0 = []
        a11 = st.number_input('Горизонт_1', min_value = 3, max_value = 16, value = 3, step = 1)
        num0.append(a11)
        n11 = st.checkbox('Добавить горизонт_2')
        if n11:
            num0.append(st.number_input('Горизонт_2', min_value = 3, max_value = 16, value = 3, step = 1))
            n12 = st.checkbox('Добавить горизонт_3')
            if n12:
                num0.append(st.number_input('Горизонт_3', min_value = 3, max_value = 16, value = 3, step = 1))
                n13 = st.checkbox('Добавить горизонт_4')
                if n13:
                    num0.append(st.number_input('Горизонт_4', min_value = 3, max_value = 16, value = 3, step = 1))
                    n14 = st.checkbox('Добавить горизонт_5')    
                    if n14:
                        num0.append(st.number_input('Горизонт_5', min_value = 3, max_value = 16, value = 3, step = 1))
                        n15 = st.checkbox('Добавить горизонт_6')
                        if n15:
                            num0.append(st.number_input('Горизонт_6', min_value = 3, max_value = 16, value = 3, step = 1))
                            n16 = st.checkbox('Добавить горизонт_7')
                            if n16:
                                num0.append(st.number_input('Горизонт_7', min_value = 3, max_value = 16, value = 3, step = 1))
    else:
        num0 = [0]

    n2 = st.checkbox('Ключевой параметр')
    if n2:
        rates1 = {'Влажность':2, 'Песок':3, 'Индекс набухания':4, 'Электропроводность':5,'Монтмориллонит':7, 'КОЕ':6}
        num111_ = st.selectbox('Ключевой параметр', list(rates1))
        num111 = [rates1[num111_]]
        if num111 == [2]:
            g = 'Влажность'
            g1 = 'Влажность'
        elif num111 == [3]:
            g = 'Песок'
            g1 = 'Песок'
        elif num111 == [4]:
            g = 'Индекс'
            g1 = 'Индекс'
        elif num111 == [5]:
            g = 'Электропроводность'
            g1 = 'Электропроводность'
        elif num111 == [6]:
            g = 'КОЕ'
            g1 = 'КОЕ'
        elif num111 == [7]:
            g = 'Монтмориллонит'
            g1 = 'Монтмориллонит'
    else:
        num111 = [0]
        g = 'Hor'
        g1 = 'Horizont'
    m1 = st.checkbox('Задать пределы влажности')
    if m1:
        num1 = []
        num1.append(st.number_input('min', min_value = 10.0, max_value = 40.0, value = 10.0, step = 5.0))
        num1.append(st.number_input('max', min_value = 10.0, max_value = 40.0, value = 10.0, step = 5.0))
    else:
        num1 = [0]
    m2 = st.checkbox('Задать пределы песка')
    if m2:
        num2 = []
        num2.append(st.number_input('min', min_value = 0.0, max_value = 10.0, value = 0.0, step = 0.5))
        num2.append(st.number_input('max', min_value = 0.0, max_value = 10.0, value = 0.0, step = 0.5))
    else:
        num2 = [0]
    m3 = st.checkbox('Задать пределы индекса набухания')
    if m3:
        num3 = []
        num3.append(st.number_input('min', min_value = 5.0, max_value = 30.0, value = 5.0, step = 5.0))
        num3.append(st.number_input('max', min_value = 5.0, max_value = 30.0, value = 5.0, step = 5.0))
    else:
        num3 = [0]    
    m4 = st.checkbox('Задать пределы электропроводности')
    if m4:
        num4 = []
        num4.append(st.number_input('min', min_value = 20, max_value = 200, value = 20, step = 30.0))
        num4.append(st.number_input('max', min_value = 20, max_value = 200, value = 20, step = 30.0))
    else:
        num4 = [0]
    m11 = st.checkbox('Задать пределы монтмориллонита')
    if m11:
        num11 = []
        num11.append(st.number_input('min', min_value = 30, max_value = 100, value = 30, step = 10))
        num11.append(st.number_input('max', min_value = 30, max_value = 100, value = 30, step = 10))
    else:
        num11 = [0]

    m10 = st.checkbox('Задать пределы КОЕ')
    if m10:
        num10 = []
        num10.append(st.number_input('min', min_value = 30, max_value = 100, value = 30, step = 10))
        num10.append(st.number_input('max', min_value = 30, max_value = 100, value = 30, step = 10))
    else:
        num10 = [0]

    ###отметка о необходимости классификации по функциональности
    ###num666 = 1
    ##num666 = float(input('Классификация сырья по функциональности: '))
    ### тип классификации
    ###R = ['O']
    ##R = [input('Тип классификации: ')]
    ###ТОЧНОСТЬ
    ###sw = 0.5
    ##sw = float(input('Введите точность: '))
    ### отметка о построении вклада в LM модель классификации по функциональности сырья
    ##num555 = 0
    ### отметка об использовании полного датасета
    ###num777 = 0
    ##num777 = float(input('Полный df: '))
    ### список горизонтов
    ###num0 = [0]
    ##num0 = input('горизонты: ')
    ##num0 = num0.split(sep=',')
    ##num0 = [int(i) for i in num0]
    ### выбор параметра для расчета
    ###num111 = [0]
    ##num111 = [int(input('ключевой параметр: '))]
    ### отметка о построении вырезки 
    ###num444 = 1
    ##num444 = float(input('использовать глайдеры: '))
    ### влажность
    ###num1 = [0]
    ##num1 = input('влажность: ')
    ##num1 = num1.split(sep = ',')
    ##num1 = [float(i) for i in num1]
    ### песок
    ###num2 = [0]
    ##num2 = input('песок: ')
    ##num2 = num2.split(sep = ',')
    ##num2 = [float(i) for i in num2]
    ### индекс
    ###num3 = [0]
    ##num3 = input('индекс: ')
    ##num3 = num3.split(sep = ',')
    ##num3 = [float(i) for i in num3]
    ### электро
    ###num4 = [0]
    ##num4 = input('электро: ')
    ##num4 = num4.split(sep = ',')
    ##num4 = [float(i) for i in num4]
    ### монт
    ###num11 = [0]
    ##num11 = input('монт: ')
    ##num11 = num11.split(sep = ',')
    ##num11 = [float(i) for i in num11]
    ### кое
    ###num10 = [0]
    ##num10 = input('кое: ')
    ##num10 = num10.split(sep = ',')
    ##num10 = [float(i) for i in num10]
    ### цвет палитры
    ##color = 3
    ### признак нужности выбор палитры
    ##colo = 1
    with open('ddf.pkl', 'rb') as f:
        d = pickle.load(f)
    ddf = pickle.loads(d)

    if st.button('Расчет'):
        
        if num444 != 0:
            if num111[0] != 0:
                if num666 != 0:
                    r2, roc, pres, rec, S_R, VO, df_n, FX_m, ass = ddf(aa, bb, num666, R, num555, num777, num0, num111, num444, num1, num2, num3, num4, num11, num10, sw)
                    st.success(f'Объем сырья: {VO}')
                    st.success(f'Площадь участка: {S_R}')
                    st.warning(f'качество модели: {r2}')
                    st.warning(f'качество классификации сырья: {roc}')
                    st.warning(f'точность класса: {pres}')
                    st.warning(f'полнота класса: {rec}')
                    print(r2, roc, pres, rec, S_R, VO, df_n[:3], FX_m[:3], ass[:3])
                else:
                    
                    r2, S_R, VO, df_n, FX_m, ass = ddf(aa, bb, num666, R, num555, num777, num0, num111, num444, num1, num2, num3, num4, num11, num10, sw)
                    st.success(f'Объем сырья: {VO}')
                    st.success(f'Площадь участка: {S_R}')
                    st.warning(f'качество модели: {r2}')
                    print(r2, S_R, VO, df_n[:3], FX_m[:3], ass[:3])
            else:
                if num666 != 0:
                    r2_, roc, pres, rec, S_R, VO, df_n, FX_m, ass = ddf(aa, bb, num666, R, num555, num777, num0, num111, num444, num1, num2, num3, num4, num11, num10, sw)
                    st.success(f'Объем сырья: {VO}')
                    st.success(f'Площадь участка: {S_R}')
                    st.warning(f'качество модели: {r2_}')
                    st.warning(f'качество классификации сырья: {roc}')
                    st.warning(f'точность класса: {pres}')
                    st.warning(f'полнота класса: {rec}')
                    print(r2_, roc, pres, rec, S_R, VO, df_n[:3], FX_m[:3], ass[:3])
                else:
                    r2_, S_R, VO, df_n, FX_m, ass = ddf(aa, bb, num666, R, num555, num777, num0, num111, num444, num1, num2, num3, num4, num11, num10, sw)
                    st.success(f'Объем сырья: {VO}')
                    st.success(f'Площадь участка: {S_R}')
                    st.warning(f'качество модели: {r2_}')
                    print(r2_, S_R, VO, df_n[:3], FX_m[:3], ass[:3])
        else:
            if num111[0] != 0:
                if num666 != 0:
                    r2, roc, pres, rec, S4, V1, df_n, FX_m, ass = ddf(aa, bb, num666, R, num555, num777, num0, num111, num444, num1, num2, num3, num4, num11, num10, sw)
                    st.success(f'Объем сырья: {V1}')
                    st.success(f'Площадь участка: {S4}')
                    st.warning(f'качество модели: {r2}')
                    st.warning(f'качество классификации сырья: {roc}')
                    st.warning(f'точность класса: {pres}')
                    st.warning(f'полнота класса: {rec}')
                    print(r2, roc, pres, rec, S4, V1, df_n[:3], FX_m[:3], ass[:3])
                else:
                    r2, S4, V1, df_n, FX_m, ass = ddf(aa, bb, num666, R, num555, num777, num0, num111, num444, num1, num2, num3, num4, num11, num10, sw)
                    st.success(f'Объем сырья: {V1}')
                    st.success(f'Площадь участка: {S4}')
                    st.warning(f'качество модели: {r2}')
                    print(r2, S4, V1, df_n[:3], FX_m[:3], ass[:3])
            else:
                if num666 != 0:
                    r2_, roc, pres, rec, S4, V1, df_n, FX_m, ass = ddf(aa, bb, num666, R, num555, num777, num0, num111, num444, num1, num2, num3, num4, num11, num10, sw)
                    st.success(f'Объем сырья: {V1}')
                    st.success(f'Площадь участка: {S4}')
                    st.warning(f'качество модели: {r2_}')
                    st.warning(f'качество классификации сырья: {roc}')
                    st.warning(f'точность класса: {pres}')
                    st.warning(f'полнота класса: {rec}')
                    print(r2_, roc, pres, rec, S4, V1, df_n[:3], FX_m[:3], ass[:3])
                else:
                    r2_, S4, V1, df_n, FX_m, ass = ddf(aa, bb, num666, R, num555, num777, num0, num111, num444, num1, num2, num3, num4, num11, num10, sw)
                    st.success(f'Объем сырья: {V1}')
                    st.success(f'Площадь участка: {S4}')
                    st.warning(f'качество модели: {r2_}')
                    print(r2_, S4, V1, df_n[:3], FX_m[:3], ass[:3])


        

               
        x = df_n['X']
        y = df_n['Y']
        z = df_n['Z_']
        c = df_n[g]
        fig = px.scatter_3d(x=x, y=y, z=z, color=c, size_max=2, opacity=0.7, color_continuous_scale=['pink', 'red', "orange", "yellow",
                                              "green", "blue", 'indigo', 'violet',
                                             "purple"])
        fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig)

        x1 = FX_m['X']
        y1 = FX_m['Y']
        z1 = FX_m['Z_']
        c1 = FX_m[g1]
        fig1 = px.scatter_3d(x=x1, y=y1, z=z1, color=c1, size_max=2, opacity=0.7, color_continuous_scale=['pink', 'red', "orange", "yellow",
                                              "green", "blue", 'indigo', 'violet',
                                             "purple"])
        fig1.update_layout(margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig1)

       

        fig1 = px.scatter_3d(FX_m, x=x1, y=y1, z=z1, color=c1, size_max=2, opacity=0.7, color_continuous_scale='Reds')
        fig2 = px.scatter_3d(df_n, x=x, y=y, z=z, color=c, size_max=2, opacity=0.7, color_continuous_scale='Reds')
        
        
        fig = go.Figure(data = fig1.data + fig2.data)
        fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig)



except:
    st.error("Ошибка загрузки данных, вероятно выбранный участок за пределами месторождения")
#finally:
 #   st.error('Вероятно выбранный участок за пределами месторождения') 
       
##                   
##
