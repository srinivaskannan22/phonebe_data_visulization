import streamlit as st 

import  plotly.express  as pe

from database import data_injection
import pandas as pd

st.title('Plotly Data-visulization')

tap1,tap2,tap3=st.tabs(['insurance','transaction','user'] )


 

with tap1:
    data,column_name=data_injection('top_transaction_state')
    data_=pd.DataFrame(data,columns=column_name)
    x_axis=st.selectbox(label='xaxsis',options=column_name)
    y_axis=st.selectbox(label='yaxsis',options=column_name)
    # st.dataframe(data_)
    button=st.button(label='onclick')
    if button:
        plotly=pe.bar(data_frame=data_,x=x_axis,y=y_axis)
        st.plotly_chart(plotly)

    




