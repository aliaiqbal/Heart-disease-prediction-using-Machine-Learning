#import libraries
import streamlit as st
import pickle
import pandas as pd
#Headings
st.title("Heart disease prediction")
#Function
def user_report():
 age=st.slider('Age', 29, 77,54,disabled=False)
 sex=st.selectbox('sex', ['0', '1'])
 cpt=st.selectbox('Chest pain type', ['0', '1','2','3'])
 bp=st.slider('BP', 94, 200,80, disabled=False)
 cholesterol=st.slider('Cholesterol', 126, 564,249, disabled=False)
 fbs=st.selectbox('FBS over 120', ['0', '1'])
 ekg=st.selectbox('EKG results', ['0', '1','2'])
 max_hr=st.slider('Max HR', 71, 202,149, disabled=False)
 angina=st.selectbox('Exercise angina', ['0', '1'])
 st_depression=st.slider('ST depression', 0, 6,1, disabled=False)
 st_slope=st.selectbox('Slope OF ST', ['1', '2','3'])
 no_vessels=st.selectbox('Number of vessels fluro', ['0', '1','2','3'])
 thallium=st.slider('Thallium', 0, 100, disabled=False)
 user_report_data={"age":age,"sex":sex,"cpt":cpt,"bp":bp,"cholesterol":cholesterol,"fbs":fbs,"ekg":ekg,"max_hr":max_hr,"angina":angina,"st_depression":st_depression,
                  "st_slope":st_slope,"no_vessels":no_vessels,"thallium":thallium}
 report_data=pd.DataFrame(user_report_data,index=[0])
 return report_data
user_data=user_report()
st.write(user_data)
#ml models
st.sidebar.selectbox('Select model', ('KNN','SVM'))
model=["KNN","SVM"]
if model=='KNN':#
 model=pickle.load(open('kNeighbor_classifier','rb'))
else:
 model=pickle.load(open('SVM_model','rb'))
if st.button('Predict'):
 st.subheader("Predicted Result")
 user_result=model.predict(user_data)
 if user_result==0:
  st.success('you are healthy')
 else:
  st.error('you have chances to have heart disease.please consult a specialist')
 
