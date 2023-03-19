import streamlit as st
from streamlit_chat import message

st.title("Chatbot thingy")



if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input("You: ",placeholder="Hello, how are you?", key="input")
    return input_text 

user_input = get_text()

if user_input:
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append("I am bot beep boop beep")

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

# message("My message") 
# message("Hello bot!", is_user=True)  # align's the message to the right