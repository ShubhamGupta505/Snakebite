from snakebite.client import Client

client = Client('localhost', 9000)

for p in client.delete(['/data_demo/output/8_09_4/'], recurse=True):
   print (p)
