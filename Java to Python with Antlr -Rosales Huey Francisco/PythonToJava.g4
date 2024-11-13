grammar PythonToJava;

// Lexer 
METHOD: 'def';
RETURN: 'return';
PRINT: 'print';
ASSIGN: '=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
COMMA: ',';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
COLON: ':';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+;
NEWLINE:'\n';
WS: [ \t]+ -> skip;

// Parser 
program: method*;
method: METHOD ID LPAREN params? RPAREN COLON NEWLINE block;
params: ID (COMMA ID)*;
block: (statement NEWLINE)+;
statement: assignment | operation | returnStmt | printStmt;
assignment: ID ASSIGN expr;
operation: expr (PLUS | MINUS | MULT | DIV) expr;
returnStmt: RETURN expr;
printStmt: PRINT LPAREN expr RPAREN;
expr: expr (PLUS | MINUS | MULT | DIV) expr  
     | ID LPAREN args? RPAREN               
     | NUMBER
     | ID
     | LPAREN expr RPAREN;                  

args: expr (COMMA expr)*;  
