from sly import Lexer

class TryCodeLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, FLOAT,NULL, IF, THEN, ELSE, FOR, FUN, WHILE, TO, ARROW, EQEQ , NOEQ, LTEQ, GTEQ, LT, GT, TRUE , FALSE , AND, OR, NOT }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', '{', '}', ',', ';' }

    # Define tokens
    IF = r'IF'
    THEN = r'THEN'
    ELSE = r'ELSE'
    FOR = r'FOR'
    WHILE=r'WHILE'
    FUN = r'FUN'
    TO = r'TO'
    TRUE = r'TRUE'
    FALSE = r'FALSE'
    NULL= r'NULL'
    AND = r'AND'
    OR = r'OR'
    NOT = r'NOT'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    
    EQEQ = r'=='
    NOEQ = r'!='
    LTEQ = r'<='
    GTEQ = r'>='
    LT = r'<'
    GT = r'>'

    @_(r"[0-9]+\.[0-9]+")
    def FLOAT(self, t):
        t.value = float(t.value)
        return t
    
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1



    # @_(r'\n+')
    # def newline(self,t ):
    #     self.lineno = t.value.count('\n') 
    #     print(self.lineno)



    # Line number tracking
# if __name__ == '__main__':
#     data = '''
#         # Counting
#         x = 0;
#         2+2;
#         x;
#         '''

#     listaExpresion = []  # Tokens dentro de una expresion
#     listaExpresiones=[]  # Lista de expresiones
#     lexer = TryCodeLexer()
#     for tok in lexer.tokenize(data):
#         if tok.type != ';':
#             listaExpresion.append(tok)
#         else:
#             # listaExpresion.append(tok)
#             listaExpresiones.append(listaExpresion)
#             print(listaExpresion)
#             listaExpresion = []
#             print("<----------------------->")
#         # print(tok)
#     print("<-------Lista expresiones---------------->")
#     print(listaExpresiones)