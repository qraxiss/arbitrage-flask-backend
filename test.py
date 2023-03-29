from api import interface

for token in interface.get_token():
    interface.open(token['address'])

    