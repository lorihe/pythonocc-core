from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Adaptor3d import *
from OCC.Core.Adaptor2d import *
from OCC.Core.math import *
from OCC.Core.GeomAbs import *
from OCC.Core.gp import *


class GCPnts_DeflectionType(IntEnum):
	GCPnts_Linear: int = ...
	GCPnts_Circular: int = ...
	GCPnts_Curved: int = ...
	GCPnts_DefComposite: int = ...
GCPnts_Linear = GCPnts_DeflectionType.GCPnts_Linear
GCPnts_Circular = GCPnts_DeflectionType.GCPnts_Circular
GCPnts_Curved = GCPnts_DeflectionType.GCPnts_Curved
GCPnts_DefComposite = GCPnts_DeflectionType.GCPnts_DefComposite

class GCPnts_AbscissaType(IntEnum):
	GCPnts_LengthParametrized: int = ...
	GCPnts_Parametrized: int = ...
	GCPnts_AbsComposite: int = ...
GCPnts_LengthParametrized = GCPnts_AbscissaType.GCPnts_LengthParametrized
GCPnts_Parametrized = GCPnts_AbscissaType.GCPnts_Parametrized
GCPnts_AbsComposite = GCPnts_AbscissaType.GCPnts_AbsComposite

class GCPnts_AbscissaPoint:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_Curve, Abscissa: float, U0: float) -> None: ...
	@overload
	def __init__(self, Tol: float, C: Adaptor3d_Curve, Abscissa: float, U0: float) -> None: ...
	@overload
	def __init__(self, Tol: float, C: Adaptor2d_Curve2d, Abscissa: float, U0: float) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_Curve2d, Abscissa: float, U0: float) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_Curve, Abscissa: float, U0: float, Ui: float) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_Curve2d, Abscissa: float, U0: float, Ui: float) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_Curve, Abscissa: float, U0: float, Ui: float, Tol: float) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_Curve2d, Abscissa: float, U0: float, Ui: float, Tol: float) -> None: ...
	def IsDone(self) -> bool: ...
	@staticmethod
	def Length(self, C: Adaptor3d_Curve) -> float: ...
	@staticmethod
	def Length(self, C: Adaptor2d_Curve2d) -> float: ...
	@staticmethod
	def Length(self, C: Adaptor3d_Curve, Tol: float) -> float: ...
	@staticmethod
	def Length(self, C: Adaptor2d_Curve2d, Tol: float) -> float: ...
	@staticmethod
	def Length(self, C: Adaptor3d_Curve, U1: float, U2: float) -> float: ...
	@staticmethod
	def Length(self, C: Adaptor2d_Curve2d, U1: float, U2: float) -> float: ...
	@staticmethod
	def Length(self, C: Adaptor3d_Curve, U1: float, U2: float, Tol: float) -> float: ...
	@staticmethod
	def Length(self, C: Adaptor2d_Curve2d, U1: float, U2: float, Tol: float) -> float: ...
	def Parameter(self) -> float: ...

class GCPnts_DistFunction2dMV(math_MultipleVarFunction):
	def __init__(self, theCurvLinDist: GCPnts_DistFunction2d) -> None: ...
	def NbVariables(self) -> int: ...
	def Value(self, X: math_Vector) -> Tuple[bool, float]: ...

class GCPnts_DistFunctionMV(math_MultipleVarFunction):
	def __init__(self, theCurvLinDist: GCPnts_DistFunction) -> None: ...
	def NbVariables(self) -> int: ...
	def Value(self, X: math_Vector) -> Tuple[bool, float]: ...

class GCPnts_QuasiUniformAbscissa:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_Curve, NbPoints: int) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_Curve, NbPoints: int, U1: float, U2: float) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_Curve2d, NbPoints: int) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_Curve2d, NbPoints: int, U1: float, U2: float) -> None: ...
	def Initialize(self, C: Adaptor3d_Curve, NbPoints: int) -> None: ...
	def Initialize(self, C: Adaptor3d_Curve, NbPoints: int, U1: float, U2: float) -> None: ...
	def Initialize(self, C: Adaptor2d_Curve2d, NbPoints: int) -> None: ...
	def Initialize(self, C: Adaptor2d_Curve2d, NbPoints: int, U1: float, U2: float) -> None: ...
	def IsDone(self) -> bool: ...
	def NbPoints(self) -> int: ...
	def Parameter(self, Index: int) -> float: ...

class GCPnts_QuasiUniformDeflection:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_Curve, Deflection: float, Continuity: Optional[GeomAbs_Shape]) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_Curve2d, Deflection: float, Continuity: Optional[GeomAbs_Shape]) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_Curve, Deflection: float, U1: float, U2: float, Continuity: Optional[GeomAbs_Shape]) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_Curve2d, Deflection: float, U1: float, U2: float, Continuity: Optional[GeomAbs_Shape]) -> None: ...
	def Deflection(self) -> float: ...
	def Initialize(self, C: Adaptor3d_Curve, Deflection: float, Continuity: Optional[GeomAbs_Shape]) -> None: ...
	def Initialize(self, C: Adaptor2d_Curve2d, Deflection: float, Continuity: Optional[GeomAbs_Shape]) -> None: ...
	def Initialize(self, C: Adaptor3d_Curve, Deflection: float, U1: float, U2: float, Continuity: Optional[GeomAbs_Shape]) -> None: ...
	def Initialize(self, C: Adaptor2d_Curve2d, Deflection: float, U1: float, U2: float, Continuity: Optional[GeomAbs_Shape]) -> None: ...
	def IsDone(self) -> bool: ...
	def NbPoints(self) -> int: ...
	def Parameter(self, Index: int) -> float: ...
	def Value(self, Index: int) -> gp_Pnt: ...

