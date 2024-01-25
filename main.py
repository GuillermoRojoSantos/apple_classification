# rfc -> Random Forest Classifier
# lgr -> Logistic Regression
# nvb -> Naive Bayes
import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Apple Classification", layout="wide")
st.title("Clasificador de manzanas :apple:")

st.markdown('''
Gracias a este modelo, vas a poder clasificar una manzana :apple:! (**buena** :apple: o **mala** :apple:)
en base a distintos parámetros como: *Tamaño, Peso, Dulzor, Crujiente, Jugosidad, Madurez, Acidez.*


Además, te damos la psoibilidad de elegir 1 de nuestros **3** modelos para clasificar tu manzana!!
 ''')

st.markdown('''
Podras elegir entre: 
* Random Forest Classifier 
* Logistic Regression 
* Naive Bayes (GausianNB)
''')

st.divider()

st.subheader("Parámetros de la :apple:")

col1, col2, col3, col4 = st.columns(4)
# col1:
Size = col1.number_input("Tamaño", min_value=-6.00, max_value=5.00,value=0.0)
# col2:
Weight = col2.number_input("Peso",min_value=-6.00,max_value=4.00,value=0.0)
# col3:
Sweetness = col3.number_input("Dulzor",min_value=-6.00,max_value=6.00,value=0.0)
# col4:
Crunchiness = col4.number_input("Crujiente",min_value=-6.00,max_value=4.00,value=0.0)


col1b, col2b, col3b = st.columns(3)
# col1b:
Juiciness = col1b.number_input("Jugosidad", min_value=-6.00, max_value=6.00,value=0.0)
# col2b:
Ripeness = col2b.number_input("Madurez",min_value=-5.00,max_value=6.00,value=0.0)
# col3b:
Acidity = col3b.number_input("Acidez",min_value=-6.00,max_value=7.00,value=0.0)

st.divider()

st.subheader("Selección del Modelo :robot_face:")

models_dict = {"Random Forest Classifier":1,"Logistic Regression":2,"Naive Bayes":3}

model_choice = st.selectbox("Seleccione un modelo para usar",[x for x in models_dict.values()])

st.divider()
if st.button("Clasificar :apple:"):
    if model_choice == 1:
        model = joblib.load("./models/rfc.pkl")
    elif model_choice == 2:
        model = joblib.load("./models/lgr.pkl")
    else:
        model = joblib.load("./models/nvb.pkl")

    p = {
        'Size': [Size],
        'Weight': [Weight],
        'Sweetness': [Sweetness],
        'Crunchiness': [Crunchiness],
        'Juiciness': [Juiciness],
        'Ripeness': [Ripeness],
        'Acidity': [Acidity]
    }
    p = pd.DataFrame(p)
    res = model.predict(p)

    if(res == 1):
        st.write("Enhorabuena!! Tu :apple: es de buena calidad!!")
    else:
        st.write("Vaya, lo sentimos... Tu :apple: no parece que sea de buena calidad...")