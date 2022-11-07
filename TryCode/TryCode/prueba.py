TT_INT = "INT"

def hola():
    print("hola")

class Prueba1:
    def __init__(self):
        self.p = None
        self.tokens={ "TT_INT"	: 'INT', "TT_FLOAT"    : 'FLOAT', "TT_PLUS"     : 'PLUS', "TT_MINUS"    : 'MINUS', "TT_MUL"      : 'MUL', "TT_DIV"      : 'DIV', "TT_LPAREN"   : 'LPAREN', "TT_RPAREN"   : 'RPAREN'}    
    
    def comp(self, hola):
        self.p = hola
        print(self.p)
    
    def mostrarToken(self, tk):
        print(self.tokens[tk])
