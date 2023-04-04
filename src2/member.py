import datetime
import subprocess
import tkinter
import tkinter as tk

import mysql.connector
import customtkinter
import mysql


class Member_landing(customtkinter.CTkFrame):
    def __init__(self, master=None, username=None):
        super().__init__(master)
        self.master = master
        self.pack(fill='both', expand=True)

            # Create the frame to hold the components
        self.inner_frame = customtkinter.CTkFrame(self)  # set background color of inner frame to black
        self.inner_frame.pack(fill='both', expand=True)

        # Create the components
        self.welcome = customtkinter.CTkLabel(self.inner_frame, text=f"Welcome {username}!",
                                            font=('Century Gothic', 25))
        self.request_entry = customtkinter.CTkEntry(self.inner_frame, width=50)
        self.request_button = customtkinter.CTkButton(self.inner_frame, text="Request",
                                                    command=lambda: self.save_request(username))
        
        def run_script():
            # Use subprocess to launch a new process that runs script2.py
            subprocess.Popen(['python', 'quiz.py'])

        # Create the new button
        self.new_button = customtkinter.CTkButton(self.inner_frame, text="Survey", command=run_script)

        def run_script1():
            # Use subprocess to launch a new process that runs script2.py
            subprocess.Popen(['python', 'chatbot.py'])

        # Create the second button
        self.second_button = customtkinter.CTkButton(self.inner_frame, text="Chat Bot",
                                                    command=run_script1)

        # Place the components
        self.welcome.pack(side='top', padx=20, pady=50)
        self.request_entry.pack(side='top', padx=20, pady=10)
        self.request_button.pack(side='top', padx=20, pady=10)
        self.new_button.pack(side='top', padx=20, pady=10)
        self.second_button.pack(side='top', padx=20, pady=10)

    def save_request(self, username):
        # Get the request message from the entry widget
        print("Request Button clicked!!!")
        request_message = self.request_entry.get()

        # Get the username of the current member
        member_username = username  # replace with the actual username

        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root@1234",
            database="serenity"
        )

        # Insert the request into the database
        cursor = db.cursor()
        sql = "INSERT INTO requests (member_username, request_message) VALUES (%s, %s)"
        val = (member_username, request_message)
        cursor.execute(sql, val)
        db.commit()
        print("Request Inserted into database")

        # Close the database connection
        db.close()
