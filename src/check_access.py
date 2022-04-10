from src.config import soup


def check_private(url):
    a = soup.find_all('p', class_='mt-3 mb-0')
    if len(a) == 0:
        return False
    return True


# check_private(url)
