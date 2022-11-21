import streamlit as st




from see_customers import read
from update_db import update_customer

from check_in import check_in
from check_out import delete



def main():
    st.title("Hotel Management System")
    menu = ["Check in", "View customers", "Edit customer Info", "check out"]
    choice = st.sidebar.selectbox("Menu", menu)

    
    if choice == "Check in":
        st.subheader("Enter customer Details:")
        check_in()

    elif choice == "View customers":
        st.subheader("View customers Details:")
        read()

    elif choice == "Edit customers Info":
        st.subheader("Edited customers Details:")
        update_customer()

    elif choice == "check out":
        st.subheader("check out:")
        delete()

    else:
        st.subheader("About hotel")


if __name__ == '__main__':
    main()
