import tkinter
import customtkinter
from PIL import ImageTk, Image
import mysql.connector
from homepage import HomePage

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Create a database connection
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kedar@2004",
        database="serenity",
    )

    print("Database connection established!")
except mysql.connector.Error as error:
    print("Error while connecting to MySQL: ", error)



# Create a cursor to execute SQL queries
mycursor = mydb.cursor()


# Create member and listener tables with account_type column
try:
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS members (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), account_type VARCHAR(255))")
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS listeners (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), account_type VARCHAR(255))")
    print("Tables created successfully!")
except mysql.connector.Error as error:
    print("Error while creating tables: ", error)


app = customtkinter.CTk()  # creating cutstom tkinter window
app.geometry("600x440")
app.title('Login')


def button_function():
    global account_type_var
    account_type = account_type_var.get()
    print(f"Selected account type: {account_type}")

    # Check if a user with the given username and password exists in the selected table
    if account_type == "member":
        table_name = "members"
    else:
        table_name = "listeners"

    mycursor.execute(f"SELECT * FROM {table_name} WHERE username=%s AND password=%s AND account_type=%s",
                     (entry1.get(), entry2.get(), account_type))
    user = mycursor.fetchone()

    if user:
        app.destroy()  # destroy current window
        w = customtkinter.CTk()
        w.geometry("1280x600")
        w.title('Welcome')

        # Create new frame in the new window
        frame2 = customtkinter.CTkFrame(master=w, width=1280, height=720, corner_radius=0)
        frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        l1 = customtkinter.CTkLabel(master=frame2, text=f"Welcome, {user[1]}!", font=('Century Gothic', 60))
        l1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        # Pass the database connection and user to the home page
        home_page = HomePage(master=frame2, mydb=mydb, user=user)

        w.mainloop()
    else:
        # Show error message if user is not found
        error_label = customtkinter.CTkLabel(master=frame, text="Invalid username or password",
                                             font=('Century Gothic', 12), fg_color='red')
        error_label.place(x=50, y=280)


# creating custom frame
frame = customtkinter.CTkFrame(master=app, width=320, height=360, corner_radius=15)
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
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=240)

# create account type selection radio buttons
# account_type_var = tkinter.StringVar()
# member_radio_btn = customtkinter.CTkRadioButton(master=frame, text='Member', variable=account_type_var, value='member')
# listener_radio_btn = customtkinter.CTkRadioButton(master=frame, text='Listener', variable=account_type_var,
#                                                   value='listener')
#
# # place the radio buttons on the window
# member_radio_btn.place(relx=0.4, rely=0.8, anchor=tkinter.CENTER)
# listener_radio_btn.place(relx=0.7, rely=0.8, anchor=tkinter.CENTER)

app.mainloop()


