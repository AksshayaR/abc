import pandas as pd
import streamlit as st
import plotly.express as px
from db import view_all_customer


def read():
    result = view_all_customer()
    # st.write(result)
    df = pd.DataFrame(result, columns=['c_id', 'cust_name', 'cust_mobile', 'cust_email', 'check_in', 'check_out'])
    with st.expander("View all Customers"):
        st.dataframe(df)
    '''with st.expander("Room Details"):
        train_df = df['Availability'].value_counts().to_frame()
        train_df = train_df.reset_index()
        st.dataframe(train_df)
        p1 = px.pie(train_df, names='index', values='Availability')
        st.plotly_chart(p1)'''