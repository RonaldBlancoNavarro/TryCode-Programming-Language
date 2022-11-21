from tkinter import END

class TryCodeExecute:
    def __init__(self, tree, env, txtOutput):
        self.txtOutput = txtOutput
        self.env = env
        result = self.walkTree(tree)
        if result is not None and isinstance(result, int):
            # print(result)
            txtOutput.insert(1.0,result)
        if result is not None and isinstance(result, float):
            # print(result)
            txtOutput.insert(1.0,result)
        if isinstance(result, str) and result[0] == '"':
            # print(result)
            txtOutput.insert(1.0,result)
        if result is not None and result=="TRUE" :
            # print(result)
            txtOutput.insert(1.0,result)
        if result is not None and result=="FALSE" :
            # print(result)
            txtOutput.insert(1.0,result)

    def walkTree(self, node):

        if isinstance(node, int):
            return node
        if isinstance(node, float):
            return node
        if isinstance(node, str):
            return node
        if isinstance(node, bool):
            return node

        if node is None:
            return None

        if node[0] == "program":
            if node[1] == None:
                self.walkTree(node[2])
            else:
                self.walkTree(node[1])
                self.walkTree(node[2])

        if node[0] == "num":
            return node[1]

        if node[0] == "float":
            return node[1]

        if node[0] == "str":
            return node[1]
        
        if node[0] == "bool":
            return node[2]

        if node[0] == "if_stmt":
            result = self.walkTree(node[1])
            if result:
                return self.walkTree(node[2][1])
            return self.walkTree(node[2][2])

        if node[0] == "condition_eqeq":
            return self.walkTree(node[1]) == self.walkTree(node[2])

        if node[0] == "fun_def":
            self.env[node[1]] = node[2]

        if node[0] == "fun_call":
            try:
                return self.walkTree(self.env[node[1]])
            except LookupError:
                print("Undefined function '%s'" % node[1])
                return 0

        if node[0] == "add":
            return self.walkTree(node[1]) + self.walkTree(node[2])
        elif node[0] == "sub":
            return self.walkTree(node[1]) - self.walkTree(node[2])
        elif node[0] == "mul":
            return self.walkTree(node[1]) * self.walkTree(node[2])
        elif node[0] == "neg":
            return -1 * self.walkTree(node[1])            
        elif node[0] == "div":
            return self.walkTree(node[1]) / self.walkTree(node[2])

        if node[0] == "var_assign":
            self.env[node[1]] = self.walkTree(node[2])
            return node[1]

        if node[0] == "var":
            try:
                return self.env[node[1]]
            except LookupError:
                print("Undefined variable '" + node[1] + "' found!")
                return 0
        
        if node[0] == "bool_assign":
            self.env[node[1]] = self.walkTree(node[2])
            return node[1]

        if node[0] == "for_loop":
            if node[1][0] == "for_loop_setup":
                loop_setup = self.walkTree(node[1])

                loop_count = self.env[loop_setup[0]]
                loop_limit = loop_setup[1]

                for i in range(loop_count + 1, loop_limit + 1):
                    res = self.walkTree(node[2])
                    if res is not None:
                        # print(res)
                        self.txtOutput.insert(END,res)
                    self.env[loop_setup[0]] = i
                del self.env[loop_setup[0]]

        if node[0] == "for_loop_setup":
            return (self.walkTree(node[1]), self.walkTree(node[2]))


# def ejecutar(input, txtOutput):
#     lexer = TryCodeLexer()
#     parser = TryCodeParser()
#     env = {}
#     try:
#         text = input
#     except EOFError:
#         return
#     if text:
#         tree = parser.parse(lexer.tokenize(text))
#         TryCodeExecute(tree, env , txtOutput)
#         txtOutput.see(END)



# if __name__ == "__main__":
#     lexer = TryCodeLexer()
#     parser = TryCodeParser()
#     env = {}
#     while True:
#         try:
#             text = input("TryCode > ")
#         except EOFError:
#             break
#         if text:
#             tree = parser.parse(lexer.tokenize(text))
#             TryCodeExecute(tree, env)
