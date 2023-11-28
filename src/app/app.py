# Importing necessary libraries
import random
import streamlit as st
import datetime


import pandas as pd

st.set_page_config(layout="wide", initial_sidebar_state="auto")


# Sample data for the table
data = {
    "Host ID": [1, 2, 3],
    "Firstname": ["John", "Alice", "Bob"],
    "Lastname": ["Doe", "Smith", "Johnson"],
    "Address": ["123 Main St", "456 Oak Ave", "789 Pine Blvd"],
    "Postcode": ["10001", "20002", "30003"],
    "Phone Number": ["555-1234", "555-5678", "555-9876"],
    "Email Address": ["john@example.com", "alice@example.com", "bob@example.com"],
    "Date": ["2023-01-01", "2023-02-15", "2023-03-30"],
    "Button": [False, True, True],
}

# Creating a DataFrame from the sample data
df = pd.DataFrame(data)


def display_requests(request, telephone=False):
    if request.get("status") not in ["New"]:
        disabled = True
    else:
        disabled = False

    if not telephone:
        st.markdown(f"### REQ. ID: {request.get('request_id')}")
        st.button(
            f"Send message to Hosts for {str(request.get('request_id'))}",
            disabled=disabled,
        )
        st.write(f"`Status: {request.get('status')}`")
        st.write(f"**Time:** {request.get('date')}")
        st.write(f"**Guest:** {request.get('guest_name')}")
        st.write(f"**Post Code:** {request.get('guest_postcode')}")
        st.write(f"**Accomodation Type:** {request.get('guest_accomodation_type')}")
        st.markdown("---")
    else:
        st.markdown(f"### REQ. ID: {request.get('request_id')}")
        st.button(
            f"Send message to Hosts for {str(request.get('request_id'))}",
            disabled=disabled,
        )
        st.write(f"`Status: {request.get('status')}`")
        st.write(f"**Time:** {request.get('date')}")
        st.write(f"**Message:** {request.get('transcription')}")
        st.markdown("---")


def display_requests_for_host(request, telephone=False):
    if request.get("status") not in ["New"]:
        disabled = True
    else:
        disabled = False

    if not telephone:
        st.markdown(f"### REQ. ID: {request.get('request_id')}")
        st.write(f"**Time:** {request.get('date')}")
        st.write(f"**Guest:** {request.get('guest_name')}")
        st.write(f"**Accomodation Type:** {request.get('guest_accomodation_type')}")
        col1, col2 = st.columns(
            [
                0.1,
                0.8,
            ]
        )
        with col1:
            st.button(f"Approve", key=f"Approve_{request.get('request_id')}")
        with col2:
            st.button(f"Reject", key=f"Reject_{request.get('request_id')}")
        st.markdown("---")
    else:
        st.markdown(f"### REQ. ID: {request.get('request_id')}")

        st.write(f"**Time:** {request.get('date')}")
        st.write(f"**Message:** {request.get('transcription')}")
        col1, col2 = st.columns(
            [
                0.1,
                0.8,
            ]
        )
        with col1:
            st.button(f"Approve", key=f"Approve_{request.get('request_id')}")
        with col2:
            st.button(f"Reject", key=f"Reject_{request.get('request_id')}")
        st.markdown("---")


status_options = ["New", "Submitted", "Accepted", "Rejected"]
transcription_message = "Hi, is this the charity? yeah I need a place to stay for 2 days, my family kicked me out so I'm on the street. No I don't have any kids or pets, where am I? I'm around north london, tower hill. I'm 33 years old, female. Yeah thank you so much I'll waiting for your call"
summary_message = "A 33-year-old female from North London near Tower Hill is looking for a place to stay for two days after being kicked out of her family home. She does not have any children or pets."
accomodation_types = ["Private room", "Shared room", "Sofa bed"]


