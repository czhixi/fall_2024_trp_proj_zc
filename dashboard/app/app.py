import plotly.express as px

# Load data and compute static values
from shinywidgets import render_plotly

from shiny import ui, render, App, reactive
import xarray as xr
import plotly.express as px
import plotly.graph_objects as go

app_ui = ui.page_fillable(
    ui.h1("ENSO Teleconnection Maps"),
    ui.input_select(
        "variable",  
        "Select an climate variable below:", 
        {"precip": "Precipitation", "SSR": "Solar Radiation", "temp": "Temperature"}
    ),

    ui.input_selectize(
        "oscillation",  
        "Select type of oscillation below:",  
        {"A":"La Nina", "E":"El Nino", "N": "Neutral"}, 
    ),

    ui.input_select(
        "season",  
        "Select season below:", 
        {"NDJ": "November-December-January",
         "DJF": "December-January-February",
         "JFM": "January-February-March",
         "FMA": "February-March-April",
         "MAM": "March-April-May",
         "AMJ": "April-May-June",
         "MJJ": "May-June-July",
         "JJA": "June-July-August",
         "JAS": "July-August-September",
         "ASO": "August-September-October",
         "SON": "September-October-November",
         "OND": "October-November-December"}
    ),


    ui.card(
        ui.card_header("P-Value"),
        ui.output_image("pvaluemap")
    ),

    ui.card(
        ui.card_header("Seasonal"),
        ui.output_image("seasonalmap")
    ),
)

def server(input, output, session):
    def pvaluemap():
        return
    
    def seasonalmap():
        return

app=App(app_ui, server)