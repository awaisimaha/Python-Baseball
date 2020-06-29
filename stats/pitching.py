import pandas as pd
import matplotlib.pyplot as plt
from data import games

# Step 1
plays = games[games['type'] == 'play']

# Step 2
strike_outs = plays[plays['event'].str.contains('K')]

# Step 3
strike_outs = strike_outs.groupby(['year', 'game_id']).size()

# Step 4
strike_outs = strike_outs.reset_index(name = 'strike_outs')

# Step 5
strike_outs = strike_outs.loc[:, ['year', 'strike_outs']].apply(pd.to_numeric)


# Step 6
strike_outs.plot(x = 'year', y = 'strike_outs', kind = 'scatter')
plt.legend(['Strike Outs'])
plt.show()
