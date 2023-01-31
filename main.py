import streamlit as st


with st.form("my_form", clear_on_submit=False):
    name = st.text_input('タイトル')
    evaluation = st.slider('評価', 1, 10, 5, 1)
    description = st.text_area('説明')
    description = st.text_area('感想')
    submitted = st.form_submit_button("submit")

    if submitted:
        st.write("Thanks!")

with st.form("form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")