from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColgp import *
from OCC.Core.Adaptor3d import *
from OCC.Core.Geom2d import *
from OCC.Core.gp import *
from OCC.Core.Adaptor2d import *
from OCC.Core.GeomAbs import *
from OCC.Core.TColStd import *
from OCC.Core.AppParCurves import *
from OCC.Core.math import *
from OCC.Core.Geom import *
from OCC.Core.GeomAdaptor import *


class ProjLib:
	@staticmethod
	def IsAnaSurf(self, theAS: Adaptor3d_HSurface) -> bool: ...
	@staticmethod
	def MakePCurveOfType(self, PC: ProjLib_ProjectedCurve, aC: Geom2d_Curve) -> None: ...
	@staticmethod
	def Project(self, Pl: gp_Pln, P: gp_Pnt) -> gp_Pnt2d: ...
	@staticmethod
	def Project(self, Pl: gp_Pln, L: gp_Lin) -> gp_Lin2d: ...
	@staticmethod
	def Project(self, Pl: gp_Pln, C: gp_Circ) -> gp_Circ2d: ...
	@staticmethod
	def Project(self, Pl: gp_Pln, E: gp_Elips) -> gp_Elips2d: ...
	@staticmethod
	def Project(self, Pl: gp_Pln, P: gp_Parab) -> gp_Parab2d: ...
	@staticmethod
	def Project(self, Pl: gp_Pln, H: gp_Hypr) -> gp_Hypr2d: ...
	@staticmethod
	def Project(self, Cy: gp_Cylinder, P: gp_Pnt) -> gp_Pnt2d: ...
	@staticmethod
	def Project(self, Cy: gp_Cylinder, L: gp_Lin) -> gp_Lin2d: ...
	@staticmethod
	def Project(self, Cy: gp_Cylinder, Ci: gp_Circ) -> gp_Lin2d: ...
	@staticmethod
	def Project(self, Co: gp_Cone, P: gp_Pnt) -> gp_Pnt2d: ...
	@staticmethod
	def Project(self, Co: gp_Cone, L: gp_Lin) -> gp_Lin2d: ...
	@staticmethod
	def Project(self, Co: gp_Cone, Ci: gp_Circ) -> gp_Lin2d: ...
	@staticmethod
	def Project(self, Sp: gp_Sphere, P: gp_Pnt) -> gp_Pnt2d: ...
	@staticmethod
	def Project(self, Sp: gp_Sphere, Ci: gp_Circ) -> gp_Lin2d: ...
	@staticmethod
	def Project(self, To: gp_Torus, P: gp_Pnt) -> gp_Pnt2d: ...
	@staticmethod
	def Project(self, To: gp_Torus, Ci: gp_Circ) -> gp_Lin2d: ...

class ProjLib_CompProjectedCurve(Adaptor2d_Curve2d):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: Adaptor3d_HSurface, C: Adaptor3d_HCurve, TolU: float, TolV: float) -> None: ...
	@overload
	def __init__(self, S: Adaptor3d_HSurface, C: Adaptor3d_HCurve, TolU: float, TolV: float, MaxDist: float) -> None: ...
	def Bounds(self, Index: int) -> Tuple[float, float]: ...
	def D0(self, U: float, P: gp_Pnt2d) -> None: ...
	def D1(self, U: float, P: gp_Pnt2d, V: gp_Vec2d) -> None: ...
	def D2(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
	def DN(self, U: float, N: int) -> gp_Vec2d: ...
	def FirstParameter(self) -> float: ...
	def GetCurve(self) -> Adaptor3d_HCurve: ...
	def GetSequence(self) -> ProjLib_HSequenceOfHSequenceOfPnt: ...
	def GetSurface(self) -> Adaptor3d_HSurface: ...
	def GetTolerance(self) -> Tuple[float, float]: ...
	def GetType(self) -> GeomAbs_CurveType: ...
	def Init(self) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsSinglePnt(self, Index: int, P: gp_Pnt2d) -> bool: ...
	def IsUIso(self, Index: int) -> Tuple[bool, float]: ...
	def IsVIso(self, Index: int) -> Tuple[bool, float]: ...
	def LastParameter(self) -> float: ...
	def Load(self, S: Adaptor3d_HSurface) -> None: ...
	def Load(self, C: Adaptor3d_HCurve) -> None: ...
	def MaxDistance(self, Index: int) -> float: ...
	def NbCurves(self) -> int: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def Trim(self, FirstParam: float, LastParam: float, Tol: float) -> Adaptor2d_HCurve2d: ...
	def Value(self, U: float) -> gp_Pnt2d: ...

class ProjLib_ComputeApprox:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_HCurve, S: Adaptor3d_HSurface, Tol: float) -> None: ...
	def BSpline(self) -> Geom2d_BSplineCurve: ...
	def Bezier(self) -> Geom2d_BezierCurve: ...
	def Perform(self, C: Adaptor3d_HCurve, S: Adaptor3d_HSurface) -> None: ...
	def SetBndPnt(self, theBndPnt: AppParCurves_Constraint) -> None: ...
	def SetDegree(self, theDegMin: int, theDegMax: int) -> None: ...
	def SetMaxSegments(self, theMaxSegments: int) -> None: ...
	def SetTolerance(self, theTolerance: float) -> None: ...
	def Tolerance(self) -> float: ...

