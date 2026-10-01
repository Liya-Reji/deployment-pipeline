import streamlit as st
import ollama

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Study Assistant")
st.write("Ask a question and get an answer from a local AI model.")

question = st.text_area(
    "Enter your question:",
    placeholder="Explain what a deployment pipeline is in simple words."
)

if st.button("Ask AI"):
    if question.strip():

        with st.spinner("Generating answer..."):
            response = ollama.chat(
                model="gemma3:1b",
                messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

        st.subheader("AI Response")
        st.write(response["message"]["content"])

    else:
        st.warning("Please enter a question.")