# Importing necessary libraries
import streamlit as st
import datetime
import pandas as pd

# Sample data for the table
data = {
    'Host ID': [1, 2, 3],
    'Firstname': ['John', 'Alice', 'Bob'],
    'Lastname': ['Doe', 'Smith', 'Johnson'],
    'Address': ['123 Main St', '456 Oak Ave', '789 Pine Blvd'],
    'Postcode': ['10001', '20002', '30003'],
    'Phone Number': ['555-1234', '555-5678', '555-9876'],
    'Email Address': ['john@example.com', 'alice@example.com', 'bob@example.com'],
    'Date': ['2023-01-01', '2023-02-15', '2023-03-30']
}

# Creating a DataFrame from the sample data
df = pd.DataFrame(data)


def add_user(user_details):
    user_details

    {
    'Host ID': [1, 2, 3],
    'Firstname': ['John', 'Alice', 'Bob'],
    'Lastname': ['Doe', 'Smith', 'Johnson'],
    'Address': ['123 Main St', '456 Oak Ave', '789 Pine Blvd'],
    'Postcode': ['10001', '20002', '30003'],
    'Phone Number': ['555-1234', '555-5678', '555-9876'],
    'Email Address': ['john@example.com', 'alice@example.com', 'bob@example.com']
    }

# def add_availability(first_date = datetime.datetime.now(), last_date):
#     d = st.date_input(
#         "Select your availabiltiy for hosting:",
#         (first_date, datetime.date(next_year, 1, 7)),
#         first_date,
#         last_date,
#         format="MM.DD.YYYY",
#     )



# Streamlit app
def main():
    # Title of the app
    st.title("Simple Streamlit App with Table")

    # User input for a number
    # Add a calendar input to select a date
    selected_date = st.date_input("Select a date", datetime.date.today())

    st.write("You selected:", selected_date)
    

    # Display the table
    st.write("Sample Table:")
    st.table(df)

# Run the app
if __name__ == "__main__":
    main()
