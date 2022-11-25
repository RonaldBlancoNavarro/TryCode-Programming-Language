from tkinter import END
from sly import Lexer
_='_'
class TryCodeLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, FLOAT,NULL, IF, THEN, ELSE, FOR, WHILE, FUN,PRINT, TO, ARROW, EQEQ , NOEQ, LTEQ, GTEQ, LT, GT, TRUE , FALSE , AND, OR, NOT }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', '{', '}', ',', ';' }

    # Deficion de tokens
    IF = r'IF'
    THEN = r'THEN'
    ELSE = r'ELSE'
    FOR = r'FOR'
    WHILE = r'WHILE'
    FUN = r'FUN'
    PRINT= r'PRINT'
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

    @_(r"[0-9]+\.[0-9]+")# flotante
    def FLOAT(self, t):
        t.value = float(t.value)
        return t
    
    @_(r'\d+')#entero
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')#comentario
    def COMMENT(self, t):
        pass

    @_(r'\n+')#salto de linea
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1
