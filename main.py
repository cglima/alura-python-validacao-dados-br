from documento import Documento

# cpf = "15316264754"
#
# objeto_cpf = CpfCnpj(cpf)
# print(objeto_cpf)

exemplo_cnpj = "08027715000140"
exemplo_cpf = "15316264754"
documento = Documento.cria_documento(exemplo_cpf)
print(documento)