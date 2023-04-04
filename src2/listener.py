import tkinter

import customtkinter

import mysql.connector

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
        self.request_list = tkinter.Listbox(self.inner_frame, height=10, width=50)
        self.accept_button = customtkinter.CTkButton(self.inner_frame, text="Accept",
                                                     font=('Century Gothic', 15), command=self.accept_request)

        # Place the components
        self.welcome.pack(side='top', padx=20, pady=50)
        self.request_label.pack(side='top', padx=20, pady=10)
        self.request_list.pack(side='top', padx=20, pady=10)
        self.accept_button.pack(side='top', padx=20, pady=10)

        # Fetch requests initially
        self.fetch_requests()

        # Set up a timer to fetch requests every 5 seconds
        self.master.after(5000, self.fetch_requests)

    def accept_request(self):
        # Get the selected item from the listbox
        selection = self.request_list.curselection()
        if len(selection) == 0:
            return

        # Get the request message from the selected item
        request_message = self.request_list.get(selection[0])

        # Remove the request from the database
        db = mysql.connector.connect(host='localhost', user='root', password='Kedar@2004', database='serenity')
        cursor = db.cursor()
        cursor.execute("DELETE FROM requests WHERE message=%s", (request_message,))
        db.commit()

        # Clear the listbox and fetch requests again
        self.request_list.delete(0, tkinter.END)
        self.fetch_requests()

    def fetch_requests(self):
        # Connect to the database
        db = mysql.connector.connect(host='localhost', user='root', password='Kedar@2004', database='serenity')

        # Create a cursor object
        cursor = db.cursor()

        # Execute the SQL query to fetch all requests
        cursor.execute("SELECT * FROM requests")

        # Fetch all the rows and store them in a list
        rows = cursor.fetchall()

        # Clear the existing list items
        self.request_list.delete(0, tkinter.END)

        # Add the new list items
        for row in rows:
            username = row[1]
            request_message = row[2]
            self.request_list.insert(tkinter.END, f"{username}: {request_message}")

        # Set up a timer to fetch requests every 5 seconds
        self.master.after(5000, self.fetch_requests)
