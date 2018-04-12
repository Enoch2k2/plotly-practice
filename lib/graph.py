import pandas
import os
import plotly
cwd = os.getcwd()

def create_graph():
  file_name = cwd + "/lib/cities.xlsx"
  travel_df = pandas.read_excel(file_name)
  cities = travel_df.to_dict("records")
  city_names = grab_all_names(cities)
  city_populations = grab_all_populations(cities)
  x_values = city_names
  y_values = city_populations
  trace_first_three_pops = {'type': 'bar', 'x': x_values, 'y': y_values}
  plotly.offline.plot([trace_first_three_pops])

def grab_all_names(cities):
  names = []
  for city in cities:
    names.append('{0} ({1})'.format(city['City'], city['Country']))
  return names

def grab_all_populations(cities):
  population = []
  for city in cities:
    population.append(city['Population'])
  return population