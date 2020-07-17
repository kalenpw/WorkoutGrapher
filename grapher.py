import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import datetime as dt


def handle_graphing(exercises):
    graph_number = 1
    for key in exercises:
        graph_exercise(exercises[key], graph_number)



def graph_exercise(exercise, graph_number):
    # used for title
    exercise_name = exercise[0].name

    # X axis
    weights = []
    # Y axis
    dates = []

    # Y limits
    y_min = 0
    y_max = 0

    # build x axis of weights with y axis of date
    for day in exercise:
        for set in day.sets:
            dates.append(day.date)
            weights.append(int(set.weight))
            if int(set.weight) > y_max:
                y_max = int(set.weight)

    x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]
    y = weights

    # The colormap
    cmap = cm.jet

    # show 1 week before and after to have some padding
    date_min = np.datetime64(exercise[0].date)
    date_min = date_min - np.timedelta64(7, 'D')
    date_max = np.datetime64(exercise[-1].date)
    date_max = date_max + np.timedelta64(7, 'D')

    # leave arbitrary padding at top (+15)
    major_ticks = np.arange(0, y_max + 15, 25)
    minor_ticks = np.arange(0, y_max + 15, 5)

    # Create figure and axes
    fig = plt.figure(graph_number)
    fig.canvas.set_window_title("Workouts")
    fig.clf()
    ax = fig.add_subplot(1, 1, 1)

    c = np.linspace(0, 10, len(dates))
    ax.scatter(x, y, c=c, cmap=cmap)
    ax.set_xlim(date_min, date_max)
    ax.set_ylim(y_min, y_max + 15)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)
    ax.grid(which='major', axis='y')
    plt.xticks(rotation='vertical')
    plt.title(exercise_name.title())

    plt.show()
