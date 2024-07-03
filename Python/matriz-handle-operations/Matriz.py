class Matriz:
    # Representa uma matriz de números com operações de álgebra linear.

    def __init__(self, linhas, colunas):
        # Inicializa uma matriz de dimensões especificadas com todos os elementos zerados.

        self.data = []  # Inicia uma lista vazia

        for _ in range(linhas):
            self.data.append([0] * colunas)  # Adiciona uma nova linha de zeros

        self.linhas = linhas
        self.colunas = colunas

    def __getitem__(self, posicao):
        # Permite o acesso a elementos via índices, matriz[i, j].

        i, j = posicao
        return self.data[i][j]

    def __setitem__(self, posicao, valor):
        # Permite a definição de valores via índices, matriz[i, j] = valor.

        i, j = posicao
        self.data[i][j] = valor

    def setar_valores(self, valores):
        # Define toda a matriz a partir de uma lista de listas de valores.
        # Setar valores em matriz

        for i in range(self.linhas):
            for j in range(self.colunas):
                self.data[i][j] = valores[i][j]

    def _checa_dimensoes_para_operacao(self, outra, operacao):
        # Validação para checar dimensões das duas matrizes em operação de soma e produto
        # E garante que 'outra' é uma instância de Matriz.

        if not isinstance(outra, Matriz):
            raise TypeError("O operando deve ser uma instância de Matriz.")

        if operacao == "soma":
            if self.linhas != outra.linhas or self.colunas != outra.colunas:
                raise ValueError("Dimensões incompatíveis para soma.")
            return True
        elif operacao == "produto":
            if self.colunas != outra.linhas:
                raise ValueError("Dimensões incompatíveis para multiplicação.")
            return True
        else:
            raise ValueError("Operação desconhecida.")

    def __add__(self, outra):
        # Implementa soma

        if not self._checa_dimensoes_para_operacao(outra, "soma"):
            raise ValueError("Dimensões incompatíveis para soma.")

        resultado = Matriz(self.linhas, self.colunas)

        for i in range(self.linhas):
            for j in range(self.colunas):
                resultado[i, j] = self[i, j] + outra[i, j]
        return resultado

    def __mul__(self, outra):
        # Implementa a multiplicação de matrizes ou por escalar

        if isinstance(outra, Matriz):
            if not self._checa_dimensoes_para_operacao(outra, "produto"):
                raise ValueError("Dimensões incompatíveis para multiplicação.")

            resultado = Matriz(self.linhas, outra.colunas)

            for i in range(self.linhas):
                for j in range(outra.colunas):
                    resultado[i, j] = sum(self[i, k] * outra[k, j] for k in range(self.colunas))
            return resultado
        else:
            resultado = Matriz(self.linhas, self.colunas)

            for i in range(self.linhas):
                for j in range(self.colunas):
                    resultado[i, j] = self[i, j] * outra
            return resultado

    def __eq__(self, outra):
        # Verifica a igualdade entre duas matrizes.

        if self.linhas != outra.linhas or self.colunas != outra.colunas:
            return False

        for i in range(self.linhas):
            for j in range(self.colunas):
                if self[i, j] != outra[i, j]:
                    return False
        return True

    def __ne__(self, outra):
        # Verifica a desigualdade entre duas matrizes.

        return not self.__eq__(outra)

    @classmethod
    def identidade(cls, tamanho):
        # Gera uma matriz identidade de tamanho especificado.

        resultado = cls(tamanho, tamanho)

        for i in range(tamanho):
            resultado[i, i] = 1
        return resultado

    def __str__(self):
        # Retorna uma representação em string da matriz para impressão.

        return '\n'.join(' '.join(str(x) for x in row) for row in self.data)


def main():
    a = Matriz(3, 3)
    a[0, 2] = 1
    a[1, 1] = 1
    a[2, 0] = 1
    print('Matriz A:')
    print(a)

    b = Matriz(3, 3)
    b.setar_valores([[1.0, 2.0, 0.0], [2.0, 4.0, 5.0], [3.0, 3.0, 0.0]])

    print('Matriz B:')
    print(b)

    print('A + B:')
    print(a + b)

    print('A * B:')
    print(a * b)

    print('B * escalar:')
    print(b * 5)

    print(f'A != B: {a != b}')
    b.setar_valores([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    print(f'A == B: {a == b}')

    ident = Matriz.identidade(3)
    print("Matriz Identidade:")
    print(ident)


if __name__ == "__main__":
    main()
