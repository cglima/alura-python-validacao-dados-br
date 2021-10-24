import requests

from acesso_cep import BuscaEndereco

cep = "01001000"
objeto_cep = BuscaEndereco(cep)
# print(objeto_cep)

# r = requests.get("http://viacep.com.br/ws/01001000/json/")
# print(type(r.text))

# a = objeto_cep.acessa_via_cep()
# print(type(a.text))
# print(a.text)
# print(type(a.json()))
# print(a.json())
# print(a.json()['bairro'])

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)