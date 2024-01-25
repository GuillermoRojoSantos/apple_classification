# rfc -> Random Forest Classifier
# lgr -> Logistic Regression
# nvb -> Naive Bayes
import streamlit as st
import joblib

st.set_page_config(page_title="Apple Classification", layout="wide")
st.title("Clasificador de manzanas :apple:")

st.markdown('''
Gracias a este modelo, vas a poder clasificar una manzana :apple:! (**buena** :apple: o **mala** :apple:)
en base a distintos parámetros como: *Tamaño, Peso, Dulzor, Crujiente, Jugosidad, Madurez, Acidez, Calidad.*


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
size = col1.number_input("Tamaño", min_value=-6, max_value=5)

# col2:
weight = col2.number_input("Peso",min_value=-6,max_value=4)