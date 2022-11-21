import streamlit as st

from create import create
from database import create_table
from delete import delete
from see_customers import read
from update import update

from check_in import check_in
from check_out import check_out



def main():
    st.title("Hotel Management System")
    menu = ["Check in", "View customers", "Edit customer Info", "check out"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
    if choice == "Check in":
        st.subheader("Enter customer Details:")
        check_in()

    elif choice == "View customers":
        st.subheader("View customers Details:")
        read()

    elif choice == "Edit customers Info":
        st.subheader("Edited customers Details:")
        update()

    elif choice == "check out":
        st.subheader("check out:")
        check_out()

    else:
        st.subheader("About hotel")


if __name__ == '__main__':
    main()