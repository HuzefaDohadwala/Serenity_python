import datetime
import tkinter
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import customtkinter
import mysql

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Create a database connection
# try:
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kedar@2004",
    database="serenity",
)

# print("Database connection established!")
# except mysql.connector.Error as error:
# print("Error while connecting to MySQL: ", error)

cursor = conn.cursor()

# Create member and listener tables with account_type column
try:
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), "
        "password VARCHAR(255), role VARCHAR(255))")
    # cursor.execute(
    #     "CREATE TABLE IF NOT EXISTS listeners (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), "
    #     "password VARCHAR(255), account_type VARCHAR(255))")
    print("Tables created successfully!")
except mysql.connector.Error as error:
    print("Error while creating tables: ", error)


class SignupApp(customtkinter.CTkFrame):
    def __init__(self, master):
        self.master = master
        self.master.title("Authentication")
        # set the dimensions of the main window
        window_width = 500
        window_height = 400

        # get the dimensions of the screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # calculate the x and y coordinates to center the window
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # set the geometry of the main window
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")
        # master.geometry("300x300")

        # Create Frame
        self.frame = customtkinter.CTkFrame(self.master, width=320, height=360, corner_radius=15)

        # Create the Sign-up form
        self.label = customtkinter.CTkLabel(self.frame, text="Welcome to Serenity", font=('Century Gothic', 25))
        self.entry1 = customtkinter.CTkEntry(self.frame, width=220, placeholder_text='Username')
        self.entry2 = customtkinter.CTkEntry(self.frame, width=220, placeholder_text='Password', show="*")
        # self.label2 = customtkinter.CTkLabel(self.frame,  text="Forget password?", font=('Century Gothic', 12))
        self.entry3 = customtkinter.CTkEntry(self.frame, width=220, placeholder_text='Confirm Password', show="*")
        self.button = customtkinter.CTkButton(self.frame, text="Sign Up", width=220, command=self.sign_in,
                                              corner_radius=6)
        self.label3 = customtkinter.CTkLabel(self.frame, text="Already have an account?", font=('Century Gothic', 10))
        self.label4 = customtkinter.CTkLabel(self.frame, text="Login", font=('Century Gothic', 10))

        # Place everything
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.label.place(x=35, y=45)
        self.entry1.place(x=50, y=110)
        self.entry2.place(x=50, y=165)
        self.entry3.place(x=50, y=220)
        # self.label2.place(x=155, y=195)
        self.button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        self.label3.place(x=80, y=310)
        self.label4.place(x=220, y=310)

        # Binding Login text
        self.label4.bind("<Button-1>", lambda event: self.go_to_login())

    def go_to_login(self):
        print("I create login instance!!")
        self.frame.destroy()
        login_frame = LoginApp(self.master)

    def create_user(self):
        success = False  # initialize the flag variable

        # check if the passwords match
        if self.entry2.get() == self.entry3.get():
            username = self.entry1.get()
            password = self.entry3.get()
            role = "member"

            # check if the user already exists in the database
            cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
            result = cursor.fetchone()

            if result is None:
                # insert the user into the database
                cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                               (username, password, role))
                conn.commit()
                success = True  # set the flag variable

                # create the Member_landing frame
                landing = Member_landing(self.master, username)
            else:
                error_label = customtkinter.CTkLabel(self.frame, font=('Century Gothic', 12), fg_color='red',
                                                     text="Username already exists!")
                error_label.pack()

        else:
            error_label = customtkinter.CTkLabel(self.frame, font=('Century Gothic', 12), fg_color='red',
                                                 text="Both passwords should be the same!!")
            error_label.pack()

        return success  # return the flag variable

    def sign_in(self):

        if self.create_user():
            self.frame.destroy()


