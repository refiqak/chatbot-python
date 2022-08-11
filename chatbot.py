#!/usr/bin/python3


import aiml
import time
import re
time.clock = time.time
BRAIN_FILE = "brain.dump"

k = aiml.Kernel()


k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
k.saveBrain(BRAIN_FILE)
print("Loading from brain file: " + BRAIN_FILE)
k.loadBrain(BRAIN_FILE)


def response_question(question):
    try:
        question_clean = re.sub(r'[^\w\s]', '', question)
        response = k.respond(question_clean)
        return response
    except:
        return "Pertanyaan tidak ditemukan"


# while True:
#     input_text = input("Enter the query> ")
#     if(input_text == "quit"):
#         break
#     response = response_question(input_text)
#     print(response)
