import streamlit as st

st.write("""
<h1 style= 'text-align:center;'> User registration form
""", unsafe_allow_html=True)

#way 1 to create form. Create object and use . operator

# form = st.form("Form 1")
# form.text_input("What is your reason!")
# form.form_submit_button("Submit")

#way 2 is with help of with keyword
with st.form("Form 2", clear_on_submit = True):

    #columns: returns number of columns
    col1, col2 = st.columns(2)
    fname = col1.text_input("First Name")
    lname = col2.text_input("Last Name")
    email = st.text_input("Email address")
    password = col1.text_input("Password")
    cpassword = col2.text_input("Confirm Password")

    day, month, year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")

    s_state = st.form_submit_button("Submit")
    if s_state:
        if fname == "" or lname == "":
            st.warning("Name can't be empty")
        else:
            st.success("Submitted Successfully")
