#ex 3.1
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"

# Заменить "FastEthernet" на "GigabitEthernet"
NAT = NAT.replace("FastEthernet", "GigabitEthernet")

# Вывести результат на стандартный поток вывода
print(NAT)

#ex 3.2
MAC = 'AAAA:BBBB:CCCC'

# Заменить ":" на "."
MAC = MAC.replace(":", ".")

# Вывести результат на стандартный поток вывода
print(MAC)

#ex 3.3
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'

# Получить строку со списком VLANов
vlans = CONFIG.split()[-1]

# Разбить строку на отдельные VLANы
vlan_list = vlans.split(',')

# Вывести результат на стандартный поток вывода
print(vlan_list)

#ex 3.4
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

# Получить список VLANов из command1
vlans1 = set(command1.split()[-1].split(','))

# Получить список VLANов из command2
vlans2 = set(command2.split()[-1].split(','))

# Получить пересечение списков VLANов
common_vlans = list(vlans1 & vlans2)

# Преобразовать элементы списка в целые числа
common_vlans = [int(vlan) for vlan in common_vlans]

# Вывести результат на стандартный поток вывода
print(common_vlans)

#ex 3.5
ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

# Разбить строку на отдельные поля
fields = ospf_route.split()

# Получить префикс и протокол
prefix = fields[1]
protocol = "OSPF"

# Получить AD/Metric
ad_metric = fields[2][1:-1]

# Получить Next-Hop
next_hop = fields[4][:-1]

# Получить Last update
last_update = fields[5][:-1]

# Получить интерфейс
interface = fields[6]

# Вывести результат на стандартный поток вывода
print("Protocol: {}".format(protocol))
print("Prefix: {}".format(prefix))
print("AD/Metric: {}".format(ad_metric))
print("Next-Hop: {}".format(next_hop))
print("Last update: {}".format(last_update))
print("Outbound Interface: {}".format(interface))

#ex 3.7
MAC = 'AAAA:BBBB:CCCC'

# Удалить ":" из MAC-адреса
mac_no_colon = MAC.replace(":", "")

# Преобразовать MAC-адрес в двоичную строку
binary_mac = bin(int(mac_no_colon, 16))[2:]

# Вывести результат на стандартный поток вывода
print(binary_mac)

#ex 3.8
IP = '192.168.3.1'

# Разбить IP-адрес на отдельные байты
ip_bytes = IP.split(".")

# Преобразовать каждый байт в двоичную строку
binary_bytes = [bin(int(byte))[2:].zfill(8) for byte in ip_bytes]

# Вывести десятичные значения байтов
print("{:<10} {:<10} {:<10} {:<10}".format(ip_bytes[0], ip_bytes[1], ip_bytes[2], ip_bytes[3]))

# Вывести двоичные значения байтов
print("{:<10} {:<10} {:<10} {:<10}".format(binary_bytes[0], binary_bytes[1], binary_bytes[2], binary_bytes[3]))

#ex 3.9
def last_index(lst, element):
    return len(lst) - 1 - lst[::-1].index(element)

# Пример использования функции
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

# Найти индекс последнего вхождения числа 10 в num_list
num_index = last_index(num_list, 10)
print("Index of last occurrence of 10 in num_list: {}".format(num_index))

# Найти индекс последнего вхождения слова 'ruby' в word_list
word_index = last_index(word_list, 'ruby')
print("Index of last occurrence of 'ruby' in word_list: {}".format(word_index))