
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND BOOLEAN DO ELIF ELSE EQUAL FALSE FCONST FLOAT FOR ICONST ID IF INT LEQT MEQT NEQUAL OR SCONST STRING TRUE WHILE\n    block : stmt ';' block\n        | stmt ';'\n    \n    block : loop block\n        | cond block\n        | loop\n        | cond\n    \n    stmt : ID '=' expr\n        | expr\n        | decl\n    \n    expr : strexpr\n        | numexpr\n        | boolexpr\n    \n    strexpr : strexpr '+' strexpr\n    \n    strexpr : SCONST\n        | ID\n    \n    numexpr : number\n        | numexpr '+' numexpr\n        | numexpr '-' numexpr\n        | numexpr '*' numexpr\n        | numexpr '/' numexpr\n        | numexpr '^' numexpr\n    \n    number : ICONST\n        | FCONST\n        | ID\n    \n    boolexpr : boolval\n        | boolcomp\n        | boolexpr AND boolexpr\n        | boolexpr OR boolexpr\n        | '(' boolexpr AND boolexpr ')'\n        | '(' boolexpr OR boolexpr ')'\n    \n    boolval : ID\n        | TRUE\n        | FALSE\n    \n    boolcomp : number EQUAL number\n        | number NEQUAL number\n        | number '>' number\n        | number '<' number\n        | number LEQT number\n        | number MEQT number\n        | strexpr EQUAL strexpr\n        | strexpr NEQUAL strexpr\n    \n    decl : numdecl\n        | strdecl\n        | booldecl\n    \n    numdecl : INT ID\n        | FLOAT ID\n        | INT ID '=' numexpr\n        | FLOAT ID '=' numexpr\n    \n    strdecl : STRING ID\n        | STRING ID '=' strexpr\n    \n    booldecl : BOOLEAN ID\n        | BOOLEAN ID '=' boolexpr\n    \n    cond : IF boolblock braceb\n        | IF boolblock braceb ELSE braceb\n        | IF boolblock braceb condelif ELSE braceb\n    \n    condelif : ELIF boolblock braceb\n        | ELIF boolblock braceb condelif\n    \n    boolblock : '(' boolexpr ')'\n    \n    braceb : '{' block '}'\n    \n    loop : forctrl\n        | whilectrl\n        | dowhilectrl\n    \n    forctrl : FOR forcond braceb\n    \n    forcond : '(' stmt ';' stmt ';' stmt ')'\n    \n    whilectrl : WHILE boolblock braceb\n    \n    dowhilectrl : DO braceb WHILE boolblock ';'\n    "
    
