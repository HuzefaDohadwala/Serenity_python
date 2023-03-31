import tkinter

import customtkinter
import mysql.connector

# Create a new window
window = customtkinter.CTk()
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("blue")

# Set the window title
window.title("Login")

# Set the window size
window.geometry("300x150")

# Create a database connection
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kedar@2004",
        database="serenity",
    )

    print("Database connection established!")
except mysql.connector.Error as error:
    print("Error while connecting to MySQL: ", error)

cursor = conn.cursor()

# Create member and listener tables with account_type column
try:
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS members (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), account_type VARCHAR(255))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS listeners (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), account_type VARCHAR(255))")
    print("Tables created successfully!")
except mysql.connector.Error as error:
    print("Error while creating tables: ", error)


# def login_function():
#     # Check if a user with the given username and password exists in the selected table
#     if account_type == "member":
#         table_name = "members"
#     else:
#         table_name = "listeners"
#
#     cursor.execute(f"SELECT * FROM {table_name} WHERE username=%s AND password=%s AND account_type=%s",
#                    (entry1.get(), entry2.get(), account_type))
#     user = cursor.fetchone()
#
#     if user:
#         window.destroy()  # destroy current window
#         w = customtkinter.CTk()
#         w.geometry("1280x600")
#         w.title('Welcome')
#
#         # Create new frame in the new window
#         frame2 = customtkinter.CTkFrame(master=w, width=1280, height=720, corner_radius=0)
#         frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#
#         l1 = customtkinter.CTkLabel(master=frame2, text=f"Welcome, {user[1]}!", font=('Century Gothic', 60))
#         l1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
#
#         # Pass the database connection and user to the home page
#         # home_page = HomePage(master=frame2, mydb=mydb, user=user)
#
#         w.mainloop()
#     else:
#         # Show error message if user is not found
#         error_label = customtkinter.CTkLabel(master=frame, text="Invalid username or password",
#                                              font=('Century Gothic', 12), fg_color='red')
#         error_label.place(x=50, y=280)

#
def login_as_member():
    # Update account_type to "member" in the database
    cursor.execute("UPDATE members SET account_type = 'member' WHERE username = %s", ('username',))
    conn.commit()

    # Create the new "Member" page and switch to it
    frame = customtkinter.CTkFrame(master=window, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=frame, text="Welcome to Serenity", font=('Century Gothic', 20))
    l2.place(x=50, y=45)

    entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
    entry1.place(x=50, y=110)

    entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
    entry2.place(x=50, y=165)

    l3 = customtkinter.CTkLabel(master=frame, text="Forget password?", font=('Century Gothic', 12))
    l3.place(x=155, y=195)

    # Create custom button
    button1 = customtkinter.CTkButton(master=frame, width=220, text="Login",
                                      command=lambda: member_login_button(entry1, entry2, frame), corner_radius=6)
    # button1.place(x=50, y=240)
    button1.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
    # member_frame = customtkinter.CTkFrame(window)
    # member_label = customtkinter.CTkLabel(member_frame, text="Welcome, Member!")
    # member_label.pack(pady=10)
    # member_frame.pack(expand=True)
    # Flush login buttons
    member_button.destroy()
    listener_button.destroy()


def member_login_button(entry1, entry2, frame):
    print("Button clicked")

    cursor.execute(f"SELECT * FROM members WHERE username=%s AND password=%s ",
                   (entry1.get(), entry2.get()))
    user = cursor.fetchone()

    if user:
        window.destroy()  # destroy current window
        # w = customtkinter.CTk()
        # w.geometry("1280x600")
        # w.title('Welcome')

        # Create new frame in the new window
        # frame2 = customtkinter.CTkFrame(master=w, width=1280, height=720, corner_radius=0)
        # frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        #
        # l1 = customtkinter.CTkLabel(master=frame2, text=f"Welcome, {user[1]}!", font=('Century Gothic', 60))
        # l1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        # Pass the database connection and user to the home page
        # home_page = HomePage(master=frame2, mydb=mydb, user=user)

        # w.mainloop()
        # Import and launch the new file after successful login
        import Landing.mem_landing
        Landing.mem_landing.launch_member_page(user, conn)

    else:
        # Show error message if user is not found
        error_label = customtkinter.CTkLabel(master=frame, text="Invalid username or password",
                                             font=('Century Gothic', 12), fg_color='red')
        error_label.place(x=50, y=280)


def login_as_listener():
    # Update account_type to "listener" in the database
    # cursor.execute("UPDATE listeners SET account_type = 'listener'")
    # conn.commit()

    # Create the new "Listener" page and switch to it

    frame = customtkinter.CTkFrame(master=window, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=frame, text="Welcome to Serenity", font=('Century Gothic', 20))
    l2.place(x=50, y=45)

    entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
    entry1.place(x=50, y=110)
    username = entry1.get()

    entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
    entry2.place(x=50, y=165)
    pw = entry2.get()

    l3 = customtkinter.CTkLabel(master=frame, text="Forget password?", font=('Century Gothic', 12))
    l3.place(x=155, y=195)

    # Create custom button
    button1 = customtkinter.CTkButton(master=frame, width=220, text="Login",
                                      command=lambda: listener_login_button(entry1, entry2, frame), corner_radius=6)
    button1.place(x=50, y=240)

    # Flush login buttons
    member_button.destroy()
    listener_button.destroy()

    # listener_frame = customtkinter.CTkFrame(window)
    # listener_label = customtkinter.CTkLabel(listener_frame, text="Welcome, Listener!")
    # listener_label.pack(pady=10)
    # listener_frame.pack(expand=True)


def listener_login_button(entry1, entry2, frame):
    print("Button clicked")

    cursor.execute(f"SELECT * FROM listeners WHERE username=%s AND password=%s ",
                   (entry1.get(), entry2.get()))
    user = cursor.fetchone()

    if user:
        # window.destroy()  # destroy current window
        # w = customtkinter.CTk()
        # w.geometry("1280x600")
        # w.title('Welcome')
        #
        # # Create new frame in the new window
        # frame2 = customtkinter.CTkFrame(master=w, width=1280, height=720, corner_radius=0)
        # frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        #
        # l1 = customtkinter.CTkLabel(master=frame2, text=f"Welcome, {user[1]}!", font=('Century Gothic', 60))
        # l1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        #
        # # Pass the database connection and user to the home page
        # # home_page = HomePage(master=frame2, mydb=mydb, user=user)
        #
        # w.mainloop()
        # Import and launch the new file after successful login
        import Landing.list_landing
        Landing.list_landing.launch_listener_page(user, conn)

    else:
        # Show error message if user is not found
        error_label = customtkinter.CTkLabel(master=frame, text="Invalid username or password",
                                             font=('Century Gothic', 12), fg_color='red')
        error_label.place(x=50, y=280)


member_button = customtkinter.CTkButton(window, text="Login as member", command=login_as_member)
listener_button = customtkinter.CTkButton(window, text="Login as listener", command=login_as_listener)

# Pack the buttons onto the window
member_button.pack(pady=10)
listener_button.pack(pady=10)

# Start the main event loop
window.mainloop()
