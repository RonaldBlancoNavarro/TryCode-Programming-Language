from TryCode import lexico
from TryCode import analizador
from TryCode import interprete


def run(fn, text):
    # Generate tokens
    lexer = lexico.Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error

    # Generate AST
    parser = analizador.Parser(tokens)
    ast = parser.parse()
    if ast.error:
        return None, ast.error

    # Run program
    interpreter = interprete.Interpreter()
    context = interprete.Context("<program>")
    result = interpreter.visit(ast.node, context)

    return result.value, result.error


# from TryCode import prueba ---> NO FUNCIONA

# IMPORTACION FUNCIONAL
# import prueba


# def funtionprueba():
#     e = prueba.Prueba1()
#     e.comp("hola")
#     e.mostrarToken("TT_FLOAT")
#     prueba.hola()
#     print(prueba.TT_INT)


# funtionprueba()
