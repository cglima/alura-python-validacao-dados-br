import re

# padrao = "[0-9][a-z]{2}[0-9]"
# texto = "123 1ac2 1cc aa1"
# resposta = re.search(padrao, texto)
# print(resposta.group())

padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "aaabbbccc rodrigo123@gmail.com.br ahuhsuhahdauhda ahusahuhasha"
resposta = re.search(padrao, texto)
print(resposta.group())