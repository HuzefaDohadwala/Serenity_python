import customtkinter, tkinter

class HomePage:
    def __init__(self, master, mydb, user):
        self.master = master
        self.mydb = mydb
        self.user = user

        self.create_widgets()

    def create_widgets(self):
        # Create a button to log out and destroy the current window
        button01 = customtkinter.CTkButton(master=self.master, width=220, text="Log Out", command=self.log_out, corner_radius=6)
        button01.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        # Display the user's information
        info_label = customtkinter.CTkLabel(master=self.master, text=f"ID: {self.user[0]}\nUsername: {self.user[1]}",
                                            font=('Century Gothic', 16))
        info_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def log_out(self):
        self.master.destroy()