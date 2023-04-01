from tkinter import *

# GUI
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


# Send function
def send():
	send = "You -> " + e.get()
	txt.insert(END, "\n" + send)

	user = e.get().lower()

	if (user == "hello"):
		txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")

	elif (user == "hi" or user == "hii" or user == "hiiii"):
		txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")

	elif (user == "how are you"):
		txt.insert(END, "\n" + "Bot -> fine! and you")

	elif (user == "fine" or user == "i am good" or user == "i am doing good"):
		txt.insert(END, "\n" + "Bot -> Great! how can I help you.")

	elif (user == "thanks" or user == "thank you" or user == "now its my time"):
		txt.insert(END, "\n" + "Bot -> My pleasure !")

	elif (user == "what do you sell" or user == "what kinds of items are there" or user == "have you something"):
		txt.insert(END, "\n" + "Bot -> We have coffee and tea")

	elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
		txt.insert(END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison.! ")

	elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
		txt.insert(END, "\n" + "Bot -> Have a nice day!")

	elif ("anxiety" in user):
		txt.insert(END, "\n" + "Bot -> That's okay. Sometimes it can be difficult to pinpoint the exact cause of anxiety. Have you tried any relaxation techniques, such as deep breathing or meditation, that might help you feel more calm and centered?")

	elif ("anxious" in user):
		txt.insert(END, "\n" + "Bot -> I'm sorry to hear that. Can you tell me more about what's making you feel anxious?")

	elif ("tried deep breathing" in user):
		txt.insert(END, "\n" + "Bot -> It's great that you're trying different techniques to manage your anxiety. Have you considered talking to a mental health professional ")

	elif ("mental health professional"in user or "doctor"in user and "not" in user):
		txt.insert(END, "\n" + "Bot -> That's understandable. If you're not ready to see a professional, there are other options available to you, such as online therapy or support groups.")

	elif ("dealing with stress" in user or "stress problems"in user or "coping with stress" in user):
		txt.insert(END, "\n" + "Bot -> Yes, I can suggest some strategies such as exercise, mindfulness, deep breathing, or talking to a friend or professional")

	elif ("improve productivity" in user or "productivity" in user):
		txt.insert(END, "\n" + "Bot -> There are several ways to improve productivity such as setting clear goals, using a task manager, taking breaks, and prioritizing tasks.")

	elif ("meaning of life" in user or "what is life" in user):
		txt.insert(END, "\n" + "Bot -> The meaning of life is subjective and can vary from person to person. Some people find meaning in their work, relationships, spirituality, or personal growth.")

	elif ("improve my communication" in user or "work up on my communication" in user):
		txt.insert(END, "\n" + "Bot -> To improve your communication skills, you can practice active listening, speaking clearly and confidently, using body language effectively, and empathizing with others.")

	elif ("improve my time management"in user or "work up on my time management"in user ):
		txt.insert(END, "\n" + "Bot -> To improve your time management skills, you can prioritize your tasks, set goals and deadlines, use a planner or calendar, delegate tasks, and learn to say no to unnecessary commitments.")

	elif ("improve my public speaking" in user or "work up on my public speaking" in user):
		txt.insert(END, "\n" + "Bot -> To improve your public speaking skills, you can practice, prepare and rehearse your speeches, use visual aids, speak clearly and confidently, and engage with your audience.")

	elif ("focus on studying"in user):
		txt.insert(END, "\n" + "Bot -> To stay focused while studying, you can create a study plan, eliminate distractions, take breaks, and use active learning strategies such as summarizing or teaching the material.")

	elif ("strategies for exam" in user or "exams strategies"in user):
		txt.insert(END, "\n" + "Bot -> Effective study strategies for exams include reviewing notes and material regularly, creating flashcards, practicing with practice exams or quizzes, and using mnemonic devices to help remember key information.")

	elif ("achieve my goals" in user or "get closer to my goals"in user):
		txt.insert(END, "\n" + "Bot -> Stay motivated to achieve your goals, you can break them down into smaller, achievable tasks, celebrate your progress, seek support from friends or a mentor, and remind yourself of why you set the goal in the first place.")

	elif ("improve my memory " in user or "work up on my memory" in user):
		txt.insert(END, "\n" + "Bot -> To improve your memory, you can try using mnemonic devices, practicing active recall by quizzing yourself, getting enough sleep, and engaging in regular exercise or physical activity.")

	elif ("improve my self confidence" in user or "work up on my self confidence" in user):
		txt.insert(END, "\n" + "Bot -> To improve your self-confidence, you can practice positive self-talk, set achievable goals and celebrate your successes, focus on your strengths, and seek support from friends or a therapist.")

	elif ("make friends" in user):
		txt.insert(END, "\n" + "Bot -> Making friends can be challenging for shy people, but you can start by taking small steps such as joining a club or group that interests you, attending social events, and practicing your social skills. You can also try reaching out to people online or through mutual acquaintances.")

	elif ("reduce work pressure" in user):
		txt.insert(END, "\n" + "Bot -> To reduce work pressure, you can try prioritizing your tasks, delegating responsibilities, taking breaks, practicing stress-reducing techniques such as deep breathing or meditation, and speaking with your supervisor or HR about workload concerns.")

	elif ("healthy lifestyle" in user):
		txt.insert(END, "\n" + "Bot -> To maintain a healthy lifestyle, you can eat a balanced and nutritious diet, engage in regular physical activity, get enough sleep, manage stress, and avoid unhealthy habits such as smoking or excessive alcohol consumption.")

	elif ("improve my mental health" in user):
		txt.insert(END, "\n" + "Bot -> To improve your mental health, you can try practicing self-care, seeking support from friends or a therapist, engaging in regular physical activity, getting enough sleep, and practicing mindfulness or meditation")

	elif ("reduce stress" in user):
		txt.insert(END, "\n" + "Bot -> To reduce stress in your life, you can try practicing mindfulness, exercising regularly, getting enough sleep, eating a healthy diet, and seeking support from friends or a professional.")

	elif ("healthy work life balance" in user):
		txt.insert(END, "\n" + "Bot -> Tips for maintaining a healthy work-life balance include setting boundaries, prioritizing your time, taking breaks, delegating tasks, and making time for hobbies or activities that you enjoy.")

	elif ("improve my mood" in user or "change my mood" in user):
		txt.insert(END, "\n" + "Bot -> To improve your mood, you can try engaging in physical activity, practicing relaxation techniques such as deep breathing or meditation, seeking out positive experiences or interactions, and speaking with a mental health professional if needed.")

	elif ("improve my sleep quality" in user or "insomnia" in user or "not able to sleep" in user):
		txt.insert(END, "\n" + "Bot ->To improve your sleep quality, you can try creating a relaxing sleep environment, sticking to a consistent sleep schedule, limiting caffeine and alcohol intake, and practicing relaxation techniques such as deep breathing or meditation before bed.")

	elif ("experiencing depression" in user):
		txt.insert(END, "\n" + "Bot -> Symptoms of depression can include persistent feelings of sadness or hopelessness, loss of interest in activities, changes in appetite or weight, difficulty sleeping or oversleeping, fatigue, feelings of worthlessness or guilt, difficulty concentrating, and thoughts of suicide. If you are experiencing these symptoms, it may be helpful to speak with a mental health professional.")

	elif ("i think i am depressed" in user or "feeling depressed" in user):
		txt.insert(END, "\n" + "Bot -> If you think you are depressed, it's important to seek help from a mental health professional. They can provide an accurate diagnosis and work with you to develop a treatment plan that meets your individual needs.")

	elif ("treat depression" in user or "come out of depression" in user):
		txt.insert(END, "\n" + "Bot -> Treatment for depression can involve a combination of therapy, medication, and lifestyle changes. Therapy can help individuals identify and change negative thought patterns, while medication can help balance brain chemicals that are associated with depression. Lifestyle changes such as exercise, healthy eating, and stress management can also be helpful.")

	elif ("can depression be cured" in user):
		txt.insert(END, "\n" + "Bot -> While depression can be a chronic condition, it is treatable with the right combination of therapies and lifestyle changes. Many individuals who receive treatment for depression are able to experience significant improvement in their symptoms and quality of life.")

	elif ("recover from depression" in user):
		txt.insert(END, "\n" + "Bot -> The length of time it takes to recover from depression can vary depending on the severity of the condition and the effectiveness of treatment. It's important to be patient and committed to your treatment plan, as improvement can take time.")

	else:
		txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")

	e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Hey,Bubbles here!!!!", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

root.mainloop()
