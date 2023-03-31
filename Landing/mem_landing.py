import time
import threading
import customtkinter, tkinter

from Login.login import cursor, conn


def launch_member_page(user, mydb):
    def initiate_chat(username):
        chat_window = customtkinter.CTk()
        chat_window.geometry("400x600")
        chat_window.title(f"Chatting with {username}")

        chat_frame = customtkinter.CTkFrame(master=chat_window, width=400, height=600, corner_radius=0)
        chat_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        chat_area = customtkinter.CTkTextbox(master=chat_frame, width=50, height=25)
        chat_area.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        entry_area = customtkinter.CTkEntry(master=chat_frame, width=30)
        entry_area.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

        def send_message():
            message = entry_area.get()
            entry_area.delete(0, tkinter.END)
            chat_area.insert(tkinter.END, f"{user[1]}: {message}\n")
            sql = "INSERT INTO messages (sender, receiver, message, timestamp) VALUES (%s, %s, %s, %s)"
            val = (user[0], username_id_dict[username], message, time.strftime('%Y-%m-%d %H:%M:%S'))
            cursor.execute(sql, val)
            mydb.commit()

        send_button = customtkinter.CTkButton(master=chat_frame, text="Send", command=send_message, corner_radius=6)
        send_button.place(relx=0.8, rely=0.85)

        # Retrieve previous messages from the database
        sql = "SELECT * FROM messages WHERE (sender = %s AND receiver = %s) OR (sender = %s AND receiver = %s) ORDER BY timestamp ASC"
        val = (user[0], username_id_dict[username], username_id_dict[username], user[0])
        cursor.execute(sql, val)
        messages = cursor.fetchall()

        for message in messages:
            sender_name = None
            if message[1] == user[0]:
                sender_name = user[1]
            else:
                sender_name = username
            chat_area.insert(tkinter.END, f"{sender_name}: {message[3]}\n")

        chat_window.mainloop()

    # Create the new "Home" page and switch to it
    window = customtkinter.CTk()
    window.geometry("1280x600")
    window.title('Home')

    # Create new frame in the new window
    frame = customtkinter.CTkFrame(master=window, width=1280, height=720, corner_radius=0)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l1 = customtkinter.CTkLabel(master=frame, text=f"Welcome to the Home Page, {user[1]}!", font=('Century Gothic', 60))
    l1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    # Create buttons for each listener
    sql = "SELECT * FROM listeners"
    cursor.execute(sql)
    listeners = cursor.fetchall()

    username_id_dict = {}
    for listener in listeners:
        username_id_dict[listener[1]] = listener[0]

    button_y = 0.6
    for listener in listeners:
        username = listener[1]
        chat_button = customtkinter.CTkButton(master=frame, text=f"Chat with {username}",
                                              command=lambda u=username: initiate_chat(u),
                                              width=20, height=2, corner_radius=6)
        chat_button.place(relx=0.5, rely=button_y, anchor=tkinter.CENTER)
        button_y += 0.1


    window.mainloop()
