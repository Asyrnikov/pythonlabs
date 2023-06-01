#ex 5.1

def check_ip_address(ip_address):
    octets = ip_address.split('.')

    # Проверяем введенный IP-адрес на правильность формата
    if len(octets) != 4:
        return 'Неправильный формат IP-адреса'

    # Проверяем каждый октет на диапазон значений
    try:
        first_octet = int(octets[0])
        if first_octet == 0:
            return 'unassigned'
        elif first_octet == 255 and all(octet == '255' for octet in octets[1:]):
            return 'local broadcast'
        elif 1 <= first_octet <= 127:
            return 'unicast'
        elif 128 <= first_octet <= 191:
            return 'unicast'
        elif 192 <= first_octet <= 223:
            return 'unicast'
        elif 224 <= first_octet <= 239:
            return 'multicast'
        else:
            return 'unused'
    except ValueError:
        return 'Неправильный формат IP-адреса'


# Запрос у пользователя ввода IP-адреса
ip_address = input('Введите IP-адрес в формате 10.0.1.1: ')

# Проверка класса IP-адреса и вывод результата
result = check_ip_address(ip_address)
print(result)

#ex 5.1a
def check_ip_address(ip_address):
    octets = ip_address.split('.')

    # Проверяем введенный IP-адрес на правильность формата
    if len(octets) != 4:
        return 'Incorrect IPv4 address'

    # Проверяем каждый октет на диапазон значений
    try:
        for octet in octets:
            value = int(octet)
            if value < 0 or value > 255:
                return 'Incorrect IPv4 address'
    except ValueError:
        return 'Incorrect IPv4 address'

    # Проверяем класс IP-адреса
    first_octet = int(octets[0])
    if first_octet == 0:
        return 'unassigned'
    elif first_octet == 255 and all(octet == '255' for octet in octets[1:]):
        return 'local broadcast'
    elif 1 <= first_octet <= 127:
        return 'unicast'
    elif 128 <= first_octet <= 191:
        return 'unicast'
    elif 192 <= first_octet <= 223:
        return 'unicast'
    elif 224 <= first_octet <= 239:
        return 'multicast'
    else:
        return 'unused'


# Запрос у пользователя ввода IP-адреса
ip_address = input('Введите IP-адрес в формате 10.0.1.1: ')

# Проверка корректности введенного IP-адреса
result = check_ip_address(ip_address)
print(result)

#ex 5.1b
def check_ip_address(ip_address):
    octets = ip_address.split('.')

    # Проверяем введенный IP-адрес на правильность формата
    if len(octets) != 4:
        return 'Incorrect IPv4 address'

    # Проверяем каждый октет на диапазон значений
    try:
        for octet in octets:
            value = int(octet)
            if value < 0 or value > 255:
                return 'Incorrect IPv4 address'
    except ValueError:
        return 'Incorrect IPv4 address'

    # Проверяем класс IP-адреса
    first_octet = int(octets[0])
    if first_octet == 0:
        return 'unassigned'
    elif first_octet == 255 and all(octet == '255' for octet in octets[1:]):
        return 'local broadcast'
    elif 1 <= first_octet <= 127:
        return 'unicast'
    elif 128 <= first_octet <= 191:
        return 'unicast'
    elif 192 <= first_octet <= 223:
        return 'unicast'
    elif 224 <= first_octet <= 239:
        return 'multicast'
    else:
        return 'unused'


# Запрос у пользователя ввода IP-адреса
while True:
    ip_address = input('Введите IP-адрес в формате 10.0.1.1: ')
    result = check_ip_address(ip_address)
    if result != 'Incorrect IPv4 address':
        break
    else:
        print('Некорректный IP-адрес. Пожалуйста, попробуйте еще раз.')

# Вывод результата
print(result)

#ex 5.2
mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []

for mac_address in mac:
    mac_cisco.append(mac_address.replace(':', '.'))

print(mac_cisco)

#ex 5.3
access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan']

fast_int = {
    'access': {
        '0/12': '10',
        '0/14': '11',
        '0/16': '17',
        '0/17': '150'
    },
    'trunk': {
        '0/1': ['add', '10', '20'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17']
    }
}

for intf, vlan in fast_int['trunk'].items():
    print('interface FastEthernet' + intf)
    for command in trunk_template:
        if command.endswith('allowed vlan'):
            action = vlan[0]
            vlans = ','.join(vlan[1:])
            if action == 'add':
                print(' {} add {}'.format(command, vlans))
            elif action == 'del':
                print(' {} remove {}'.format(command, vlans))
            elif action == 'only':
                print(' {} {}'.format(command, vlans))
        else:
            print(' {}'.format(command))
