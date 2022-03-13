from lark import Lark, Transformer
from lark.visitors import Interpreter

class MyInterpreter(Interpreter):
    def __init__(self):
        self.num_ifs = 0
        self.output = {}

    def start(self, tree):
        print(" - Start - ")
        r = self.visit(tree.children[0])
        self.output = self.num_ifs
        return self.output

    def operacoes(self, tree):
        r = self.visit(tree.children[1])
        pass 

    def decls(self, tree):
        pass
    
    def atrib(self, tree):
        r = self.visit(tree.children[1])
        pass
    
    def tipo_atrib(self, tree):
        print(tree.pretty())
        for elem in tree.children:
            if elem.data == 'cond' or elem.data == 'elses':
                r = self.visit(elem)
        pass
    
    def comment(self, tree):
        pass
    
    def ciclo(self, tree):
        pass
    
    def cond(self, tree):
        self.num_ifs += 1
        r = self.visit(tree.children[1])
        pass
    
    def elses(self, tree):
        r = self.visit(tree.children[0])
        pass
    
    def logica(self, tree):
        pass
    
    def op_logica(self, tree):
        pass
    
    def atr(self, tree):
        pass
    
    def cauda_atr(self, tree):
        pass
    
    def expressao(self, tree):
        pass
    
    def cauda_expr(self, tree):
        pass
    
    def termo(self, tree):
        pass
    
    def cauda_termo(self, tree):
        pass
    
    def factor(self, tree):
        pass
    
    def chamada(self, tree):
        pass
    
    def argumentos(self, tree):
        pass
    
    def funcao(self, tree):
        pass
    
    def id(self, tree):
        pass
    
    def valor(self, tree):
        pass
    
    def cauda_array(self, tree):
        pass
    


f = open('gramatica.txt')
grammar = "".join(f.readlines())
f.close()

f = open('programa.wee')
code = "".join(f.readlines())
f.close()

l = Lark(grammar)
tree = l.parse(code)

data = MyInterpreter().visit(tree)
print(data)