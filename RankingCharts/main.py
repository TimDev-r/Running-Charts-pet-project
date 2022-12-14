import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import numpy as np

db = pd.read_csv('dragon_ball_pl.csv')

one_row = db.iloc[0]
one_row_ascending = one_row.sort_values()
characters = db.columns

plt.scatter(X[:,-1], y, c=y)

num = 3
fig, axs = plt.subplots(nrows=1, ncols=num, figsize=(10, 5), tight_layout=True)
for i, ax in enumerate(axs):
    ax.barh(y=db.iloc[i].rank(),
            tick_label=db.iloc[i].index,
            width=db.iloc[i].values,
            color=plt.cm.Set1(range(6)))
    ax.set_title(f'{i}-th row', fontsize='larger')
    [spine.set_visible(False) for spine in ax.spines.values()]  # remove chart outlines


def update(i):
    ax.clear()
    ax.set_facecolor(plt.cm.Greys(0.2))
    [spine.set_visible(False) for spine in ax.spines.values()]
    hbars = ax.barh(y = db.iloc[i].rank().values,
                    tick_label=db.iloc[i].index,
                    width = db.iloc[i].values,
                    height = 0.8,
                    color = plt.cm.Set1(range(11))
                    )
    ax.set_title(f'Frame: {i}')
    #ax.bar_label(hbars, fmt='%.2d')


fig, ax = plt.subplots(  #figsize=(10,7),
    facecolor = plt.cm.Greys(0.2),
    dpi = 150,
    tight_layout=True
)

data_anime = FuncAnimation(
    fig = fig,
    func = update,
    frames= len(db),
    interval=300
)
data_anime.save('DrgBl.gif')