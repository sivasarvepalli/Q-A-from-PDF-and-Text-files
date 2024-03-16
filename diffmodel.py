#Importing libraries
import streamlit as st
import requests


def huggingface(prompt, data):
    API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": {
            "question": prompt,
            "context": data
        },
    })
    return output

text = st.file_uploader("Upload a file")

if text:
    words = text.read().decode('utf-8')
    if len(words) > 2000:
        st.error('Oh no! Too many words! I\'ll show results for the first 2000 words!')

    query = st.text_input("Enter your query...")
    if query and st.button('Answer me!'):
        response = huggingface(query, words[:2000])
        print(response)  # Print the response for debugging
        st.header(response.get('answer', 'No answer found'))

    elif not query:
        st.warning('Please enter a query.')
