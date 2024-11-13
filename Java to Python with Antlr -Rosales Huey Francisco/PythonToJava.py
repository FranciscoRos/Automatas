from antlr4 import *
from PythonToJavaLexer import PythonToJavaLexer  # Separa los tokens
from PythonToJavaParser import PythonToJavaParser  # Valida la posición con las reglas
from InPythonToJava import InPythonToJava  # Clase para convertir el código de Python a Java

#Rosales Huey Francisco Jareth
def main():
    # Leer la entrada del archivo de Python
    with open('codigo_prueba.py', 'r') as file:
        in_python_code = file.read()

    lexer = PythonToJavaLexer(InputStream(in_python_code))
    t_stream = CommonTokenStream(lexer)

    parser = PythonToJavaParser(t_stream)
    tree = parser.program()

    walker = ParseTreeWalker()
    converter = InPythonToJava()
    
    walker.walk(converter, tree)
    
    with open('Main.java', 'w') as java_file:
        java_file.write(converter.java_code)

    print("\nCódigo convertido a Java guardado en 'Main.java'.")

if __name__ == '__main__':
    main()