class Member_landing(customtkinter.CTkFrame):
    def __init__(self, master=None, username=None):
        super().__init__(master)
        self.send_message = lambda: None
        self.type = None
        self.chatframe = None
        self.send_button = None
        self.master = master
        self.pack(fill='both', expand=True)

        # Create the frame to hold the components
        self.inner_frame = customtkinter.CTkFrame(self)  # set background color of inner frame to black
        self.inner_frame.pack(fill='both', expand=True)

        # Create the welcome label
        self.welcome = customtkinter.CTkLabel(self.inner_frame, text=f"Welcome {username}!",
                                              font=('Century Gothic', 25))

        # Place the welcome label
        self.welcome.pack(side='top', padx=20, pady=50)

        # Create the chat buttons component
        chat_buttons = customtkinter.CTkFrame(self.inner_frame)
        chat_buttons.pack(side='right', fill='y', padx=20, pady=(0, 50))

        # Set the size of the chat buttons component
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        chat_buttons_width = int(screen_width / 4)
        chat_buttons_height = int(screen_height / 8)
        chat_buttons.configure(width=chat_buttons_width, height=chat_buttons_height)

        # Create the chat buttons
        sql = "SELECT * FROM users WHERE role='listener';"
        cursor.execute(sql)
        listeners = cursor.fetchall()

        # Set the size of the chat buttons component
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        chat_buttons_width = int(screen_width / 4)
        chat_buttons_height = int(screen_height / 8)
        chat_buttons.configure(width=chat_buttons_width, height=chat_buttons_height)

        # Create the chat buttons
        button_x = 0
        button_y = 0
        for listener in listeners:
            listener_username = listener[1]
            chat_button = customtkinter.CTkButton(master=chat_buttons, text=f"Chat with {listener_username}",
                                                  command=lambda u=username, l=listener_username: self.initiate_chat(u,
                                                                                                                     l),
                                                  width=400, height=100, corner_radius=0)
            chat_button.place(x=button_x, y=button_y)
            button_y += 120
            chat_button.pack(padx=0, pady=0, ipadx=0, ipady=0, fill='none')

    def initiate_chat(self, username, listener_username):
        print("Listener button pressed!!")
        print(username)
        print(listener_username)

        cursor.execute("Select * from users WHERE username=%s;", (username,))
        sender_user = cursor.fetchone()

        def send_message():
            print("Message sent!!")
            message_text = self.type.get()
            sender_id = sender_user[0]

            # receiver_username = listener_username
            cursor.execute("Select * from users WHERE username=%s;", (listener_username,))
            receiver_username = cursor.fetchone()[0]
            timestamp = str(datetime.datetime.now())
            print(receiver_username)
            print(listener_username)
            print(sender_user[0])

            cursor.execute("INSERT INTO messages (sender, receiver, message, timestamp) VALUES (%s, %s, %s, %s);",
                           (sender_id, receiver_username, message_text, timestamp))
            conn.commit()
            print("Message inserted into db")
            self.chatframe.insert(tkinter.END, f"{sender_user[1]}: {message_text}\n")
            self.type.delete(0, 'end')  # Clear the message from the entry component

        self.send_message = send_message  # assign the function to self.send_message

        self.chatframe = customtkinter.CTkTextbox(self.inner_frame, width=600, corner_radius=6, fg_color="black",
                                                  height=500)
        self.type = customtkinter.CTkEntry(self.inner_frame, width=550, corner_radius=6, height=25)
        # self.send_message = lambda: self.send_message_command(username_id_dict, listener_username)
        self.send_button = customtkinter.CTkButton(self.inner_frame,
                                                   command=lambda: self.send_message(),
                                                   text="Send", width=80,
                                                   height=25, corner_radius=6)

        self.chatframe.place(x=370, y=150)
        self.type.place(x=370, y=660)
        self.send_button.place(x=920, y=660)

        cursor.execute("Select * from users WHERE username=%s;", (listener_username,))
        reciever = cursor.fetchone()[0]

        # Retrieve texts from database
        sql = "SELECT * FROM messages WHERE (sender = %s AND receiver = %s) OR (sender = %s AND receiver = %s) ORDER " \
              "BY timestamp ASC "
        val = (sender_user[0], reciever, reciever, sender_user[0])
        cursor.execute(sql, val)
        messages = cursor.fetchall()  # fetch all the rows from the query result
        print(sender_user)
        print(listener_username)

        for message in messages:
            sender_name = None
            id = message[1]

            cursor.execute("Select username from users WHERE id=%s", (id,))
            sender_name = cursor.fetchone()[0]
            self.chatframe.insert(tkinter.END, f"{sender_name}: {message[3]}\n")


