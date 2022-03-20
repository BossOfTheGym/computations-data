import sys
import json
import pathlib as pa
from collections import defaultdict as dedict

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# get args. argparse is for pussies
tiled  = sys.argv[1] # tiled methods 
simple = sys.argv[2] # single base method called here 'simple' for whatever reason
decrease_steps = int(sys.argv[3]) # used to adjust steps parameter, red_black methods use steps decreased by one

# print shit, ultimate coding ritual
print('shit') # this is required, trust me. otherwise it doesn't work. Babylon was built using this command

# print directory contents
print('tiled:')
for path in pa.Path(tiled).iterdir():
	print(path)
print()
print('simple:')
for path in pa.Path(simple).iterdir():
	print(path)

# process each directory
# result is dict (steps, x_split, y_split) / (work_x, work_y) / 'method' : time
def keyfrommeta(meta):
	return meta['steps'] - decrease_steps, meta['x_split'], meta['y_split']

def keyfrommetasimple(meta):
	return 1, meta['x_split'], meta['y_split']	

def workfrommeta(meta):
	return meta['workgroup_size_x'], meta['workgroup_size_y']

def transformtiled(data, meta):
	steps = meta['steps'] - decrease_steps
	steps = steps if steps > 0 else 1
	return {method:int(np.mean(stats['elapsed'][50:]) / steps) for method,stats in data.items()}

def transformsimple(data, meta):
	return {method:int(np.mean(stats['elapsed'][50:])) for method,stats in data.items()}

def processdir(dirpath, keyfunc, transformfunc):
	processed = dedict(dict)
	for path in pa.Path(dirpath).iterdir():
		with open(path) as file:
			data = json.load(file)
		meta = data['meta']
		data = data['data']

		processed[keyfunc(meta)][workfrommeta(meta)] = transformfunc(data, meta)
	return processed

tiled_processed = processdir(tiled, keyfrommeta, transformtiled)
simple_processed = processdir(simple, keyfrommetasimple, transformsimple)

# print processed
def treeprint(data, depth = 0):
	stride = "    " * depth
	for key, value in data.items():
		print(f"{stride}   >{key}")
		if isinstance(value, dict):
			treeprint(value, depth + 1)
		else:
			print(f"{stride}    {value}")

treeprint(tiled_processed)
print()
treeprint(simple_processed)

# draw test chart
def key2str(key):
		steps, x_split, y_split = key
		return f"steps:{steps} x_split:{x_split} y_split:{y_split}"

def buildchart(title, tiled_frame, simple_frame):
	dfs = {} # data fragments
	for work, tiled_data in tiled_frame.items():
		simple_data = simple_frame[work]

		tiled_df  = pd.DataFrame(tiled_data.items(), columns = ['method', 'time'])
		simple_df = pd.DataFrame(simple_data.items(), columns = ['method', 'time'])

		df = pd.concat([tiled_df, simple_df], ignore_index = True)

		dfs[str(work)] = df

	charts = []
	for work, df in dfs.items():
		charts.append(go.Bar(name = work, x = df['method'], y = df['time']))

	fig = go.Figure(data = charts)
	fig.update_layout(barmode = 'group',
		title={
			'text': f"<b>{title}</b>",
			'y':0.9,
			'x':0.5,
			'xanchor': 'center',
			'yanchor': 'top'},
		legend_title='размер блока', # workgroup size
		yaxis_title="ср. время на итерацию(нс)", # average time(nano sec)
		font={
			'size':14,
		},
		height = 450,
		width = 800)
	fig.show()

# build all charts
for tiled_key in tiled_processed:
	simple_key = (1, tiled_key[1], tiled_key[2])

	title = key2str(tiled_key)
	tiled_frame = tiled_processed[tiled_key]
	simple_frame = simple_processed[simple_key]
	buildchart(title, tiled_frame, simple_frame)