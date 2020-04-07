from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.TColStd import *


class IntAna_ResultType(IntEnum):
	IntAna_Point: int = ...
	IntAna_Line: int = ...
	IntAna_Circle: int = ...
	IntAna_PointAndCircle: int = ...
	IntAna_Ellipse: int = ...
	IntAna_Parabola: int = ...
	IntAna_Hyperbola: int = ...
	IntAna_Empty: int = ...
	IntAna_Same: int = ...
	IntAna_NoGeometricSolution: int = ...
IntAna_Point = IntAna_ResultType.IntAna_Point
IntAna_Line = IntAna_ResultType.IntAna_Line
IntAna_Circle = IntAna_ResultType.IntAna_Circle
IntAna_PointAndCircle = IntAna_ResultType.IntAna_PointAndCircle
IntAna_Ellipse = IntAna_ResultType.IntAna_Ellipse
IntAna_Parabola = IntAna_ResultType.IntAna_Parabola
IntAna_Hyperbola = IntAna_ResultType.IntAna_Hyperbola
IntAna_Empty = IntAna_ResultType.IntAna_Empty
IntAna_Same = IntAna_ResultType.IntAna_Same
IntAna_NoGeometricSolution = IntAna_ResultType.IntAna_NoGeometricSolution

class IntAna_Curve:
	def __init__(self) -> None: ...
	def D1u(self, Theta: float, P: gp_Pnt, V: gp_Vec) -> bool: ...
	def Domain(self) -> Tuple[float, float]: ...
	def FindParameter(self, P: gp_Pnt, theParams: TColStd_ListOfReal) -> None: ...
	def IsConstant(self) -> bool: ...
	def IsFirstOpen(self) -> bool: ...
	def IsLastOpen(self) -> bool: ...
	def IsOpen(self) -> bool: ...
	def SetConeQuadValues(self, Cone: gp_Cone, Qxx: float, Qyy: float, Qzz: float, Qxy: float, Qxz: float, Qyz: float, Qx: float, Qy: float, Qz: float, Q1: float, Tol: float, DomInf: float, DomSup: float, TwoZForATheta: bool, ZIsPositive: bool) -> None: ...
	def SetCylinderQuadValues(self, Cylinder: gp_Cylinder, Qxx: float, Qyy: float, Qzz: float, Qxy: float, Qxz: float, Qyz: float, Qx: float, Qy: float, Qz: float, Q1: float, Tol: float, DomInf: float, DomSup: float, TwoZForATheta: bool, ZIsPositive: bool) -> None: ...
	def SetDomain(self, theFirst: float, theLast: float) -> None: ...
	def SetIsFirstOpen(self, Flag: bool) -> None: ...
	def SetIsLastOpen(self, Flag: bool) -> None: ...
	def Value(self, Theta: float) -> gp_Pnt: ...

