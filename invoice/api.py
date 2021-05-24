import veryfi
import pprint

import os


file = open('../api_keys.txt', 'r+')


client_id= file.readline()[:-1]
client_secret = file.readline()[:-1]
username = file.readline()[:-1]
api_key = file.readline()[:-1]
file.close()


def InvoiceAPI(url):
    
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    url  = os.path.join(BASE_DIR,'media/')+str(url)

    client = veryfi.Client(client_id, client_secret, username, api_key)
    res = client.process_document(url)

    return res
