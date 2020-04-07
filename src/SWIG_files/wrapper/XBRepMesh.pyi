from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.BRepMesh import *


class XBRepMesh:
	@staticmethod
	def Discret(self, theShape: TopoDS_Shape, theDeflection: float, theAngle: float, theAlgo: BRepMesh_DiscretRoot) -> int: ...
