from snakebite.client import Client

client = Client('localhost', 9000)

for p in client.mkdir(['/second/test', '/input1','/demo2'], create_parent=True):
   print (p)
