import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Study Hours Analysis", page_icon="📚", layout="wide")
st.title("📚 Students Study Hours Analysis Dashboard")
st.caption("Analyze study habits and academic performance.")
uploaded = st.sidebar.file_uploader("Upload CSV (optional)", type=["csv"])
data = pd.read_csv(uploaded) if uploaded else pd.read_csv("students.csv")
st.sidebar.header("Filters")
genders=st.sidebar.multiselect("Gender",sorted(data.Gender.unique()),default=sorted(data.Gender.unique()))
ages=st.sidebar.slider("Age",int(data.Age.min()),int(data.Age.max()),(int(data.Age.min()),int(data.Age.max())))
results=st.sidebar.multiselect("Result",sorted(data.Final_Result.unique()),default=sorted(data.Final_Result.unique()))
d=data[data.Gender.isin(genders)&data.Age.between(*ages)&data.Final_Result.isin(results)]
if d.empty:
    st.warning("No records match the filters."); st.stop()
a,b,c,e,f=st.columns(5)
a.metric("Students",len(d)); b.metric("Avg study hours",f"{d.Study_Hours.mean():.1f}")
c.metric("Avg exam score",f"{d.Exam_Score.mean():.1f}"); e.metric("Pass rate",f"{100*d.Final_Result.eq('Pass').mean():.1f}%")
f.metric("Avg sleep hours",f"{d.Sleep_Hours.mean():.1f}")
x,y=st.columns(2)
with x:
    st.plotly_chart(px.scatter(d,x="Study_Hours",y="Exam_Score",color="Final_Result",hover_data=["Student_ID"],trendline="ols",title="Study hours vs exam score"),use_container_width=True)
with y:
    t=d.copy(); t["Study_Group"]=pd.cut(t.Study_Hours,[0,2,4,6,8,10.1],labels=["0-2","2-4","4-6","6-8","8-10"],include_lowest=True)
    g=t.groupby("Study_Group",observed=False).Exam_Score.mean().reset_index()
    st.plotly_chart(px.bar(g,x="Study_Group",y="Exam_Score",title="Average score by study-hour group"),use_container_width=True)
x,y=st.columns(2)
with x:
    counts=d.Final_Result.value_counts().rename_axis("Result").reset_index(name="Students")
    st.plotly_chart(px.pie(counts,names="Result",values="Students",hole=.5,title="Pass vs fail"),use_container_width=True)
with y:
    st.plotly_chart(px.scatter(d,x="Sleep_Hours",y="Exam_Score",color="Gender",title="Sleep hours vs exam score"),use_container_width=True)
st.subheader("Student records")
st.dataframe(d,use_container_width=True,hide_index=True)
st.download_button("Download filtered CSV",d.to_csv(index=False),"filtered_students.csv","text/csv")
