import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import datetime as dt

# The data
# x = np.linspace(0, 10, 1000)
# y = np.sin(2 * np.pi * x)
dates = [
    '2020-06-01',
    '2020-06-02',
    '2020-06-03',
]

x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]

y = [2,2,3]

# The colormap
# cmap = cm.jet
cmap, norm = mpl.colors.from_levels_and_colors([0, 1, 5, 6], ['red', 'green', 'blue'])

# Create figure and axes
fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(1, 1, 1)

c = np.linspace(0, 3, 3)
ax.scatter(x, y, c=c, cmap=cmap, norm=norm)

plt.show()