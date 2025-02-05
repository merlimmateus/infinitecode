import re


# Code authored by Mateus Merlim Mattos
# Contact: merlimmateus@gmail.com


class PreProcessador:

    def __init__(self, texto):
        self.texto = texto
        self.lista_palavras = []

    def processa(self):
        self.lista_palavras = re.findall(r'\b\w+\b', self.texto.lower())

    def __str__(self):
        return f"Lista de palavras: {self.lista_palavras}"


class ContadorPalavras(PreProcessador):

    def __init__(self, texto):
        super().__init__(texto)
        self.ocorrencias = {}

    def processa(self):
        super().processa()

        for palavra in self.lista_palavras:
            if palavra in self.ocorrencias:
                self.ocorrencias[palavra] += 1
            else:
                self.ocorrencias[palavra] = 1

    def __str__(self):
        return "Frequencia das palavras:\n" + "\n".join(
            [f"{palavra}: {contagem} vezes" for palavra, contagem in self.ocorrencias.items()])


class Tradutor(PreProcessador):
    def __init__(self, texto):
        super().__init__(texto)

        self.traducoes = {
            "olá": "hello", "este": "this", "é": "is", "um": "a", "exemplo": "example",
            "de": "of", "texto": "text", "com": "with", "termos": "terms", "repetidos": "repeated",
            "possui": "has", "vários": "various"
        }

        self.lista_palavras_trad = []

    def processa(self):
        super().processa()
        self.lista_palavras_trad = [self.traducoes.get(palavra, palavra) for palavra in self.lista_palavras]

    def __str__(self):
        return "Tradução robótica:\n" + " ".join(self.lista_palavras_trad)


class ProcessadorTexto:
    def __init__(self, texto):
        self.texto = texto

    def processa(self):
        contador = ContadorPalavras(self.texto)
        contador.processa()
        tradutor = Tradutor(self.texto)
        tradutor.processa()

        print(contador)
        print()
        print(tradutor)


if __name__ == '__main__':
    # Descomente a seguir para testar apenas a classe PreProcessador
    # preprocessador = PreProcessador('OLá! Este é um exemplo de texto com termos repetidos.'
    #                                 ' Este texto possui vários termos repetidos:'
    #                                 ' este, Este, ESte, esTE!')
    # preprocessador.processa()
    # print(preprocessador)

    # Descomente a seguir para testar apenas a classe ContadorPalavras
    # contador = ContadorPalavras('OLá! Este é um exemplo de texto com termos repetidos.'
    #                             ' Este texto possui vários termos repetidos:'
    #                             ' este, Este, ESte, esTE!')
    # contador.processa()
    # print(contador)

    # Descomente a seguir para testar apenas a classe Tradutor
    # tradutor = Tradutor('OLá! Este é um exemplo de texto com termos repetidos.'
    #                     ' Este texto possui vários termos repetidos:'
    #                     ' este, Este, ESte, esTE!')
    # tradutor.processa()
    # print(tradutor)

    processadortexto = ProcessadorTexto(
        'OLá! Este é um exemplo de texto com termos repetidos. Este texto possui vários termos repetidos: este, Este, ESte, esTE!')
    processadortexto.processa()
