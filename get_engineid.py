#!/usr/bin/python3
import csv
import os

credentials_file = open(r'credentials.txt')
credentials = list(csv.reader(credentials_file))
devices_file = open(r'devices.txt')
devices = list(csv.reader(devices_file))

output_file = f'output.txt'
with open(output_file, 'w+') as outfile:
    for i in range(1, len(devices)):
        for j in range(1, len(credentials)):
            command = 'snmpwalk -v3 -l ' + credentials[j][1] + ' -u ' + credentials[j][0] + ' -a ' + credentials[j][2] + ' -A ' + credentials[j][3] + ' -x ' + credentials[j][4] + ' -X ' + credentials[j][5] + ' ' + devices[i][0] + ' .1.3.6.1.6.3.10.2.1.1'
            print(command)
            command_result = os.popen(command)
            response = command_result.read()
            print(response)
            try:
                value = response.split(':')[3].replace(' ', '').replace('\n', '')
                if value.startswith('8000'):
                    outfile.write('createUser -e ' + value + ' ' + credentials[j][0] + ' ' +
                                  credentials[j][2] + ' ' + credentials[j][3] + ' ' +
                                  credentials[j][4] + ' ' + credentials[j][5] + '\n')
                else:
                    continue
            except IndexError:
                continue