class Listener_landing(customtkinter.CTkFrame):
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

        # Place the components
        self.welcome.pack(side='top', padx=20, pady=50)

        sql = "SELECT * FROM users WHERE role='member';"
        cursor.execute(sql)
        members = cursor.fetchall()

        # Create the chat buttons component
        chat_buttons = customtkinter.CTkFrame(self.inner_frame)
        chat_buttons.pack(side='right', fill='y', padx=20, pady=(0, 50))

        # Set the size of the chat buttons component
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        chat_buttons_width = int(screen_width / 4)
        chat_buttons_height = int(screen_height / 8)
        chat_buttons.configure(width=chat_buttons_width, height=chat_buttons_height)

        # Create the chat buttons
        button_x = 0
        button_y = 0
        for member in members:
            member_username = member[1]
            chat_button = customtkinter.CTkButton(master=chat_buttons, text=f"Chat with {member_username}",
                                                  command=lambda u=username, l=member_username: self.initiate_chat(u,
                                                                                                                   l),
                                                  width=400, height=100, corner_radius=0)
            chat_button.place(x=button_x, y=button_y)
            button_y += 120
            chat_button.pack(padx=0, pady=0, ipadx=0, ipady=0, fill='none')

    #
    def initiate_chat(self, username, member_username):
        print("Member button pressed!!")
        print(username)
        print(member_username)

        cursor.execute("Select * from users WHERE username=%s;", (username,))
        sender_user = cursor.fetchone()

        def send_message():
            print("Message sent!!")
            message_text = self.type.get()
            sender_id = sender_user[0]

            # receiver_username = listener_username
            cursor.execute("Select * from users WHERE username=%s;", (member_username,))
            receiver_username = cursor.fetchone()[0]
            timestamp = str(datetime.datetime.now())
            print(receiver_username)
            print(member_username)
            print(sender_user[0])

            cursor.execute("INSERT INTO messages (sender, receiver, message, timestamp) VALUES (%s, %s, %s, %s);",
                           (sender_id, receiver_username, message_text, timestamp))
            conn.commit()
            print("Message inserted into db")
            self.chatframe.insert(tkinter.END, f"{sender_user[1]}: {message_text}\n")
            self.type.delete(0, 'end')  # Clear the message from the entry component

        self.send_message = send_message  # assign the function to self.send_message

        self.chatframe = customtkinter.CTkTextbox(self.inner_frame, width=600, corner_radius=6, fg_color="black",
                                                  height=500)
        self.type = customtkinter.CTkEntry(self.inner_frame, width=550, corner_radius=6, height=25)
        # self.send_message = lambda: self.send_message_command(username_id_dict, listener_username)
        self.send_button = customtkinter.CTkButton(self.inner_frame,
                                                   command=lambda: self.send_message(),
                                                   text="Send", width=80,
                                                   height=25, corner_radius=6)

        self.chatframe.place(x=370, y=150)
        self.type.place(x=370, y=660)
        self.send_button.place(x=920, y=660)

        cursor.execute("Select * from users WHERE username=%s;", (member_username,))
        reciever = cursor.fetchone()[0]

        # Retrieve texts from database
        sql = "SELECT * FROM messages WHERE (sender = %s AND receiver = %s) OR (sender = %s AND receiver = %s) ORDER " \
              "BY timestamp ASC "
        val = (sender_user[0], reciever, reciever, sender_user[0])
        cursor.execute(sql, val)
        messages = cursor.fetchall()  # fetch all the rows from the query result
        print(sender_user)
        print(member_username)

        for message in messages:
            sender_name = None
            id = message[1]

            cursor.execute("Select username from users WHERE id=%s", (id,))
            sender_name = cursor.fetchone()[0]
            self.chatframe.insert(tkinter.END, f"{sender_name}: {message[3]}\n")


class LoginApp(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.pack(fill='both', expand=True)

        # set the dimensions of the main window
        window_width = 500
        window_height = 400

        # get the dimensions of the screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # calculate the x and y coordinates to center the window
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # set the geometry of the main window
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")
        # master.geometry("300x300")

        self.role_var = tk.StringVar(value="member")

        # Create Frame
        self.frame = customtkinter.CTkFrame(self.master, width=320, height=360, corner_radius=15)

        # Create the Sign-up form
        self.label = customtkinter.CTkLabel(self.frame, text="Log into Serenity", font=('Century Gothic', 25))
        self.entry1 = customtkinter.CTkEntry(self.frame, width=220, placeholder_text='Username')
        self.entry2 = customtkinter.CTkEntry(self.frame, width=220, placeholder_text='Password', show="*")

        self.role1 = customtkinter.CTkRadioButton(self.frame, text="Member", variable=self.role_var, value="member")
        self.role2 = customtkinter.CTkRadioButton(self.frame, text="Listener", variable=self.role_var, value="listener")
        self.button = customtkinter.CTkButton(self.frame, text="Login", width=220,
                                              corner_radius=6)
        self.label3 = customtkinter.CTkLabel(self.frame, text="Don't have an account?", font=('Century Gothic', 10))
        self.label4 = customtkinter.CTkLabel(self.frame, text="SignUp", font=('Century Gothic', 10))

        # Place everything
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.label.place(x=60, y=45)
        self.entry1.place(x=50, y=110)
        self.entry2.place(x=50, y=165)
        self.role1.place(x=50, y=220)
        self.role2.place(x=200, y=220)

        # self.label2.place(x=155, y=195)
        self.button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        self.label3.place(x=80, y=310)
        self.label4.place(x=220, y=310)

        self.label4.bind("<Button-1>", lambda event: self.go_to_signup())

        self.button.bind("<Button-1>", lambda event: self.login())

    def login(self):
        username = self.entry1.get()
        password = self.entry2.get()
        role = self.role_var.get()  # if self.role1.get() == "member" else self.role2.get()

        # check if the user exists in the database
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s AND role=%s", (username, password, role))
        result = cursor.fetchone()

        if result is not None:
            # login successful, create the appropriate landing page
            if role == "member":
                landing = Member_landing(self.master, username)
            elif role == "listener":
                landing = Listener_landing(self.master, username)
        else:
            error_label = customtkinter.CTkLabel(self.frame, font=('Century Gothic', 12), fg_color='red',
                                                 text="Incorrect username, password, or role!")
            error_label.place(x=50, y=270)

    def go_to_signup(self):
        print("Pressed!!!")
        self.frame.destroy()
        signup_frame = SignupApp(self.master)


root = customtkinter.CTk()
app = SignupApp(root)
root.mainloop()
