import pandas as pd
import matplotlib.pyplot as plt

# Step 1
from frames import games, info, events

# Step 2
plays = games.query("type == 'play' & event != 'NP'")

# Step 3
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches',
'event', 'game_id', 'year']


# Step 4
pa = plays.loc[plays['player'].shift() != plays['player'],
['year', 'game_id', 'inning', 'team', 'player']]

# Step 5
pa = pa.groupby(['year', 'game_id', 'team']).size().reset_index(name = 'PA')

# Step 6
events = events.set_index(['year', 'game_id', 'team', 'event_type'])

# Step 7
events = events.unstack().fillna(0).reset_index()

# Step 8
events.columns = events.columns.droplevel()
events.columns = ['year', 'game_id', 'team', 'BB', 'E', 'H', 'HBP', 'HR', 'ROE', 'SO']
events = events.rename_axis(None, axis = 'columns')

# Step 9
events_plus_pa = pd.merge(events, pa, how = 'outer',
left_on = ['year', 'game_id', 'team'], right_on = ['year', 'game_id', 'team'])

# Step 10
defense = pd.merge(events_plus_pa, info)

# Step 11
defense.loc[:, 'DER'] = 1 - ((defense['H'] + defense['ROE']) / (defense['PA'] - defense['BB'] -
 defense['SO'] - defense['HBP'] - defense['HR']))
defense.loc[:, 'year'] = pd.to_numeric(defense.loc[:, 'year'])

# Step 12
der = defense.loc[defense['year'] >= 1978, ['year', 'defense', 'DER']]
der = der.pivot(index = 'year', columns = 'defense', values = 'DER')

# Step 13
der.plot(x_compat = True, xticks = range(1978, 2018, 4), rot = 45)
plt.show()