_lr_action_items = {'ID':([0,3,4,8,9,10,25,26,27,28,29,34,37,39,40,41,42,43,44,45,46,47,48,49,51,54,55,56,57,58,59,60,72,87,89,98,99,100,101,102,103,108,110,117,121,124,126,],[5,5,5,-60,-61,-62,62,65,66,67,68,5,70,62,75,75,75,80,80,80,80,80,62,62,5,5,80,80,80,80,80,80,-53,-63,-65,62,62,80,80,75,62,5,-59,-54,-66,-55,5,]),'IF':([0,3,4,8,9,10,34,54,72,87,89,110,117,121,124,],[11,11,11,-60,-61,-62,11,11,-53,-63,-65,-59,-54,-66,-55,]),'FOR':([0,3,4,8,9,10,34,54,72,87,89,110,117,121,124,],[18,18,18,-60,-61,-62,18,18,-53,-63,-65,-59,-54,-66,-55,]),'WHILE':([0,3,4,8,9,10,34,53,54,72,87,89,110,117,121,124,],[19,19,19,-60,-61,-62,19,90,19,-53,-63,-65,-59,-54,-66,-55,]),'DO':([0,3,4,8,9,10,34,54,72,87,89,110,117,121,124,],[20,20,20,-60,-61,-62,20,20,-53,-63,-65,-59,-54,-66,-55,]),'SCONST':([0,3,4,8,9,10,25,34,37,39,40,41,42,48,49,51,54,72,87,89,98,99,102,103,108,110,117,121,124,126,],[21,21,21,-60,-61,-62,21,21,21,21,21,21,21,21,21,21,21,-53,-63,-65,21,21,21,21,21,-59,-54,-66,-55,21,]),'(':([0,3,4,8,9,10,11,18,19,25,34,37,39,48,49,51,54,72,87,89,90,98,99,103,106,108,110,117,121,124,126,],[25,25,25,-60,-61,-62,39,51,39,25,25,25,25,25,25,25,25,-53,-63,-65,39,25,25,25,39,25,-59,-54,-66,-55,25,]),'INT':([0,3,4,8,9,10,34,51,54,72,87,89,108,110,117,121,124,126,],[26,26,26,-60,-61,-62,26,26,26,-53,-63,-65,26,-59,-54,-66,-55,26,]),'FLOAT':([0,3,4,8,9,10,34,51,54,72,87,89,108,110,117,121,124,126,],[27,27,27,-60,-61,-62,27,27,27,-53,-63,-65,27,-59,-54,-66,-55,27,]),'STRING':([0,3,4,8,9,10,34,51,54,72,87,89,108,110,117,121,124,126,],[28,28,28,-60,-61,-62,28,28,28,-53,-63,-65,28,-59,-54,-66,-55,28,]),'BOOLEAN':([0,3,4,8,9,10,34,51,54,72,87,89,108,110,117,121,124,126,],[29,29,29,-60,-61,-62,29,29,29,-53,-63,-65,29,-59,-54,-66,-55,29,]),'ICONST':([0,3,4,8,9,10,25,34,37,39,43,44,45,46,47,48,49,51,54,55,56,57,58,59,60,72,87,89,98,99,100,101,103,108,110,117,121,124,126,],[30,30,30,-60,-61,-62,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-53,-63,-65,30,30,30,30,30,30,-59,-54,-66,-55,30,]),'FCONST':([0,3,4,8,9,10,25,34,37,39,43,44,45,46,47,48,49,51,54,55,56,57,58,59,60,72,87,89,98,99,100,101,103,108,110,117,121,124,126,],[31,31,31,-60,-61,-62,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-53,-63,-65,31,31,31,31,31,31,-59,-54,-66,-55,31,]),'TRUE':([0,3,4,8,9,10,25,34,37,39,48,49,51,54,72,87,89,98,99,103,108,110,117,121,124,126,],[32,32,32,-60,-61,-62,32,32,32,32,32,32,32,32,-53,-63,-65,32,32,32,32,-59,-54,-66,-55,32,]),'FALSE':([0,3,4,8,9,10,25,34,37,39,48,49,51,54,72,87,89,98,99,103,108,110,117,121,124,126,],[33,33,33,-60,-61,-62,33,33,33,33,33,33,33,33,-53,-63,-65,33,33,33,33,-59,-54,-66,-55,33,]),'$end':([1,3,4,8,9,10,34,35,36,69,72,87,89,110,117,121,124,],[0,-5,-6,-60,-61,-62,-2,-3,-4,-1,-53,-63,-65,-59,-54,-66,-55,]),';':([2,5,6,7,12,13,14,15,16,17,21,22,23,24,30,31,32,33,62,65,66,67,68,70,71,74,75,76,77,78,79,80,81,82,83,84,85,86,88,92,93,94,95,96,97,107,109,113,114,115,116,120,122,123,],[34,-15,-8,-9,-10,-11,-12,-42,-43,-44,-14,-16,-25,-26,-22,-23,-32,-33,-31,-45,-46,-49,-51,-15,-7,-13,-15,-40,-41,-17,-16,-24,-18,-19,-20,-21,-27,-28,108,-34,-35,-36,-37,-38,-39,-58,121,-47,-48,-50,-52,126,-29,-30,]),'}':([3,4,8,9,10,34,35,36,69,72,87,89,91,110,117,121,124,],[-5,-6,-60,-61,-62,-2,-3,-4,-1,-53,-63,-65,110,-59,-54,-66,-55,]),'=':([5,65,66,67,68,],[37,100,101,102,103,]),'+':([5,12,13,21,22,30,31,62,64,70,74,75,76,77,78,79,80,81,82,83,84,113,114,115,],[-15,40,43,-14,-16,-22,-23,-15,40,-15,40,-15,40,40,43,-16,-24,43,43,43,43,43,43,40,]),'EQUAL':([5,12,21,22,30,31,62,63,64,70,74,75,],[-15,41,-14,55,-22,-23,-15,55,41,-15,-13,-15,]),'NEQUAL':([5,12,21,22,30,31,62,63,64,70,74,75,],[-15,42,-14,56,-22,-23,-15,56,42,-15,-13,-15,]),')':([5,6,7,12,13,14,15,16,17,21,22,23,24,30,31,32,33,62,65,66,67,68,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,92,93,94,95,96,97,111,112,113,114,115,116,122,123,128,],[-15,-8,-9,-10,-11,-12,-42,-43,-44,-14,-16,-25,-26,-22,-23,-32,-33,-31,-45,-46,-49,-51,-15,-7,107,-13,-15,-40,-41,-17,-16,-24,-18,-19,-20,-21,-27,-28,-34,-35,-36,-37,-38,-39,122,123,-47,-48,-50,-52,-29,-30,129,]),'>':([5,22,30,31,62,63,70,],[-24,57,-22,-23,-24,57,-24,]),'<':([5,22,30,31,62,63,70,],[-24,58,-22,-23,-24,58,-24,]),'LEQT':([5,22,30,31,62,63,70,],[-24,59,-22,-23,-24,59,-24,]),'MEQT':([5,22,30,31,62,63,70,],[-24,60,-22,-23,-24,60,-24,]),'-':([5,13,22,30,31,70,78,79,80,81,82,83,84,113,114,],[-24,44,-16,-22,-23,-24,44,-16,-24,44,44,44,44,44,44,]),'*':([5,13,22,30,31,70,78,79,80,81,82,83,84,113,114,],[-24,45,-16,-22,-23,-24,45,-16,-24,45,45,45,45,45,45,]),'/':([5,13,22,30,31,70,78,79,80,81,82,83,84,113,114,],[-24,46,-16,-22,-23,-24,46,-16,-24,46,46,46,46,46,46,]),'^':([5,13,22,30,31,70,78,79,80,81,82,83,84,113,114,],[-24,47,-16,-22,-23,-24,47,-16,-24,47,47,47,47,47,47,]),'AND':([5,14,21,23,24,30,31,32,33,61,62,70,73,74,75,76,77,80,85,86,92,93,94,95,96,97,111,112,116,122,123,],[-31,48,-14,-25,-26,-22,-23,-32,-33,98,-31,-31,48,-13,-15,-40,-41,-24,48,48,-34,-35,-36,-37,-38,-39,48,48,48,-29,-30,]),'OR':([5,14,21,23,24,30,31,32,33,61,62,70,73,74,75,76,77,80,85,86,92,93,94,95,96,97,111,112,116,122,123,],[-31,49,-14,-25,-26,-22,-23,-32,-33,99,-31,-31,49,-13,-15,-40,-41,-24,49,49,-34,-35,-36,-37,-38,-39,49,49,49,-29,-30,]),'{':([20,38,50,52,104,107,118,119,129,],[54,54,54,54,54,-58,54,54,-64,]),'ELSE':([72,105,110,125,127,],[104,118,-59,-56,-57,]),'ELIF':([72,110,125,],[106,-59,106,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'block':([0,3,4,34,54,],[1,35,36,69,91,]),'stmt':([0,3,4,34,51,54,108,126,],[2,2,2,2,88,2,120,128,]),'loop':([0,3,4,34,54,],[3,3,3,3,3,]),'cond':([0,3,4,34,54,],[4,4,4,4,4,]),'expr':([0,3,4,34,37,51,54,108,126,],[6,6,6,6,71,6,6,6,6,]),'decl':([0,3,4,34,51,54,108,126,],[7,7,7,7,7,7,7,7,]),'forctrl':([0,3,4,34,54,],[8,8,8,8,8,]),'whilectrl':([0,3,4,34,54,],[9,9,9,9,9,]),'dowhilectrl':([0,3,4,34,54,],[10,10,10,10,10,]),'strexpr':([0,3,4,25,34,37,39,40,41,42,48,49,51,54,98,99,102,103,108,126,],[12,12,12,64,12,12,64,74,76,77,64,64,12,12,64,64,115,64,12,12,]),'numexpr':([0,3,4,34,37,43,44,45,46,47,51,54,100,101,108,126,],[13,13,13,13,13,78,81,82,83,84,13,13,113,114,13,13,]),'boolexpr':([0,3,4,25,34,37,39,48,49,51,54,98,99,103,108,126,],[14,14,14,61,14,14,73,85,86,14,14,111,112,116,14,14,]),'numdecl':([0,3,4,34,51,54,108,126,],[15,15,15,15,15,15,15,15,]),'strdecl':([0,3,4,34,51,54,108,126,],[16,16,16,16,16,16,16,16,]),'booldecl':([0,3,4,34,51,54,108,126,],[17,17,17,17,17,17,17,17,]),'number':([0,3,4,25,34,37,39,43,44,45,46,47,48,49,51,54,55,56,57,58,59,60,98,99,100,101,103,108,126,],[22,22,22,63,22,22,63,79,79,79,79,79,63,63,22,22,92,93,94,95,96,97,63,63,79,79,63,22,22,]),'boolval':([0,3,4,25,34,37,39,48,49,51,54,98,99,103,108,126,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'boolcomp':([0,3,4,25,34,37,39,48,49,51,54,98,99,103,108,126,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'boolblock':([11,19,90,106,],[38,52,109,119,]),'forcond':([18,],[50,]),'braceb':([20,38,50,52,104,118,119,],[53,72,87,89,117,124,125,]),'condelif':([72,125,],[105,127,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> block","S'",1,None,None,None),
  ('block -> stmt ; block','block',3,'p_block','syntax.py',90),
  ('block -> stmt ;','block',2,'p_block','syntax.py',91),
  ('block -> loop block','block',2,'p_block_ctrl','syntax.py',101),
  ('block -> cond block','block',2,'p_block_ctrl','syntax.py',102),
  ('block -> loop','block',1,'p_block_ctrl','syntax.py',103),
  ('block -> cond','block',1,'p_block_ctrl','syntax.py',104),
  ('stmt -> ID = expr','stmt',3,'p_stmt','syntax.py',114),
  ('stmt -> expr','stmt',1,'p_stmt','syntax.py',115),
  ('stmt -> decl','stmt',1,'p_stmt','syntax.py',116),
  ('expr -> strexpr','expr',1,'p_expr','syntax.py',126),
  ('expr -> numexpr','expr',1,'p_expr','syntax.py',127),
  ('expr -> boolexpr','expr',1,'p_expr','syntax.py',128),
  ('strexpr -> strexpr + strexpr','strexpr',3,'p_strexpr','syntax.py',135),
  ('strexpr -> SCONST','strexpr',1,'p_strexpr_const','syntax.py',142),
  ('strexpr -> ID','strexpr',1,'p_strexpr_const','syntax.py',143),
  ('numexpr -> number','numexpr',1,'p_numexpr','syntax.py',157),
  ('numexpr -> numexpr + numexpr','numexpr',3,'p_numexpr','syntax.py',158),
  ('numexpr -> numexpr - numexpr','numexpr',3,'p_numexpr','syntax.py',159),
  ('numexpr -> numexpr * numexpr','numexpr',3,'p_numexpr','syntax.py',160),
  ('numexpr -> numexpr / numexpr','numexpr',3,'p_numexpr','syntax.py',161),
  ('numexpr -> numexpr ^ numexpr','numexpr',3,'p_numexpr','syntax.py',162),
  ('number -> ICONST','number',1,'p_number','syntax.py',172),
  ('number -> FCONST','number',1,'p_number','syntax.py',173),
  ('number -> ID','number',1,'p_number','syntax.py',174),
  ('boolexpr -> boolval','boolexpr',1,'p_boolexpr','syntax.py',181),
  ('boolexpr -> boolcomp','boolexpr',1,'p_boolexpr','syntax.py',182),
  ('boolexpr -> boolexpr AND boolexpr','boolexpr',3,'p_boolexpr','syntax.py',183),
  ('boolexpr -> boolexpr OR boolexpr','boolexpr',3,'p_boolexpr','syntax.py',184),
  ('boolexpr -> ( boolexpr AND boolexpr )','boolexpr',5,'p_boolexpr','syntax.py',185),
  ('boolexpr -> ( boolexpr OR boolexpr )','boolexpr',5,'p_boolexpr','syntax.py',186),
  ('boolval -> ID','boolval',1,'p_boolval','syntax.py',198),
  ('boolval -> TRUE','boolval',1,'p_boolval','syntax.py',199),
  ('boolval -> FALSE','boolval',1,'p_boolval','syntax.py',200),
  ('boolcomp -> number EQUAL number','boolcomp',3,'p_boolcomp','syntax.py',207),
  ('boolcomp -> number NEQUAL number','boolcomp',3,'p_boolcomp','syntax.py',208),
  ('boolcomp -> number > number','boolcomp',3,'p_boolcomp','syntax.py',209),
  ('boolcomp -> number < number','boolcomp',3,'p_boolcomp','syntax.py',210),
  ('boolcomp -> number LEQT number','boolcomp',3,'p_boolcomp','syntax.py',211),
  ('boolcomp -> number MEQT number','boolcomp',3,'p_boolcomp','syntax.py',212),
  ('boolcomp -> strexpr EQUAL strexpr','boolcomp',3,'p_boolcomp','syntax.py',213),
  ('boolcomp -> strexpr NEQUAL strexpr','boolcomp',3,'p_boolcomp','syntax.py',214),
  ('decl -> numdecl','decl',1,'p_decl','syntax.py',221),
  ('decl -> strdecl','decl',1,'p_decl','syntax.py',222),
  ('decl -> booldecl','decl',1,'p_decl','syntax.py',223),
  ('numdecl -> INT ID','numdecl',2,'p_numdecl','syntax.py',230),
  ('numdecl -> FLOAT ID','numdecl',2,'p_numdecl','syntax.py',231),
  ('numdecl -> INT ID = numexpr','numdecl',4,'p_numdecl','syntax.py',232),
  ('numdecl -> FLOAT ID = numexpr','numdecl',4,'p_numdecl','syntax.py',233),
  ('strdecl -> STRING ID','strdecl',2,'p_strdecl','syntax.py',244),
  ('strdecl -> STRING ID = strexpr','strdecl',4,'p_strdecl','syntax.py',245),
  ('booldecl -> BOOLEAN ID','booldecl',2,'p_booldecl','syntax.py',256),
  ('booldecl -> BOOLEAN ID = boolexpr','booldecl',4,'p_booldecl','syntax.py',257),
  ('cond -> IF boolblock braceb','cond',3,'p_cond','syntax.py',268),
  ('cond -> IF boolblock braceb ELSE braceb','cond',5,'p_cond','syntax.py',269),
  ('cond -> IF boolblock braceb condelif ELSE braceb','cond',6,'p_cond','syntax.py',270),
  ('condelif -> ELIF boolblock braceb','condelif',3,'p_condelif','syntax.py',282),
  ('condelif -> ELIF boolblock braceb condelif','condelif',4,'p_condelif','syntax.py',283),
  ('boolblock -> ( boolexpr )','boolblock',3,'p_boolblock','syntax.py',293),
  ('braceb -> { block }','braceb',3,'p_braceb','syntax.py',300),
  ('loop -> forctrl','loop',1,'p_loop','syntax.py',307),
  ('loop -> whilectrl','loop',1,'p_loop','syntax.py',308),
  ('loop -> dowhilectrl','loop',1,'p_loop','syntax.py',309),
  ('forctrl -> FOR forcond braceb','forctrl',3,'p_forctrl','syntax.py',316),
  ('forcond -> ( stmt ; stmt ; stmt )','forcond',7,'p_forcond','syntax.py',330),
  ('whilectrl -> WHILE boolblock braceb','whilectrl',3,'p_whilectrl','syntax.py',337),
  ('dowhilectrl -> DO braceb WHILE boolblock ;','dowhilectrl',5,'p_dowhilectrl','syntax.py',344),
]
