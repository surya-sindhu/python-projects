from tkinter import *    #the program imports necessary modules for GUI
from tkinter import ttk, messagebox
from datetime import datetime

#these function validate entering mob no. and email to meet certain criteria
def validate_mobile(mobile):
    return len(mobile) == 10 and mobile[0] in ['9', '7', '8', '6']
    

def validate_email(email):
    return email.endswith("@gmail.com")


#this function creates a new window for seat selection, taking no. of passengers and details as parameters
def open_seat_window(num_passengers, passenger_details):
    
    #It creates a new top-level window for seat selection, which will appear when this function is called.
    seat_selection_window = Toplevel(root)
    seat_selection_window.title("Seat Selection")
    
    #This nested function handles the submission of seat selections made by the user.
    def submit_selection():
        
        #These variables are initialized to store selected seats and their corresponding prices.
        selected_seats = []
        semi_sleeper_price = 0
        sleeper_price = 0
    
        for seat, var in semi_sleeper_checkboxes.items():
            if var.get():
                selected_seats.append(seat)
                semi_sleeper_price += 500  # Accumulate price for each selected seat
    
        for seat, var in sleeper_checkboxes.items():
            if var.get():
                selected_seats.append(seat)
                sleeper_price += 1000  # Accumulate price for each selected seat

        #It calculates the total price of selected seats.
        total_price = semi_sleeper_price + sleeper_price
        messagebox.showinfo("Booking Details", f"From: {dropvar.get()}\nTo: {dropvar1.get()}\nDate: {dropvar_day.get()}-{dropvar_month.get()}-{dropvar_year.get()}\nNumber of Passengers: {num_passengers}\nSelected Seats: {selected_seats}\nTotal Price: {total_price}")

    #These dictionaries are initialized to store semi-sleeper and sleeper seat checkboxes.
    semi_sleeper_checkboxes = {}
    sleeper_checkboxes = {}
    
    #This loop iterates over the range of seat numbers.
    for i in range(1, 31):

        #It determines whether the seat is semi-sleeper or sleeper type and sets the column accordingly.
        if i <= 20:
            col = 0
            seat_type = "Semi Sleeper"
        else:
            col = 1
            seat_type = "Sleeper"

        #It calculates the row position of the current seat and creates a checkbox widget for the seat.
        row = (i - 1) % 16
        seat_checkbox = Checkbutton(seat_selection_window, text=str(i))
        seat_checkbox.grid(row=row+1, column=col, padx=5, pady=5)
        if seat_type == "Semi Sleeper":
            semi_sleeper_checkboxes[i] = IntVar()
            if num_passengers == 1:
                semi_sleeper_checkboxes[i].set(0)
                seat_checkbox.config(state="disabled")
            Checkbutton(seat_selection_window, text="Price 500", variable=semi_sleeper_checkboxes[i]).grid(row=row+1, column=col, sticky="e", padx=5, pady=5)
        else:
            sleeper_checkboxes[i] = IntVar()
            if num_passengers == 1:
                sleeper_checkboxes[i].set(0)
                seat_checkbox.config(state="disabled")
            
            #It creates a checkbox for sleeper seat price.
            Checkbutton(seat_selection_window, text="Price 1000", variable=sleeper_checkboxes[i]).grid(row=row+1, column=col, sticky="e", padx=5, pady=5)
    

    #These lines create labels to display the prices for semi-sleeper and sleeper seats.
    label_semi=Label(seat_selection_window, text="500 - Semi sleeper")
    label_semi.grid(row=21, columnspan=2, padx=5, pady=10)

    label_sleeper=Label(seat_selection_window, text="1000 - Sleeper")
    label_sleeper.grid(row=22, columnspan=2, padx=5, pady=10)

    time=Label(seat_selection_window, text="Time - 8.00 PM")
    time.grid(row=23, columnspan=2, padx=5, pady=10)
    
    #It creates a button to confirm seat selections, calling the submit_selection function when clicked.
    confirm_button = Button(seat_selection_window, text="Confirm Selection", command=submit_selection)
    confirm_button.grid(row=24, columnspan=2, padx=10, pady=10)


