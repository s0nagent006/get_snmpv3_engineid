Step 1: Ensure that prerequisite software packages have been installed in your system:
- net-snmp including snmpwalk
- python3

Step 2: Copy all 3 files into a working directory of a machine where you have reachablity to all the network devices needed to sweep. 
Ideally this should be a jumphost that has been granted access via firewall for all the network devices via ICMP and SNMP (UDP/161).

Step 3: Edit the credentials.txt file to include all possible combination of SNMPv3 credentials used in the network, including Priv and Auth security level and passphrases.

Step 4: Edit the devices.txt file to include the IP addresses and ranges to sweep, in order to sweep only required IP subnets.

Step 5: Execute the get_engineid.py script using python. An output.txt file including all captured SNMPv3 engineIDs will be generated at the end in the same working directory.