class ProjLib_ComputeApproxOnPolarSurface:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_HCurve, S: Adaptor3d_HSurface, Tol: Optional[float]) -> None: ...
	@overload
	def __init__(self, InitCurve2d: Adaptor2d_HCurve2d, C: Adaptor3d_HCurve, S: Adaptor3d_HSurface, Tol: float) -> None: ...
	@overload
	def __init__(self, InitCurve2d: Adaptor2d_HCurve2d, InitCurve2dBis: Adaptor2d_HCurve2d, C: Adaptor3d_HCurve, S: Adaptor3d_HSurface, Tol: float) -> None: ...
	def BSpline(self) -> Geom2d_BSplineCurve: ...
	def BuildInitialCurve2d(self, Curve: Adaptor3d_HCurve, S: Adaptor3d_HSurface) -> Adaptor2d_HCurve2d: ...
	def Curve2d(self) -> Geom2d_Curve: ...
	def IsDone(self) -> bool: ...
	def Perform(self, C: Adaptor3d_HCurve, S: Adaptor3d_HSurface) -> None: ...
	def Perform(self, InitCurve2d: Adaptor2d_HCurve2d, C: Adaptor3d_HCurve, S: Adaptor3d_HSurface) -> Geom2d_BSplineCurve: ...
	def ProjectUsingInitialCurve2d(self, Curve: Adaptor3d_HCurve, S: Adaptor3d_HSurface, InitCurve2d: Adaptor2d_HCurve2d) -> Geom2d_BSplineCurve: ...
	def SetBndPnt(self, theBndPnt: AppParCurves_Constraint) -> None: ...
	def SetDegree(self, theDegMin: int, theDegMax: int) -> None: ...
	def SetMaxDist(self, theMaxDist: float) -> None: ...
	def SetMaxSegments(self, theMaxSegments: int) -> None: ...
	def SetTolerance(self, theTolerance: float) -> None: ...
	def Tolerance(self) -> float: ...

class ProjLib_HCompProjectedCurve(Adaptor2d_HCurve2d):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: ProjLib_CompProjectedCurve) -> None: ...
	def ChangeCurve2d(self) -> ProjLib_CompProjectedCurve: ...
	def Curve2d(self) -> Adaptor2d_Curve2d: ...
	def Set(self, C: ProjLib_CompProjectedCurve) -> None: ...

class ProjLib_HProjectedCurve(Adaptor2d_HCurve2d):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: ProjLib_ProjectedCurve) -> None: ...
	def ChangeCurve2d(self) -> ProjLib_ProjectedCurve: ...
	def Curve2d(self) -> Adaptor2d_Curve2d: ...
	def Set(self, C: ProjLib_ProjectedCurve) -> None: ...

class ProjLib_PrjFunc(math_FunctionSetWithDerivatives):
	def __init__(self, C: Adaptor3d_CurvePtr, FixVal: float, S: Adaptor3d_SurfacePtr, Fix: int) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def NbEquations(self) -> int: ...
	def NbVariables(self) -> int: ...
	def Solution(self) -> gp_Pnt2d: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class ProjLib_PrjResolve:
	def __init__(self, C: Adaptor3d_Curve, S: Adaptor3d_Surface, Fix: int) -> None: ...
	def IsDone(self) -> bool: ...
	def Perform(self, t: float, U: float, V: float, Tol: gp_Pnt2d, Inf: gp_Pnt2d, Sup: gp_Pnt2d, FTol: Optional[float], StrictInside: Optional[bool]) -> None: ...
	def Solution(self) -> gp_Pnt2d: ...

