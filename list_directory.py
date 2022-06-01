from snakebite.client import Client

client = Client('localhost', 9000)
for x in client.ls(['/']):
    print (x)


'''
The Client() method accepts the following parameters:

host (string)
Hostname or IP address of the NameNode

port (int)
RPC port of the NameNode

hadoop_version (int)
The Hadoop protocol version to be used (default: 9)

use_trash (boolean)
Use trash when removing files

effective_use (string)
Effective user for the HDFS operations (default: None or cur‐
rent user)
'''
