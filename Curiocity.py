# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 23:48:58 2025

@author: Hemal
"""

import streamlit as st
import speech_recognition as sr
import wikipediaapi

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Please ask your question...")
        audio = recognizer.listen(source)
        try:
            question = recognizer.recognize_google(audio)
            st.write(f"You said: {question}")
            return question
        except sr.UnknownValueError:
            st.write("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            st.write("Could not request results; check your network connection.")
            return None

def search_wikipedia(question):
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent='VoiceWikiSearch/1.0 (johndoe@example.com)'
    )
    try:
        page = wiki_wiki.page(question)
        if page.exists():
            return page.summary
        else:
            return "No results found."
    except Exception as e:
        return str(e)

st.title("Voice-Activated Wikipedia Search")

if st.button("Ask a Question"):
    question = recognize_speech()
    if question:
        answer = search_wikipedia(question)
        st.write(f"**Answer:** {answer}")
