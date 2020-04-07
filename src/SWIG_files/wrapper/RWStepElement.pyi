from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.StepData import *
from OCC.Core.Interface import *
from OCC.Core.StepElement import *


class RWStepElement_RWAnalysisItemWithinRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepElement_AnalysisItemWithinRepresentation) -> None: ...
	def Share(self, ent: StepElement_AnalysisItemWithinRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepElement_AnalysisItemWithinRepresentation) -> None: ...

class RWStepElement_RWCurve3dElementDescriptor:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepElement_Curve3dElementDescriptor) -> None: ...
	def Share(self, ent: StepElement_Curve3dElementDescriptor, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepElement_Curve3dElementDescriptor) -> None: ...

class RWStepElement_RWCurveElementEndReleasePacket:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepElement_CurveElementEndReleasePacket) -> None: ...
	def Share(self, ent: StepElement_CurveElementEndReleasePacket, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepElement_CurveElementEndReleasePacket) -> None: ...

class RWStepElement_RWCurveElementSectionDefinition:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepElement_CurveElementSectionDefinition) -> None: ...
	def Share(self, ent: StepElement_CurveElementSectionDefinition, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepElement_CurveElementSectionDefinition) -> None: ...

class RWStepElement_RWCurveElementSectionDerivedDefinitions:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepElement_CurveElementSectionDerivedDefinitions) -> None: ...
	def Share(self, ent: StepElement_CurveElementSectionDerivedDefinitions, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepElement_CurveElementSectionDerivedDefinitions) -> None: ...

class RWStepElement_RWElementDescriptor:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepElement_ElementDescriptor) -> None: ...
	def Share(self, ent: StepElement_ElementDescriptor, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepElement_ElementDescriptor) -> None: ...

class RWStepElement_RWElementMaterial:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepElement_ElementMaterial) -> None: ...
	def Share(self, ent: StepElement_ElementMaterial, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepElement_ElementMaterial) -> None: ...

class RWStepElement_RWSurface3dElementDescriptor:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepElement_Surface3dElementDescriptor) -> None: ...
	def Share(self, ent: StepElement_Surface3dElementDescriptor, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepElement_Surface3dElementDescriptor) -> None: ...

class RWStepElement_RWSurfaceElementProperty:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepElement_SurfaceElementProperty) -> None: ...
	def Share(self, ent: StepElement_SurfaceElementProperty, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepElement_SurfaceElementProperty) -> None: ...

class RWStepElement_RWSurfaceSection:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepElement_SurfaceSection) -> None: ...
	def Share(self, ent: StepElement_SurfaceSection, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepElement_SurfaceSection) -> None: ...

class RWStepElement_RWSurfaceSectionField:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepElement_SurfaceSectionField) -> None: ...
	def Share(self, ent: StepElement_SurfaceSectionField, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepElement_SurfaceSectionField) -> None: ...

class RWStepElement_RWSurfaceSectionFieldConstant:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepElement_SurfaceSectionFieldConstant) -> None: ...
	def Share(self, ent: StepElement_SurfaceSectionFieldConstant, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepElement_SurfaceSectionFieldConstant) -> None: ...

class RWStepElement_RWSurfaceSectionFieldVarying:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepElement_SurfaceSectionFieldVarying) -> None: ...
	def Share(self, ent: StepElement_SurfaceSectionFieldVarying, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepElement_SurfaceSectionFieldVarying) -> None: ...

class RWStepElement_RWUniformSurfaceSection:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepElement_UniformSurfaceSection) -> None: ...
	def Share(self, ent: StepElement_UniformSurfaceSection, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepElement_UniformSurfaceSection) -> None: ...

class RWStepElement_RWVolume3dElementDescriptor:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepElement_Volume3dElementDescriptor) -> None: ...
	def Share(self, ent: StepElement_Volume3dElementDescriptor, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepElement_Volume3dElementDescriptor) -> None: ...
