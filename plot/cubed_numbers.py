import matplotlib.pyplot as plt

plt.style.use('seaborn')

def main():
    x_values = range(1, 5001)
    y_values = [x**3 for x in x_values]

    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=5)

    ax.set_title('Cubes')
    ax.set_xlabel('Values')
    ax.set_ylabel('Cubed Value')

    plt.show()


if __name__ == '__main__':
    main()
