import streamlit as st

USERS = ['admin', 'manager']
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

def login():
    st.title("Login page")
    username = st.text_input("User name")
    if st.button("Login"):
        if username:
            if username in USERS:
                st.session_state.logged_in = True
                st.session_state.user_name = username
            else:
                st.session_state.logged_in = False
                st.session_state.user_name = username
        else:
            st.warning("Please input your username")

def factorial_calculator():
    st.write(f"Hello, {st.session_state.user_name}")
    if st.button("Sign out"):
        st.session_state.logged_in = False
        st.session_state.user_name = ""
        
    number = st.number_input("Please input a number", min_value = 0, max_value = 100)
    if st.button("Calculate"):
        result = fact(number)
        st.write(f"The factorial of {number} is {result}")


def main():
    st.title('Factorial Calculation App')

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if "username" not in st.session_state:
        st.session_state.username = ""
    
    if st.session_state.logged_in:
        factorial_calculator()
    else:
        login()

if __name__ == "__main__":
    main()