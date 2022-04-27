from src.config import get_url, get_soup


def check_private(link):
    url = get_url(link)[0]
    soup = get_soup(url)
    a = soup.find_all('p', class_='mt-3 mb-0')
    if len(a) == 0:
        return False
    return True


# print(check_private('bendover#fast'))
