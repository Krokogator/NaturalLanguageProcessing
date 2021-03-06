
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BYE OPEN RUN CLOSE WEBPHRASE DOCPHRASE PROGPHRASE WEBSITE EXECUTABLE TXTPATH VOICEoperation : docopen TXTPATHdocopen : OPEN\n               | OPEN DOCPHRASEoperation : webopen WEBSITEwebopen : OPEN\n               | OPEN WEBPHRASEoperation : progopen EXECUTABLEprogopen : OPEN\n    | OPEN PROGPHRASE\n    | RUN\n    | RUN PROGPHRASEoperation : progclose EXECUTABLEprogclose : CLOSE\n               | CLOSE PROGPHRASEoperation : RUN VOICEoperation : CLOSE VOICEoperation : BYE\n    | CLOSE'
    
_lr_action_items = {'OPEN':([0,],[1,]),'$end':([2,6,9,13,15,16,17,18,20,],[-17,0,-18,-12,-15,-4,-1,-7,-16,]),'DOCPHRASE':([1,],[12,]),'VOICE':([4,9,],[15,20,]),'WEBPHRASE':([1,],[11,]),'RUN':([0,],[4,]),'PROGPHRASE':([1,4,9,],[10,14,19,]),'CLOSE':([0,],[9,]),'TXTPATH':([1,7,12,],[-2,17,-3,]),'WEBSITE':([1,5,11,],[-5,16,-6,]),'BYE':([0,],[2,]),'EXECUTABLE':([1,3,4,8,9,10,14,19,],[-8,13,-10,18,-13,-9,-11,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'webopen':([0,],[5,]),'docopen':([0,],[7,]),'operation':([0,],[6,]),'progclose':([0,],[3,]),'progopen':([0,],[8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> operation","S'",1,None,None,None),
  ('operation -> docopen TXTPATH','operation',2,'p_operation_open_txt','Konsola.py',98),
  ('docopen -> OPEN','docopen',1,'p_docopen','Konsola.py',103),
  ('docopen -> OPEN DOCPHRASE','docopen',2,'p_docopen','Konsola.py',104),
  ('operation -> webopen WEBSITE','operation',2,'p_operation_open_website','Konsola.py',107),
  ('webopen -> OPEN','webopen',1,'p_webopen','Konsola.py',113),
  ('webopen -> OPEN WEBPHRASE','webopen',2,'p_webopen','Konsola.py',114),
  ('operation -> progopen EXECUTABLE','operation',2,'p_operation_open_exe','Konsola.py',117),
  ('progopen -> OPEN','progopen',1,'p_progopen','Konsola.py',126),
  ('progopen -> OPEN PROGPHRASE','progopen',2,'p_progopen','Konsola.py',127),
  ('progopen -> RUN','progopen',1,'p_progopen','Konsola.py',128),
  ('progopen -> RUN PROGPHRASE','progopen',2,'p_progopen','Konsola.py',129),
  ('operation -> progclose EXECUTABLE','operation',2,'p_operation_close_exe','Konsola.py',132),
  ('progclose -> CLOSE','progclose',1,'p_progclose','Konsola.py',141),
  ('progclose -> CLOSE PROGPHRASE','progclose',2,'p_progclose','Konsola.py',142),
  ('operation -> RUN VOICE','operation',2,'p_operation_voiceOn','Konsola.py',145),
  ('operation -> CLOSE VOICE','operation',2,'p_operation_voiceOff','Konsola.py',151),
  ('operation -> BYE','operation',1,'p_operation_exit','Konsola.py',157),
  ('operation -> CLOSE','operation',1,'p_operation_exit','Konsola.py',158),
]
