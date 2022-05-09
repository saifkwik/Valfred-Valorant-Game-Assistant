import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def bar_chart(saved_match_data, player_name):
    kills = []
    deaths = []
    maps = []
    try:
        for g in range(10):
            kills.append(saved_match_data[2][g]['Kills'])
            deaths.append(saved_match_data[2][g]['Deaths'])
            maps.append(saved_match_data[2][g]['Map'])
    except IndexError:
        pass
    kills = [int(i) for i in kills]
    deaths = [int(i) for i in deaths]

    x = np.arange(len(maps))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, kills, width, color='blue', label='Kills')
    rects2 = ax.bar(x + width / 2, deaths, width, color='orange', label='Deaths')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('')
    ax.set_title('Last 10 Match results')
    ax.set_xticks(x, maps)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    # plt.savefig(f'C:\\Users\\Rango\PycharmProjects\\valorant-stats-tracker\\images\\{player_name}-kill_vs_deaths.jpg', bbox_inches='tight', dpi =300)
    plt.savefig(f'C:\\Users\\Rango\PycharmProjects\\valorant-stats-tracker\\images\\KILLvsDEATHS.jpg',
                bbox_inches='tight', dpi=300)

    average_damage = []
    headshot_percentage = []
    maps = []
    try:
        for g in range(15):
            average_damage.append(saved_match_data[2][g]['AvgDmg'])
            headshot_percentage.append(saved_match_data[2][g]['HS %'].replace('%', ''))
            maps.append(saved_match_data[2][g]['Map'])
    except IndexError:
        pass
    average_damage = [int(i) for i in average_damage]
    headshot_percentage = [float(i) for i in headshot_percentage]

    data = {'Average Damage': average_damage,
            'Headshot Percent': headshot_percentage
            }
    df = pd.DataFrame(data, columns=['Average Damage', 'Headshot Percent'], index=maps)

    plt.style.use('ggplot')

    df.plot.barh()

    plt.title('Avg Damage and Headshot %')
    plt.ylabel('← 1 to 15 matches')
    # plt.savefig(f'C:\\Users\\Rango\PycharmProjects\\valorant-stats-tracker\\images\\{player_name}-avg_dmg&hs%.jpg', bbox_inches='tight', dpi =300)
    plt.savefig(f'C:\\Users\\Rango\PycharmProjects\\valorant-stats-tracker\\images\\average_damage&headshot_percentage.jpg',
                bbox_inches='tight', dpi=300)
