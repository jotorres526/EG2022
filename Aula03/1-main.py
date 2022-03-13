from lib2to3.pgen2 import grammar
from lark import Lark, Transformer, Discard
from lark.tree import pydot__tree_to_png

class TransformList(Transformer):
    def __init__(self):
        self.active = False
        self.ocorrencias = dict()
        self.output = dict()
        self.soma = 0
        self.comprimento = 0

    def start(self, item):
        self.output['soma'] = self.soma
        self.output['comprimento'] = self.comprimento
        self.output['mais frequente'] = max(self.ocorrencias, key=self.ocorrencias.get)
        #self.output['mais frequente'] = list(self.ocorrencias)[0]
        print(item)
        return self.output

    def lista(self, lista):
        return lista

    def elems(self, elems):
        return elems

    def elem(self, elem):
        x = elem[0] 
        self.comprimento += 1
        self.ocorrencias[x] = self.ocorrencias.setdefault(x, 0) + 1
        return x

    def NUM(self, num):
        if self.active:
            self.soma += int(num)
        return int(num)

    def WORD(self, word):
        if str(word) == "agora":
            self.active = True
        elif str(word) == "fim":
            self.active = False
        return str(word)

    # A virgula é importante para o input ser legível mas não tem significado
    # Podemos dar discard
    def VIR(self, vir):
        return Discard
        #pass # O pass retorna um valor None mas não é o que se quer


# A gramática deve ser uma especificação formal
grammar = r'''
start : lista elems "."
lista : "Lista" | "LISTA"
elems : elem (VIR elem)* 
elem : NUM | WORD 
NUM : "0".."9"
WORD : ("a".."z" | "A".."Z")+
VIR : ","
%import common.WS
%ignore WS
'''

l = Lark(grammar)
tree = l.parse(input("> "))

data = TransformList().transform(tree)
print(data)