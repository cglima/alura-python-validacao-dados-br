import re

# padrao = "[0-9][a-z]{2}[0-9]"
# texto = "123 1ac2 1cc aa1"
# resposta = re.search(padrao, texto)
# print(resposta.group())

# padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
# texto = "aaabbbccc rodrigo123@gmail.com.br ahuhsuhahdauhda ahusahuhasha"
# resposta = re.search(padrao, texto)
# print(resposta.group())

padrao_molde = "(xx)aaaa-wwww"
padrao = '[0-9]{2}[0-9]{4,5}[0-9]{4}'
texto = "eu gosto do numero 2126451234 e gosto também do 2136431234"
resposta = re.findall(padrao,texto)
resposta2 = re.search(padrao, texto)
print(resposta)
print(resposta2.group())