def main():
    if "requests" not in st.session_state:
        st.session_state["requests"] = [
            (
                {
                    "request_id": 1234,
                    "status": status_options[0],
                    "transcription": summary_message,
                    "date": datetime.date.today(),
                },
                True,
            ),
            (
                {
                    "request_id": 1235,
                    "status": status_options[1],
                    "guest_name": "Amanda",
                    "guest_postcode": "W1A 1AA",
                    "guest_accomodation_type": accomodation_types[0],
                    "date": datetime.date.today(),
                },
                False,
            ),
        ]

    if "create_new_request" not in st.session_state:
        st.session_state["create_new_request"] = False

    if "host_inbox" not in st.session_state:
        st.session_state["host_inbox"] = []

    tab1, tab2, tab3 = st.tabs(["HOST", "Charity", "Requests"])
    # ! HOST
    with tab1:
        host_col1, host_col2 = st.columns(2)
        with host_col1:
            st.title("Host Profile")
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Name", "Alice")
            with col2:
                last_name = st.text_input("Last_name", "Smith")
            col1, col2 = st.columns(2)
            with col1:
                address = st.text_input("Address", "42 Acacia Avenue")
            with col2:
                guest_postcode = st.text_input("Host Postcode", "W1A 1AA")
            col1, col2 = st.columns(2)
            with col1:
                guest_phone = st.text_input("Phone", "020 1234 5678")
            with col2:
                email = st.text_input("Email", "alice@example.com")

            guest_accomodation_type = st.selectbox(
                "Accomodation", accomodation_types, 1, key="host_accomodation"
            )

            update_details = st.button("Update Details")

            today = datetime.datetime.now()
            next_year = today.year + 1
            jan_1 = datetime.date(next_year, 1, 1)
            dec_31 = datetime.date(next_year, 12, 31)

            availability = st.date_input(
                "Select your availability",
                (jan_1, datetime.date(next_year, 1, 7)),
                jan_1,
                dec_31,
                format="MM.DD.YYYY",
            )
        with host_col2:
            st.title("Host Inbox")

            for req, telephone in st.session_state["requests"]:
                display_requests_for_host(req, telephone)

    # ! Charity
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.title("Charity")

            selected_date = st.date_input("Select a date", datetime.date.today())
            st.write("You selected:", selected_date)

            guest_postcode = st.text_input("Homeless Postcode")
            guest_accomodation_type = st.selectbox(
                "Accomodation",
                ["Private room", "Shared room", "Sofa bed"],
                0,
                key="guest_accomodation",
            )

            # Display the table
            st.write("Sample Table:")
            
            st.table(df)

        with col2:
            st.title("Charity Inbox")

            for request, telephone in st.session_state["requests"]:
                display_requests(request, telephone)

                # if send_message_button:
                #     st.warning("Message sent!")

    # ! Requests
    with tab3:
        st.title("Requests")
        request_col1, request_col2 = st.columns(2)

        with request_col1:
            st.title("New Request")
            col1, col2 = st.columns(2)
            with col1:
                guest_name = st.text_input("Guest Name")
            with col2:
                guest_postcode = st.text_input("Guest Postcode")
            col1, col2 = st.columns(2)
            with col1:
                guest_phone = st.text_input("Guest Phone")

            guest_accomodation_type = st.selectbox(
                "Guest Accomodation", ["Private room", "Shared room", "Sofa bed"], 0
            )
            new_request = dict(
                request_id=random.randint(1000, 9999),
                date=str(datetime.datetime.today().strftime("%D %M %Y | %H:%M:%S")),
                status="New",
                guest_name=guest_name,
                guest_postcode=guest_postcode,
                guest_phone=guest_phone,
                guest_accomodation_type=guest_accomodation_type,
            )
            st.session_state["create_new_request"] = st.button("Create new request")
            if st.session_state["create_new_request"]:
                st.session_state["requests"].append((new_request, False))
                st.session_state["create_new_request"] = False

        # st.session_state["host_inbox"].append(new_request)

        # with request_col2:
        # st.title("Requests Feed")
        # display_requests(st.session_state["requests"])


# Run the app
if __name__ == "__main__":
    main()
