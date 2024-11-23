import streamlit as st
import pandas as pd

df_mezun = pd.read_excel("streamlibs_data_tr.xlsx", sheet_name="df_mezun")
df_yetenekler = pd.read_excel("streamlibs_data_tr.xlsx", sheet_name="df_yetenekler")


st.set_page_config("Sana en uygun mesleği bul!",page_icon="🎓", layout="wide")

uploaded_file = st.file_uploader("CV'ni Yükle")

if uploaded_file != None:
    st.write("Otomatik doldurulamadı!")

form_values = {
    "grad": None,
    "skills": None
}


with st.form("Özgeçmiş Formu"):
    form_values["grad"] = st.selectbox("Bölümün: ",options=df_mezun.iloc[:,1].unique(),index=None)
    form_values["skills"] = st.multiselect("Mevcut Yeteneklerin: ",options=df_yetenekler.iloc[:,1].unique())

    submit_button = st.form_submit_button("Sorgula")
    if submit_button:
        if not all(form_values.values()):
            st.warning("Tüm bölümleri doldurun!")
        else:
            suggestions = df_mezun[df_mezun["Mezun Olunan Bolum"]==form_values["grad"]].iloc[:,[0,2]]
            merged_df = pd.merge(suggestions, df_yetenekler, on="Meslek", how="inner")
            merged_df = merged_df[merged_df.apply(lambda row: any(yet in row["Yetenekler"] for yet in form_values["skills"]),axis=1)]    
            final_df = merged_df.groupby("Meslek").agg(Yetenekler=("Yetenekler", lambda x: ", ".join(set(x))),Yuzde=("Yuzde", "sum")).reset_index()
            final_df.rename(columns={"Yuzde": "Toplam Skor"}, inplace=True)
            final_df = final_df.sort_values(by="Toplam Skor", ascending=False)
            st.dataframe(final_df,hide_index=True)
            
            
