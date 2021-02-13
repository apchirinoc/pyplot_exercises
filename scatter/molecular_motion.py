import matplotlib.pyplot as plt

from randomwalk import RandomWalk

plt.style.use('seaborn')


def main():
    rw = RandomWalk()
    rw.fill_walk()

    fig, ax = plt.subplots()
    ax.plot(rw.x_values, rw.y_values, linewidth=5)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()


if __name__=='__main__':
    main()