#This function handles obtaining details of passengers, such as their names, ages, mobile numbers, and email addresses.
def get_passenger_details():
    root.withdraw()
    num_passengers = int(e1.get())
    
    #It checks if the number of passengers is valid (greater than zero). If not, it displays an error message.
    if num_passengers <= 0:
        messagebox.showerror("Error", "Please enter a valid number of passengers.")
        return
    
    #It creates a new top-level window to collect passenger details.
    passenger_details_window = Toplevel(root)
    passenger_details_window.title("Passenger Details")
    
    mobile_label = Label(passenger_details_window, text="Mobile:")
    mobile_label.grid(row=0, column=0, padx=10, pady=5)
    mobile_entry = Entry(passenger_details_window)
    mobile_entry.grid(row=0, column=1, padx=10, pady=5)
    
    email_label = Label(passenger_details_window, text="Gmail:")
    email_label.grid(row=1, column=0, padx=10, pady=5)
    email_entry = Entry(passenger_details_window)
    email_entry.grid(row=1, column=1, padx=10, pady=5)
    
    # List to store passenger details
    passenger_details = []  
    

    def save_passenger():

        #It retrieves the entered mobile number and email address.
        mobile = mobile_entry.get()
        email = email_entry.get()
        
        #It validates the entered mobile number using the validate_mobile and validate_gmail function. If invalid, it displays an error message.
        if not validate_mobile(mobile):
            messagebox.showerror("Error", "Please enter a valid 10-digit mobile number.")
            return
        
        if not validate_email(email):
            messagebox.showerror("Error", "Please enter a valid Gmail address.")
            return
        
        #It retrieves the entered name and age of the passenger.
        passenger_name = name_entry.get()
        passenger_age = age_entry.get()

        if not passenger_name or not passenger_age:
            messagebox.showerror("Error", "Please fill in all the required entries.")
            return
        
        #It appends the passenger's name and age to the passenger_details list.
        passenger_details.append((passenger_name, passenger_age))  # Append passenger details
        
        #It clears the entry fields after saving passenger details.
        name_entry.delete(0, END)
        age_entry.delete(0, END)

        passenger_details_window.destroy()  # Close passenger details window
        open_seat_window(num_passengers, passenger_details)

    #This loop iterates over the range of passengers to create entry widgets for each passenger's name and age. 
    for i in range(num_passengers):
        passenger_frame = Frame(passenger_details_window)
        passenger_frame.grid(row=i+2, columnspan=2, padx=10, pady=5)
        
        name_label = Label(passenger_frame, text=f"Passenger {i+1} Name:")
        name_label.grid(row=0, column=0, padx=10, pady=5)
        name_entry = Entry(passenger_frame)
        name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        age_label = Label(passenger_frame, text=f"Passenger {i+1} Age:")
        age_label.grid(row=1, column=0, padx=10, pady=5)
        age_entry = Entry(passenger_frame)
        age_entry.grid(row=1, column=1, padx=10, pady=5)
            
    confirm_button = Button(passenger_details_window, text="Confirm", command=save_passenger)
    confirm_button.grid(row=num_passengers+3, columnspan=2, padx=10, pady=5)

#It creates the main application window.
root = Tk()

#It retrieves the current date, year, month, and day.
now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day

def getvalues(selected):
    return
    
def getvalues1(selected):
    return

current_date = datetime.now().strftime("%Y-%m-%d")

#This function opens the passenger details window when called.
def open_passenger_details():

    #It validates user inputs for 'From' and 'To' locations and the number of passengers before proceeding to passenger details entry.
    if dropvar.get() == '---Select One---' or dropvar1.get() == '---Select One---':
        messagebox.showerror("Error", "Please select both 'From' and 'To' locations.")
        return
    elif dropvar.get() == dropvar1.get():
        messagebox.showerror("Error", "Please select different 'From' and 'To' locations.")
        return
    elif not e1.get():
        messagebox.showerror("Error", "Please enter the number of passengers.")
        return
    else:
        get_passenger_details()

