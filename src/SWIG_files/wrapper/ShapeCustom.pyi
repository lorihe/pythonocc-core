from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.GeomAbs import *
from OCC.Core.Geom import *
from OCC.Core.Geom2d import *
from OCC.Core.TColgp import *
from OCC.Core.BRepTools import *
from OCC.Core.ShapeExtend import *
from OCC.Core.Message import *
from OCC.Core.gp import *
from OCC.Core.TopLoc import *


class ShapeCustom:
	@staticmethod
	def BSplineRestriction(self, S: TopoDS_Shape, Tol3d: float, Tol2d: float, MaxDegree: int, MaxNbSegment: int, Continuity3d: GeomAbs_Shape, Continuity2d: GeomAbs_Shape, Degree: bool, Rational: bool, aParameters: ShapeCustom_RestrictionParameters) -> TopoDS_Shape: ...
	@staticmethod
	def ConvertToBSpline(self, S: TopoDS_Shape, extrMode: bool, revolMode: bool, offsetMode: bool, planeMode: Optional[bool]) -> TopoDS_Shape: ...
	@staticmethod
	def ConvertToRevolution(self, S: TopoDS_Shape) -> TopoDS_Shape: ...
	@staticmethod
	def DirectFaces(self, S: TopoDS_Shape) -> TopoDS_Shape: ...
	@staticmethod
	def ScaleShape(self, S: TopoDS_Shape, scale: float) -> TopoDS_Shape: ...
	@staticmethod
	def SweptToElementary(self, S: TopoDS_Shape) -> TopoDS_Shape: ...

class ShapeCustom_Curve:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Geom_Curve) -> None: ...
	def ConvertToPeriodic(self, substitute: bool, preci: Optional[float]) -> Geom_Curve: ...
	def Init(self, C: Geom_Curve) -> None: ...

class ShapeCustom_Curve2d:
	@staticmethod
	def ConvertToLine2d(self, theCurve: Geom2d_Curve, theFirstIn: float, theLastIn: float, theTolerance: float) -> Tuple[Geom2d_Line, float, float, float]: ...
	@staticmethod
	def IsLinear(self, thePoles: TColgp_Array1OfPnt2d, theTolerance: float) -> Tuple[bool, float]: ...
	@staticmethod
	def SimplifyBSpline2d(self, theBSpline2d: Geom2d_BSplineCurve, theTolerance: float) -> bool: ...

class ShapeCustom_Modification(BRepTools_Modification):
	def MsgRegistrator(self) -> ShapeExtend_BasicMsgRegistrator: ...
	def SendMsg(self, shape: TopoDS_Shape, message: Message_Msg, gravity: Optional[Message_Gravity]) -> None: ...
	def SetMsgRegistrator(self, msgreg: ShapeExtend_BasicMsgRegistrator) -> None: ...

class ShapeCustom_RestrictionParameters(Standard_Transient):
	def __init__(self) -> None: ...
	def GetConvertBezierSurf(self) -> bool: ...
	def SetConvertBezierSurf(self, value: bool) -> None: ...
	def GetConvertConicalSurf(self) -> bool: ...
	def SetConvertConicalSurf(self, value: bool) -> None: ...
	def GetConvertCurve2d(self) -> bool: ...
	def SetConvertCurve2d(self, value: bool) -> None: ...
	def GetConvertCurve3d(self) -> bool: ...
	def SetConvertCurve3d(self, value: bool) -> None: ...
	def GetConvertCylindricalSurf(self) -> bool: ...
	def SetConvertCylindricalSurf(self, value: bool) -> None: ...
	def GetConvertExtrusionSurf(self) -> bool: ...
	def SetConvertExtrusionSurf(self, value: bool) -> None: ...
	def GetConvertOffsetCurv2d(self) -> bool: ...
	def SetConvertOffsetCurv2d(self, value: bool) -> None: ...
	def GetConvertOffsetCurv3d(self) -> bool: ...
	def SetConvertOffsetCurv3d(self, value: bool) -> None: ...
	def GetConvertOffsetSurf(self) -> bool: ...
	def SetConvertOffsetSurf(self, value: bool) -> None: ...
	def GetConvertPlane(self) -> bool: ...
	def SetConvertPlane(self, value: bool) -> None: ...
	def GetConvertRevolutionSurf(self) -> bool: ...
	def SetConvertRevolutionSurf(self, value: bool) -> None: ...
	def GetConvertSphericalSurf(self) -> bool: ...
	def SetConvertSphericalSurf(self, value: bool) -> None: ...
	def GetConvertToroidalSurf(self) -> bool: ...
	def SetConvertToroidalSurf(self, value: bool) -> None: ...
	def GetGMaxDegree(self) -> int: ...
	def SetGMaxDegree(self, value: int) -> None: ...
	def GetGMaxSeg(self) -> int: ...
	def SetGMaxSeg(self, value: int) -> None: ...
	def GetSegmentSurfaceMode(self) -> bool: ...
	def SetSegmentSurfaceMode(self, value: bool) -> None: ...