class IntAna_Int3Pln:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, P1: gp_Pln, P2: gp_Pln, P3: gp_Pln) -> None: ...
	def IsDone(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def Perform(self, P1: gp_Pln, P2: gp_Pln, P3: gp_Pln) -> None: ...
	def Value(self) -> gp_Pnt: ...

class IntAna_IntConicQuad:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, L: gp_Lin, Q: IntAna_Quadric) -> None: ...
	@overload
	def __init__(self, C: gp_Circ, Q: IntAna_Quadric) -> None: ...
	@overload
	def __init__(self, E: gp_Elips, Q: IntAna_Quadric) -> None: ...
	@overload
	def __init__(self, P: gp_Parab, Q: IntAna_Quadric) -> None: ...
	@overload
	def __init__(self, H: gp_Hypr, Q: IntAna_Quadric) -> None: ...
	@overload
	def __init__(self, L: gp_Lin, P: gp_Pln, Tolang: float, Tol: Optional[float], Len: Optional[float]) -> None: ...
	@overload
	def __init__(self, C: gp_Circ, P: gp_Pln, Tolang: float, Tol: float) -> None: ...
	@overload
	def __init__(self, E: gp_Elips, P: gp_Pln, Tolang: float, Tol: float) -> None: ...
	@overload
	def __init__(self, Pb: gp_Parab, P: gp_Pln, Tolang: float) -> None: ...
	@overload
	def __init__(self, H: gp_Hypr, P: gp_Pln, Tolang: float) -> None: ...
	def IsDone(self) -> bool: ...
	def IsInQuadric(self) -> bool: ...
	def IsParallel(self) -> bool: ...
	def NbPoints(self) -> int: ...
	def ParamOnConic(self, N: int) -> float: ...
	def Perform(self, L: gp_Lin, Q: IntAna_Quadric) -> None: ...
	def Perform(self, C: gp_Circ, Q: IntAna_Quadric) -> None: ...
	def Perform(self, E: gp_Elips, Q: IntAna_Quadric) -> None: ...
	def Perform(self, P: gp_Parab, Q: IntAna_Quadric) -> None: ...
	def Perform(self, H: gp_Hypr, Q: IntAna_Quadric) -> None: ...
	def Perform(self, L: gp_Lin, P: gp_Pln, Tolang: float, Tol: Optional[float], Len: Optional[float]) -> None: ...
	def Perform(self, C: gp_Circ, P: gp_Pln, Tolang: float, Tol: float) -> None: ...
	def Perform(self, E: gp_Elips, P: gp_Pln, Tolang: float, Tol: float) -> None: ...
	def Perform(self, Pb: gp_Parab, P: gp_Pln, Tolang: float) -> None: ...
	def Perform(self, H: gp_Hypr, P: gp_Pln, Tolang: float) -> None: ...
	def Point(self, N: int) -> gp_Pnt: ...

class IntAna_IntLinTorus:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, L: gp_Lin, T: gp_Torus) -> None: ...
	def IsDone(self) -> bool: ...
	def NbPoints(self) -> int: ...
	def ParamOnLine(self, Index: int) -> float: ...
	def ParamOnTorus(self, Index: int) -> Tuple[float, float]: ...
	def Perform(self, L: gp_Lin, T: gp_Torus) -> None: ...
	def Value(self, Index: int) -> gp_Pnt: ...

