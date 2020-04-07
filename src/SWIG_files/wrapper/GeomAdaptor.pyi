from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Adaptor3d import *
from OCC.Core.Geom import *
from OCC.Core.gp import *
from OCC.Core.GeomAbs import *
from OCC.Core.TColStd import *


class GeomAdaptor:
	@staticmethod
	def MakeCurve(self, C: Adaptor3d_Curve) -> Geom_Curve: ...
	@staticmethod
	def MakeSurface(self, theS: Adaptor3d_Surface, theTrimFlag: Optional[bool]) -> Geom_Surface: ...

class GeomAdaptor_Curve(Adaptor3d_Curve):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Geom_Curve) -> None: ...
	@overload
	def __init__(self, C: Geom_Curve, UFirst: float, ULast: float) -> None: ...
	def BSpline(self) -> Geom_BSplineCurve: ...
	def Bezier(self) -> Geom_BezierCurve: ...
	def Circle(self) -> gp_Circ: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def Curve(self) -> Geom_Curve: ...
	def D0(self, U: float, P: gp_Pnt) -> None: ...
	def D1(self, U: float, P: gp_Pnt, V: gp_Vec) -> None: ...
	def D2(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
	def D3(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
	def DN(self, U: float, N: int) -> gp_Vec: ...
	def Degree(self) -> int: ...
	def Ellipse(self) -> gp_Elips: ...
	def FirstParameter(self) -> float: ...
	def GetType(self) -> GeomAbs_CurveType: ...
	def Hyperbola(self) -> gp_Hypr: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsClosed(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def IsRational(self) -> bool: ...
	def LastParameter(self) -> float: ...
	def Line(self) -> gp_Lin: ...
	def Load(self, C: Geom_Curve) -> None: ...
	def Load(self, C: Geom_Curve, UFirst: float, ULast: float) -> None: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbKnots(self) -> int: ...
	def NbPoles(self) -> int: ...
	def OffsetCurve(self) -> Geom_OffsetCurve: ...
	def Parabola(self) -> gp_Parab: ...
	def Period(self) -> float: ...
	def Reset(self) -> None: ...
	def Resolution(self, R3d: float) -> float: ...
	def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HCurve: ...
	def Value(self, U: float) -> gp_Pnt: ...

class GeomAdaptor_GHCurve(Adaptor3d_HCurve):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: GeomAdaptor_Curve) -> None: ...
	def ChangeCurve(self) -> GeomAdaptor_Curve: ...
	def Curve(self) -> Adaptor3d_Curve: ...
	def GetCurve(self) -> Adaptor3d_Curve: ...
	def Set(self, C: GeomAdaptor_Curve) -> None: ...

class GeomAdaptor_GHSurface(Adaptor3d_HSurface):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: GeomAdaptor_Surface) -> None: ...
	def ChangeSurface(self) -> GeomAdaptor_Surface: ...
	def Set(self, S: GeomAdaptor_Surface) -> None: ...
	def Surface(self) -> Adaptor3d_Surface: ...

class GeomAdaptor_HSurfaceOfLinearExtrusion(Adaptor3d_HSurface):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: GeomAdaptor_SurfaceOfLinearExtrusion) -> None: ...
	def ChangeSurface(self) -> GeomAdaptor_SurfaceOfLinearExtrusion: ...
	def Set(self, S: GeomAdaptor_SurfaceOfLinearExtrusion) -> None: ...
	def Surface(self) -> Adaptor3d_Surface: ...

class GeomAdaptor_HSurfaceOfRevolution(Adaptor3d_HSurface):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: GeomAdaptor_SurfaceOfRevolution) -> None: ...
	def ChangeSurface(self) -> GeomAdaptor_SurfaceOfRevolution: ...
	def Set(self, S: GeomAdaptor_SurfaceOfRevolution) -> None: ...
	def Surface(self) -> Adaptor3d_Surface: ...

