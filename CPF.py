from validate_docbr import CPF

class ValidaCPF:

    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!!")

    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def formata_cpf(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)

    def __str__(self):
        return self.formata_cpf()