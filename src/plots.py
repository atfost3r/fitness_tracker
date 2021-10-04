#! python3

# plots.py - this is to get graphs for the progress etc.

import matplotlib.pyplot as plt

# TODO load in progress data daily
df_cals = pd.read_csv("src/databases/dailyProgressStats.csv", encoding="utf-8")
# TODO load in progress data weekly
df_cals = pd.read_csv("src/databases/weeklyProgressStats.csv", encoding="utf-8")
# TODO create weekly plot

#TODO create daily plot

# TODO Show the plot
plt.plot ([1,2,3,4])
plt.ylabel('some numbers')
plt.show()