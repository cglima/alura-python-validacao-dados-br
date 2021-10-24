from documento import CpfCnpj

# cpf = "15316264754"
#
# objeto_cpf = CpfCnpj(cpf)
# print(objeto_cpf)

exemplo_cnpj = "08027715000140"
exemplo_cpf = "15316264754"
documento = CpfCnpj(exemplo_cpf, 'cpf')
print(documento)