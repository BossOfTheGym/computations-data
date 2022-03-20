import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

tiled_data = [
	[0,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,2,2,2,2,2,2,2,2,1,0],
	[0,1,2,3,3,3,3,3,3,2,1,0],
	[0,1,2,3,3,3,3,3,3,2,1,0],
	[0,1,2,3,3,3,3,3,3,2,1,0],
	[0,1,2,3,3,3,3,3,3,2,1,0],
	[0,1,2,3,3,3,3,3,3,2,1,0],
	[0,1,2,3,3,3,3,3,3,2,1,0],
	[0,1,2,2,2,2,2,2,2,2,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,0],
	[0,0,0,0,0,0,0,0,0,0,0,0],
]

tiled_store_mask = [
	[0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,1,1,1,1,1,1,0,0,0],
	[0,0,0,1,1,1,1,1,1,0,0,0],
	[0,0,0,1,1,1,1,1,1,0,0,0],
	[0,0,0,1,1,1,1,1,1,0,0,0],
	[0,0,0,1,1,1,1,1,1,0,0,0],
	[0,0,0,1,1,1,1,1,1,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0],
]

small_tile_st0_data = [
	[0,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,2,2,2,2,2,2,2,2,1,0],
	[0,1,2,2,2,2,2,2,2,2,1,0],
	[0,1,2,2,2,2,2,2,2,2,1,0],
	[0,1,2,2,2,2,2,2,2,2,1,0],
	[0,1,2,2,2,2,2,2,2,2,1,0],
	[0,1,2,2,2,2,2,2,2,2,1,0],
	[0,1,2,2,2,2,2,2,2,2,1,0],
	[0,1,2,2,2,2,2,2,2,2,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,0],
	[0,0,0,0,0,0,0,0,0,0,0,0],
]

small_tile_st0_store_mask = [
	[0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,2,2,2,0,0,0,0],
	[0,0,0,0,2,2,2,2,2,0,0,0],
	[0,0,3,5,5,5,5,5,5,0,0,0],
	[0,3,3,5,5,5,5,5,5,1,0,0],
	[0,3,3,5,5,5,5,5,5,1,1,0],
	[0,3,3,5,5,5,5,5,5,1,1,0],
	[0,0,3,5,5,5,5,5,5,1,1,0],
	[0,0,0,5,5,5,5,5,5,1,0,0],
	[0,0,0,4,4,4,4,4,0,0,0,0],
	[0,0,0,0,4,4,4,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0],
]

small_tile_st1_data = [
	[2,2,2,2,2,2,2,2],
	[2,2,2,2,2,2,2,2],
	[2,2,1,1,1,1,2,2],
	[2,2,1,0,0,1,2,2],
	[2,2,1,0,0,1,2,2],
	[2,2,1,1,1,1,2,2],
	[2,2,2,2,2,2,2,2],
	[2,2,2,2,2,2,2,2],
]

small_tile_st1_store_mask = [
	[5,5,5,5,5,5,5,5],
	[5,4,4,4,4,4,3,5],
	[5,1,4,4,4,3,3,5],
	[5,1,1,0,0,3,3,5],
	[5,1,1,0,0,3,3,5],
	[5,1,1,2,2,2,3,5],
	[5,1,2,2,2,2,2,5],
	[5,5,5,5,5,5,5,5],
]

good_store_mask = [
	[5,1,1,0,0,0,0],
	[5,1,1,0,0,0,0],
	[5,1,1,0,0,0,0],
	[5,1,1,0,0,0,0],
	[5,1,1,2,2,2,2],
	[5,1,2,2,2,2,2],
	[5,5,5,5,5,5,5],
]

bad_store_mask = [
	[5,0,0,0,0,0,0],
	[5,1,0,0,0,0,0],
	[5,1,1,0,0,0,0],
	[5,1,1,0,0,0,0],
	[5,1,1,2,2,2,0],
	[5,1,2,2,2,2,2],
	[5,5,5,5,5,5,5],
]

