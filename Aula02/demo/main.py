from lib2to3.pgen2 import grammar
from tokenize import String
from lark import Lark,Token
from lark.tree import pydot__tree_to_png
from lark import Transformer


# Esta class encapsula a gramatica o que permite definir os nossos próprios outputs 
# Mucho poderoso :)
class TransformList(Transformer):
    def start(self, item):
        output = {} # podemos criar um dic para o output
        len = len(item[1])
        sum = sum(item[1])
        output["soma"] = sum
        output["length"] = len
        return output

    def elemento(self, elemento):
        r = [x for x in elemento if x != ","]
        return r

    def NUM(self, num):
        return int(num)

    def PE(self, pe):
        return str(pe)

    def PD(self, pd):
        return str(pd)
    
    def VIR(self, vir):
        return str(vir)

grammar = r'''
start : PE elemento PD
elemento : NUM (VIR NUM)*
NUM : ("0".."9")+
PE : "["
PD : "]"
VIR : ","
%import common.WS
%ignore WS
'''

# Obter parser e construir árvore de parsing
l = Lark(grammar)
frase = "[1,2,3]"
tree = l.parse(frase)

#print(tree)
#print(tree.pretty())

# Pode-se percorrer a arvore com um ciclo
#for element in tree.children:
#    print(element)

# Itera sobre a tree e filtra os elementos
tokens = tree.scan_values(lambda x: isinstance(x, Token))
#print(tokens)
#for token in tokens:
#    print(token)

#pydot__tree_to_png(tree, "aula2.png")

# Transformer, temos de criar uma class do tipo Transformer, e definir
# métodos para cada produção
data = TransformList().transform(tree)
print(data)
