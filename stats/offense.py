import pandas as pd
import matplotlib.pyplot as plt

from data import games

# Step 1
plays = games[games['type'] == 'play']
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event',
 'game_id', 'year']

# Step 2
hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)'), ['inning', 'event']]

# Step 3
hits.loc[:, 'inning'] = pd.to_numeric(hits.loc[:, 'inning'])

# Step 4
replacements = {
r'^S(.*)': 'single',
r'^D(.*)': 'double',
r'^T(.*)': 'triple',
r'^HR(.*)': 'hr'
}

# Step 5
hit_type = hits['event'].replace(replacements, regex=True)

# Step 6
hits = hits.assign(hit_type=hit_type)

# Step 7
hits = hits.groupby(['inning', 'hit_type']).size().reset_index(name='count')

# Step 8
hits['hit_type'] = pd.Categorical(hits['hit_type'], ['single', 'double', 'triple', 'hr'])

# Step 9
hits = hits.sort_values(['inning', 'hit_type'])

# Step 10
hits = hits.pivot(index = 'inning', columns = 'hit_type', values = 'count')

# Step 11
hits.plot.bar(stacked = True)
plt.show()