class GeomAdaptor_Surface(Adaptor3d_Surface):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: Geom_Surface) -> None: ...
	@overload
	def __init__(self, S: Geom_Surface, UFirst: float, ULast: float, VFirst: float, VLast: float, TolU: Optional[float], TolV: Optional[float]) -> None: ...
	def AxeOfRevolution(self) -> gp_Ax1: ...
	def BSpline(self) -> Geom_BSplineSurface: ...
	def BasisCurve(self) -> Adaptor3d_HCurve: ...
	def BasisSurface(self) -> Adaptor3d_HSurface: ...
	def Bezier(self) -> Geom_BezierSurface: ...
	def Cone(self) -> gp_Cone: ...
	def Cylinder(self) -> gp_Cylinder: ...
	def D0(self, U: float, V: float, P: gp_Pnt) -> None: ...
	def D1(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec) -> None: ...
	def D2(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, D2UV: gp_Vec) -> None: ...
	def D3(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, D2UV: gp_Vec, D3U: gp_Vec, D3V: gp_Vec, D3UUV: gp_Vec, D3UVV: gp_Vec) -> None: ...
	def DN(self, U: float, V: float, Nu: int, Nv: int) -> gp_Vec: ...
	def Direction(self) -> gp_Dir: ...
	def FirstUParameter(self) -> float: ...
	def FirstVParameter(self) -> float: ...
	def GetType(self) -> GeomAbs_SurfaceType: ...
	def IsUClosed(self) -> bool: ...
	def IsUPeriodic(self) -> bool: ...
	def IsURational(self) -> bool: ...
	def IsVClosed(self) -> bool: ...
	def IsVPeriodic(self) -> bool: ...
	def IsVRational(self) -> bool: ...
	def LastUParameter(self) -> float: ...
	def LastVParameter(self) -> float: ...
	def Load(self, S: Geom_Surface) -> None: ...
	def Load(self, S: Geom_Surface, UFirst: float, ULast: float, VFirst: float, VLast: float, TolU: Optional[float], TolV: Optional[float]) -> None: ...
	def NbUIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbUKnots(self) -> int: ...
	def NbUPoles(self) -> int: ...
	def NbVIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbVKnots(self) -> int: ...
	def NbVPoles(self) -> int: ...
	def OffsetValue(self) -> float: ...
	def Plane(self) -> gp_Pln: ...
	def Sphere(self) -> gp_Sphere: ...
	def Surface(self) -> Geom_Surface: ...
	def Torus(self) -> gp_Torus: ...
	def UContinuity(self) -> GeomAbs_Shape: ...
	def UDegree(self) -> int: ...
	def UIntervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def UPeriod(self) -> float: ...
	def UResolution(self, R3d: float) -> float: ...
	def UTrim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HSurface: ...
	def VContinuity(self) -> GeomAbs_Shape: ...
	def VDegree(self) -> int: ...
	def VIntervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def VPeriod(self) -> float: ...
	def VResolution(self, R3d: float) -> float: ...
	def VTrim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HSurface: ...
	def Value(self, U: float, V: float) -> gp_Pnt: ...

class GeomAdaptor_HCurve(GeomAdaptor_GHCurve):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, AS: GeomAdaptor_Curve) -> None: ...
	@overload
	def __init__(self, S: Geom_Curve) -> None: ...
	@overload
	def __init__(self, S: Geom_Curve, UFirst: float, ULast: float) -> None: ...

class GeomAdaptor_HSurface(GeomAdaptor_GHSurface):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, AS: GeomAdaptor_Surface) -> None: ...
	@overload
	def __init__(self, S: Geom_Surface) -> None: ...
	@overload
	def __init__(self, S: Geom_Surface, UFirst: float, ULast: float, VFirst: float, VLast: float, TolU: Optional[float], TolV: Optional[float]) -> None: ...

