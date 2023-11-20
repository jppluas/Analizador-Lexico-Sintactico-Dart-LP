
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT AS ASSERT ASSIGN ASYNC AWAIT BLOCKCOMMENT BOOLEAN_TYPE BREAK CASE CATCH COLON COMMA COMMENT CONST CONTINUE DEFAULT DEFERRED DIVIDE DO DOT DOUBLE DOUBLE_TYPE DYNAMIC_TYPE ELSE ENUM ENUM_TYPE EQUAL EXPORT EXTENDS EXTENSION EXTERNAL FALSE FINAL FINALLY FOR GET GREATER GREATER_EQUAL HIDE IDENTIFIER IF IMPLEMENTS IMPORT IN INTEGER INTEGER_TYPE INTERFACE IS KEYWORD LATE LBRACE LESS LESS_EQUAL LIBRARY LINE_BREAK LIST_TYPE LOGICAL_AND LOGICAL_NOT LOGICAL_OR LPAREN LSQUARE MAP_TYPE MINUS NOT_EQUAL NULL ON OPERATOR PART PLUS PRINT QUESTION_MARK QUEUE_TYPE RBRACE RETHROW RETURN RPAREN RSQUARE SEMICOLON SET SET_TYPE SHOW STATIC STRING STRING_TYPE SUPER SWITCH SYNC THROW TIMES TRUE TRY TYPEDEF VAR VOID WHILE WITH YIELD\n    statement : expression\n              | assignment\n              | print\n              | function\n              | if_statement\n              | while_statement\n              | for_statement\n              | lines\n              | LBRACE lines RBRACE\n              | \n      assignment : modifier type nullable IDENTIFIER ASSIGN expression SEMICOLON\n                    | type nullable IDENTIFIER ASSIGN expression SEMICOLON\n                    | modifier type IDENTIFIER ASSIGN expression SEMICOLON\n                    | type IDENTIFIER ASSIGN expression SEMICOLON\n     nullable : QUESTION_MARK\n     modifier : LATE\n                | FINAL\n                | CONST\n      print : PRINT LPAREN expression RPAREN SEMICOLON\n                | PRINT LPAREN RPAREN SEMICOLON\n    \n    if_statement : IF LPAREN logic RPAREN LBRACE lines RBRACE\n                 | if_statement ELSE if_statement\n                 | if_statement ELSE LBRACE lines RBRACE\n    \n    function_call : IDENTIFIER LPAREN parameters RPAREN SEMICOLON\n     type : INTEGER_TYPE\n            | DOUBLE_TYPE\n            | BOOLEAN_TYPE\n            | QUEUE_TYPE\n            | STRING_TYPE\n            | ENUM_TYPE\n            | VAR\n            | LIST_TYPE\n            | MAP_TYPE\n            | SET_TYPE\n            | DYNAMIC_TYPE\n            | VOID\n\n      expression : arithmetic\n                    | logic\n                    | function_call\n     arithmetic : value\n        |   arithmetic arith_op arithmetic\n        |   LPAREN arithmetic arith_op arithmetic RPAREN\n     comparison : value\n        |   boolean\n        |   comparison comp_op comparison\n        |   LPAREN comparison comp_op comparison RPAREN\n     logic : comparison\n        |   logic logic_op logic\n        |   LPAREN logic logic_op logic RPAREN\n        |   LOGICAL_NOT logic\n     logic_op : LOGICAL_AND\n        |   LOGICAL_OR\n     arith_op : PLUS\n        |   MINUS\n        |   TIMES\n        |   DIVIDE\n    \n      comp_op : EQUAL\n                 | NOT_EQUAL\n                 | LESS\n                 | LESS_EQUAL\n                 | GREATER\n                 | GREATER_EQUAL\n       values : value\n             | value COMMA values\n value : IDENTIFIER\n         | number\n         | string\n         | list\n  number : INTEGER \n                | DOUBLE\n      string : STRING\n     boolean : TRUE\n                | FALSE\n     list : LSQUARE RSQUARE\n            | LSQUARE values RSQUARE\n    \n    \n    function : type IDENTIFIER LPAREN parameters RPAREN LBRACE lines RBRACE\n     lines : line LINE_BREAK lines\n            | line lines\n            | line\n            | \n\n     line : print\n            | assignment\n            | function\n            | if_statement\n    \n      parameters : VOID\n                 | parameter\n                 | parameter COMMA parameters\n                 |\n      \n  parameter : type IDENTIFIER\n            | IDENTIFIER \n  \n    map : MAP_TYPE LESS type COMMA type GREATER\n        | MAP_TYPE LESS type COMMA type GREATER LSQUARE values RSQUARE\n        | MAP_TYPE LESS type COMMA type GREATER LSQUARE RSQUARE\n    \n    set : SET_TYPE LESS type GREATER\n        | SET_TYPE LESS type GREATER LSQUARE values RSQUARE\n        | SET_TYPE LESS type GREATER LSQUARE RSQUARE\n    \n    queue : QUEUE_TYPE LESS type GREATER\n          | QUEUE_TYPE LESS type GREATER LSQUARE values RSQUARE\n          | QUEUE_TYPE LESS type GREATER LSQUARE RSQUARE\n    \n    while_statement : WHILE LPAREN logic RPAREN LBRACE lines RBRACE\n    \n    for_statement : FOR LPAREN assignment SEMICOLON logic SEMICOLON assignment RPAREN LBRACE lines RBRACE\n    '
    
