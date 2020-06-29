## Step 1
import pandas as pd

## Step 2
import matplotlib.pyplot as plt

## Step 3
from data import games

## Step 4
attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'), ['year', 'multi3']]

## Step 5
attendance.columns = ['year', 'attendance']

## Step 6
attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])
print(attendance)

## Step 7 and 8
attendance.plot(x = 'year', y = 'attendance', figsize = (15, 7), kind = 'bar')
plt.xlabel('Year')
plt.ylabel('Attendance')
## Step 9
plt.axhline(y = attendance['attendance'].mean(), label = 'Mean', linestyle = '--', color = 'green')

plt.show()
