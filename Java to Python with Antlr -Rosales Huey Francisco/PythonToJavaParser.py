# Generated from PythonToJava.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,108,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,1,1,1,1,1,1,1,3,1,33,8,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,
        2,43,8,2,10,2,12,2,46,9,2,1,3,1,3,1,3,4,3,51,8,3,11,3,12,3,52,1,
        4,1,4,1,4,1,4,3,4,59,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,81,8,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,3,9,90,8,9,1,9,1,9,1,9,5,9,95,8,9,10,9,12,9,98,9,9,
        1,10,1,10,1,10,5,10,103,8,10,10,10,12,10,106,9,10,1,10,0,1,18,11,
        0,2,4,6,8,10,12,14,16,18,20,0,1,1,0,5,8,109,0,25,1,0,0,0,2,28,1,
        0,0,0,4,39,1,0,0,0,6,50,1,0,0,0,8,58,1,0,0,0,10,60,1,0,0,0,12,64,
        1,0,0,0,14,68,1,0,0,0,16,71,1,0,0,0,18,89,1,0,0,0,20,99,1,0,0,0,
        22,24,3,2,1,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,
        0,0,0,26,1,1,0,0,0,27,25,1,0,0,0,28,29,5,1,0,0,29,30,5,15,0,0,30,
        32,5,10,0,0,31,33,3,4,2,0,32,31,1,0,0,0,32,33,1,0,0,0,33,34,1,0,
        0,0,34,35,5,11,0,0,35,36,5,14,0,0,36,37,5,17,0,0,37,38,3,6,3,0,38,
        3,1,0,0,0,39,44,5,15,0,0,40,41,5,9,0,0,41,43,5,15,0,0,42,40,1,0,
        0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,5,1,0,0,0,46,44,
        1,0,0,0,47,48,3,8,4,0,48,49,5,17,0,0,49,51,1,0,0,0,50,47,1,0,0,0,
        51,52,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,7,1,0,0,0,54,59,3,10,
        5,0,55,59,3,12,6,0,56,59,3,14,7,0,57,59,3,16,8,0,58,54,1,0,0,0,58,
        55,1,0,0,0,58,56,1,0,0,0,58,57,1,0,0,0,59,9,1,0,0,0,60,61,5,15,0,
        0,61,62,5,4,0,0,62,63,3,18,9,0,63,11,1,0,0,0,64,65,3,18,9,0,65,66,
        7,0,0,0,66,67,3,18,9,0,67,13,1,0,0,0,68,69,5,2,0,0,69,70,3,18,9,
        0,70,15,1,0,0,0,71,72,5,3,0,0,72,73,5,10,0,0,73,74,3,18,9,0,74,75,
        5,11,0,0,75,17,1,0,0,0,76,77,6,9,-1,0,77,78,5,15,0,0,78,80,5,10,
        0,0,79,81,3,20,10,0,80,79,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,
        90,5,11,0,0,83,90,5,16,0,0,84,90,5,15,0,0,85,86,5,10,0,0,86,87,3,
        18,9,0,87,88,5,11,0,0,88,90,1,0,0,0,89,76,1,0,0,0,89,83,1,0,0,0,
        89,84,1,0,0,0,89,85,1,0,0,0,90,96,1,0,0,0,91,92,10,5,0,0,92,93,7,
        0,0,0,93,95,3,18,9,6,94,91,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,
        97,1,0,0,0,97,19,1,0,0,0,98,96,1,0,0,0,99,104,3,18,9,0,100,101,5,
        9,0,0,101,103,3,18,9,0,102,100,1,0,0,0,103,106,1,0,0,0,104,102,1,
        0,0,0,104,105,1,0,0,0,105,21,1,0,0,0,106,104,1,0,0,0,9,25,32,44,
        52,58,80,89,96,104
    ]

