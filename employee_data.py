import streamlit as st
import pandas as pd
from PIL import Image
import altair as alt
from bokeh.plotting import figure
import matplotlib.pyplot as plt

image=Image.open("gm.jpg")
st.image(image,caption="General Motors")
st.title("Employee data")
st.text("Aqui se muestran los KPIs de los empleados")
upload_file=st.file_uploader("upload your file here")
if upload_file:
    st.header("Estadisticos")
    df=pd.read_csv(upload_file)
    st.write(df.describe())
    selected_class=st.radio("Select class",df["gender"].unique())
    st.write("Selected Class:",selected_class)
    st.header("Data header")
    st.write(df.head())
    optionals=st.expander("Optional Condigurations",True)
    fare_selected=optionals.slider("Select range",min_value=float(df["performance_score"].min()),max_value=float(df["performance_score"].max()))
    subset_fare=df[(df["performance_score"]>=fare_selected)]
    st.write(f"performance_score{fare_selected}:{subset_fare.shape[0]}")
    selected_class=st.radio("Select class",df["marital_status"].unique())
    st.write("Selected Class:",selected_class)
    



