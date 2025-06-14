# В исходном текстовом файле(radio_stations.txt) найти все домены из URL-адресов

import re

def find_domains(filename):
    with open(filename) as f:
        content = f.read()
        urls = re.findall(r'http://([\w.-]+)(?::\d+)?', content)
        domains = set(url.split('/')[0] for url in urls)
        return sorted(domains)

domains = find_domains('radio_stations.txt')
print("Найденные домены:")
for domain in domains:
    print(domain)