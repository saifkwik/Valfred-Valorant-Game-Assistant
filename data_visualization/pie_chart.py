
import matplotlib.pyplot as plt


def get_results(saved_match_data):
    end_result = []
    maps = []
    try:
        for g in range(30):
            end_result.append(saved_match_data[2][g]['END_RESULT'])
            maps.append(saved_match_data[2][g]['Map'])
    except IndexError:
        pass

    result = []
    for x in range(len(maps)):
        a = {maps[x]: end_result[x]}
        result.append(a)
    # pprint.pprint(result)
    return result


all_maps = ['Ascent', 'Bind', 'Breeze', 'Fracture', 'Haven', 'Icebox', 'Split']

matches_played = []


def get_freq(all_maps, saved_match_data):
    res = []
    result = get_results(saved_match_data)
    matches_played.append(len(result))
    for names in all_maps:
        i = 0
        j = 0
        a = []
        for freq in result:
            for key, value in freq.items():
                if key == names:
                    if key == names and value == 'Victory':
                        i += 1
                        j += 1
                    else:
                        j += 1
                    a = [names, i, j]
        res.append(a)
    return res


def pie_chart(player_name, saved_match_data):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    result = get_freq(all_maps, saved_match_data)
    result = list(filter(None, result))
    labels = []
    sizes = []
    won_matches = 0
    x = 0
    for label in range(len(result)):
        l = f'\n{all_maps[label]} \n Won {result[label][1]}/{result[label][2]}'
        labels.append(l)
        label += 1
        total_matches = len(result)
        size = result[x][2] / total_matches
        sizes.append(size)
        victory = result[x][1]
        won_matches = won_matches + victory

        x += 1
    max_val = max(sizes)
    max_index = sizes.index(max_val)
    explode_value = tuple([0 if i != max_index else 0.1 for i in range(len(sizes))])

    fig1, ax1 = plt.subplots()
    ax1.set_title(
        f'Map frequency of last 30 matches or less\n Win Percentage-{round(won_matches / matches_played[0] * 100, 2)}%')
    ax1.pie(sizes, explode=explode_value, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.savefig(f'C:\\Users\\Rango\PycharmProjects\\valorant-stats-tracker\\images\\{player_name}-MapFrequency&Win%', bbox_inches='tight', dpi=300)


# pie_chart()
