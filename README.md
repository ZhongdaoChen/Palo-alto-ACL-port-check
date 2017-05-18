# Palo-alto-ACL-port-check

The port_to_check.py will extract all ports and IP pairs that need to be checked. If you want to add or delete ports/services that you want or don’t want to check, just add string in the python file. It’s easy to understand. 

The port_check.sh will try to connect to each port using natcat. If there is no response in 2 seconds, then move to check the next pair. However, if connection is established, the script will stop itself…. So there will be some manual work to do. 
