import os
import aiml
import time
import re
time.clock = time.time
BRAIN_FILE = "brain.dump"

k = aiml.Kernel()

# To increase the startup speed of the bot it is
# possible to save the parsed aiml files as a
# dump. This code checks if a dump exists and
# otherwise loads the aiml from the xml files
# and saves the brain dump.
if os.path.exists(BRAIN_FILE):
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
# # Endless loop which passes the input to the bot and prints
# # its response
# while True:
#     input_text = input("Enter the query> ")
#     if(input_text == "quit"):
#         break
#     response = response_question(input_text)
#     print(response)
