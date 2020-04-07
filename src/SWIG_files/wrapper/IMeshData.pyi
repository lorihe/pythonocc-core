from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.gp import *
from OCC.Core.TopAbs import *
from OCC.Core.BRepAdaptor import *


class IMeshData_Status(IntEnum):
	IMeshData_NoError: int = ...
	IMeshData_OpenWire: int = ...
	IMeshData_SelfIntersectingWire: int = ...
	IMeshData_Failure: int = ...
	IMeshData_ReMesh: int = ...
	IMeshData_UnorientedWire: int = ...
	IMeshData_TooFewPoints: int = ...
	IMeshData_Outdated: int = ...
	IMeshData_Reused: int = ...
IMeshData_NoError = IMeshData_Status.IMeshData_NoError
IMeshData_OpenWire = IMeshData_Status.IMeshData_OpenWire
IMeshData_SelfIntersectingWire = IMeshData_Status.IMeshData_SelfIntersectingWire
IMeshData_Failure = IMeshData_Status.IMeshData_Failure
IMeshData_ReMesh = IMeshData_Status.IMeshData_ReMesh
IMeshData_UnorientedWire = IMeshData_Status.IMeshData_UnorientedWire
IMeshData_TooFewPoints = IMeshData_Status.IMeshData_TooFewPoints
IMeshData_Outdated = IMeshData_Status.IMeshData_Outdated
IMeshData_Reused = IMeshData_Status.IMeshData_Reused

class IMeshData_ParametersList(Standard_Transient):
	def Clear(self, isKeepEndPoints: bool) -> None: ...
	def GetParameter(self, theIndex: int) -> float: ...
	def ParametersNb(self) -> int: ...

class IMeshData_Shape(Standard_Transient):
	def GetShape(self) -> TopoDS_Shape: ...
	def SetShape(self, theShape: TopoDS_Shape) -> None: ...

class IMeshData_StatusOwner:
	def GetStatusMask(self) -> int: ...
	def IsEqual(self, theValue: IMeshData_Status) -> bool: ...
	def IsSet(self, theValue: IMeshData_Status) -> bool: ...
	def SetStatus(self, theValue: IMeshData_Status) -> None: ...
	def UnsetStatus(self, theValue: IMeshData_Status) -> None: ...

class IMeshData_Curve(IMeshData_ParametersList):
	def AddPoint(self, thePoint: gp_Pnt, theParamOnCurve: float) -> None: ...
	def GetPoint(self, theIndex: int) -> gp_Pnt: ...
	def InsertPoint(self, thePosition: int, thePoint: gp_Pnt, theParamOnPCurve: float) -> None: ...
	def RemovePoint(self, theIndex: int) -> None: ...

class IMeshData_Model(IMeshData_Shape):
	def AddEdge(self, theEdge: TopoDS_Edge) -> False: ...
	def AddFace(self, theFace: TopoDS_Face) -> False: ...
	def EdgesNb(self) -> int: ...
	def FacesNb(self) -> int: ...
	def GetEdge(self, theIndex: int) -> False: ...
	def GetFace(self, theIndex: int) -> False: ...
	def GetMaxSize(self) -> float: ...

class IMeshData_PCurve(IMeshData_ParametersList):
	def AddPoint(self, thePoint: gp_Pnt2d, theParamOnPCurve: float) -> None: ...
	def GetFace(self) -> False: ...
	def GetIndex(self, theIndex: int) -> int: ...
	def GetOrientation(self) -> TopAbs_Orientation: ...
	def GetPoint(self, theIndex: int) -> gp_Pnt2d: ...
	def InsertPoint(self, thePosition: int, thePoint: gp_Pnt2d, theParamOnPCurve: float) -> None: ...
	def IsForward(self) -> bool: ...
	def IsInternal(self) -> bool: ...
	def RemovePoint(self, theIndex: int) -> None: ...

class IMeshData_TessellatedShape(IMeshData_Shape):
	def GetDeflection(self) -> float: ...
	def SetDeflection(self, theValue: float) -> None: ...

class IMeshData_Edge(IMeshData_TessellatedShape, IMeshData_StatusOwner):
	def Clear(self, isKeepEndPoints: bool) -> None: ...
	def GetAngularDeflection(self) -> float: ...
	def GetCurve(self) -> False: ...
	def GetDegenerated(self) -> bool: ...
	def GetEdge(self) -> TopoDS_Edge: ...
	def GetPCurve(self, theIndex: int) -> False: ...
	def GetSameParam(self) -> bool: ...
	def GetSameRange(self) -> bool: ...
	def IsFree(self) -> bool: ...
	def PCurvesNb(self) -> int: ...
	def SetAngularDeflection(self, theValue: float) -> None: ...
	def SetDegenerated(self, theValue: bool) -> None: ...
	def SetSameParam(self, theValue: bool) -> None: ...
	def SetSameRange(self, theValue: bool) -> None: ...

class IMeshData_Face(IMeshData_TessellatedShape, IMeshData_StatusOwner):
	def AddWire(self, theWire: TopoDS_Wire, theEdgeNb: Optional[int]) -> False: ...
	def GetFace(self) -> TopoDS_Face: ...
	def GetSurface(self) -> BRepAdaptor_HSurface: ...
	def GetWire(self, theIndex: int) -> False: ...
	def IsValid(self) -> bool: ...
	def WiresNb(self) -> int: ...

class IMeshData_Wire(IMeshData_TessellatedShape, IMeshData_StatusOwner):
	def EdgesNb(self) -> int: ...
	def GetEdge(self, theIndex: int) -> False: ...
	def GetEdgeOrientation(self, theIndex: int) -> TopAbs_Orientation: ...
	def GetWire(self) -> TopoDS_Wire: ...
