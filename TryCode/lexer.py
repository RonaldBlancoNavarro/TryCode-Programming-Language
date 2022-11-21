from sly import Lexer

class TryCodeLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, FLOAT, IF, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ , TRUE , FALSE }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Define tokens
    IF = r'IF'
    THEN = r'THEN'
    ELSE = r'ELSE'
    FOR = r'FOR'
    FUN = r'FUN'
    TO = r'TO'
    TRUE = r'TRUE'
    FALSE = r'FALSE'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    

    EQEQ = r'=='


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
    def newline(self,t ):
        self.lineno = t.value.count('\n')

