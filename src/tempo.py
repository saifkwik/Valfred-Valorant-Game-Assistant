game_name = []


def take_input(username=''):
    if username == '':
        username = input('Enter your gamename with tag (ex -peacemaker#dceu) : ').strip().lower()
        if '#' not in username:
            print("missing tag '#'")
            exit()
    username = username.replace(' ', '').replace('#', '-')
    # game_name.append(username)
    url = "https://dak.gg/valorant/profile/{username}".format(username=username)
    game_name.append(username)
    # print(url)
    return url, game_name


def validate_input(soup):
    print('Checking if username is valid')
    a = soup.find_all('span', text='Please check nickname#tag and try again.')
    if len(a) == 0:
        print('Username is correct')
        return False
    print('Username is wrong')
    return True


# a = take_input(username='sensodyne#clear')
# print(a)
