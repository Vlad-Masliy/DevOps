import threading
import requests
import json


response_list = list()


def check_urls(url):
    res ={'url': url}
    try:
        response = requests.get(url)
        res['status_code'] = response.status_code
        res['is_ok'] = response.ok
    except requests.exceptions.RequestException:
        res['status_code'] = None
        res['is_ok'] = False
    response_list.append(res)


def give_urls(links_file_path, json_file_path):
    links = open(links_file_path, 'r')
    links_list = links.read().splitlines()
    threads = list()
    for link in links_list:
        threads.append(threading.Thread(target=check_urls, args=(link,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    with open(json_file_path, 'w+') as result_file:
        json.dump(response_list, result_file, indent=2)


if __name__ == '__main__':
    give_urls(r'C:\Users\Vladyslav_Maslii\Desktop\utils_links.txt', r'C:\Users\Vladyslav_Maslii\Desktop\utils_links.json')
