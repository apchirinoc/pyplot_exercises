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
    dice_list = [die_1, die_2]

    # Make some rolls, and store results in a list
    results = roll_dice(dice_list, 1000)

    # Analyze the results.
    frequencies = get_roll_frequencies(results, dice_list)
    max_result = sum([die.num_sides for die in dice_list])
    min_result = len(dice_list)

    # Visualize the results.
    x_values = list(range(min_result, max_result+1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result', 'dtick': 1}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = Layout(title='Results of rolling two D8 50.000 times',
                    xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='d8.html')



def roll_dice(dice_list: List[Die], rolls: int = 1) -> List[int]:
    """Roll the dice in dice_list a given number of times"""
    results = []
    for roll_num in range(rolls):
        result = 0
        for die in dice_list:
            result += die.roll()

        results.append(result)

    return results


def get_roll_frequencies(results_list: List[int], dice_list: List[Die]) -> List[int]:
    min_result = len(dice_list)

    max_result = 0
    for die in dice_list:
        max_result += die.num_sides

    frequencies = []
    for value in range(min_result, max_result + 1):
        frequency = results_list.count(value)
        frequencies.append(frequency)

    return frequencies


def main():
    #d6_d10()
    d8()


if __name__ == "__main__":
    main()