f=Frame(root,bg="black",borderwidth=50,relief=SUNKEN)
f.pack(side=TOP,fill="both",pady=20)
l=Label(f,text="Yourbus",font="arial 38 bold",bg="black",fg="white").pack()

f=Frame(root,bg="black",borderwidth=50,relief=SUNKEN)
f.pack(side=BOTTOM,fill="both",pady=20)
l=Label(f,text="Amenities:      1.Wifi      2.TV      3.First Aid Kit      4.A/C      5.Water bottle      6.Snack",font="arial 10 bold",bg="black",fg="white").pack()
l_customer=Label(f, text="Call Customer Support:  +91 9876543210       mail: yourbus@gmail.com",font="arial 10 bold",bg="black",fg="white").pack()


l1 = Label(root, text="From")
l1.place(x=650,y=250)
dropvar = StringVar()
option = ["Chennai", "Kancheepuram", "Tiruvallur", "Cuddalore", "Vellore", "Viluppuram", "Salem", "Erode",
          "Tiruppur", "Namakkal", "Perambalur", "Tiruchirappalli", "Karur", "Thanjavur", "Nagapattinam", "Thiruvarur",
          "Pudukkottai", "Dindigul", "Theni", "Virudhunagar", "Madurai", "Sivagangai", "Ramanathapuram",
          "Tirunelveli", "Thoothukudi", "Kanniyakumari"]
dm = ttk.OptionMenu(root, dropvar, '---Select One---', *option, command=getvalues)
dm.place(x=750,y=250)


l2 = Label(root, text="To")
l2.place(x=650,y=280)
dropvar1 = StringVar()
option1 = ["Chennai", "Kancheepuram", "Tiruvallur", "Cuddalore", "Vellore", "Viluppuram", "Salem", "Erode",
           "Tiruppur", "Namakkal", "Perambalur", "Tiruchirappalli", "Karur", "Thanjavur", "Nagapattinam",
           "Thiruvarur", "Pudukkottai", "Dindigul", "Theni", "Virudhunagar", "Madurai", "Sivagangai",
           "Ramanathapuram", "Tirunelveli", "Thoothukudi", "Kanniyakumari"]
dm1 = ttk.OptionMenu(root, dropvar1, '---Select One---', *option1, command=getvalues1)
dm1.place(x=750,y=280)


l_date = Label(root, text="Date")
l_date.place(x=650,y=310)
days = [str(day) for day in range(1, 32)]
dropvar_day = StringVar()
drop_day = ttk.OptionMenu(root, dropvar_day, current_day, *days)
drop_day.place(x=750,y=310)

l_month = Label(root, text="Month")
l_month.place(x=650,y=340)
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]
dropvar_month = StringVar()
drop_month = ttk.OptionMenu(root, dropvar_month, months[current_month - 1], *months)
drop_month.place(x=750,y=340)

l_year = Label(root, text="Year")
l_year.place(x=650,y=370)
years = [str(year) for year in range(current_year, current_year + 5)]
dropvar_year = StringVar()
drop_year = ttk.OptionMenu(root, dropvar_year, current_year, *years)
drop_year.place(x=750,y=370)

l3 = Label(root, text="No. of passengers")
l3.place(x=650,y=400)
a = StringVar()
e1 = Entry(root, textvariable=a)
e1.place(x=750,y=400)

#It creates a button in the main application window to initiate the process of entering passenger details.
passenger_button = Button(root, text="Enter Passenger Details", command=open_passenger_details)
passenger_button.place(x=750,y=450)


root.title("Yourbus")
root.state("zoomed")
root.configure(bg="beige")
root.mainloop()
