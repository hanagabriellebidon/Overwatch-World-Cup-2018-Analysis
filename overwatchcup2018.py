import json
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set_style("white")
sns.set_context("paper", font_scale=0.9, rc={"lines.linewidth": 1.0})

AUSTRALIApal = ['#012169', '#FFFFFF', '#E4002B']
AUSTRIApal = ['#ED2939', '#FFFFFF']
BRAZILpal = ['#009C3B', '#FFDF00', '#002776', '#FFFFFF']
CANADApal = ['#FF0000', '#FFFFFF']
CHINApal = ['#DE2910', '#FFDE00']
DENMARKpal = ['#C60C30', '#FFFFFF']
FINLANDpal = ['#002F6C', '#FFFFFF']
FRANCEpal = ['#0055A4', '#FFFFFF', '#EF4135']
GERMANYpal = ['#000000', '#DD0000', '#FFCE00']
HONGKONGpal = ['#DE2408', '#FFFFFF']
ITALYpal = ['#008C45', '#F4F5F0', '#CD212A']
JAPANpal = ['#FFFFFF', '#BC002D']
NETHERLANDSpal = ['#AE1C28', '#FFFFFF', '#21468B']
NORWAYpal = ['#C8102E', '#FFFFFF', '#003087']
POLANDpal = ['#FFFFFF', '#DC143C']
RUSSIApal = ['#FFFFFF', '#0033A0', '#DA291C']
SOUTHKOREApal = ['#000000', '#FFFFFF', '#CD2E3A', '#0047A0']
SPAINpal = ['#AA151B', '#F1BF00', '#0039F0', '#CCCCCC', '#ED72AA', '#058E6E']
SWEDENpal = ['#004B87', '#FFCD00']
SWITZERLANDpal = ['#D52B1E', '#FFFFFF']
TAIWANpal = ['#000097', '#FFFFFF', '#FE0000']
THAILANDpal = ['#A51931', '#F4F5F8', '#2D2A4A']
UNITEDKINGDOMpal = ['#00247D', '#FFFFFF', '#CF142B']
UNITEDSTATESpal = ['#3C3B6E', '#FFFFFF', '#B22234']

with open('players.json') as json_data:
    players = json.load(json_data)

df_players = pd.DataFrame(players)

df_players = df_players[['playername', 'team', 'role']]

df_players.head()
print(df_players.head())
