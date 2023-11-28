# Importing necessary libraries
import streamlit as st

# Streamlit app
def main():
    # Title of the app
    st.title("Simple Streamlit App")

    # User input for a number
    user_input = st.number_input("Enter a number")

    # Square the input and display the result
    result = user_input ** 2
    st.write(f"The square of {user_input} is {result}")

# Run the app
if __name__ == "__main__":
    main()
