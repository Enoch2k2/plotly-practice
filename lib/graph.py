import pandas
import os
import plotly
cwd = os.getcwd()

def create_graph():
  file_name = cwd + "/lib/cities.xlsx"
  travel_df = pandas.read_excel(file_name)
  cities = travel_df.to_dict("records")
  x_values = [cities[0]['City'], cities[1]['City'], cities[2]['City']]
  y_values = [cities[0]['Population'], cities[1]['Population'], cities[2]['Population']]
  trace_first_three_pops = {'type': 'bar', 'x': x_values, 'y': y_values}
  plotly.offline.plot([trace_first_three_pops])