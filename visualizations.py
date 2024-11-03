import streamlit as st
import pandas as pd
import plotly.express as px

def display_visualizations():
    """Display data visualizations on environmental impacts."""
    st.header("Data Visualization on Environmental Impacts")
    st.write("Explore trends in deforestation and CO₂ emissions over the years.")

    mock_data = {
        'Year': [2000, 2005, 2010, 2015, 2020],
        'Deforestation (sq km)': [12000, 13000, 11500, 14000, 12500],
        'CO2 Emissions (million tons)': [2200, 2500, 2700, 3000, 3300]
    }
    df = pd.DataFrame(mock_data)
    fig = px.line(df, x='Year', y=['Deforestation (sq km)', 'CO2 Emissions (million tons)'], title="Environmental Impact Over Time")
    st.plotly_chart(fig)

    # Feedback Section
    st.header("Rate Your Eco-Art Experience")
    rating = st.slider("Rate your eco-art experience (1 = Needs Improvement, 5 = Excellent)", 1, 5)
    if st.button("Submit Rating"):
        st.write("Thank you for your feedback! Your rating helps us improve.")