class PythonToJavaParser ( Parser ):

    grammarFileName = "PythonToJava.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'return'", "'print'", "'='", 
                     "'+'", "'-'", "'*'", "'/'", "','", "'('", "')'", "'{'", 
                     "'}'", "':'", "<INVALID>", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "METHOD", "RETURN", "PRINT", "ASSIGN", 
                      "PLUS", "MINUS", "MULT", "DIV", "COMMA", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "COLON", "ID", "NUMBER", 
                      "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_method = 1
    RULE_params = 2
    RULE_block = 3
    RULE_statement = 4
    RULE_assignment = 5
    RULE_operation = 6
    RULE_returnStmt = 7
    RULE_printStmt = 8
    RULE_expr = 9
    RULE_args = 10

    ruleNames =  [ "program", "method", "params", "block", "statement", 
                   "assignment", "operation", "returnStmt", "printStmt", 
                   "expr", "args" ]

    EOF = Token.EOF
    METHOD=1
    RETURN=2
    PRINT=3
    ASSIGN=4
    PLUS=5
    MINUS=6
    MULT=7
    DIV=8
    COMMA=9
    LPAREN=10
    RPAREN=11
    LBRACE=12
    RBRACE=13
    COLON=14
    ID=15
    NUMBER=16
    NEWLINE=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToJavaParser.MethodContext)
            else:
                return self.getTypedRuleContext(PythonToJavaParser.MethodContext,i)


        def getRuleIndex(self):
            return PythonToJavaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = PythonToJavaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 22
                self.method()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def METHOD(self):
            return self.getToken(PythonToJavaParser.METHOD, 0)

        def ID(self):
            return self.getToken(PythonToJavaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(PythonToJavaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PythonToJavaParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(PythonToJavaParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(PythonToJavaParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(PythonToJavaParser.BlockContext,0)


        def params(self):
            return self.getTypedRuleContext(PythonToJavaParser.ParamsContext,0)


        def getRuleIndex(self):
            return PythonToJavaParser.RULE_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod" ):
                listener.enterMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod" ):
                listener.exitMethod(self)




    def method(self):

        localctx = PythonToJavaParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(PythonToJavaParser.METHOD)
            self.state = 29
            self.match(PythonToJavaParser.ID)
            self.state = 30
            self.match(PythonToJavaParser.LPAREN)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 31
                self.params()


            self.state = 34
            self.match(PythonToJavaParser.RPAREN)
            self.state = 35
            self.match(PythonToJavaParser.COLON)
            self.state = 36
            self.match(PythonToJavaParser.NEWLINE)
            self.state = 37
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PythonToJavaParser.ID)
            else:
                return self.getToken(PythonToJavaParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PythonToJavaParser.COMMA)
            else:
                return self.getToken(PythonToJavaParser.COMMA, i)

        def getRuleIndex(self):
            return PythonToJavaParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = PythonToJavaParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(PythonToJavaParser.ID)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 40
                self.match(PythonToJavaParser.COMMA)
                self.state = 41
                self.match(PythonToJavaParser.ID)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToJavaParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonToJavaParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PythonToJavaParser.NEWLINE)
            else:
                return self.getToken(PythonToJavaParser.NEWLINE, i)

        def getRuleIndex(self):
            return PythonToJavaParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = PythonToJavaParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 47
                self.statement()
                self.state = 48
                self.match(PythonToJavaParser.NEWLINE)
                self.state = 52 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 99340) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(PythonToJavaParser.AssignmentContext,0)


        def operation(self):
            return self.getTypedRuleContext(PythonToJavaParser.OperationContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(PythonToJavaParser.ReturnStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(PythonToJavaParser.PrintStmtContext,0)


        def getRuleIndex(self):
            return PythonToJavaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PythonToJavaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.operation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.returnStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.printStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PythonToJavaParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(PythonToJavaParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonToJavaParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonToJavaParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = PythonToJavaParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(PythonToJavaParser.ID)
            self.state = 61
            self.match(PythonToJavaParser.ASSIGN)
            self.state = 62
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToJavaParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonToJavaParser.ExprContext,i)


        def PLUS(self):
            return self.getToken(PythonToJavaParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(PythonToJavaParser.MINUS, 0)

        def MULT(self):
            return self.getToken(PythonToJavaParser.MULT, 0)

        def DIV(self):
            return self.getToken(PythonToJavaParser.DIV, 0)

        def getRuleIndex(self):
            return PythonToJavaParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)




    def operation(self):

        localctx = PythonToJavaParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.expr(0)
            self.state = 65
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 66
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(PythonToJavaParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonToJavaParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonToJavaParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)




    def returnStmt(self):

        localctx = PythonToJavaParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(PythonToJavaParser.RETURN)
            self.state = 69
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(PythonToJavaParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(PythonToJavaParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonToJavaParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(PythonToJavaParser.RPAREN, 0)

        def getRuleIndex(self):
            return PythonToJavaParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)




    def printStmt(self):

        localctx = PythonToJavaParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(PythonToJavaParser.PRINT)
            self.state = 72
            self.match(PythonToJavaParser.LPAREN)
            self.state = 73
            self.expr(0)
            self.state = 74
            self.match(PythonToJavaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PythonToJavaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(PythonToJavaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PythonToJavaParser.RPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(PythonToJavaParser.ArgsContext,0)


        def NUMBER(self):
            return self.getToken(PythonToJavaParser.NUMBER, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToJavaParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonToJavaParser.ExprContext,i)


        def PLUS(self):
            return self.getToken(PythonToJavaParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(PythonToJavaParser.MINUS, 0)

        def MULT(self):
            return self.getToken(PythonToJavaParser.MULT, 0)

        def DIV(self):
            return self.getToken(PythonToJavaParser.DIV, 0)

        def getRuleIndex(self):
            return PythonToJavaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonToJavaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 77
                self.match(PythonToJavaParser.ID)
                self.state = 78
                self.match(PythonToJavaParser.LPAREN)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 99328) != 0):
                    self.state = 79
                    self.args()


                self.state = 82
                self.match(PythonToJavaParser.RPAREN)
                pass

            elif la_ == 2:
                self.state = 83
                self.match(PythonToJavaParser.NUMBER)
                pass

            elif la_ == 3:
                self.state = 84
                self.match(PythonToJavaParser.ID)
                pass

            elif la_ == 4:
                self.state = 85
                self.match(PythonToJavaParser.LPAREN)
                self.state = 86
                self.expr(0)
                self.state = 87
                self.match(PythonToJavaParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonToJavaParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 91
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 92
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 93
                    self.expr(6) 
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToJavaParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonToJavaParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PythonToJavaParser.COMMA)
            else:
                return self.getToken(PythonToJavaParser.COMMA, i)

        def getRuleIndex(self):
            return PythonToJavaParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = PythonToJavaParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.expr(0)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 100
                self.match(PythonToJavaParser.COMMA)
                self.state = 101
                self.expr(0)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         




