# YourBus Ticket Booking System

YourBus is a Python-based GUI application for booking bus tickets. It allows users to select their journey details, enter passenger information, and choose seats. The program includes validation for mobile numbers and email addresses, ensuring that only valid information is entered.

## Features

- **Journey Details Selection**: Choose the 'From' and 'To' locations and select the date of travel.
- **Passenger Details Entry**: Input passenger names, ages, mobile numbers, and Gmail addresses.
- **Seat Selection**: Select semi-sleeper and sleeper seats with pricing information.
- **Validation**: Validates mobile numbers and Gmail addresses to ensure accuracy.
- **Booking Summary**: Displays a summary of the booking details, including total price and selected seats.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/yourbus.git
    cd bus-ticket-app
    ```

2. **Install Dependencies**:
    This application uses the Tkinter library, which is included in the standard Python library. Ensure you have Python installed on your machine.

    ```bash
    pip install tkinter
    pip install datetime
    ```

3. **Run the Application**:
    ```bash
    python main.py
    ```

## Usage

1. **Launch the Application**:
   Run the Python script to open the main application window.

2. **Enter Journey Details**:
   - Select the 'From' and 'To' locations from the dropdown menus.
   - Choose the travel date (day, month, and year).

3. **Enter Number of Passengers**:
   - Input the number of passengers and click the "Enter Passenger Details" button.

4. **Enter Passenger Information**:
   - A new window will open to input the name, age, mobile number, and Gmail address for each passenger.
   - Ensure the mobile number is a valid 10-digit number starting with 9, 8, 7, or 6.
   - Ensure the email address ends with "@gmail.com".

5. **Select Seats**:
   - Another window will open for seat selection.
   - Choose semi-sleeper or sleeper seats by checking the appropriate boxes.
   - Click "Confirm Selection" to finalize your seat selection.

6. **Booking Summary**:
   - After confirming seat selection, a summary window will display the booking details, including the total price and selected seats.




