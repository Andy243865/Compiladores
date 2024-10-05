
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BOOL BOOL_VALUE COMMA COMMENT DIVIDE DO ELSE EQUALS FI FLOAT FLOAT_NUMBER GREATER GREATEREQUAL IDENTIFIER IF INT LBRACE LESS LESSEQUAL LPAREN MAIN MINUS MULTILINE_COMMENT NOTEQUALS NUMBER OR PLUS RBRACE RPAREN SEMICOLON THEN TIMES UNTIL WHILE WRITEmain : MAIN LBRACE declarations statements RBRACEdeclarations : declarations declaration\n                    | emptydeclaration : INT var_list SEMICOLON\n                   | FLOAT var_list SEMICOLON\n                   | BOOL var_list SEMICOLONvar_list : var_list COMMA IDENTIFIER\n                | IDENTIFIERstatements : statements statement\n                  | emptystatement : assignment\n                 | if_statement\n                 | write_statement\n                 | do_statement\n                 | while_statementassignment : IDENTIFIER ASSIGN expression SEMICOLONif_statement : IF LPAREN condition RPAREN THEN LBRACE statements RBRACE ELSE LBRACE statements RBRACE FI\n                    | IF LPAREN condition RPAREN THEN LBRACE statements RBRACE FIwrite_statement : WRITE expression SEMICOLONdo_statement : DO LBRACE statements RBRACE WHILE LPAREN condition RPAREN SEMICOLONwhile_statement : WHILE LPAREN condition RPAREN LBRACE statements RBRACEexpression : expression PLUS term\n                  | expression MINUS term\n                  | termterm : term TIMES factor\n            | term DIVIDE factor\n            | factorfactor : LPAREN expression RPAREN\n              | NUMBER\n              | FLOAT_NUMBER\n              | IDENTIFIERcondition : expression EQUALS expression\n                 | expression NOTEQUALS expression\n                 | expression LESS expression\n                 | expression LESSEQUAL expression\n                 | expression GREATER expression\n                 | expression GREATEREQUAL expression\n                 | expression AND expression\n                 | expression OR expressionempty :expression : expression PLUS empty\n                  | expression MINUS empty'
    
