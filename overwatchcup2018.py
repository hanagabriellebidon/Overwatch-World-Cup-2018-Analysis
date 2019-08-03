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

# Parse all the team fights between two teams in each map and round type.
def parse_match(mat):
    num_teamfight = len(mat['Map']['Roundtype'])
    df_teamfightStats = pd.DataFrame({mat['teamfightID']:{'Map': mat['Map'], 'Round Type': mat['Roundtype'],
    'Blue Team': mat['Blue Team'], 'Red Team': mat['Red Team'], 'Beginning of Fight': mat['Time stamp when fight began'],
    'Length of Teamfight': mat['length of fight in seconds'], 'Kils Blue': mat['Kills Blue'], 'Kills Red': mat['Kills Red'],
    'Ults Blue': mat['Ults Blue'], 'Ults Red': mat['Ults Red'], 'First Blood': mat['First Blood']}})
    return (df_teamfightStats.transpose())

with open('owc_teamfight.json') as json_data:
    teamfight_stats = json.load(json_data)
init_teamfight = teamfight_stats[0].copy()
init_teamfight['teamfightID'] = 'teamfight'

df_teamfightStats = parse_match(init_teamfight)

# with open('owl.json') as json_data:
#     match_stats = json.load(json_data)
#
# init_match = match_stats[0].copy()
# init_match['matchID']= 'trial'
# df_matchStats = parse_match(init_match)
#
# for match in match_stats:
#
#     df_matchStats = pd.concat([df_matchStats, parse_match(match)])
#
# df_matchStats = df_matchStats.drop('trial', axis = 0)
# df_matchStats = df_matchStats[['Date', 'Team1', 'Team2', 'Team1_Score', 'Team2_Score',
#                              'Fights_1', 'Fights_2', 'Kills_1', 'Kills_2',
#                              'Map1', 'Score_1_1', 'Score_1_2', 'MatchDet_1_1', 'MatchDet_1_2',
#                              'Map2', 'Score_2_1', 'Score_2_2', 'MatchDet_2_1', 'MatchDet_2_2',
#                              'Map3', 'Score_3_1', 'Score_3_2', 'MatchDet_3_1', 'MatchDet_3_2',
#                              'Map4', 'Score_4_1', 'Score_4_2', 'MatchDet_4_1', 'MatchDet_4_2',
#                              'Map5', 'Score_5_1', 'Score_5_2', 'MatchDet_5_1', 'MatchDet_5_2'
#                              ]]
#
# df_matchStats['Team1_Score'] = pd.to_numeric(df_matchStats['Team1_Score'])
# df_matchStats['Team2_Score'] = pd.to_numeric(df_matchStats['Team2_Score'])
# df_matchStats['Fights_1'] = pd.to_numeric(df_matchStats['Fights_1'])
# df_matchStats['Fights_2'] = pd.to_numeric(df_matchStats['Fights_2'])
# df_matchStats['Kills_1'] = pd.to_numeric(df_matchStats['Kills_1'])
# df_matchStats['Kills_2'] = pd.to_numeric(df_matchStats['Kills_2'])
# df_matchStats['Score_1_1'] = pd.to_numeric(df_matchStats['Score_1_1'])
# df_matchStats['Score_1_2'] = pd.to_numeric(df_matchStats['Score_1_2'])
# df_matchStats['Score_2_1'] = pd.to_numeric(df_matchStats['Score_2_1'])
# df_matchStats['Score_2_2'] = pd.to_numeric(df_matchStats['Score_2_2'])
# df_matchStats['Score_3_1'] = pd.to_numeric(df_matchStats['Score_3_1'])
# df_matchStats['Score_3_2'] = pd.to_numeric(df_matchStats['Score_3_2'])
# df_matchStats['Score_4_1'] = pd.to_numeric(df_matchStats['Score_4_1'])
# df_matchStats['Score_4_2'] = pd.to_numeric(df_matchStats['Score_4_2'])
