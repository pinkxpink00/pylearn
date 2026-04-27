#Напиши функцию parse_ips(text) которая принимает строку с текстом, находит все IP адреса и возвращает их списком.
#Пример входа: "hosts: 192.168.1.1 and 10.0.0.1 are active". Это реальная задача из пентеста — парсинг вывода инструментов.
import re

def parse_ips(text):
    ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', text)
    return ips

print(parse_ips("hosts: 192.168.1.1 and 10.0.0.1 are active"))