class GCPnts_TangentialDeflection:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_Curve, AngularDeflection: float, CurvatureDeflection: float, MinimumOfPoints: Optional[int], UTol: Optional[float], theMinLen: Optional[float]) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_Curve, FirstParameter: float, LastParameter: float, AngularDeflection: float, CurvatureDeflection: float, MinimumOfPoints: Optional[int], UTol: Optional[float], theMinLen: Optional[float]) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_Curve2d, AngularDeflection: float, CurvatureDeflection: float, MinimumOfPoints: Optional[int], UTol: Optional[float], theMinLen: Optional[float]) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_Curve2d, FirstParameter: float, LastParameter: float, AngularDeflection: float, CurvatureDeflection: float, MinimumOfPoints: Optional[int], UTol: Optional[float], theMinLen: Optional[float]) -> None: ...
	def AddPoint(self, thePnt: gp_Pnt, theParam: float, theIsReplace: Optional[bool]) -> int: ...
	@staticmethod
	def ArcAngularStep(self, theRadius: float, theLinearDeflection: float, theAngularDeflection: float, theMinLength: float) -> float: ...
	def Initialize(self, C: Adaptor3d_Curve, AngularDeflection: float, CurvatureDeflection: float, MinimumOfPoints: Optional[int], UTol: Optional[float], theMinLen: Optional[float]) -> None: ...
	def Initialize(self, C: Adaptor3d_Curve, FirstParameter: float, LastParameter: float, AngularDeflection: float, CurvatureDeflection: float, MinimumOfPoints: Optional[int], UTol: Optional[float], theMinLen: Optional[float]) -> None: ...
	def Initialize(self, C: Adaptor2d_Curve2d, AngularDeflection: float, CurvatureDeflection: float, MinimumOfPoints: Optional[int], UTol: Optional[float], theMinLen: Optional[float]) -> None: ...
	def Initialize(self, C: Adaptor2d_Curve2d, FirstParameter: float, LastParameter: float, AngularDeflection: float, CurvatureDeflection: float, MinimumOfPoints: Optional[int], UTol: Optional[float], theMinLen: Optional[float]) -> None: ...
	def NbPoints(self) -> int: ...
	def Parameter(self, I: int) -> float: ...
	def Value(self, I: int) -> gp_Pnt: ...

class GCPnts_UniformAbscissa:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_Curve, Abscissa: float, Toler: Optional[float]) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_Curve, Abscissa: float, U1: float, U2: float, Toler: Optional[float]) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_Curve, NbPoints: int, Toler: Optional[float]) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_Curve, NbPoints: int, U1: float, U2: float, Toler: Optional[float]) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_Curve2d, Abscissa: float, Toler: Optional[float]) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_Curve2d, Abscissa: float, U1: float, U2: float, Toler: Optional[float]) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_Curve2d, NbPoints: int, Toler: Optional[float]) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_Curve2d, NbPoints: int, U1: float, U2: float, Toler: Optional[float]) -> None: ...
	def Abscissa(self) -> float: ...
	def Initialize(self, C: Adaptor3d_Curve, Abscissa: float, Toler: Optional[float]) -> None: ...
	def Initialize(self, C: Adaptor3d_Curve, Abscissa: float, U1: float, U2: float, Toler: Optional[float]) -> None: ...
	def Initialize(self, C: Adaptor3d_Curve, NbPoints: int, Toler: Optional[float]) -> None: ...
	def Initialize(self, C: Adaptor3d_Curve, NbPoints: int, U1: float, U2: float, Toler: Optional[float]) -> None: ...
	def Initialize(self, C: Adaptor2d_Curve2d, Abscissa: float, Toler: Optional[float]) -> None: ...
	def Initialize(self, C: Adaptor2d_Curve2d, Abscissa: float, U1: float, U2: float, Toler: Optional[float]) -> None: ...
	def Initialize(self, C: Adaptor2d_Curve2d, NbPoints: int, Toler: Optional[float]) -> None: ...
	def Initialize(self, C: Adaptor2d_Curve2d, NbPoints: int, U1: float, U2: float, Toler: Optional[float]) -> None: ...
	def IsDone(self) -> bool: ...
	def NbPoints(self) -> int: ...
	def Parameter(self, Index: int) -> float: ...

class GCPnts_UniformDeflection:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_Curve, Deflection: float, WithControl: Optional[bool]) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_Curve2d, Deflection: float, WithControl: Optional[bool]) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_Curve, Deflection: float, U1: float, U2: float, WithControl: Optional[bool]) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_Curve2d, Deflection: float, U1: float, U2: float, WithControl: Optional[bool]) -> None: ...
	def Deflection(self) -> float: ...
	def Initialize(self, C: Adaptor3d_Curve, Deflection: float, WithControl: Optional[bool]) -> None: ...
	def Initialize(self, C: Adaptor2d_Curve2d, Deflection: float, WithControl: Optional[bool]) -> None: ...
	def Initialize(self, C: Adaptor3d_Curve, Deflection: float, U1: float, U2: float, WithControl: Optional[bool]) -> None: ...
	def Initialize(self, C: Adaptor2d_Curve2d, Deflection: float, U1: float, U2: float, WithControl: Optional[bool]) -> None: ...
	def IsDone(self) -> bool: ...
	def NbPoints(self) -> int: ...
	def Parameter(self, Index: int) -> float: ...
	def Value(self, Index: int) -> gp_Pnt: ...

#classnotwrapped
class GCPnts_DistFunction:
	pass

#classnotwrapped
class GCPnts_DistFunction2d:
	pass