class IntAna_IntQuadQuad:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: gp_Cylinder, Q: IntAna_Quadric, Tol: float) -> None: ...
	@overload
	def __init__(self, C: gp_Cone, Q: IntAna_Quadric, Tol: float) -> None: ...
	def Curve(self, N: int) -> IntAna_Curve: ...
	def HasNextCurve(self, I: int) -> bool: ...
	def HasPreviousCurve(self, I: int) -> bool: ...
	def IdenticalElements(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def NbCurve(self) -> int: ...
	def NbPnt(self) -> int: ...
	def NextCurve(self, I: int) -> Tuple[int, bool]: ...
	def Parameters(self, N: int) -> Tuple[float, float]: ...
	def Perform(self, C: gp_Cylinder, Q: IntAna_Quadric, Tol: float) -> None: ...
	def Perform(self, C: gp_Cone, Q: IntAna_Quadric, Tol: float) -> None: ...
	def Point(self, N: int) -> gp_Pnt: ...
	def PreviousCurve(self, I: int) -> Tuple[int, bool]: ...

class IntAna_QuadQuadGeo:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, P1: gp_Pln, P2: gp_Pln, TolAng: float, Tol: float) -> None: ...
	@overload
	def __init__(self, P: gp_Pln, C: gp_Cylinder, Tolang: float, Tol: float, H: Optional[float]) -> None: ...
	@overload
	def __init__(self, P: gp_Pln, S: gp_Sphere) -> None: ...
	@overload
	def __init__(self, P: gp_Pln, C: gp_Cone, Tolang: float, Tol: float) -> None: ...
	@overload
	def __init__(self, Cyl1: gp_Cylinder, Cyl2: gp_Cylinder, Tol: float) -> None: ...
	@overload
	def __init__(self, Cyl: gp_Cylinder, Sph: gp_Sphere, Tol: float) -> None: ...
	@overload
	def __init__(self, Cyl: gp_Cylinder, Con: gp_Cone, Tol: float) -> None: ...
	@overload
	def __init__(self, Sph1: gp_Sphere, Sph2: gp_Sphere, Tol: float) -> None: ...
	@overload
	def __init__(self, Sph: gp_Sphere, Con: gp_Cone, Tol: float) -> None: ...
	@overload
	def __init__(self, Con1: gp_Cone, Con2: gp_Cone, Tol: float) -> None: ...
	@overload
	def __init__(self, Pln: gp_Pln, Tor: gp_Torus, Tol: float) -> None: ...
	@overload
	def __init__(self, Cyl: gp_Cylinder, Tor: gp_Torus, Tol: float) -> None: ...
	@overload
	def __init__(self, Con: gp_Cone, Tor: gp_Torus, Tol: float) -> None: ...
	@overload
	def __init__(self, Sph: gp_Sphere, Tor: gp_Torus, Tol: float) -> None: ...
	@overload
	def __init__(self, Tor1: gp_Torus, Tor2: gp_Torus, Tol: float) -> None: ...
	def Circle(self, Num: int) -> gp_Circ: ...
	def Ellipse(self, Num: int) -> gp_Elips: ...
	def HasCommonGen(self) -> bool: ...
	def Hyperbola(self, Num: int) -> gp_Hypr: ...
	def IsDone(self) -> bool: ...
	def Line(self, Num: int) -> gp_Lin: ...
	def NbSolutions(self) -> int: ...
	def PChar(self) -> gp_Pnt: ...
	def Parabola(self, Num: int) -> gp_Parab: ...
	def Perform(self, P1: gp_Pln, P2: gp_Pln, TolAng: float, Tol: float) -> None: ...
	def Perform(self, P: gp_Pln, C: gp_Cylinder, Tolang: float, Tol: float, H: Optional[float]) -> None: ...
	def Perform(self, P: gp_Pln, S: gp_Sphere) -> None: ...
	def Perform(self, P: gp_Pln, C: gp_Cone, Tolang: float, Tol: float) -> None: ...
	def Perform(self, Cyl1: gp_Cylinder, Cyl2: gp_Cylinder, Tol: float) -> None: ...
	def Perform(self, Cyl: gp_Cylinder, Sph: gp_Sphere, Tol: float) -> None: ...
	def Perform(self, Cyl: gp_Cylinder, Con: gp_Cone, Tol: float) -> None: ...
	def Perform(self, Sph1: gp_Sphere, Sph2: gp_Sphere, Tol: float) -> None: ...
	def Perform(self, Sph: gp_Sphere, Con: gp_Cone, Tol: float) -> None: ...
	def Perform(self, Con1: gp_Cone, Con2: gp_Cone, Tol: float) -> None: ...
	def Perform(self, Pln: gp_Pln, Tor: gp_Torus, Tol: float) -> None: ...
	def Perform(self, Cyl: gp_Cylinder, Tor: gp_Torus, Tol: float) -> None: ...
	def Perform(self, Con: gp_Cone, Tor: gp_Torus, Tol: float) -> None: ...
	def Perform(self, Sph: gp_Sphere, Tor: gp_Torus, Tol: float) -> None: ...
	def Perform(self, Tor1: gp_Torus, Tor2: gp_Torus, Tol: float) -> None: ...
	def Point(self, Num: int) -> gp_Pnt: ...
	def TypeInter(self) -> IntAna_ResultType: ...

class IntAna_Quadric:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, P: gp_Pln) -> None: ...
	@overload
	def __init__(self, Sph: gp_Sphere) -> None: ...
	@overload
	def __init__(self, Cyl: gp_Cylinder) -> None: ...
	@overload
	def __init__(self, Cone: gp_Cone) -> None: ...
	def Coefficients(self) -> Tuple[float, float, float, float, float, float, float, float, float, float]: ...
	def NewCoefficients(self, Axis: gp_Ax3) -> Tuple[float, float, float, float, float, float, float, float, float, float]: ...
	def SetQuadric(self, P: gp_Pln) -> None: ...
	def SetQuadric(self, Sph: gp_Sphere) -> None: ...
	def SetQuadric(self, Con: gp_Cone) -> None: ...
	def SetQuadric(self, Cyl: gp_Cylinder) -> None: ...
	def SpecialPoints(self) -> False: ...
