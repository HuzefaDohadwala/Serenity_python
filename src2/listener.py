import tkinter

import customtkinter

import mysql.connector

# class Listener_landing(customtkinter.CTkFrame):
#     def __init__(self, master=None, username=None):
#         super().__init__(master)
#         self.master = master
#         self.pack(fill='both', expand=True)
#
#         # Create the frame to hold the components
#         self.inner_frame = customtkinter.CTkFrame(self)  # set background color of inner frame to black
#         self.inner_frame.pack(fill='both', expand=True)
#
#         # Create the components
#         self.welcome = customtkinter.CTkLabel(self.inner_frame, text=f"Welcome {username}!",
#                                               font=('Century Gothic', 25))
#         self.request_label = customtkinter.CTkLabel(self.inner_frame, text="Requests:", font=('Century Gothic', 15))
#         self.request_frame = customtkinter.CTkFrame(self.inner_frame)
#         self.accept_buttons = []
#
#         # Place the components
#         self.welcome.pack(side='top', padx=20, pady=50)
#         self.request_label.pack(side='top', padx=20, pady=10)
#         self.request_frame.pack(side='top', padx=20, pady=10)
#
#         # Fetch requests initially
#         self.fetch_requests()
#
#         # Set up a timer to fetch requests every 5 seconds
#         self.master.after(5000, self.fetch_requests)
#
#     def accept_request(self, request_id):
#         # Remove the request from the database
#         db = mysql.connector.connect(host='localhost', user='root', password='Kedar@2004', database='serenity')
#         cursor = db.cursor()
#         cursor.execute("DELETE FROM requests WHERE id=%s", (request_id,))
#         db.commit()
#
#         # Clear the request frame and fetch requests again
#         for button in self.accept_buttons:
#             button.destroy()
#         self.accept_buttons = []
#         self.fetch_requests()
#
#     def fetch_requests(self):
#         # Connect to the database
#         db = mysql.connector.connect(host='localhost', user='root', password='Kedar@2004', database='serenity')
#
#         # Create a cursor object
#         cursor = db.cursor()
#
#         # Execute the SQL query to fetch all requests
#         cursor.execute("SELECT * FROM requests")
#
#         # Fetch all the rows and store them in a list
#         rows = cursor.fetchall()
#
#         # Clear the existing requests
#         for button in self.accept_buttons:
#             button.destroy()
#         self.accept_buttons = []
#
#         # Add the new requests
#         for row in rows:
#             request_frame = customtkinter.CTkFrame(self.request_frame)
#             request_frame.pack(side='top', padx=10, pady=10, fill='x')
#
#             username = row[1]
#             request_message = row[2]
#             request_label = customtkinter.CTkLabel(request_frame, text=f"{username}: {request_message}")
#             request_label.pack(side='left', padx=10)
#
#             accept_button = customtkinter.CTkButton(request_frame, text="Accept",
#                                                     font=('Century Gothic', 15),
#                                                     command=lambda id=row[0]: self.accept_request(id))
#             accept_button.pack(side='right', padx=10)
#             self.accept_buttons.append(accept_button)
#
#         # Set up a timer to fetch requests every 5 seconds
#         self.master.after(5000, self.fetch_requests)

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
        self.request_label = customtkinter.CTkLabel(self.inner_frame, text="Requests:", font=('Century Gothic', 15))
        self.request_frame = customtkinter.CTkFrame(self.inner_frame)
        self.accept_buttons = []

        # Place the components
        self.welcome.pack(side='top', padx=20, pady=50)
        self.request_label.pack(side='top', padx=20, pady=10)
        self.request_frame.pack(side='top', padx=20, pady=10)

        # Fetch requests initially
        self.fetch_and_display_requests()

        # Set up a timer to fetch requests every 5 seconds
        # Set up a timer to fetch requests every 5 seconds
        self.master.after(5000, self.fetch_and_display_requests_periodically)

    def fetch_and_display_requests_periodically(self):
        self.fetch_and_display_requests()
        self.master.after(5000, self.fetch_and_display_requests_periodically)

    def accept_request(self, request_id):
        # Remove the request from the database
        db = mysql.connector.connect(host='localhost', user='root', password='Root@1234', database='serenity')
        cursor = db.cursor()
        cursor.execute("DELETE FROM requests WHERE id=%s", (request_id,))
        db.commit()
        print("Request accepted!!")

        # Clear the request frame and fetch requests again
        for button in self.accept_buttons:
            button.destroy()
        self.accept_buttons = []
        self.fetch_and_display_requests()
        self.Chatframe()

    def Chatframe(self):

        self.chatframe = customtkinter.CTk()
        self.chatframe = customtkinter.CTkScrollableFrame(self.inner_frame, width=200, height=200)
        self.entry = customtkinter.CTkEntry(self.inner_frame, width=150, height=30)
        self.send_btn = customtkinter.CTkButton(self.inner_frame, width=50, height=30)

        self.chatframe.place(x=50, y=50)
        self.entry.place(x=50, y=250)
        self.send_btn.place(x=200, y=250)







    def fetch_and_display_requests(self):
        # Clear the request frame
        for child in self.request_frame.winfo_children():
            child.destroy()

        # Connect to the database and fetch all requests
        db = mysql.connector.connect(host='localhost', user='root', password='Root@1234', database='serenity')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM requests")
        rows = cursor.fetchall()

        # Display each request with an accept button
        for row in rows:
            username = row[1]
            request_message = row[2]

            request_frame = customtkinter.CTkFrame(self.request_frame)
            request_label = customtkinter.CTkLabel(request_frame, text=f"{username}: {request_message}")
            accept_button = customtkinter.CTkButton(request_frame, text="Accept", font=('Century Gothic', 15),
                                                    command=lambda request_id=row[0]: self.accept_request(request_id))
            request_label.pack(side='left')
            accept_button.pack(side='left', padx=10)

            request_frame.pack(side='top', padx=20, pady=5)
            self.accept_buttons.append(accept_button)

        db.close()