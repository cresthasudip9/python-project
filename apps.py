import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
col1, col2 =st.columns(2)
with col1:
    st.image("./images/ss.jpg", width=500)
    with col2:
        st.title("sudeep shrestha")
        content ="""
        Neymar da Silva Santos Júnior, commonly known as Neymar, is a Brazilian professional footballer born on February 5, 1992, in Mogi das Cruzes, Brazil. 
        He began his career at Santos FC, where his impressive performances caught the attention of top European clubs. 
        In 2013, he joined FC Barcelona, forming a formidable attacking trio with Lionel Messi and Luis Suárez. Neymar's skill, flair,
          and goal-scoring ability helped Barcelona secure numerous titles, including the UEFA Champions League in 2015. In 2017, 
          he made a record-breaking transfer to Paris Saint-Germain (PSG) for €222 million. Known for his dribbling, creativity, and playmaking,
            Neymar is also a key player for the Brazilian national team, contributing significantly in various international tournaments.
        """ 
        st.info(content)
content_2 ="""
Here are some of my projects that i have create while doing  python course:
"""
st.write(content_2)

col3, empty_col,col4 =st.columns([1.5,0.5,1.5])
df = pd.read_csv("./data.csv",sep=";")
with col3:
    for index,row in df[:10].iterrows():
        st.header (row["title"])
        st.write (row["description"])
        st.image ("images/"+row["image"])
        st.write(f"[source code]({row["url"]})")

with col4:
      for index,row in df[10:].iterrows():
        st.header (row["title"])
        st.write (row["description"])
        st.image ("images/"+row["image"])
        st.write(f"[source code]({row["url"]})")

