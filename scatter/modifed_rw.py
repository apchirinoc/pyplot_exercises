import matplotlib.pyplot as plt

from randomwalk import RandomWalk

plt.style.use('seaborn')

def main():
    """Root function."""

    while True:
        rw = RandomWalk()
        rw.fill_walk()

        fig, ax = plt.subplots()
        point_numbers = range(rw.num_points)
        ax.scatter(rw.x_values, rw.y_values, s=5, c=point_numbers, 
                cmap=plt.cm.Blues, edgecolors='none')

        ax.scatter(0, 0, c='green', s=50)
        ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=50)

        plt.show()

        keep_running = input('Do you want to make another walk? (y/n): ')
        if keep_running.lower() == 'n':
            break

if __name__=='__main__':
    main()