class GeomAdaptor_SurfaceOfLinearExtrusion(GeomAdaptor_Surface):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_HCurve) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_HCurve, V: gp_Dir) -> None: ...
	def AxeOfRevolution(self) -> gp_Ax1: ...
	def BSpline(self) -> Geom_BSplineSurface: ...
	def BasisCurve(self) -> Adaptor3d_HCurve: ...
	def Bezier(self) -> Geom_BezierSurface: ...
	def Cone(self) -> gp_Cone: ...
	def Cylinder(self) -> gp_Cylinder: ...
	def Direction(self) -> gp_Dir: ...
	def FirstUParameter(self) -> float: ...
	def FirstVParameter(self) -> float: ...
	def GetType(self) -> GeomAbs_SurfaceType: ...
	def IsUClosed(self) -> bool: ...
	def IsUPeriodic(self) -> bool: ...
	def IsURational(self) -> bool: ...
	def IsVClosed(self) -> bool: ...
	def IsVPeriodic(self) -> bool: ...
	def IsVRational(self) -> bool: ...
	def LastUParameter(self) -> float: ...
	def LastVParameter(self) -> float: ...
	def Load(self, C: Adaptor3d_HCurve) -> None: ...
	def Load(self, V: gp_Dir) -> None: ...
	def NbUIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbUPoles(self) -> int: ...
	def NbVIntervals(self, S: GeomAbs_Shape) -> int: ...
	def Plane(self) -> gp_Pln: ...
	def Sphere(self) -> gp_Sphere: ...
	def Torus(self) -> gp_Torus: ...
	def UContinuity(self) -> GeomAbs_Shape: ...
	def UDegree(self) -> int: ...
	def UIntervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def UPeriod(self) -> float: ...
	def UResolution(self, R3d: float) -> float: ...
	def UTrim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HSurface: ...
	def VContinuity(self) -> GeomAbs_Shape: ...
	def VIntervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def VPeriod(self) -> float: ...
	def VResolution(self, R3d: float) -> float: ...
	def VTrim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HSurface: ...

class GeomAdaptor_SurfaceOfRevolution(GeomAdaptor_Surface):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_HCurve) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_HCurve, V: gp_Ax1) -> None: ...
	def AxeOfRevolution(self) -> gp_Ax1: ...
	def Axis(self) -> gp_Ax3: ...
	def BSpline(self) -> Geom_BSplineSurface: ...
	def BasisCurve(self) -> Adaptor3d_HCurve: ...
	def Bezier(self) -> Geom_BezierSurface: ...
	def Cone(self) -> gp_Cone: ...
	def Cylinder(self) -> gp_Cylinder: ...
	def FirstUParameter(self) -> float: ...
	def FirstVParameter(self) -> float: ...
	def GetType(self) -> GeomAbs_SurfaceType: ...
	def IsUClosed(self) -> bool: ...
	def IsUPeriodic(self) -> bool: ...
	def IsURational(self) -> bool: ...
	def IsVClosed(self) -> bool: ...
	def IsVPeriodic(self) -> bool: ...
	def IsVRational(self) -> bool: ...
	def LastUParameter(self) -> float: ...
	def LastVParameter(self) -> float: ...
	def Load(self, C: Adaptor3d_HCurve) -> None: ...
	def Load(self, V: gp_Ax1) -> None: ...
	def NbUIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbVIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbVKnots(self) -> int: ...
	def NbVPoles(self) -> int: ...
	def Plane(self) -> gp_Pln: ...
	def Sphere(self) -> gp_Sphere: ...
	def Torus(self) -> gp_Torus: ...
	def UContinuity(self) -> GeomAbs_Shape: ...
	def UIntervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def UPeriod(self) -> float: ...
	def UResolution(self, R3d: float) -> float: ...
	def UTrim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HSurface: ...
	def VContinuity(self) -> GeomAbs_Shape: ...
	def VDegree(self) -> int: ...
	def VIntervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def VPeriod(self) -> float: ...
	def VResolution(self, R3d: float) -> float: ...
	def VTrim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HSurface: ...
