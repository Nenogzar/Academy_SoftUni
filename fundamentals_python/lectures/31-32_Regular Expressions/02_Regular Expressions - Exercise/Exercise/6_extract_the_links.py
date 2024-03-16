import re

info = input()
site_list = []

while info:
    pattern = r'(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)'
    match = re.search(pattern, info)

    if match:
        searching_sites = match.group(1)
        site_list.append(searching_sites)

    info = input()

for site in site_list:
    print("".join(site))