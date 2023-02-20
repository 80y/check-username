import requests
import random
import time

with open('username.txt', 'r') as f:
    usernames = f.read().splitlines()

with open('proxy.txt', 'r') as f:
    proxies = [line.strip() for line in f]

while usernames:
    username = usernames.pop(0)
    proxy = random.choice(proxies)
    try:
        response = requests.get(f'https://github.com/{username}', proxies={'http': proxy}, timeout=5)
        if response.status_code == 404:
            print(f'\033[1;32m{username}\033[0m')
            with open('r.txt', 'a') as f:
                f.write(username + '\n')
        else:
            print(f'\033[1;31m{username}\033[0m')
        time.sleep(3)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e} with proxy {proxy}")
