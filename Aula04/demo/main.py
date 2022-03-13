from lib2to3.pgen2 import grammar
from lark import Lark, Token, Transformer
from lark.tree import pydot__tree_to_png
from lark.visitors import Interpreter 


# Não é uma boa solução, pois devemos sempre tentar fazer as coisas no nivel mais baixo
class TransformList(Transformer):
    def sumRange(self, list):
        sum = 0
        isActive = False
        for elem in list:
            if elem == "agora":
                isActive = True
            elif elem == "fim":
                isActive = False
            elif isActive and isinstance(elem, int):
                sum = sum + elem
        return sum

    def start(self, item):
        output = {}
        output["Comprimento"] = len(item[1])
        output["Mais Frequente"] = max(set(item[1]), key = item[1].count) # Not a good solution
        output["Soma intervalo"] = self.sumRange(item[1])
        return output

    def lista(self, lista):
        return lista

    def elems(self, elems):
        r = [x for x in elems if x != ',']
        return r

    def elem(self, elem):
        return elem[0]  # Obter apenas o numero e nao uma lista

    def NUM(self, num):
        return int(num)

    def WORD(self, word):
        return str(word)

    def VIR(self, vir):
        return str(vir)


class MyInterpreter(Interpreter):
    def __init__(self):
        self.comprimento = 0

        
    def start(self, tree):
        print(" - Start - ")
        r = self.visit(tree.children())
        print("Entramos nos elementos")


    def elems(self, tree):
        print(tree.pretty())
        r = 0
        for elem in tree.children():
            print("Elemento: ")
            if elem.data == "elem":
                r = self.visit(elem)
        return r

    def elem(self, tree):
        print(tree)
        r = self.visit_children()
        if (r[0].type == "NUM"):
            self.comprimento += 1
            return (int(r[0]))
        else:
            return 0



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

#data = TransformList().transform(tree)
data = MyInterpreter().visit(tree)
print(data)