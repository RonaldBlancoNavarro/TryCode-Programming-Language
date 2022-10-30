from TryCode import lexico

def run(fn, text):

    # Generate tokens
    lexer = lexico.Lexico(fn, text)
    tokens, error = lexer.make_tokens()

    #Generate Arbol Analizador Sintactico 
    
    #Interpretar y correr el programa

    return tokens, error

    #from TryCode import prueba
    #e = prueba.Prueba1()
    #e.comp("hola")
    #e.mostrarToken("TT_FLOAT")