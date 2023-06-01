#ex 7.1
def generate_access_config(access):
    access_template = [
        'switchport mode access',
        'switchport access vlan',
        'switchport nonegotiate',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    config = []
    for port, vlan in access.items():
        config.append('interface ' + port)
        for command in access_template:
            if command.endswith('access vlan'):
                config.append(' {} {}'.format(command, vlan))
            else:
                config.append(' {}'.format(command))

    return config

access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

result = generate_access_config(access_dict)
for line in result:
    print(line)

#ex 7.1a
def generate_access_config(access, psecurity=False):
    access_template = [
        'switchport mode access',
        'switchport access vlan',
        'switchport nonegotiate',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]
    port_security = [
        'switchport port-security maximum 2',
        'switchport port-security violation restrict',
        'switchport port-security'
    ]

    config = []
    for port, vlan in access.items():
        config.append('interface ' + port)
        for command in access_template:
            if command.endswith('access vlan'):
                config.append(' {} {}'.format(command, vlan))
            else:
                config.append(' {}'.format(command))

        if psecurity:
            config.extend(port_security)

    return config

access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

result_with_psecurity = generate_access_config(access_dict, psecurity=True)
for line in result_with_psecurity:
    print(line)

print('----------------')

result_without_psecurity = generate_access_config(access_dict)
for line in result_without_psecurity:
    print(line)

#ex 7.1b
def generate_access_config(access, psecurity=False):
    access_template = [
        'switchport mode access',
        'switchport access vlan',
        'switchport nonegotiate',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]
    port_security = [
        'switchport port-security maximum 2',
        'switchport port-security violation restrict',
        'switchport port-security'
    ]

    config = {}
    for port, vlan in access.items():
        config[port] = []
        config[port].append('interface ' + port)
        for command in access_template:
            if command.endswith('access vlan'):
                config[port].append(' {} {}'.format(command, vlan))
            else:
                config[port].append(' {}'.format(command))

        if psecurity:
            config[port].extend(port_security)

    return config

access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

result_with_psecurity = generate_access_config(access_dict, psecurity=True)
for port, commands in result_with_psecurity.items():
    print('Interface', port)
    for command in commands:
        print(command)
    print('----------------')

print()

result_without_psecurity = generate_access_config(access_dict)
for port, commands in result_without_psecurity.items():
    print('Interface', port)
    for command in commands:
        print(command)
    print('----------------')

#ex 7.2
def generate_trunk_config(trunk):
    trunk_template = [
        'switchport trunk encapsulation dot1q',
        'switchport mode trunk',
        'switchport trunk native vlan 999',
        'switchport trunk allowed vlan'
    ]

    config = []
    for port, vlans in trunk.items():
        config.append('interface ' + port)
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                config.append(' {} {}'.format(command, ','.join(str(v) for v in vlans)))
            else:
                config.append(' {}'.format(command))

    return config

trunk_dict = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

trunk_config = generate_trunk_config(trunk_dict)
for command in trunk_config:
    print(command)

#ex 7.2a
def generate_trunk_config(trunk):
    trunk_template = [
        'switchport trunk encapsulation dot1q',
        'switchport mode trunk',
        'switchport trunk native vlan 999',
        'switchport trunk allowed vlan'
    ]

    config = {}
    for port, vlans in trunk.items():
        port_config = []
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                port_config.append(' {} {}'.format(command, ','.join(str(v) for v in vlans)))
            else:
                port_config.append(' {}'.format(command))
        config[port] = port_config

    return config

trunk_dict = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

trunk_config = generate_trunk_config(trunk_dict)
for port, commands in trunk_config.items():
    print('Interface', port)
    for command in commands:
        print(command)
    print()

#ex 7.3
import re

def get_int_vlan_map(config_file):
    access_ports = {}
    trunk_ports = {}

    with open(config_file, 'r') as file:
        lines = file.readlines()

        interface_pattern = r'^interface (\S+)$'
        access_pattern = r'switchport mode access\n\s+switchport access vlan (\d+)'
        trunk_pattern = r'switchport mode trunk\n\s+switchport trunk allowed vlan (.+)'

        interface = None
        for line in lines:
            line = line.strip()

            interface_match = re.match(interface_pattern, line)
            if interface_match:
                interface = interface_match.group(1)
                continue

            if interface and re.search(access_pattern, line):
                access_vlan = re.search(access_pattern, line).group(1)
                access_ports[interface] = int(access_vlan)
                interface = None
                continue

            if interface and re.search(trunk_pattern, line):
                trunk_vlans = re.search(trunk_pattern, line).group(1).split(',')
                trunk_ports[interface] = [int(vlan) for vlan in trunk_vlans]
                interface = None
                continue

    return access_ports, trunk_ports

config_file = 'config_sw1.txt'
access_ports, trunk_ports = get_int_vlan_map(config_file)

print('Access Ports:')
print(access_ports)
print()
print('Trunk Ports:')
print(trunk_ports)

#ex 7.2a
import re

def get_int_vlan_map(config_file):
    access_ports = {}
    trunk_ports = {}

    with open(config_file, 'r') as file:
        lines = file.readlines()

        interface_pattern = r'^interface (\S+)$'
        access_pattern = r'switchport mode access\n\s+switchport access vlan (\d+)'
        access_vlan_1_pattern = r'switchport mode access'
        trunk_pattern = r'switchport mode trunk\n\s+switchport trunk allowed vlan (.+)'

        interface = None
        for line in lines:
            line = line.strip()

            interface_match = re.match(interface_pattern, line)
            if interface_match:
                interface = interface_match.group(1)
                continue

            if interface and re.search(access_pattern, line):
                access_vlan = re.search(access_pattern, line).group(1)
                access_ports[interface] = int(access_vlan)
                interface = None
                continue

            if interface and re.search(access_vlan_1_pattern, line):
                access_ports[interface] = 1
                interface = None
                continue

            if interface and re.search(trunk_pattern, line):
                trunk_vlans = re.search(trunk_pattern, line).group(1).split(',')
                trunk_ports[interface] = [int(vlan) for vlan in trunk_vlans]
                interface = None
                continue

    return access_ports, trunk_ports

config_file = 'config_sw2.txt'
access_ports, trunk_ports = get_int_vlan_map(config_file)

print('Access Ports:')
print(access_ports)
print()
print('Trunk Ports:')
print(trunk_ports)

#ex 7.4
def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    """
    for word in ignore:
        if word in command:
            return True
    return False

def config_to_dict(config):
    """
    config - имя конфигурационного файла коммутатора
    Возвращает словарь:
    - Все команды верхнего уровня (глобального режима конфигурации) будут ключами.
    - Если у команды верхнего уровня есть подкоманды,
    они должны быть в значении у соответствующего ключа, в виде списка (пробелы вначале можно оставлять).
    - Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
    """
    config_dict = {}
    ignore = ['duplex', 'alias', 'Current configuration']

    with open(config, 'r') as file:
        lines = file.readlines()

        command = ''
        for line in lines:
            line = line.strip()

            if ignore_command(line, ignore) or line.startswith('!'):
                continue

            if line.startswith(' '):
                config_dict[command].append(line)
            else:
                command = line
                config_dict[command] = []

    return config_dict

config_file = 'config_sw1.txt'
config_dict = config_to_dict(config_file)

for command, subcommands in config_dict.items():
    print(command)
    for subcommand in subcommands:
        print(f'  {subcommand}')

#ex 7.4a
def check_ignore(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    """
    for word in ignore:
        if word in command:
            return True
    return False

def config_to_dict(config):
    """
    config - имя конфигурационного файла
    """
    config_dict = {}
    ignore = ['duplex', 'alias', 'Current configuration']

    with open(config, 'r') as file:
        lines = file.readlines()

        command_stack = []
        for line in lines:
            line = line.strip()

            if check_ignore(line, ignore) or line.startswith('!'):
                continue

            indentation = len(line) - len(line.lstrip())
            command = line.strip()

            if indentation == 0:
                command_stack = [command]
                config_dict[command] = []
            elif indentation == 1:
                config_dict[command_stack[0]].append(command)
            else:
                nested_dict = config_dict
                for level in range(indentation - 1):
                    nested_dict = nested_dict[command_stack[level]]
                nested_dict[command] = {}

            command_stack = command_stack[:indentation] + [command]

    return config_dict

config_file = 'config_sw1.txt'
config_dict = config_to_dict(config_file)

def print_config(config_dict, indent=0):
    for key, value in config_dict.items():
        if isinstance(value, list):
            for command in value:
                print(' ' * indent + command)
        elif isinstance(value, dict):
            print(' ' * indent + key)
            print_config(value, indent + 2)

print_config(config_dict)
