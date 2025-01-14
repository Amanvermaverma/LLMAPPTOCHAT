import streamlit as st
from langchain_groq import ChatGroq

st.title('🦜🔗 ChatGroq Quickstart')
groq_api_key = st.secrets['GROQ_api_key']


def generate_response(input_text):
    llm = ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768")
    response = llm.invoke(input_text)  # Use `invoke` to generate the response

    # Directly access the content attribute from the response
    content = response.content if hasattr(response, 'content') else 'No content returned from the model.'

    # Display only the content
    st.info(content)


with st.form('input_form'):
    text = st.text_area('Enter text:', '...')
    submitted = st.form_submit_button('Submit')
    if not groq_api_key:
        st.warning('API key is missing!', icon='⚠')
    elif submitted:
        generate_response(text)
