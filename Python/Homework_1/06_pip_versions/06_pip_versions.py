import requests


def versions(pkg_name):
    url = f'https://pypi.python.org/pypi/{pkg_name}/json'
    releases = requests.get(url).json()['releases'].keys()
    return list(releases)
