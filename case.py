'''
exc_type: O tipo de exceção que ocorreu, se houver.
        Se não ocorreu nenhuma exceção, este parâmetro será None.

exc_val: O valor de exceção que ocorreu, se houver.
    Se não ocorreu nenhuma excelção, este parâmetro será None.

exc_tb: O traceback (rastreamento de pilha) associado à exceção que ocorreu, se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None.
'''

class AlgumaCoisa():
    def __enter__(self):
        print("Estou entrando")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Estou saindo")

with AlgumaCoisa() as something:
    print("Estou no meio")