_lr_action_items = {'MAIN':([0,],[2,]),'$end':([1,12,],[0,-1,]),'LBRACE':([2,22,73,74,93,],[3,37,84,85,96,]),'INT':([3,4,5,7,39,41,42,],[-40,9,-3,-2,-4,-5,-6,]),'FLOAT':([3,4,5,7,39,41,42,],[-40,10,-3,-2,-4,-5,-6,]),'BOOL':([3,4,5,7,39,41,42,],[-40,11,-3,-2,-4,-5,-6,]),'RBRACE':([3,4,5,6,7,8,13,14,15,16,17,18,37,39,41,42,46,52,55,84,85,87,88,90,94,95,96,97,99,],[-40,-40,-3,12,-2,-10,-9,-11,-12,-13,-14,-15,-40,-4,-5,-6,-19,72,-16,-40,-40,90,91,-21,-18,-20,-40,98,-17,]),'IDENTIFIER':([3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,21,28,29,33,37,38,39,40,41,42,46,47,48,49,50,52,55,57,58,59,60,61,62,63,64,84,85,86,87,88,90,94,95,96,97,99,],[-40,-40,-3,19,-2,-10,25,25,25,-9,-11,-12,-13,-14,-15,36,36,36,36,-40,36,-4,54,-5,-6,-19,36,36,36,36,19,-16,36,36,36,36,36,36,36,36,-40,-40,36,19,19,-21,-18,-20,-40,19,-17,]),'IF':([3,4,5,6,7,8,13,14,15,16,17,18,37,39,41,42,46,52,55,84,85,87,88,90,94,95,96,97,99,],[-40,-40,-3,20,-2,-10,-9,-11,-12,-13,-14,-15,-40,-4,-5,-6,-19,20,-16,-40,-40,20,20,-21,-18,-20,-40,20,-17,]),'WRITE':([3,4,5,6,7,8,13,14,15,16,17,18,37,39,41,42,46,52,55,84,85,87,88,90,94,95,96,97,99,],[-40,-40,-3,21,-2,-10,-9,-11,-12,-13,-14,-15,-40,-4,-5,-6,-19,21,-16,-40,-40,21,21,-21,-18,-20,-40,21,-17,]),'DO':([3,4,5,6,7,8,13,14,15,16,17,18,37,39,41,42,46,52,55,84,85,87,88,90,94,95,96,97,99,],[-40,-40,-3,22,-2,-10,-9,-11,-12,-13,-14,-15,-40,-4,-5,-6,-19,22,-16,-40,-40,22,22,-21,-18,-20,-40,22,-17,]),'WHILE':([3,4,5,6,7,8,13,14,15,16,17,18,37,39,41,42,46,52,55,72,84,85,87,88,90,94,95,96,97,99,],[-40,-40,-3,23,-2,-10,-9,-11,-12,-13,-14,-15,-40,-4,-5,-6,-19,23,-16,83,-40,-40,23,23,-21,-18,-20,-40,23,-17,]),'ASSIGN':([19,],[28,]),'LPAREN':([20,21,23,28,29,33,38,47,48,49,50,57,58,59,60,61,62,63,64,83,86,],[29,33,38,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,86,33,]),'NUMBER':([21,28,29,33,38,47,48,49,50,57,58,59,60,61,62,63,64,86,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'FLOAT_NUMBER':([21,28,29,33,38,47,48,49,50,57,58,59,60,61,62,63,64,86,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'SEMICOLON':([24,25,26,27,30,31,32,34,35,36,43,47,48,54,65,66,67,68,69,70,71,92,],[39,-8,41,42,46,-24,-27,-29,-30,-31,55,-40,-40,-7,-22,-41,-23,-42,-25,-26,-28,95,]),'COMMA':([24,25,26,27,54,],[40,-8,40,40,-7,]),'PLUS':([30,31,32,34,35,36,43,45,47,48,51,65,66,67,68,69,70,71,75,76,77,78,79,80,81,82,],[47,-24,-27,-29,-30,-31,47,47,-40,-40,47,-22,-41,-23,-42,-25,-26,-28,47,47,47,47,47,47,47,47,]),'MINUS':([30,31,32,34,35,36,43,45,47,48,51,65,66,67,68,69,70,71,75,76,77,78,79,80,81,82,],[48,-24,-27,-29,-30,-31,48,48,-40,-40,48,-22,-41,-23,-42,-25,-26,-28,48,48,48,48,48,48,48,48,]),'EQUALS':([31,32,34,35,36,45,47,48,65,66,67,68,69,70,71,],[-24,-27,-29,-30,-31,57,-40,-40,-22,-41,-23,-42,-25,-26,-28,]),'NOTEQUALS':([31,32,34,35,36,45,47,48,65,66,67,68,69,70,71,],[-24,-27,-29,-30,-31,58,-40,-40,-22,-41,-23,-42,-25,-26,-28,]),'LESS':([31,32,34,35,36,45,47,48,65,66,67,68,69,70,71,],[-24,-27,-29,-30,-31,59,-40,-40,-22,-41,-23,-42,-25,-26,-28,]),'LESSEQUAL':([31,32,34,35,36,45,47,48,65,66,67,68,69,70,71,],[-24,-27,-29,-30,-31,60,-40,-40,-22,-41,-23,-42,-25,-26,-28,]),'GREATER':([31,32,34,35,36,45,47,48,65,66,67,68,69,70,71,],[-24,-27,-29,-30,-31,61,-40,-40,-22,-41,-23,-42,-25,-26,-28,]),'GREATEREQUAL':([31,32,34,35,36,45,47,48,65,66,67,68,69,70,71,],[-24,-27,-29,-30,-31,62,-40,-40,-22,-41,-23,-42,-25,-26,-28,]),'AND':([31,32,34,35,36,45,47,48,65,66,67,68,69,70,71,],[-24,-27,-29,-30,-31,63,-40,-40,-22,-41,-23,-42,-25,-26,-28,]),'OR':([31,32,34,35,36,45,47,48,65,66,67,68,69,70,71,],[-24,-27,-29,-30,-31,64,-40,-40,-22,-41,-23,-42,-25,-26,-28,]),'RPAREN':([31,32,34,35,36,44,47,48,51,53,65,66,67,68,69,70,71,75,76,77,78,79,80,81,82,89,],[-24,-27,-29,-30,-31,56,-40,-40,71,73,-22,-41,-23,-42,-25,-26,-28,-32,-33,-34,-35,-36,-37,-38,-39,92,]),'TIMES':([31,32,34,35,36,65,67,69,70,71,],[49,-27,-29,-30,-31,49,49,-25,-26,-28,]),'DIVIDE':([31,32,34,35,36,65,67,69,70,71,],[50,-27,-29,-30,-31,50,50,-25,-26,-28,]),'THEN':([56,],[74,]),'ELSE':([91,],[93,]),'FI':([91,98,],[94,99,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'main':([0,],[1,]),'declarations':([3,],[4,]),'empty':([3,4,37,47,48,84,85,96,],[5,8,8,66,68,8,8,8,]),'statements':([4,37,84,85,96,],[6,52,87,88,97,]),'declaration':([4,],[7,]),'statement':([6,52,87,88,97,],[13,13,13,13,13,]),'assignment':([6,52,87,88,97,],[14,14,14,14,14,]),'if_statement':([6,52,87,88,97,],[15,15,15,15,15,]),'write_statement':([6,52,87,88,97,],[16,16,16,16,16,]),'do_statement':([6,52,87,88,97,],[17,17,17,17,17,]),'while_statement':([6,52,87,88,97,],[18,18,18,18,18,]),'var_list':([9,10,11,],[24,26,27,]),'expression':([21,28,29,33,38,57,58,59,60,61,62,63,64,86,],[30,43,45,51,45,75,76,77,78,79,80,81,82,45,]),'term':([21,28,29,33,38,47,48,57,58,59,60,61,62,63,64,86,],[31,31,31,31,31,65,67,31,31,31,31,31,31,31,31,31,]),'factor':([21,28,29,33,38,47,48,49,50,57,58,59,60,61,62,63,64,86,],[32,32,32,32,32,32,32,69,70,32,32,32,32,32,32,32,32,32,]),'condition':([29,38,86,],[44,53,89,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> main","S'",1,None,None,None),
  ('main -> MAIN LBRACE declarations statements RBRACE','main',5,'p_main','compilador.py',133),
  ('declarations -> declarations declaration','declarations',2,'p_declarations','compilador.py',137),
  ('declarations -> empty','declarations',1,'p_declarations','compilador.py',138),
  ('declaration -> INT var_list SEMICOLON','declaration',3,'p_declaration','compilador.py',145),
  ('declaration -> FLOAT var_list SEMICOLON','declaration',3,'p_declaration','compilador.py',146),
  ('declaration -> BOOL var_list SEMICOLON','declaration',3,'p_declaration','compilador.py',147),
  ('var_list -> var_list COMMA IDENTIFIER','var_list',3,'p_var_list','compilador.py',151),
  ('var_list -> IDENTIFIER','var_list',1,'p_var_list','compilador.py',152),
  ('statements -> statements statement','statements',2,'p_statements','compilador.py',159),
  ('statements -> empty','statements',1,'p_statements','compilador.py',160),
  ('statement -> assignment','statement',1,'p_statement','compilador.py',167),
  ('statement -> if_statement','statement',1,'p_statement','compilador.py',168),
  ('statement -> write_statement','statement',1,'p_statement','compilador.py',169),
  ('statement -> do_statement','statement',1,'p_statement','compilador.py',170),
  ('statement -> while_statement','statement',1,'p_statement','compilador.py',171),
  ('assignment -> IDENTIFIER ASSIGN expression SEMICOLON','assignment',4,'p_assignment','compilador.py',175),
  ('if_statement -> IF LPAREN condition RPAREN THEN LBRACE statements RBRACE ELSE LBRACE statements RBRACE FI','if_statement',13,'p_if_statement','compilador.py',191),
  ('if_statement -> IF LPAREN condition RPAREN THEN LBRACE statements RBRACE FI','if_statement',9,'p_if_statement','compilador.py',192),
  ('write_statement -> WRITE expression SEMICOLON','write_statement',3,'p_write_statement','compilador.py',199),
  ('do_statement -> DO LBRACE statements RBRACE WHILE LPAREN condition RPAREN SEMICOLON','do_statement',9,'p_do_statement','compilador.py',203),
  ('while_statement -> WHILE LPAREN condition RPAREN LBRACE statements RBRACE','while_statement',7,'p_while_statement','compilador.py',209),
  ('expression -> expression PLUS term','expression',3,'p_expression','compilador.py',213),
  ('expression -> expression MINUS term','expression',3,'p_expression','compilador.py',214),
  ('expression -> term','expression',1,'p_expression','compilador.py',215),
  ('term -> term TIMES factor','term',3,'p_term','compilador.py',222),
  ('term -> term DIVIDE factor','term',3,'p_term','compilador.py',223),
  ('term -> factor','term',1,'p_term','compilador.py',224),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','compilador.py',231),
  ('factor -> NUMBER','factor',1,'p_factor','compilador.py',232),
  ('factor -> FLOAT_NUMBER','factor',1,'p_factor','compilador.py',233),
  ('factor -> IDENTIFIER','factor',1,'p_factor','compilador.py',234),
  ('condition -> expression EQUALS expression','condition',3,'p_condition','compilador.py',241),
  ('condition -> expression NOTEQUALS expression','condition',3,'p_condition','compilador.py',242),
  ('condition -> expression LESS expression','condition',3,'p_condition','compilador.py',243),
  ('condition -> expression LESSEQUAL expression','condition',3,'p_condition','compilador.py',244),
  ('condition -> expression GREATER expression','condition',3,'p_condition','compilador.py',245),
  ('condition -> expression GREATEREQUAL expression','condition',3,'p_condition','compilador.py',246),
  ('condition -> expression AND expression','condition',3,'p_condition','compilador.py',247),
  ('condition -> expression OR expression','condition',3,'p_condition','compilador.py',248),
  ('empty -> <empty>','empty',0,'p_empty','compilador.py',254),
  ('expression -> expression PLUS empty','expression',3,'p_expression_incomplete','compilador.py',268),
  ('expression -> expression MINUS empty','expression',3,'p_expression_incomplete','compilador.py',269),
]
