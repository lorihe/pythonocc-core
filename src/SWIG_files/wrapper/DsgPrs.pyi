from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *


class DsgPrs_ArrowSide(IntEnum):
	DsgPrs_AS_NONE: int = ...
	DsgPrs_AS_FIRSTAR: int = ...
	DsgPrs_AS_LASTAR: int = ...
	DsgPrs_AS_BOTHAR: int = ...
	DsgPrs_AS_FIRSTPT: int = ...
	DsgPrs_AS_LASTPT: int = ...
	DsgPrs_AS_BOTHPT: int = ...
	DsgPrs_AS_FIRSTAR_LASTPT: int = ...
	DsgPrs_AS_FIRSTPT_LASTAR: int = ...
DsgPrs_AS_NONE = DsgPrs_ArrowSide.DsgPrs_AS_NONE
DsgPrs_AS_FIRSTAR = DsgPrs_ArrowSide.DsgPrs_AS_FIRSTAR
DsgPrs_AS_LASTAR = DsgPrs_ArrowSide.DsgPrs_AS_LASTAR
DsgPrs_AS_BOTHAR = DsgPrs_ArrowSide.DsgPrs_AS_BOTHAR
DsgPrs_AS_FIRSTPT = DsgPrs_ArrowSide.DsgPrs_AS_FIRSTPT
DsgPrs_AS_LASTPT = DsgPrs_ArrowSide.DsgPrs_AS_LASTPT
DsgPrs_AS_BOTHPT = DsgPrs_ArrowSide.DsgPrs_AS_BOTHPT
DsgPrs_AS_FIRSTAR_LASTPT = DsgPrs_ArrowSide.DsgPrs_AS_FIRSTAR_LASTPT
DsgPrs_AS_FIRSTPT_LASTAR = DsgPrs_ArrowSide.DsgPrs_AS_FIRSTPT_LASTAR

#classnotwrapped
class DsgPrs_EllipseRadiusPresentation:
	pass

#classnotwrapped
class DsgPrs_XYZPlanePresentation:
	pass

#classnotwrapped
class DsgPrs_ConcentricPresentation:
	pass

#classnotwrapped
class DsgPrs_AnglePresentation:
	pass

#classnotwrapped
class DsgPrs_ShadedPlanePresentation:
	pass

#classnotwrapped
class DsgPrs_RadiusPresentation:
	pass

#classnotwrapped
class DsgPrs_TangentPresentation:
	pass

#classnotwrapped
class DsgPrs_SymbPresentation:
	pass

#classnotwrapped
class DsgPrs_FilletRadiusPresentation:
	pass

#classnotwrapped
class DsgPrs_SymmetricPresentation:
	pass

#classnotwrapped
class DsgPrs_ShapeDirPresentation:
	pass

#classnotwrapped
class DsgPrs_FixPresentation:
	pass

#classnotwrapped
class DsgPrs_IdenticPresentation:
	pass

#classnotwrapped
class DsgPrs_MidPointPresentation:
	pass

#classnotwrapped
class DsgPrs_EqualRadiusPresentation:
	pass

#classnotwrapped
class DsgPrs_LengthPresentation:
	pass

#classnotwrapped
class DsgPrs_EqualDistancePresentation:
	pass

#classnotwrapped
class DsgPrs_DatumPrs:
	pass

#classnotwrapped
class DsgPrs_DiameterPresentation:
	pass

#classnotwrapped
class DsgPrs_ParalPresentation:
	pass

#classnotwrapped
class DsgPrs_OffsetPresentation:
	pass

#classnotwrapped
class DsgPrs_XYZAxisPresentation:
	pass

#classnotwrapped
class DsgPrs_Chamf2dPresentation:
	pass

#classnotwrapped
class DsgPrs_PerpenPresentation:
	pass

#classnotwrapped
class DsgPrs:
	pass