_lr_action_items = {'LBRACE':([0,51,138,139,149,172,],[10,94,156,157,162,173,]),'$end':([0,1,2,3,4,5,6,7,8,9,11,12,13,16,22,23,24,41,42,43,44,45,46,47,49,50,53,54,55,56,74,78,79,87,89,90,93,95,96,97,99,119,120,122,134,144,148,150,152,153,154,155,160,161,166,168,169,171,175,],[-10,0,-1,-2,-3,-4,-5,-6,-7,-8,-37,-38,-39,-65,-79,-40,-47,-66,-67,-68,-44,-69,-70,-71,-72,-73,-81,-82,-83,-84,-65,-80,-78,-50,-43,-74,-22,-9,-41,-40,-48,-77,-45,-75,-20,-23,-14,-24,-19,-42,-49,-46,-13,-12,-11,-21,-100,-76,-101,]),'PRINT':([0,3,4,5,6,10,22,53,54,55,56,78,93,94,134,144,148,152,156,157,160,161,162,166,168,171,173,],[17,-82,-81,-83,-84,17,17,-81,-82,-83,-84,17,-22,17,-20,-23,-14,-19,17,17,-13,-12,17,-11,-21,-76,17,]),'IF':([0,3,4,5,6,10,22,51,53,54,55,56,78,93,94,134,144,148,152,156,157,160,161,162,166,168,171,173,],[19,-82,-81,-83,-84,19,19,19,-81,-82,-83,-84,19,-22,19,-20,-23,-14,-19,19,19,-13,-12,19,-11,-21,-76,19,]),'WHILE':([0,],[20,]),'FOR':([0,],[21,]),'LPAREN':([0,16,17,18,19,20,21,25,57,58,59,60,61,62,63,64,67,70,75,76,80,81,82,83,84,85,86,88,98,103,112,113,114,121,126,127,140,145,],[18,69,70,18,75,76,77,88,98,-53,-54,-55,-56,88,-51,-52,104,18,88,88,121,-57,-58,-59,-60,-61,-62,88,98,18,98,88,121,121,18,18,88,18,]),'LOGICAL_NOT':([0,18,25,62,63,64,70,75,76,88,103,113,126,127,140,145,],[25,25,25,25,-51,-52,25,25,25,25,25,25,25,25,25,25,]),'IDENTIFIER':([0,15,18,25,29,30,31,32,33,34,35,36,37,38,39,40,48,57,58,59,60,61,62,63,64,65,66,68,69,70,75,76,80,81,82,83,84,85,86,88,98,100,103,104,107,109,112,113,114,118,121,123,126,127,131,140,145,],[16,67,74,74,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,74,74,-53,-54,-55,-56,74,-51,-52,101,102,-15,105,16,74,74,74,-57,-58,-59,-60,-61,-62,74,74,125,16,105,-36,132,74,74,74,141,74,74,16,16,105,74,16,]),'LATE':([0,3,4,5,6,10,22,53,54,55,56,77,78,93,94,134,144,148,152,156,157,160,161,162,165,166,168,171,173,],[26,-82,-81,-83,-84,26,26,-81,-82,-83,-84,26,26,-22,26,-20,-23,-14,-19,26,26,-13,-12,26,26,-11,-21,-76,26,]),'FINAL':([0,3,4,5,6,10,22,53,54,55,56,77,78,93,94,134,144,148,152,156,157,160,161,162,165,166,168,171,173,],[27,-82,-81,-83,-84,27,27,-81,-82,-83,-84,27,27,-22,27,-20,-23,-14,-19,27,27,-13,-12,27,27,-11,-21,-76,27,]),'CONST':([0,3,4,5,6,10,22,53,54,55,56,77,78,93,94,134,144,148,152,156,157,160,161,162,165,166,168,171,173,],[28,-82,-81,-83,-84,28,28,-81,-82,-83,-84,28,28,-22,28,-20,-23,-14,-19,28,28,-13,-12,28,28,-11,-21,-76,28,]),'INTEGER_TYPE':([0,3,4,5,6,10,14,22,26,27,28,53,54,55,56,69,77,78,93,94,104,131,134,144,148,152,156,157,160,161,162,165,166,168,171,173,],[29,-82,-81,-83,-84,29,29,29,-16,-17,-18,-81,-82,-83,-84,29,29,29,-22,29,29,29,-20,-23,-14,-19,29,29,-13,-12,29,29,-11,-21,-76,29,]),'DOUBLE_TYPE':([0,3,4,5,6,10,14,22,26,27,28,53,54,55,56,69,77,78,93,94,104,131,134,144,148,152,156,157,160,161,162,165,166,168,171,173,],[30,-82,-81,-83,-84,30,30,30,-16,-17,-18,-81,-82,-83,-84,30,30,30,-22,30,30,30,-20,-23,-14,-19,30,30,-13,-12,30,30,-11,-21,-76,30,]),'BOOLEAN_TYPE':([0,3,4,5,6,10,14,22,26,27,28,53,54,55,56,69,77,78,93,94,104,131,134,144,148,152,156,157,160,161,162,165,166,168,171,173,],[31,-82,-81,-83,-84,31,31,31,-16,-17,-18,-81,-82,-83,-84,31,31,31,-22,31,31,31,-20,-23,-14,-19,31,31,-13,-12,31,31,-11,-21,-76,31,]),'QUEUE_TYPE':([0,3,4,5,6,10,14,22,26,27,28,53,54,55,56,69,77,78,93,94,104,131,134,144,148,152,156,157,160,161,162,165,166,168,171,173,],[32,-82,-81,-83,-84,32,32,32,-16,-17,-18,-81,-82,-83,-84,32,32,32,-22,32,32,32,-20,-23,-14,-19,32,32,-13,-12,32,32,-11,-21,-76,32,]),'STRING_TYPE':([0,3,4,5,6,10,14,22,26,27,28,53,54,55,56,69,77,78,93,94,104,131,134,144,148,152,156,157,160,161,162,165,166,168,171,173,],[33,-82,-81,-83,-84,33,33,33,-16,-17,-18,-81,-82,-83,-84,33,33,33,-22,33,33,33,-20,-23,-14,-19,33,33,-13,-12,33,33,-11,-21,-76,33,]),'ENUM_TYPE':([0,3,4,5,6,10,14,22,26,27,28,53,54,55,56,69,77,78,93,94,104,131,134,144,148,152,156,157,160,161,162,165,166,168,171,173,],[34,-82,-81,-83,-84,34,34,34,-16,-17,-18,-81,-82,-83,-84,34,34,34,-22,34,34,34,-20,-23,-14,-19,34,34,-13,-12,34,34,-11,-21,-76,34,]),'VAR':([0,3,4,5,6,10,14,22,26,27,28,53,54,55,56,69,77,78,93,94,104,131,134,144,148,152,156,157,160,161,162,165,166,168,171,173,],[35,-82,-81,-83,-84,35,35,35,-16,-17,-18,-81,-82,-83,-84,35,35,35,-22,35,35,35,-20,-23,-14,-19,35,35,-13,-12,35,35,-11,-21,-76,35,]),'LIST_TYPE':([0,3,4,5,6,10,14,22,26,27,28,53,54,55,56,69,77,78,93,94,104,131,134,144,148,152,156,157,160,161,162,165,166,168,171,173,],[36,-82,-81,-83,-84,36,36,36,-16,-17,-18,-81,-82,-83,-84,36,36,36,-22,36,36,36,-20,-23,-14,-19,36,36,-13,-12,36,36,-11,-21,-76,36,]),'MAP_TYPE':([0,3,4,5,6,10,14,22,26,27,28,53,54,55,56,69,77,78,93,94,104,131,134,144,148,152,156,157,160,161,162,165,166,168,171,173,],[37,-82,-81,-83,-84,37,37,37,-16,-17,-18,-81,-82,-83,-84,37,37,37,-22,37,37,37,-20,-23,-14,-19,37,37,-13,-12,37,37,-11,-21,-76,37,]),'SET_TYPE':([0,3,4,5,6,10,14,22,26,27,28,53,54,55,56,69,77,78,93,94,104,131,134,144,148,152,156,157,160,161,162,165,166,168,171,173,],[38,-82,-81,-83,-84,38,38,38,-16,-17,-18,-81,-82,-83,-84,38,38,38,-22,38,38,38,-20,-23,-14,-19,38,38,-13,-12,38,38,-11,-21,-76,38,]),'DYNAMIC_TYPE':([0,3,4,5,6,10,14,22,26,27,28,53,54,55,56,69,77,78,93,94,104,131,134,144,148,152,156,157,160,161,162,165,166,168,171,173,],[39,-82,-81,-83,-84,39,39,39,-16,-17,-18,-81,-82,-83,-84,39,39,39,-22,39,39,39,-20,-23,-14,-19,39,39,-13,-12,39,39,-11,-21,-76,39,]),'VOID':([0,3,4,5,6,10,14,22,26,27,28,53,54,55,56,69,77,78,93,94,104,131,134,144,148,152,156,157,160,161,162,165,166,168,171,173,],[40,-82,-81,-83,-84,40,40,40,-16,-17,-18,-81,-82,-83,-84,107,40,40,-22,40,107,107,-20,-23,-14,-19,40,40,-13,-12,40,40,-11,-21,-76,40,]),'INTEGER':([0,18,25,48,57,58,59,60,61,62,63,64,70,75,76,80,81,82,83,84,85,86,88,98,103,112,113,114,121,123,126,127,140,145,],[45,45,45,45,45,-53,-54,-55,-56,45,-51,-52,45,45,45,45,-57,-58,-59,-60,-61,-62,45,45,45,45,45,45,45,45,45,45,45,45,]),'DOUBLE':([0,18,25,48,57,58,59,60,61,62,63,64,70,75,76,80,81,82,83,84,85,86,88,98,103,112,113,114,121,123,126,127,140,145,],[46,46,46,46,46,-53,-54,-55,-56,46,-51,-52,46,46,46,46,-57,-58,-59,-60,-61,-62,46,46,46,46,46,46,46,46,46,46,46,46,]),'STRING':([0,18,25,48,57,58,59,60,61,62,63,64,70,75,76,80,81,82,83,84,85,86,88,98,103,112,113,114,121,123,126,127,140,145,],[47,47,47,47,47,-53,-54,-55,-56,47,-51,-52,47,47,47,47,-57,-58,-59,-60,-61,-62,47,47,47,47,47,47,47,47,47,47,47,47,]),'LSQUARE':([0,18,25,48,57,58,59,60,61,62,63,64,70,75,76,80,81,82,83,84,85,86,88,98,103,112,113,114,121,123,126,127,140,145,],[48,48,48,48,48,-53,-54,-55,-56,48,-51,-52,48,48,48,48,-57,-58,-59,-60,-61,-62,48,48,48,48,48,48,48,48,48,48,48,48,]),'TRUE':([0,18,25,62,63,64,70,75,76,80,81,82,83,84,85,86,88,103,113,114,121,126,127,140,145,],[49,49,49,49,-51,-52,49,49,49,49,-57,-58,-59,-60,-61,-62,49,49,49,49,49,49,49,49,49,]),'FALSE':([0,18,25,62,63,64,70,75,76,80,81,82,83,84,85,86,88,103,113,114,121,126,127,140,145,],[50,50,50,50,-51,-52,50,50,50,50,-57,-58,-59,-60,-61,-62,50,50,50,50,50,50,50,50,50,]),'LINE_BREAK':([3,4,5,6,22,53,54,55,56,93,134,144,148,152,160,161,166,168,171,],[-82,-81,-83,-84,78,-81,-82,-83,-84,-22,-20,-23,-14,-19,-13,-12,-11,-21,-76,]),'ELSE':([6,56,93,144,168,],[51,51,51,-23,-21,]),'RBRACE':([10,22,52,53,54,55,56,78,79,93,94,119,124,134,144,148,152,156,157,160,161,162,163,164,166,167,168,171,173,174,],[-80,-79,95,-81,-82,-83,-84,-80,-78,-22,-80,-77,144,-20,-23,-14,-19,-80,-80,-13,-12,-80,168,169,-11,171,-21,-76,-80,175,]),'RPAREN':([11,12,13,16,23,24,41,42,43,44,45,46,47,49,50,69,70,74,87,89,90,96,97,99,104,105,106,107,108,110,115,116,120,122,129,131,132,135,136,137,148,150,151,153,154,155,160,161,166,170,],[-37,-38,-39,-65,-40,-47,-66,-67,-68,-44,-69,-70,-71,-72,-73,-88,111,-65,-50,-43,-74,-41,-40,-48,-88,-90,130,-85,-86,133,138,139,-45,-75,149,-88,-89,153,154,155,-14,-24,-87,-42,-49,-46,-13,-12,-11,172,]),'SEMICOLON':([11,12,13,16,23,24,41,42,43,44,45,46,47,49,50,74,87,89,90,96,97,99,111,117,120,122,128,130,133,146,147,148,150,153,154,155,158,159,160,161,166,],[-37,-38,-39,-65,-40,-47,-66,-67,-68,-44,-69,-70,-71,-72,-73,-65,-50,-43,-74,-41,-40,-48,134,140,-45,-75,148,150,152,160,161,-14,-24,-42,-49,-46,165,166,-13,-12,-11,]),'PLUS':([11,16,23,41,42,43,45,46,47,71,74,90,96,97,122,135,153,],[58,-65,-40,-66,-67,-68,-69,-70,-71,58,-65,-74,58,-40,-75,58,-42,]),'MINUS':([11,16,23,41,42,43,45,46,47,71,74,90,96,97,122,135,153,],[59,-65,-40,-66,-67,-68,-69,-70,-71,59,-65,-74,59,-40,-75,59,-42,]),'TIMES':([11,16,23,41,42,43,45,46,47,71,74,90,96,97,122,135,153,],[60,-65,-40,-66,-67,-68,-69,-70,-71,60,-65,-74,60,-40,-75,60,-42,]),'DIVIDE':([11,16,23,41,42,43,45,46,47,71,74,90,96,97,122,135,153,],[61,-65,-40,-66,-67,-68,-69,-70,-71,61,-65,-74,61,-40,-75,61,-42,]),'LOGICAL_AND':([12,16,23,24,41,42,43,44,45,46,47,49,50,72,73,74,87,89,90,99,115,116,120,122,136,137,154,155,158,],[63,-65,-43,-47,-66,-67,-68,-44,-69,-70,-71,-72,-73,63,-47,-65,63,-43,-74,63,63,63,-45,-75,63,-45,-49,-46,63,]),'LOGICAL_OR':([12,16,23,24,41,42,43,44,45,46,47,49,50,72,73,74,87,89,90,99,115,116,120,122,136,137,154,155,158,],[64,-65,-43,-47,-66,-67,-68,-44,-69,-70,-71,-72,-73,64,-47,-65,64,-43,-74,64,64,64,-45,-75,64,-45,-49,-46,64,]),'QUESTION_MARK':([15,29,30,31,32,33,34,35,36,37,38,39,40,65,118,],[68,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,68,68,]),'EQUAL':([16,23,24,41,42,43,44,45,46,47,49,50,73,74,89,90,120,122,137,142,155,],[-65,-43,81,-66,-67,-68,-44,-69,-70,-71,-72,-73,81,-65,-43,-74,81,-75,81,81,-46,]),'NOT_EQUAL':([16,23,24,41,42,43,44,45,46,47,49,50,73,74,89,90,120,122,137,142,155,],[-65,-43,82,-66,-67,-68,-44,-69,-70,-71,-72,-73,82,-65,-43,-74,82,-75,82,82,-46,]),'LESS':([16,23,24,41,42,43,44,45,46,47,49,50,73,74,89,90,120,122,137,142,155,],[-65,-43,83,-66,-67,-68,-44,-69,-70,-71,-72,-73,83,-65,-43,-74,83,-75,83,83,-46,]),'LESS_EQUAL':([16,23,24,41,42,43,44,45,46,47,49,50,73,74,89,90,120,122,137,142,155,],[-65,-43,84,-66,-67,-68,-44,-69,-70,-71,-72,-73,84,-65,-43,-74,84,-75,84,84,-46,]),'GREATER':([16,23,24,41,42,43,44,45,46,47,49,50,73,74,89,90,120,122,137,142,155,],[-65,-43,85,-66,-67,-68,-44,-69,-70,-71,-72,-73,85,-65,-43,-74,85,-75,85,85,-46,]),'GREATER_EQUAL':([16,23,24,41,42,43,44,45,46,47,49,50,73,74,89,90,120,122,137,142,155,],[-65,-43,86,-66,-67,-68,-44,-69,-70,-71,-72,-73,86,-65,-43,-74,86,-75,86,86,-46,]),'COMMA':([41,42,43,45,46,47,74,90,92,105,108,122,132,],[-66,-67,-68,-69,-70,-71,-65,-74,123,-90,131,-75,-89,]),'RSQUARE':([41,42,43,45,46,47,48,74,90,91,92,122,143,],[-66,-67,-68,-69,-70,-71,90,-65,-74,122,-63,-75,-64,]),'ASSIGN':([67,101,102,125,141,],[103,126,127,145,103,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,70,103,126,127,145,],[2,110,128,146,147,159,]),'assignment':([0,10,22,77,78,94,156,157,162,165,173,],[3,54,54,117,54,54,54,54,54,170,54,]),'print':([0,10,22,78,94,156,157,162,173,],[4,53,53,53,53,53,53,53,53,]),'function':([0,10,22,78,94,156,157,162,173,],[5,55,55,55,55,55,55,55,55,]),'if_statement':([0,10,22,51,78,94,156,157,162,173,],[6,56,56,93,56,56,56,56,56,56,]),'while_statement':([0,],[7,]),'for_statement':([0,],[8,]),'lines':([0,10,22,78,94,156,157,162,173,],[9,52,79,119,124,163,164,167,174,]),'arithmetic':([0,18,57,70,98,103,112,126,127,145,],[11,71,96,11,71,11,135,11,11,11,]),'logic':([0,18,25,62,70,75,76,88,103,113,126,127,140,145,],[12,72,87,99,12,115,116,72,12,136,12,12,158,12,]),'function_call':([0,70,103,126,127,145,],[13,13,13,13,13,13,]),'modifier':([0,10,22,77,78,94,156,157,162,165,173,],[14,14,14,14,14,14,14,14,14,14,14,]),'type':([0,10,14,22,69,77,78,94,104,131,156,157,162,165,173,],[15,15,65,15,109,118,15,15,109,109,15,15,15,118,15,]),'line':([0,10,22,78,94,156,157,162,173,],[22,22,22,22,22,22,22,22,22,]),'value':([0,18,25,48,57,62,70,75,76,80,88,98,103,112,113,114,121,123,126,127,140,145,],[23,23,89,92,97,89,23,89,89,89,89,97,23,97,89,89,89,92,23,23,89,23,]),'comparison':([0,18,25,62,70,75,76,80,88,103,113,114,121,126,127,140,145,],[24,73,24,24,24,24,24,120,73,24,24,137,142,24,24,24,24,]),'number':([0,18,25,48,57,62,70,75,76,80,88,98,103,112,113,114,121,123,126,127,140,145,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'string':([0,18,25,48,57,62,70,75,76,80,88,98,103,112,113,114,121,123,126,127,140,145,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'list':([0,18,25,48,57,62,70,75,76,80,88,98,103,112,113,114,121,123,126,127,140,145,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'boolean':([0,18,25,62,70,75,76,80,88,103,113,114,121,126,127,140,145,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'arith_op':([11,71,96,135,],[57,112,57,57,]),'logic_op':([12,72,87,99,115,116,136,158,],[62,113,62,62,62,62,62,62,]),'nullable':([15,65,118,],[66,100,66,]),'comp_op':([24,73,120,137,142,],[80,114,80,80,114,]),'values':([48,123,],[91,143,]),'parameters':([69,104,131,],[106,129,151,]),'parameter':([69,104,131,],[108,108,108,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement','sintactico.py',6),
  ('statement -> assignment','statement',1,'p_statement','sintactico.py',7),
  ('statement -> print','statement',1,'p_statement','sintactico.py',8),
  ('statement -> function','statement',1,'p_statement','sintactico.py',9),
  ('statement -> if_statement','statement',1,'p_statement','sintactico.py',10),
  ('statement -> while_statement','statement',1,'p_statement','sintactico.py',11),
  ('statement -> for_statement','statement',1,'p_statement','sintactico.py',12),
  ('statement -> lines','statement',1,'p_statement','sintactico.py',13),
  ('statement -> LBRACE lines RBRACE','statement',3,'p_statement','sintactico.py',14),
  ('statement -> <empty>','statement',0,'p_statement','sintactico.py',15),
  ('assignment -> modifier type nullable IDENTIFIER ASSIGN expression SEMICOLON','assignment',7,'p_assignment','sintactico.py',18),
  ('assignment -> type nullable IDENTIFIER ASSIGN expression SEMICOLON','assignment',6,'p_assignment','sintactico.py',19),
  ('assignment -> modifier type IDENTIFIER ASSIGN expression SEMICOLON','assignment',6,'p_assignment','sintactico.py',20),
  ('assignment -> type IDENTIFIER ASSIGN expression SEMICOLON','assignment',5,'p_assignment','sintactico.py',21),
  ('nullable -> QUESTION_MARK','nullable',1,'p_nullable','sintactico.py',25),
  ('modifier -> LATE','modifier',1,'p_modifier','sintactico.py',29),
  ('modifier -> FINAL','modifier',1,'p_modifier','sintactico.py',30),
  ('modifier -> CONST','modifier',1,'p_modifier','sintactico.py',31),
  ('print -> PRINT LPAREN expression RPAREN SEMICOLON','print',5,'p_print','sintactico.py',35),
  ('print -> PRINT LPAREN RPAREN SEMICOLON','print',4,'p_print','sintactico.py',36),
  ('if_statement -> IF LPAREN logic RPAREN LBRACE lines RBRACE','if_statement',7,'p_if_statement','sintactico.py',41),
  ('if_statement -> if_statement ELSE if_statement','if_statement',3,'p_if_statement','sintactico.py',42),
  ('if_statement -> if_statement ELSE LBRACE lines RBRACE','if_statement',5,'p_if_statement','sintactico.py',43),
  ('function_call -> IDENTIFIER LPAREN parameters RPAREN SEMICOLON','function_call',5,'p_function_call','sintactico.py',49),
  ('type -> INTEGER_TYPE','type',1,'p_type','sintactico.py',53),
  ('type -> DOUBLE_TYPE','type',1,'p_type','sintactico.py',54),
  ('type -> BOOLEAN_TYPE','type',1,'p_type','sintactico.py',55),
  ('type -> QUEUE_TYPE','type',1,'p_type','sintactico.py',56),
  ('type -> STRING_TYPE','type',1,'p_type','sintactico.py',57),
  ('type -> ENUM_TYPE','type',1,'p_type','sintactico.py',58),
  ('type -> VAR','type',1,'p_type','sintactico.py',59),
  ('type -> LIST_TYPE','type',1,'p_type','sintactico.py',60),
  ('type -> MAP_TYPE','type',1,'p_type','sintactico.py',61),
  ('type -> SET_TYPE','type',1,'p_type','sintactico.py',62),
  ('type -> DYNAMIC_TYPE','type',1,'p_type','sintactico.py',63),
  ('type -> VOID','type',1,'p_type','sintactico.py',64),
  ('expression -> arithmetic','expression',1,'p_expression','sintactico.py',69),
  ('expression -> logic','expression',1,'p_expression','sintactico.py',70),
  ('expression -> function_call','expression',1,'p_expression','sintactico.py',71),
  ('arithmetic -> value','arithmetic',1,'p_arithmetic','sintactico.py',75),
  ('arithmetic -> arithmetic arith_op arithmetic','arithmetic',3,'p_arithmetic','sintactico.py',76),
  ('arithmetic -> LPAREN arithmetic arith_op arithmetic RPAREN','arithmetic',5,'p_arithmetic','sintactico.py',77),
  ('comparison -> value','comparison',1,'p_comparison','sintactico.py',81),
  ('comparison -> boolean','comparison',1,'p_comparison','sintactico.py',82),
  ('comparison -> comparison comp_op comparison','comparison',3,'p_comparison','sintactico.py',83),
  ('comparison -> LPAREN comparison comp_op comparison RPAREN','comparison',5,'p_comparison','sintactico.py',84),
  ('logic -> comparison','logic',1,'p_logic','sintactico.py',88),
  ('logic -> logic logic_op logic','logic',3,'p_logic','sintactico.py',89),
  ('logic -> LPAREN logic logic_op logic RPAREN','logic',5,'p_logic','sintactico.py',90),
  ('logic -> LOGICAL_NOT logic','logic',2,'p_logic','sintactico.py',91),
  ('logic_op -> LOGICAL_AND','logic_op',1,'p_logic_op','sintactico.py',95),
  ('logic_op -> LOGICAL_OR','logic_op',1,'p_logic_op','sintactico.py',96),
  ('arith_op -> PLUS','arith_op',1,'p_arith_op','sintactico.py',100),
  ('arith_op -> MINUS','arith_op',1,'p_arith_op','sintactico.py',101),
  ('arith_op -> TIMES','arith_op',1,'p_arith_op','sintactico.py',102),
  ('arith_op -> DIVIDE','arith_op',1,'p_arith_op','sintactico.py',103),
  ('comp_op -> EQUAL','comp_op',1,'p_comp_op','sintactico.py',108),
  ('comp_op -> NOT_EQUAL','comp_op',1,'p_comp_op','sintactico.py',109),
  ('comp_op -> LESS','comp_op',1,'p_comp_op','sintactico.py',110),
  ('comp_op -> LESS_EQUAL','comp_op',1,'p_comp_op','sintactico.py',111),
  ('comp_op -> GREATER','comp_op',1,'p_comp_op','sintactico.py',112),
  ('comp_op -> GREATER_EQUAL','comp_op',1,'p_comp_op','sintactico.py',113),
  ('values -> value','values',1,'p_values','sintactico.py',118),
  ('values -> value COMMA values','values',3,'p_values','sintactico.py',119),
  ('value -> IDENTIFIER','value',1,'p_value','sintactico.py',123),
  ('value -> number','value',1,'p_value','sintactico.py',124),
  ('value -> string','value',1,'p_value','sintactico.py',125),
  ('value -> list','value',1,'p_value','sintactico.py',126),
  ('number -> INTEGER','number',1,'p_number','sintactico.py',130),
  ('number -> DOUBLE','number',1,'p_number','sintactico.py',131),
  ('string -> STRING','string',1,'p_string','sintactico.py',135),
  ('boolean -> TRUE','boolean',1,'p_boolean','sintactico.py',139),
  ('boolean -> FALSE','boolean',1,'p_boolean','sintactico.py',140),
  ('list -> LSQUARE RSQUARE','list',2,'p_list','sintactico.py',144),
  ('list -> LSQUARE values RSQUARE','list',3,'p_list','sintactico.py',145),
  ('function -> type IDENTIFIER LPAREN parameters RPAREN LBRACE lines RBRACE','function',8,'p_function','sintactico.py',151),
  ('lines -> line LINE_BREAK lines','lines',3,'p_lines','sintactico.py',155),
  ('lines -> line lines','lines',2,'p_lines','sintactico.py',156),
  ('lines -> line','lines',1,'p_lines','sintactico.py',157),
  ('lines -> <empty>','lines',0,'p_lines','sintactico.py',158),
  ('line -> print','line',1,'p_line','sintactico.py',163),
  ('line -> assignment','line',1,'p_line','sintactico.py',164),
  ('line -> function','line',1,'p_line','sintactico.py',165),
  ('line -> if_statement','line',1,'p_line','sintactico.py',166),
  ('parameters -> VOID','parameters',1,'p_parameters','sintactico.py',171),
  ('parameters -> parameter','parameters',1,'p_parameters','sintactico.py',172),
  ('parameters -> parameter COMMA parameters','parameters',3,'p_parameters','sintactico.py',173),
  ('parameters -> <empty>','parameters',0,'p_parameters','sintactico.py',174),
  ('parameter -> type IDENTIFIER','parameter',2,'p_parameter','sintactico.py',179),
  ('parameter -> IDENTIFIER','parameter',1,'p_parameter','sintactico.py',180),
  ('map -> MAP_TYPE LESS type COMMA type GREATER','map',6,'p_map','sintactico.py',184),
  ('map -> MAP_TYPE LESS type COMMA type GREATER LSQUARE values RSQUARE','map',9,'p_map','sintactico.py',185),
  ('map -> MAP_TYPE LESS type COMMA type GREATER LSQUARE RSQUARE','map',8,'p_map','sintactico.py',186),
  ('set -> SET_TYPE LESS type GREATER','set',4,'p_set','sintactico.py',191),
  ('set -> SET_TYPE LESS type GREATER LSQUARE values RSQUARE','set',7,'p_set','sintactico.py',192),
  ('set -> SET_TYPE LESS type GREATER LSQUARE RSQUARE','set',6,'p_set','sintactico.py',193),
  ('queue -> QUEUE_TYPE LESS type GREATER','queue',4,'p_queue','sintactico.py',197),
  ('queue -> QUEUE_TYPE LESS type GREATER LSQUARE values RSQUARE','queue',7,'p_queue','sintactico.py',198),
  ('queue -> QUEUE_TYPE LESS type GREATER LSQUARE RSQUARE','queue',6,'p_queue','sintactico.py',199),
  ('while_statement -> WHILE LPAREN logic RPAREN LBRACE lines RBRACE','while_statement',7,'p_while_statement','sintactico.py',203),
  ('for_statement -> FOR LPAREN assignment SEMICOLON logic SEMICOLON assignment RPAREN LBRACE lines RBRACE','for_statement',11,'p_for_statement','sintactico.py',209),
]
