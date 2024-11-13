# Generated from PythonToJava.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonToJavaParser import PythonToJavaParser
else:
    from PythonToJavaParser import PythonToJavaParser

# This class defines a complete listener for a parse tree produced by PythonToJavaParser.
class PythonToJavaListener(ParseTreeListener):

    # Enter a parse tree produced by PythonToJavaParser#program.
    def enterProgram(self, ctx:PythonToJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#program.
    def exitProgram(self, ctx:PythonToJavaParser.ProgramContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#method.
    def enterMethod(self, ctx:PythonToJavaParser.MethodContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#method.
    def exitMethod(self, ctx:PythonToJavaParser.MethodContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#params.
    def enterParams(self, ctx:PythonToJavaParser.ParamsContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#params.
    def exitParams(self, ctx:PythonToJavaParser.ParamsContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#block.
    def enterBlock(self, ctx:PythonToJavaParser.BlockContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#block.
    def exitBlock(self, ctx:PythonToJavaParser.BlockContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#statement.
    def enterStatement(self, ctx:PythonToJavaParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#statement.
    def exitStatement(self, ctx:PythonToJavaParser.StatementContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#assignment.
    def enterAssignment(self, ctx:PythonToJavaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#assignment.
    def exitAssignment(self, ctx:PythonToJavaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#operation.
    def enterOperation(self, ctx:PythonToJavaParser.OperationContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#operation.
    def exitOperation(self, ctx:PythonToJavaParser.OperationContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#returnStmt.
    def enterReturnStmt(self, ctx:PythonToJavaParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#returnStmt.
    def exitReturnStmt(self, ctx:PythonToJavaParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#printStmt.
    def enterPrintStmt(self, ctx:PythonToJavaParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#printStmt.
    def exitPrintStmt(self, ctx:PythonToJavaParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#expr.
    def enterExpr(self, ctx:PythonToJavaParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#expr.
    def exitExpr(self, ctx:PythonToJavaParser.ExprContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#args.
    def enterArgs(self, ctx:PythonToJavaParser.ArgsContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#args.
    def exitArgs(self, ctx:PythonToJavaParser.ArgsContext):
        pass



del PythonToJavaParser