class ProjLib_ProjectOnPlane(Adaptor3d_Curve):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Pl: gp_Ax3) -> None: ...
	@overload
	def __init__(self, Pl: gp_Ax3, D: gp_Dir) -> None: ...
	def BSpline(self) -> Geom_BSplineCurve: ...
	def Bezier(self) -> Geom_BezierCurve: ...
	def Circle(self) -> gp_Circ: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def D0(self, U: float, P: gp_Pnt) -> None: ...
	def D1(self, U: float, P: gp_Pnt, V: gp_Vec) -> None: ...
	def D2(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
	def D3(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
	def DN(self, U: float, N: int) -> gp_Vec: ...
	def Degree(self) -> int: ...
	def Ellipse(self) -> gp_Elips: ...
	def FirstParameter(self) -> float: ...
	def GetCurve(self) -> Adaptor3d_HCurve: ...
	def GetDirection(self) -> gp_Dir: ...
	def GetPlane(self) -> gp_Ax3: ...
	def GetResult(self) -> GeomAdaptor_HCurve: ...
	def GetType(self) -> GeomAbs_CurveType: ...
	def Hyperbola(self) -> gp_Hypr: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsClosed(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def IsRational(self) -> bool: ...
	def LastParameter(self) -> float: ...
	def Line(self) -> gp_Lin: ...
	def Load(self, C: Adaptor3d_HCurve, Tolerance: float, KeepParametrization: Optional[bool]) -> None: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbKnots(self) -> int: ...
	def NbPoles(self) -> int: ...
	def Parabola(self) -> gp_Parab: ...
	def Period(self) -> float: ...
	def Resolution(self, R3d: float) -> float: ...
	def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HCurve: ...
	def Value(self, U: float) -> gp_Pnt: ...

class ProjLib_ProjectOnSurface:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: Adaptor3d_HSurface) -> None: ...
	def BSpline(self) -> Geom_BSplineCurve: ...
	def IsDone(self) -> bool: ...

class ProjLib_ProjectedCurve(Adaptor2d_Curve2d):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: Adaptor3d_HSurface) -> None: ...
	@overload
	def __init__(self, S: Adaptor3d_HSurface, C: Adaptor3d_HCurve) -> None: ...
	@overload
	def __init__(self, S: Adaptor3d_HSurface, C: Adaptor3d_HCurve, Tol: float) -> None: ...
	def BSpline(self) -> Geom2d_BSplineCurve: ...
	def Bezier(self) -> Geom2d_BezierCurve: ...
	def Circle(self) -> gp_Circ2d: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def D0(self, U: float, P: gp_Pnt2d) -> None: ...
	def D1(self, U: float, P: gp_Pnt2d, V: gp_Vec2d) -> None: ...
	def D2(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
	def D3(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, V3: gp_Vec2d) -> None: ...
	def DN(self, U: float, N: int) -> gp_Vec2d: ...
	def Degree(self) -> int: ...
	def Ellipse(self) -> gp_Elips2d: ...
	def FirstParameter(self) -> float: ...
	def GetCurve(self) -> Adaptor3d_HCurve: ...
	def GetSurface(self) -> Adaptor3d_HSurface: ...
	def GetTolerance(self) -> float: ...
	def GetType(self) -> GeomAbs_CurveType: ...
	def Hyperbola(self) -> gp_Hypr2d: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsClosed(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def IsRational(self) -> bool: ...
	def LastParameter(self) -> float: ...
	def Line(self) -> gp_Lin2d: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbKnots(self) -> int: ...
	def NbPoles(self) -> int: ...
	def Parabola(self) -> gp_Parab2d: ...
	def Perform(self, C: Adaptor3d_HCurve) -> None: ...
	def Period(self) -> float: ...
	def Resolution(self, R3d: float) -> float: ...
	def SetBndPnt(self, theBndPnt: AppParCurves_Constraint) -> None: ...
	def SetDegree(self, theDegMin: int, theDegMax: int) -> None: ...
	def SetMaxDist(self, theMaxDist: float) -> None: ...
	def SetMaxSegments(self, theMaxSegments: int) -> None: ...
	def Trim(self, First: float, Last: float, Tol: float) -> Adaptor2d_HCurve2d: ...
	def Value(self, U: float) -> gp_Pnt2d: ...

class ProjLib_Projector:
	def __init__(self) -> None: ...
	def BSpline(self) -> Geom2d_BSplineCurve: ...
	def Bezier(self) -> Geom2d_BezierCurve: ...
	def Circle(self) -> gp_Circ2d: ...
	def Done(self) -> None: ...
	def Ellipse(self) -> gp_Elips2d: ...
	def GetType(self) -> GeomAbs_CurveType: ...
	def Hyperbola(self) -> gp_Hypr2d: ...
	def IsDone(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def Line(self) -> gp_Lin2d: ...
	def Parabola(self) -> gp_Parab2d: ...
	def Project(self, L: gp_Lin) -> None: ...
	def Project(self, C: gp_Circ) -> None: ...
	def Project(self, E: gp_Elips) -> None: ...
	def Project(self, P: gp_Parab) -> None: ...
	def Project(self, H: gp_Hypr) -> None: ...
	def SetBSpline(self, C: Geom2d_BSplineCurve) -> None: ...
	def SetBezier(self, C: Geom2d_BezierCurve) -> None: ...
	def SetPeriodic(self) -> None: ...
	def SetType(self, Type: GeomAbs_CurveType) -> None: ...
	def UFrame(self, CFirst: float, CLast: float, UFirst: float, Period: float) -> None: ...
	def VFrame(self, CFirst: float, CLast: float, VFirst: float, Period: float) -> None: ...

class ProjLib_Cone(ProjLib_Projector):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Co: gp_Cone) -> None: ...
	@overload
	def __init__(self, Co: gp_Cone, L: gp_Lin) -> None: ...
	@overload
	def __init__(self, Co: gp_Cone, C: gp_Circ) -> None: ...
	def Init(self, Co: gp_Cone) -> None: ...
	def Project(self, L: gp_Lin) -> None: ...
	def Project(self, C: gp_Circ) -> None: ...
	def Project(self, E: gp_Elips) -> None: ...
	def Project(self, P: gp_Parab) -> None: ...
	def Project(self, H: gp_Hypr) -> None: ...

class ProjLib_Cylinder(ProjLib_Projector):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Cyl: gp_Cylinder) -> None: ...
	@overload
	def __init__(self, Cyl: gp_Cylinder, L: gp_Lin) -> None: ...
	@overload
	def __init__(self, Cyl: gp_Cylinder, C: gp_Circ) -> None: ...
	@overload
	def __init__(self, Cyl: gp_Cylinder, E: gp_Elips) -> None: ...
	def Init(self, Cyl: gp_Cylinder) -> None: ...
	def Project(self, L: gp_Lin) -> None: ...
	def Project(self, C: gp_Circ) -> None: ...
	def Project(self, E: gp_Elips) -> None: ...
	def Project(self, P: gp_Parab) -> None: ...
	def Project(self, H: gp_Hypr) -> None: ...

class ProjLib_Plane(ProjLib_Projector):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Pl: gp_Pln) -> None: ...
	@overload
	def __init__(self, Pl: gp_Pln, L: gp_Lin) -> None: ...
	@overload
	def __init__(self, Pl: gp_Pln, C: gp_Circ) -> None: ...
	@overload
	def __init__(self, Pl: gp_Pln, E: gp_Elips) -> None: ...
	@overload
	def __init__(self, Pl: gp_Pln, P: gp_Parab) -> None: ...
	@overload
	def __init__(self, Pl: gp_Pln, H: gp_Hypr) -> None: ...
	def Init(self, Pl: gp_Pln) -> None: ...
	def Project(self, L: gp_Lin) -> None: ...
	def Project(self, C: gp_Circ) -> None: ...
	def Project(self, E: gp_Elips) -> None: ...
	def Project(self, P: gp_Parab) -> None: ...
	def Project(self, H: gp_Hypr) -> None: ...

class ProjLib_Sphere(ProjLib_Projector):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Sp: gp_Sphere) -> None: ...
	@overload
	def __init__(self, Sp: gp_Sphere, C: gp_Circ) -> None: ...
	def Init(self, Sp: gp_Sphere) -> None: ...
	def Project(self, L: gp_Lin) -> None: ...
	def Project(self, C: gp_Circ) -> None: ...
	def Project(self, E: gp_Elips) -> None: ...
	def Project(self, P: gp_Parab) -> None: ...
	def Project(self, H: gp_Hypr) -> None: ...
	def SetInBounds(self, U: float) -> None: ...

class ProjLib_Torus(ProjLib_Projector):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, To: gp_Torus) -> None: ...
	@overload
	def __init__(self, To: gp_Torus, C: gp_Circ) -> None: ...
	def Init(self, To: gp_Torus) -> None: ...
	def Project(self, L: gp_Lin) -> None: ...
	def Project(self, C: gp_Circ) -> None: ...
	def Project(self, E: gp_Elips) -> None: ...
	def Project(self, P: gp_Parab) -> None: ...
	def Project(self, H: gp_Hypr) -> None: ...
