import streamlit as st
import pandas as pd
import altair as alt

project_Name = "Kariyer Planlama"

df_maas = pd.read_excel("streamlibs_data_tr.xlsx", sheet_name="df_maas")
df_sektor = pd.read_excel("streamlibs_data_tr.xlsx", sheet_name="df_sektor")
df_mezun = pd.read_excel("streamlibs_data_tr.xlsx", sheet_name="df_mezun")
df_yetenekler = pd.read_excel("streamlibs_data_tr.xlsx", sheet_name="df_yetenekler")
df_search_bar = df_maas.iloc[:,0]

st.set_page_config(project_Name,page_icon="🎓", layout="wide")


with st.columns(3)[1]:
    st.title(project_Name,anchor=None)
result = st.selectbox("Meslek seçiniz: ", df_search_bar,index=None,placeholder="Mesleğin adını giriniz")

if result != None:
    
    maas = df_maas[df_maas["Meslek"] == result]
    st.subheader("Maaş Dağılımı",divider="gray")
    st.write(f"Ankete katılan {maas.iloc[0,4]} kişiden elde edilen bilgiler ile hesaplanmıştır")
    st.bar_chart(maas.iloc[0,1:4],horizontal=True,stack=False,height=200,color="#00C000")
    st.subheader("En çok mezun olunan bölümler",divider="gray")
    st.bar_chart(df_mezun[df_mezun["Meslek"]==result].iloc[:,1:],x="Mezun Olunan Bolum",y="Yuzde",horizontal=True,x_label="",y_label="",stack=False,height=300,color="#00C000")
    st.subheader("En çok çalışılan sektörler",divider="gray")
    st.bar_chart(df_sektor[df_sektor["Meslek"]==result].iloc[:,1:],x="Sektor",y="Yuzde",horizontal=True,x_label="",y_label="",stack=False,height=300,color="#00C000")
    st.subheader("Öngörülen yetkinlikler",divider="gray")
    yetenekler = df_yetenekler[df_yetenekler["Meslek"]==result].iloc[:,1:].reset_index()
    st.table(yetenekler["Yetenekler"])

    
