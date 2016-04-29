import requests

r = requests.post('http://127.0.0.1:8000/financial/transactions/', data={"date":"2016-4-28",'description':'teste', 'acc_from':2, 'acc_to':3,'value':'3.5'} ,auth=('gabrielzago','engenharia'))
print r.content
