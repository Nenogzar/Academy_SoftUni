import re

# Пътят към файла, който трябва да се обработи
file_path = r'C:\Windows\System32\drivers\etc\services'

# Прочитане на данните от файла
with open(file_path, 'r') as file:
    data = file.read()

# Дефиниране на регулярния израз
pattern = re.compile(r'(?P<service>\S+)\s+(?P<port>\d+)/(?P<protocol>\S+)\s+(?P<aliases>.*?)(?:\s+#(?P<comment>.*))?\n')

# Извличане на данните с регулярния израз
matches = pattern.finditer(data)

# Създаване на списък за съхранение на данните
services = []


# Парсиране на данните и добавяне към списъка
for match in matches:
    service = match.group('service')
    port = match.group('port')
    protocol = match.group('protocol')
    aliases = match.group('aliases').strip().split()
    comment = match.group('comment')
    services.append({'service': service, 'port': port, 'protocol': protocol, 'aliases': aliases, 'comment': comment})

# Сортиране на данните по протокол и порт
sorted_services = sorted(services, key=lambda x: (x['protocol'], int(x['port'])))
sorted_by_aliases = sorted(services, key=lambda x: x['aliases'])

# Пътят за записване на файла със сортираните данни
output_file_path = r'sorted_services.txt'
output_file_path1 = r'sorted_services_by_aliases.txt'

# Записване на сортираните данни в текстов файл
with open(output_file_path, 'w') as output_file:
    for service in sorted_services:
        output_file.write(f"{service['protocol']} : {service['port']} - {service['service']}, aliases - {', '.join(service['aliases'])} - {service['comment']}\n")

with open(output_file_path1, 'w') as output_file:
    for service in sorted_by_aliases:
        output_file.write(f"aliases - {', '.join(service['aliases'])} - {service['comment']} - {service['protocol']} : {service['port']} - {service['service']}\n")