import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load your COVID-19 dataset
covid_data = pd.read_csv("C:\\Users\\Simran Gawri\\Downloads\\archive (4)\\country_wise_latest.csv")  # Replace with the actual path to your dataset

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("COVID-19 Dashboard"),

    # Dropdown for selecting a country
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in covid_data['Country/Region'].unique()],
        value='India'
    ),

    # Graph for displaying COVID-19 data
    dcc.Graph(id='covid-graph'),
])


# Define callback to update the graph based on the selected country
@app.callback(
    Output('covid-graph', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    country_data = covid_data[covid_data['Country/Region'] == selected_country]
    fig = px.bar(country_data, x='Country/Region', y=['Confirmed', 'Deaths', 'Recovered'],
                 title=f'COVID-19 Data in {selected_country}')
    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
