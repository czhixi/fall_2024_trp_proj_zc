import plotly.express as px
# Load data and compute static values
from shinywidgets import render_plotly

from pathlib import Path

from shiny import ui, render, App, reactive
import xarray as xr
import plotly.express as px
import plotly.graph_objects as go

app_ui = ui.page_auto(
    ui.h1("ENSO Teleconnection Maps"),
    ui.input_select(
        "variable",  
        "Select an climate variable below:", 
        {"precip": "Precipitation", "ssr": "Solar Radiation", "temp": "Temperature"}
    ),

    ui.input_selectize(
        "oscillation",  
        "Select type of oscillation below:",  
        {"lanina":"La Nina", "elnino":"El Nino", "normal": "Neutral"}, 
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
        ui.output_image("pvaluemap", height="100%")
    ),

    ui.card(
        ui.card_header("Seasonal"),
        ui.output_image("seasonalmap", height="100%")
    ),
)



def server(input, output, session):
    
    @render.image
    def pvaluemap():
        #print(Path(__file__).parent /'static'/'ENSO Teleconnection Maps'/f'{input.variable()}'/f"pvalue_maps_{input.oscillation()}.png")
        #print(input.variable())
        #print(input.oscillation())
        img = {"src": str(Path(__file__).parent /'static'/'ENSO Teleconnection Maps'/f'{input.variable()}'/f"pvalue_maps_{input.oscillation()}.png"), "width": "100%"}  
        return img
    
    @render.image
    def seasonalmap():
        print(input.season())
        print(Path(__file__).parent /'static'/'ENSO Teleconnection Maps'/f'{input.variable()}'/f"prob_{input.oscillation()}_season_{input.season()}.png")
        img = {"src": str(Path(__file__).parent /'static'/'ENSO Teleconnection Maps'/f'{input.variable()}'/f"prob_{input.oscillation()}_season_{input.season()}.png"), "width": "100%"}  
        return img

app=App(app_ui, server)