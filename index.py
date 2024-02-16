import requests
import plotly.graph_objects as go
import streamlit as st

api_key = 'd711e292439bac5ac4a771bbe3a4c704'
st.set_page_config(layout="wide")
st.title("Jimmy's Wacky Weather Dashboard")
city = st.text_input("Where do you live?","berwick",key="city")

if city:
    st.balloons()
    if city.isdigit():
        params = {'zip': city, 'appid': api_key}
    else:
        params = {'q': city, 'appid': api_key}

    api_endpoint = 'https://api.openweathermap.org/data/2.5/weather?units=imperial'

    response = requests.get(api_endpoint, params=params)
    
    if response.status_code == 200:
        data = response.json()
    print(response.json())
    col1, col2, col3 = st.columns(3)  # Create three columns for the charts
    fig1 = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=data['main']['temp'],
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Temp in Fahrenheit", 'font': {'size': 24}},
        delta={'reference': 22, 'increasing': {'color': "RebeccaPurple"}},
        gauge={
            'axis': {'range': [None, 60], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 10], 'color': 'lightblue'},
                {'range': [10, 20], 'color': 'darkolivegreen'},
                {'range': [20, 30], 'color': 'yellowgreen'},
                {'range': [30, 40], 'color': 'yellow'},
                {'range': [40, 50], 'color': 'orange'},
                {'range': [50, 60], 'color': 'red'}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 22}}))
    fig2 = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=data['main']['feels_like'],
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Feels like in Fahrenheit", 'font': {'size': 24}},
        delta={'reference': 22, 'increasing': {'color': "RebeccaPurple"}},
        gauge={
            'axis': {'range': [None, 60], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 10], 'color': 'lightblue'},
                {'range': [10, 20], 'color': 'darkolivegreen'},
                {'range': [20, 30], 'color': 'yellowgreen'},
                {'range': [30, 40], 'color': 'yellow'},
                {'range': [40, 50], 'color': 'orange'},
                {'range': [50, 60], 'color': 'red'}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 22}}))
    fig3 = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=data['main']['temp_max'],
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Temp max in Fahrenheit", 'font': {'size': 24}},
        delta={'reference': 22, 'increasing': {'color': "RebeccaPurple"}},
        gauge={
            'axis': {'range': [None, 60], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 10], 'color': 'lightblue'},
                {'range': [10, 20], 'color': 'darkolivegreen'},
                {'range': [20, 30], 'color': 'yellowgreen'},
                {'range': [30, 40], 'color': 'yellow'},
                {'range': [40, 50], 'color': 'orange'},
                {'range': [50, 60], 'color': 'red'}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 22}}))
    # Dark background layout
    fig1.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent plot background
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent paper background
        height=400,  # Adjust the height
        width=400,   # Adjust the width
    )
        # Dark background layout
    fig2.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent plot background
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent paper background
        height=400,  # Adjust the height
        width=400,   # Adjust the width
    )
    fig3.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent plot background
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent paper background
        height=400,  # Adjust the height
        width=400,   # Adjust the width
    )

    # Place each chart in its own column
    with st.container():
        st.text("")  # Add empty space for alignment
        with col1:
            st.write(f"The weather outside has {data['weather'][0]['description']}")
            st.plotly_chart(fig1)
        with col2:
            st.write(f"The pressure outside is {data['main']['pressure']} Pascals")
            st.plotly_chart(fig2)
        with col3:
            st.write(f"The humidity outside is {data['main']['humidity']} g/kg")
            st.plotly_chart(fig3)



#fig.show()