steps_example = [
	[-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
	[-2,-1,-1,-1,-1,-1,-1,-1,-1,-2],
	[-2,-1,+0,+0,+0,+0,+0,+0,-1,-2],
	[-2,-1,+0,+1,+1,+1,+1,+0,-1,-2],
	[-2,-1,+0,+1,+2,+2,+1,+0,-1,-2],
	[-2,-1,+0,+1,+2,+2,+1,+0,-1,-2],
	[-2,-1,+0,+1,+1,+1,+1,+0,-1,-2],
	[-2,-1,+0,+0,+0,+0,+0,+0,-1,-2],
	[-2,-1,-1,-1,-1,-1,-1,-1,-1,-2],
	[-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
]

def greyscale(min_val=0, max_val=1):
	return [[min_val, 'rgb(0,0,0)'], [max_val, 'rgb(255,255,255)']]

def greenredscale(min_val=0, max_val=1):
	return [[min_val, 'rgb(80,240,90)'], [max_val, 'rgb(240,80,90)']]

def greybg():
	return 'rgb(225,225,225)'

def buildmaskchart(mask, transpose = True):
	fig = go.Figure()
	fig.add_trace(
		go.Heatmap(
			z = mask,
			transpose = transpose,
			colorscale=greyscale()))
	fig.update_layout(
		font={'size':20},
		paper_bgcolor = greybg(),
		plot_bgcolor = greybg(),
		width = 400)
	fig.update_traces(showscale = False)
	fig.update_xaxes(showticklabels = False, gridcolor = greybg(), showgrid = False, visible = False)
	fig.update_yaxes(showticklabels = False, scaleanchor = 'x', gridcolor = greybg(), showgrid = False, visible = False)
	fig.update_annotations(font_size=20)
	fig.show()

def builddistinctchart(data, transpose = True):
	fig = go.Figure()
	fig.add_trace(
		go.Heatmap(
			z = data,
			transpose = transpose,
			texttemplate = '%{z:d}',
			colorscale=greenredscale()
		)
	)
	fig.update_layout(width = 500, height = 500)
	fig.update_traces(showscale = False)
	fig.update_xaxes(showticklabels = False, gridcolor = greybg(), showgrid = False, visible = False)
	fig.update_yaxes(showticklabels = False, scaleanchor = 'x', gridcolor = greybg(), showgrid = False, visible = False)
	fig.update_annotations(font_size=20)
	fig.show()

def buildchart(data, store_mask, title, transpose = True):
	fig = make_subplots(1, 2, subplot_titles = ['<b>Номер итерации</b>', '<b>Шаблон сохранения</b>']) # iteration number & store mask
	fig.add_trace(
		go.Heatmap(
			z = data,
			transpose = transpose,
			texttemplate = '%{z:d}',
			colorscale=greenredscale()),
		1, 1)
	fig.add_trace(
		go.Heatmap(
			z = store_mask,
			transpose = transpose,
			colorscale=greyscale()),
		1, 2)
	fig.update_layout(
		font={'size':20},
		paper_bgcolor = greybg(),
		plot_bgcolor = greybg(),
		title = {
			'x':0.5,
			'text': f"<b>{title}</b>",
			'xanchor': 'center',
			'yanchor': 'top'}, width=800)
	fig.update_traces(showscale = False)
	fig.update_xaxes(showticklabels = False, gridcolor = greybg(), showgrid = False, visible = 	False)
	fig.update_yaxes(showticklabels = False, scaleanchor = 'x', gridcolor = greybg(), showgrid = False, visible = False)
	fig.update_annotations(font_size=20)
	fig.show()

buildchart(tiled_data, tiled_store_mask, 'Тайлинг с перекрытиями') # simple tiling with overlaps

buildchart(small_tile_st0_data, small_tile_st0_store_mask, 'Малые перекрытия. Стадия 1.') # small overlaps
buildchart(small_tile_st1_data, small_tile_st1_store_mask, 'Малые перекрытия. Стадия 2.') # small overlaps

buildmaskchart(small_tile_st0_store_mask)
buildmaskchart(small_tile_st1_store_mask)

buildmaskchart(good_store_mask, False)
buildmaskchart(bad_store_mask, False)

builddistinctchart(steps_example)