from typing import List

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


def d6_d10():
    # Create a D6 and a D10.
    die_1 = Die()
    die_2 = Die(10)

    # Make some rolls, and store results in a list.
    results = []
    for roll_num in range(50_000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    # Analyze the results.
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # Visualize the results.
    x_values = list(range(2, max_result+1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result', 'dtick': 1}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = Layout(title='Results of rolling a D6 and a D10 50.000 times',
                    xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')


def d8():
    # Create two D8.
    die_1 = Die(8)
    die_2 = Die(8)

    # Make some rolls, and store results in a list
    results = roll_dice([die_1, die_2], 1000)

    # Visualize the results.
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # Visualize the results.
    x_values = list(range(2, max_result+1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result', 'dtick': 1}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = Layout(title='Results of rolling a D6 and a D10 50.000 times',
                    xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')



def roll_dice(dice_list: List[Die], rolls: int = 1) -> list:
    results = []
    for roll_num in range(rolls):
        result = 0
        for die in dice_list:
            result += die.roll()

        results.append(result)

    return results


def main():
    #d6_d10()
    d8()


if __name__ == "__main__":
    main()