from PythonToJavaParser import PythonToJavaParser
from PythonToJavaListener import PythonToJavaListener #Este es el chismoso valida errores

class InPythonToJava(PythonToJavaListener):
    def __init__(self):
        self.java_code = "public class Main {\n"
        self.methods = ""
        self.main_code = "    public static void main(String[] args) {\n"
        self.print_statements = []

    def enterMethod(self, ctx: PythonToJavaParser.MethodContext):
        method_name = ctx.ID().getText()
        params = [param.getText() for param in ctx.params().ID()] if ctx.params() else []
        self.methods += f"    public static int {method_name}({', '.join(['int ' + p for p in params])}) {{\n"

    def exitMethod(self, ctx: PythonToJavaParser.MethodContext):
        self.methods += "    }\n"

    def enterAssignment(self, ctx: PythonToJavaParser.AssignmentContext):
        var_name = ctx.ID().getText()
        expr = ctx.expr().getText()
        self.methods += f"        int {var_name} = {expr};\n"

    def enterReturnStmt(self, ctx: PythonToJavaParser.ReturnStmtContext):
        expr = ctx.expr().getText()
        self.methods += f"        return {expr};\n"

    def enterPrintStmt(self, ctx: PythonToJavaParser.PrintStmtContext):
      expr = ctx.expr().getText()

      #método con argumentos
      if '(' in expr and ')' in expr:
          self.print_statements.append(f"        System.out.println({expr});\n")
      else:
          #si es una variable o un número
          self.print_statements.append(f"        System.out.println({expr});\n")

    def exitProgram(self, ctx: PythonToJavaParser.ProgramContext):
        #Agrega los print
        for stmt in self.print_statements:
          self.main_code += stmt
        self.main_code += "    }\n"
        self.java_code += self.methods + self.main_code + "}\n"
