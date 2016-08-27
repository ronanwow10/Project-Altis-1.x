from SpecImports import *
from toontown.toonbase import ToontownGlobals
import random
CogParent = 10000
GuardCogMidParent = 10070
GuardCogFrontParent = 10071
BattleCellId = 0
GuardMidCellId = 1
GuardFrontCellId = 2
BattleCells = {BattleCellId: {'parentEntId': CogParent,
                'pos': Point3(0, 0, 0)},
 GuardMidCellId: {'parentEntId': GuardCogMidParent,
                'pos': Point3(0, 0, 0)},
 GuardFrontCellId: {'parentEntId': GuardCogFrontParent,
                'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 1,
  'level': 13,
  'battleCell': BattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([11, 12]),
  'battleCell': BattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([11, 12]),
  'battleCell': BattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([11, 12]),
  'battleCell': BattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
  {'parentEntId': GuardCogMidParent,
  'boss': 0,
  'level': random.choice([10, 11, 12]),
  'battleCell': GuardMidCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
  {'parentEntId': GuardCogMidParent,
  'boss': 0,
  'level': random.choice([10, 11, 12]),
  'battleCell': GuardMidCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
  {'parentEntId': GuardCogMidParent,
  'boss': 0,
  'level': random.choice([10, 11, 12]),
  'battleCell': GuardMidCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
  {'parentEntId': GuardCogMidParent,
  'boss': 0,
  'level': random.choice([10, 11, 12]),
  'battleCell': GuardMidCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
  {'parentEntId': GuardCogFrontParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': GuardFrontCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
  {'parentEntId': GuardCogFrontParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': GuardFrontCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
  {'parentEntId': GuardCogFrontParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': GuardFrontCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
  {'parentEntId': GuardCogFrontParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': GuardFrontCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1}]
ReserveCogData = []
