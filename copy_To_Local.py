from snakebite.client import Client

client = Client('localhost', 9000)

for f in client.copyToLocal(['/demo/input.txt','/demo/Test.txt._COPYING_'], '/home/administrator/Desktop/MapReduceStreaming/snakebiteDemo/'):
  print (f)
