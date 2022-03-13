from lib2to3.pgen2 import grammar
from lark import Lark, Token,Transformer, Discard
from lark.tree import pydot__tree_to_png


class TransformList(Transformer):
    def __init__(self):
        self.num_alunos = 0
        self.avg = 0
        self.sum = 0
        self.length = 0
        self.aluno_atual = ''
        self.medias = dict()
        self.notas_alunos  = dict()
        self.output = dict()

    def start(self, item):
        self.output['num_alunos'] = self.num_alunos
        self.output['medias'] = self.medias
        self.output['notas alunos'] = self.notas_alunos
        return self.output

    def turma(self, turma):
        return turma

    def aluno(self, aluno):
        self.num_alunos += 1
        self.medias[str(aluno[0])] = self.avg
        # Reset Counters
        self.sum = 0
        self.length = 0
        self.aluno_atual = ''
        return aluno

    def notas(self, notas):
        self.avg = self.sum / self.length
        return notas

    def NOTA(self, nota):
        self.sum += int(nota)
        self.length += 1
        self.notas_alunos.setdefault(int(nota), set()).add(self.aluno_atual)
        return int(nota)

    def NOME(self, nome):
        self.aluno_atual = str(nome)
        return str(nome)
    def COL(self, col):
        return Discard

    def LP(self, lp):
        return Discard

    def RP(self, rp):
        return Discard


grammar = r'''
start : turma WORD NEWLINE alunos DOT
turma : "TURMA"
alunos : aluno (SC aluno)*
aluno : NOME LP notas RP
notas : NOTA (COL NOTA)*
NOME : WORD
NOTA : ("1".."2")? "0".."9"
DOT : "."
LP : "("
RP: ")"
SC: ";"
COL: ","
%import common.WS
%import common.NEWLINE
%import common.WORD
%ignore WS
'''

l = Lark(grammar)
frase = '''TURMA A
ana (12, 13, 15, 12, 13, 15, 14);
joao (9,7,3,6,9);
xico (12,16).'''
tree = l.parse(frase)

data = TransformList().transform(tree)
print(data)
