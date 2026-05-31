import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Chatbotku", page_icon="🤖")
st.title("🤖 Chatbot Pintar Pertamaku")
st.write("Halo! Tanyakan apa saja, saya siap menjawab.")


client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ketik pesanmu di sini..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
        )
        jawaban_ai = response.choices[0].message.content
        st.markdown(jawaban_ai)
    st.session_state.messages.append({"role": "assistant", "content": jawaban_ai})