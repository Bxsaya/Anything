# Importing required packages
import streamlit as st
import openai
import numpy as np
import pandas as pd
import pickle

COMPLETIONS_MODEL = "text-davinci-003"
EMBEDDING_MODEL = "text-embedding-ada-002"
openai.api_key = "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" 


st.title("Chatting with ChatGPT")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''This is a web application that allows you to interact with 
       the OpenAI API's implementation of the ChatGPT model.
       Enter a *query* in the *text box* and *press enter* to receive 
       a *response* from the ChatGPT
       '''
    )

def main():
    '''
    This function gets the user input, pass it to ChatGPT function and 
    displays the response
    '''
    # Get user input
    user_query = st.text_input("Enter query here, to exit enter :q", "How may I assist you today?")
    
    if user_query != ":q" or user_query != "":
        # Pass the query to the ChatGPT function
        completion = openai.Completion.create(
                        prompt=user_query,
                        temperature=0,
                        max_tokens=300,
                        model=COMPLETIONS_MODEL
         )["choices"][0]["text"].strip(" \n")
        response = ChatGPT(completion)
        return st.write(f"{user_query} {response}")

def ChatGPT(completion):
    ''' 
    This function uses the OpenAI API to generate a response to the given 
    user_query using the ChatGPT model
    '''
    response = completion
    return response

# call the main function
main()

