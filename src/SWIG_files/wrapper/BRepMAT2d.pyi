from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.MAT import *
from OCC.Core.GeomAbs import *
from OCC.Core.Bisector import *
from OCC.Core.Geom2d import *
from OCC.Core.gp import *
from OCC.Core.TopoDS import *
from OCC.Core.TColGeom2d import *
from OCC.Core.TColStd import *


class BRepMAT2d_BisectingLocus:
	def __init__(self) -> None: ...
	def BasicElt(self, IndLine: int, Index: int) -> MAT_BasicElt: ...
	def Compute(self, anExplo: BRepMAT2d_Explorer, LineIndex: Optional[int], aSide: Optional[MAT_Side], aJoinType: Optional[GeomAbs_JoinType], IsOpenResult: Optional[bool]) -> None: ...
	def GeomBis(self, anArc: MAT_Arc) -> Tuple[Bisector_Bisec, bool]: ...
	def GeomElt(self, aBasicElt: MAT_BasicElt) -> Geom2d_Geometry: ...
	def GeomElt(self, aNode: MAT_Node) -> gp_Pnt2d: ...
	def Graph(self) -> MAT_Graph: ...
	def IsDone(self) -> bool: ...
	def NumberOfContours(self) -> int: ...
	def NumberOfElts(self, IndLine: int) -> int: ...
	def NumberOfSections(self, IndLine: int, Index: int) -> int: ...

class BRepMAT2d_Explorer:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aFace: TopoDS_Face) -> None: ...
	def Clear(self) -> None: ...
	def Contour(self, IndexContour: int) -> TColGeom2d_SequenceOfCurve: ...
	def GetIsClosed(self) -> TColStd_SequenceOfBoolean: ...
	def Init(self, IndexContour: int) -> None: ...
	def IsModified(self, aShape: TopoDS_Shape) -> bool: ...
	def ModifiedShape(self, aShape: TopoDS_Shape) -> TopoDS_Shape: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def NumberOfContours(self) -> int: ...
	def NumberOfCurves(self, IndexContour: int) -> int: ...
	def Perform(self, aFace: TopoDS_Face) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...
	def Value(self) -> Geom2d_Curve: ...

class BRepMAT2d_LinkTopoBilo:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Explo: BRepMAT2d_Explorer, BiLo: BRepMAT2d_BisectingLocus) -> None: ...
	def GeneratingShape(self, aBE: MAT_BasicElt) -> TopoDS_Shape: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Perform(self, Explo: BRepMAT2d_Explorer, BiLo: BRepMAT2d_BisectingLocus) -> None: ...
	def Value(self) -> MAT_BasicElt: ...