class ShapeCustom_Surface:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: Geom_Surface) -> None: ...
	def ConvertToAnalytical(self, tol: float, substitute: bool) -> Geom_Surface: ...
	def ConvertToPeriodic(self, substitute: bool, preci: Optional[float]) -> Geom_Surface: ...
	def Gap(self) -> float: ...
	def Init(self, S: Geom_Surface) -> None: ...

class ShapeCustom_TrsfModification(BRepTools_TrsfModification):
	def __init__(self, T: gp_Trsf) -> None: ...
	def NewCurve(self, E: TopoDS_Edge, C: Geom_Curve, L: TopLoc_Location) -> Tuple[bool, float]: ...
	def NewCurve2d(self, E: TopoDS_Edge, F: TopoDS_Face, NewE: TopoDS_Edge, NewF: TopoDS_Face, C: Geom2d_Curve) -> Tuple[bool, float]: ...
	def NewParameter(self, V: TopoDS_Vertex, E: TopoDS_Edge) -> Tuple[bool, float, float]: ...
	def NewPoint(self, V: TopoDS_Vertex, P: gp_Pnt) -> Tuple[bool, float]: ...
	def NewSurface(self, F: TopoDS_Face, S: Geom_Surface, L: TopLoc_Location) -> Tuple[bool, float, bool, bool]: ...

class ShapeCustom_ConvertToBSpline(ShapeCustom_Modification):
	def __init__(self) -> None: ...
	def Continuity(self, E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face, NewE: TopoDS_Edge, NewF1: TopoDS_Face, NewF2: TopoDS_Face) -> GeomAbs_Shape: ...
	def NewCurve(self, E: TopoDS_Edge, C: Geom_Curve, L: TopLoc_Location) -> Tuple[bool, float]: ...
	def NewCurve2d(self, E: TopoDS_Edge, F: TopoDS_Face, NewE: TopoDS_Edge, NewF: TopoDS_Face, C: Geom2d_Curve) -> Tuple[bool, float]: ...
	def NewParameter(self, V: TopoDS_Vertex, E: TopoDS_Edge) -> Tuple[bool, float, float]: ...
	def NewPoint(self, V: TopoDS_Vertex, P: gp_Pnt) -> Tuple[bool, float]: ...
	def NewSurface(self, F: TopoDS_Face, S: Geom_Surface, L: TopLoc_Location) -> Tuple[bool, float, bool, bool]: ...
	def SetExtrusionMode(self, extrMode: bool) -> None: ...
	def SetOffsetMode(self, offsetMode: bool) -> None: ...
	def SetPlaneMode(self, planeMode: bool) -> None: ...
	def SetRevolutionMode(self, revolMode: bool) -> None: ...

class ShapeCustom_DirectModification(ShapeCustom_Modification):
	def __init__(self) -> None: ...
	def Continuity(self, E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face, NewE: TopoDS_Edge, NewF1: TopoDS_Face, NewF2: TopoDS_Face) -> GeomAbs_Shape: ...
	def NewCurve(self, E: TopoDS_Edge, C: Geom_Curve, L: TopLoc_Location) -> Tuple[bool, float]: ...
	def NewCurve2d(self, E: TopoDS_Edge, F: TopoDS_Face, NewE: TopoDS_Edge, NewF: TopoDS_Face, C: Geom2d_Curve) -> Tuple[bool, float]: ...
	def NewParameter(self, V: TopoDS_Vertex, E: TopoDS_Edge) -> Tuple[bool, float, float]: ...
	def NewPoint(self, V: TopoDS_Vertex, P: gp_Pnt) -> Tuple[bool, float]: ...
	def NewSurface(self, F: TopoDS_Face, S: Geom_Surface, L: TopLoc_Location) -> Tuple[bool, float, bool, bool]: ...

#classnotwrapped
class ShapeCustom_BSplineRestriction:
	pass

#classnotwrapped
class ShapeCustom_SweptToElementary:
	pass

#classnotwrapped
class ShapeCustom_ConvertToRevolution:
	pass
