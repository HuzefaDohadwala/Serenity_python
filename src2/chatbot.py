import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

import tkinter as tk

# Set the background color to black
BACKGROUND_COLOR = '#252525'
FOREGROUND_COLOR = 'white'
TEXT_COLOR = 'white'

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

def send():
    message = entry_box.get()
    entry_box.delete(0, tk.END)

    if message.strip() == "":
        return

    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + message + "\n\n")
    ints = predict_class(message)
    res = get_response(ints, intents)
    chat_log.insert(tk.END, "Bot: " + res + "\n\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)

root = tk.Tk()
root.title("Chatbot")
root.configure(background=BACKGROUND_COLOR)

chat_log = tk.Text(root, bd=0, bg="#1c1c1c", fg="white", height="8", width="50", font="Arial")
chat_log.config(state=tk.DISABLED)

scrollbar = tk.Scrollbar(root, command=chat_log.yview)
chat_log['yscrollcommand'] = scrollbar.set

entry_box = tk.Entry(root, bd=0, bg="#1c1c1c", fg=TEXT_COLOR, width="29", font="Arial")
entry_box.bind("<Return>", (lambda event: send()))

send_button = tk.Button(root, text="Send", command=send, bg='blue', fg=FOREGROUND_COLOR)

scrollbar.place(x=1325, y=50, height=600)
chat_log.place(x=575, y=50, height=600, width=750)
entry_box.place(x=575, y=665, height=40, width=650)
send_button.place(x=1250, y=665, height=40, width=80)

root.mainloop()
