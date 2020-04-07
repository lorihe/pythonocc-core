from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColStd import *
from OCC.Core.StepShape import *
from OCC.Core.StepData import *
from OCC.Core.StepRepr import *
from OCC.Core.StepGeom import *
from OCC.Core.TCollection import *
from OCC.Core.StepBasic import *
from OCC.Core.TColgp import *


class StepVisual_NullStyle(IntEnum):
	StepVisual_Null: int = ...
StepVisual_Null = StepVisual_NullStyle.StepVisual_Null

class StepVisual_CentralOrParallel(IntEnum):
	StepVisual_copCentral: int = ...
	StepVisual_copParallel: int = ...
StepVisual_copCentral = StepVisual_CentralOrParallel.StepVisual_copCentral
StepVisual_copParallel = StepVisual_CentralOrParallel.StepVisual_copParallel

class StepVisual_SurfaceSide(IntEnum):
	StepVisual_ssNegative: int = ...
	StepVisual_ssPositive: int = ...
	StepVisual_ssBoth: int = ...
StepVisual_ssNegative = StepVisual_SurfaceSide.StepVisual_ssNegative
StepVisual_ssPositive = StepVisual_SurfaceSide.StepVisual_ssPositive
StepVisual_ssBoth = StepVisual_SurfaceSide.StepVisual_ssBoth

class StepVisual_TextPath(IntEnum):
	StepVisual_tpUp: int = ...
	StepVisual_tpRight: int = ...
	StepVisual_tpDown: int = ...
	StepVisual_tpLeft: int = ...
StepVisual_tpUp = StepVisual_TextPath.StepVisual_tpUp
StepVisual_tpRight = StepVisual_TextPath.StepVisual_tpRight
StepVisual_tpDown = StepVisual_TextPath.StepVisual_tpDown
StepVisual_tpLeft = StepVisual_TextPath.StepVisual_tpLeft

class StepVisual_MarkerType(IntEnum):
	StepVisual_mtDot: int = ...
	StepVisual_mtX: int = ...
	StepVisual_mtPlus: int = ...
	StepVisual_mtAsterisk: int = ...
	StepVisual_mtRing: int = ...
	StepVisual_mtSquare: int = ...
	StepVisual_mtTriangle: int = ...
StepVisual_mtDot = StepVisual_MarkerType.StepVisual_mtDot
StepVisual_mtX = StepVisual_MarkerType.StepVisual_mtX
StepVisual_mtPlus = StepVisual_MarkerType.StepVisual_mtPlus
StepVisual_mtAsterisk = StepVisual_MarkerType.StepVisual_mtAsterisk
StepVisual_mtRing = StepVisual_MarkerType.StepVisual_mtRing
StepVisual_mtSquare = StepVisual_MarkerType.StepVisual_mtSquare
StepVisual_mtTriangle = StepVisual_MarkerType.StepVisual_mtTriangle

class StepVisual_AnnotationFillArea(StepShape_GeometricCurveSet):
	def __init__(self) -> None: ...

class StepVisual_AnnotationPlaneElement(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def DraughtingCallout(self) -> StepVisual_DraughtingCallout: ...
	def StyledItem(self) -> StepVisual_StyledItem: ...

class StepVisual_AnnotationText(StepRepr_MappedItem):
	def __init__(self) -> None: ...

class StepVisual_AreaInSet(Standard_Transient):
	def __init__(self) -> None: ...
	def Area(self) -> StepVisual_PresentationArea: ...
	def InSet(self) -> StepVisual_PresentationSet: ...
	def Init(self, aArea: StepVisual_PresentationArea, aInSet: StepVisual_PresentationSet) -> None: ...
	def SetArea(self, aArea: StepVisual_PresentationArea) -> None: ...
	def SetInSet(self, aInSet: StepVisual_PresentationSet) -> None: ...

class StepVisual_AreaOrView(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def PresentationArea(self) -> StepVisual_PresentationArea: ...
	def PresentationView(self) -> StepVisual_PresentationView: ...

class StepVisual_BoxCharacteristicSelect:
	def __init__(self) -> None: ...
	def RealValue(self) -> float: ...
	def SetRealValue(self, aValue: float) -> None: ...
	def SetTypeOfContent(self, aType: int) -> None: ...
	def TypeOfContent(self) -> int: ...

class StepVisual_CameraImage(StepRepr_MappedItem):
	def __init__(self) -> None: ...

class StepVisual_CameraModel(StepGeom_GeometricRepresentationItem):
	def __init__(self) -> None: ...

class StepVisual_CameraModelD3MultiClippingInterectionSelect(StepData_SelectType):
	def __init__(self) -> None: ...
	def CameraModelD3MultiClippingUnion(self) -> StepVisual_CameraModelD3MultiClippingUnion: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def Plane(self) -> StepGeom_Plane: ...

class StepVisual_CameraModelD3MultiClippingIntersection(StepGeom_GeometricRepresentationItem):
	def __init__(self) -> None: ...
	def Init(self, theName: TCollection_HAsciiString, theShapeClipping: StepVisual_HArray1OfCameraModelD3MultiClippingInterectionSelect) -> None: ...
	def SetShapeClipping(self, theShapeClipping: StepVisual_HArray1OfCameraModelD3MultiClippingInterectionSelect) -> None: ...
	def ShapeClipping(self) -> StepVisual_HArray1OfCameraModelD3MultiClippingInterectionSelect: ...

class StepVisual_CameraModelD3MultiClippingUnion(StepGeom_GeometricRepresentationItem):
	def __init__(self) -> None: ...
	def Init(self, theName: TCollection_HAsciiString, theShapeClipping: StepVisual_HArray1OfCameraModelD3MultiClippingUnionSelect) -> None: ...
	def SetShapeClipping(self, theShapeClipping: StepVisual_HArray1OfCameraModelD3MultiClippingUnionSelect) -> None: ...
	def ShapeClipping(self) -> StepVisual_HArray1OfCameraModelD3MultiClippingUnionSelect: ...

class StepVisual_CameraModelD3MultiClippingUnionSelect(StepData_SelectType):
	def __init__(self) -> None: ...
	def CameraModelD3MultiClippingIntersection(self) -> StepVisual_CameraModelD3MultiClippingIntersection: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def Plane(self) -> StepGeom_Plane: ...

class StepVisual_CameraUsage(StepRepr_RepresentationMap):
	def __init__(self) -> None: ...

class StepVisual_Colour(Standard_Transient):
	def __init__(self) -> None: ...

class StepVisual_CompositeText(StepGeom_GeometricRepresentationItem):
	def __init__(self) -> None: ...
	def CollectedText(self) -> StepVisual_HArray1OfTextOrCharacter: ...
	def CollectedTextValue(self, num: int) -> StepVisual_TextOrCharacter: ...
	def Init(self, aName: TCollection_HAsciiString, aCollectedText: StepVisual_HArray1OfTextOrCharacter) -> None: ...
	def NbCollectedText(self) -> int: ...
	def SetCollectedText(self, aCollectedText: StepVisual_HArray1OfTextOrCharacter) -> None: ...

class StepVisual_CurveStyle(Standard_Transient):
	def __init__(self) -> None: ...
	def CurveColour(self) -> StepVisual_Colour: ...
	def CurveFont(self) -> StepVisual_CurveStyleFontSelect: ...
	def CurveWidth(self) -> StepBasic_SizeSelect: ...
	def Init(self, aName: TCollection_HAsciiString, aCurveFont: StepVisual_CurveStyleFontSelect, aCurveWidth: StepBasic_SizeSelect, aCurveColour: StepVisual_Colour) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def SetCurveColour(self, aCurveColour: StepVisual_Colour) -> None: ...
	def SetCurveFont(self, aCurveFont: StepVisual_CurveStyleFontSelect) -> None: ...
	def SetCurveWidth(self, aCurveWidth: StepBasic_SizeSelect) -> None: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...

class StepVisual_CurveStyleFont(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString, aPatternList: StepVisual_HArray1OfCurveStyleFontPattern) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def NbPatternList(self) -> int: ...
	def PatternList(self) -> StepVisual_HArray1OfCurveStyleFontPattern: ...
	def PatternListValue(self, num: int) -> StepVisual_CurveStyleFontPattern: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...
	def SetPatternList(self, aPatternList: StepVisual_HArray1OfCurveStyleFontPattern) -> None: ...

class StepVisual_CurveStyleFontPattern(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aVisibleSegmentLength: float, aInvisibleSegmentLength: float) -> None: ...
	def InvisibleSegmentLength(self) -> float: ...
	def SetInvisibleSegmentLength(self, aInvisibleSegmentLength: float) -> None: ...
	def SetVisibleSegmentLength(self, aVisibleSegmentLength: float) -> None: ...
	def VisibleSegmentLength(self) -> float: ...

class StepVisual_CurveStyleFontSelect(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def CurveStyleFont(self) -> StepVisual_CurveStyleFont: ...
	def ExternallyDefinedCurveFont(self) -> StepVisual_ExternallyDefinedCurveFont: ...
	def PreDefinedCurveFont(self) -> StepVisual_PreDefinedCurveFont: ...

class StepVisual_DirectionCountSelect:
	def __init__(self) -> None: ...
	def SetTypeOfContent(self, aTypeOfContent: int) -> None: ...
	def SetUDirectionCount(self, aUDirectionCount: int) -> None: ...
	def SetVDirectionCount(self, aUDirectionCount: int) -> None: ...
	def TypeOfContent(self) -> int: ...
	def UDirectionCount(self) -> int: ...
	def VDirectionCount(self) -> int: ...

class StepVisual_DraughtingCallout(StepGeom_GeometricRepresentationItem):
	def __init__(self) -> None: ...
	def Contents(self) -> StepVisual_HArray1OfDraughtingCalloutElement: ...
	def ContentsValue(self, theNum: int) -> StepVisual_DraughtingCalloutElement: ...
	def Init(self, theName: TCollection_HAsciiString, theContents: StepVisual_HArray1OfDraughtingCalloutElement) -> None: ...
	def NbContents(self) -> int: ...
	def SetContents(self, theContents: StepVisual_HArray1OfDraughtingCalloutElement) -> None: ...
	def SetContentsValue(self, theNum: int, theItem: StepVisual_DraughtingCalloutElement) -> None: ...

class StepVisual_DraughtingCalloutElement(StepData_SelectType):
	def __init__(self) -> None: ...
	def AnnotationCurveOccurrence(self) -> StepVisual_AnnotationCurveOccurrence: ...
	def AnnotationFillAreaOccurrence(self) -> StepVisual_AnnotationFillAreaOccurrence: ...
	def AnnotationTextOccurrence(self) -> StepVisual_AnnotationTextOccurrence: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def TessellatedAnnotationOccurrence(self) -> StepVisual_TessellatedAnnotationOccurrence: ...

class StepVisual_DraughtingModel(StepRepr_Representation):
	def __init__(self) -> None: ...

class StepVisual_ExternallyDefinedCurveFont(StepBasic_ExternallyDefinedItem):
	def __init__(self) -> None: ...

class StepVisual_ExternallyDefinedTextFont(StepBasic_ExternallyDefinedItem):
	def __init__(self) -> None: ...

class StepVisual_FillAreaStyle(Standard_Transient):
	def __init__(self) -> None: ...
	def FillStyles(self) -> StepVisual_HArray1OfFillStyleSelect: ...
	def FillStylesValue(self, num: int) -> StepVisual_FillStyleSelect: ...
	def Init(self, aName: TCollection_HAsciiString, aFillStyles: StepVisual_HArray1OfFillStyleSelect) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def NbFillStyles(self) -> int: ...
	def SetFillStyles(self, aFillStyles: StepVisual_HArray1OfFillStyleSelect) -> None: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...

class StepVisual_FillAreaStyleColour(Standard_Transient):
	def __init__(self) -> None: ...
	def FillColour(self) -> StepVisual_Colour: ...
	def Init(self, aName: TCollection_HAsciiString, aFillColour: StepVisual_Colour) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def SetFillColour(self, aFillColour: StepVisual_Colour) -> None: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...

class StepVisual_FillStyleSelect(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def FillAreaStyleColour(self) -> StepVisual_FillAreaStyleColour: ...

class StepVisual_FontSelect(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ExternallyDefinedTextFont(self) -> StepVisual_ExternallyDefinedTextFont: ...
	def PreDefinedTextFont(self) -> StepVisual_PreDefinedTextFont: ...

class StepVisual_Invisibility(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aInvisibleItems: StepVisual_HArray1OfInvisibleItem) -> None: ...
	def InvisibleItems(self) -> StepVisual_HArray1OfInvisibleItem: ...
	def InvisibleItemsValue(self, num: int) -> StepVisual_InvisibleItem: ...
	def NbInvisibleItems(self) -> int: ...
	def SetInvisibleItems(self, aInvisibleItems: StepVisual_HArray1OfInvisibleItem) -> None: ...

class StepVisual_InvisibilityContext(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def DraughtingModel(self) -> StepVisual_DraughtingModel: ...
	def PresentationRepresentation(self) -> StepVisual_PresentationRepresentation: ...
	def PresentationSet(self) -> StepVisual_PresentationSet: ...

class StepVisual_InvisibleItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def PresentationLayerAssignment(self) -> StepVisual_PresentationLayerAssignment: ...
	def PresentationRepresentation(self) -> StepVisual_PresentationRepresentation: ...
	def StyledItem(self) -> StepVisual_StyledItem: ...

class StepVisual_LayeredItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def PresentationRepresentation(self) -> StepVisual_PresentationRepresentation: ...
	def RepresentationItem(self) -> StepRepr_RepresentationItem: ...

class StepVisual_MarkerMember(StepData_SelectInt):
	def __init__(self) -> None: ...
	def EnumText(self) -> str: ...
	def HasName(self) -> bool: ...
	def Name(self) -> str: ...
	def SetEnumText(self, val: int, text: str) -> None: ...
	def SetName(self, name: str) -> bool: ...
	def SetValue(self, val: StepVisual_MarkerType) -> None: ...
	def Value(self) -> StepVisual_MarkerType: ...

class StepVisual_MarkerSelect(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseMem(self, sm: StepData_SelectMember) -> int: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def MarkerMember(self) -> StepVisual_MarkerMember: ...
	def NewMember(self) -> StepData_SelectMember: ...

class StepVisual_NullStyleMember(StepData_SelectInt):
	def __init__(self) -> None: ...
	def EnumText(self) -> str: ...
	def HasName(self) -> bool: ...
	def Kind(self) -> int: ...
	def Name(self) -> str: ...
	def SetEnumText(self, theValue: int, theText: str) -> None: ...
	def SetValue(self, theValue: StepVisual_NullStyle) -> None: ...
	def Value(self) -> StepVisual_NullStyle: ...

class StepVisual_PlanarExtent(StepGeom_GeometricRepresentationItem):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString, aSizeInX: float, aSizeInY: float) -> None: ...
	def SetSizeInX(self, aSizeInX: float) -> None: ...
	def SetSizeInY(self, aSizeInY: float) -> None: ...
	def SizeInX(self) -> float: ...
	def SizeInY(self) -> float: ...

class StepVisual_PointStyle(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString, aMarker: StepVisual_MarkerSelect, aMarkerSize: StepBasic_SizeSelect, aMarkerColour: StepVisual_Colour) -> None: ...
	def Marker(self) -> StepVisual_MarkerSelect: ...
	def MarkerColour(self) -> StepVisual_Colour: ...
	def MarkerSize(self) -> StepBasic_SizeSelect: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def SetMarker(self, aMarker: StepVisual_MarkerSelect) -> None: ...
	def SetMarkerColour(self, aMarkerColour: StepVisual_Colour) -> None: ...
	def SetMarkerSize(self, aMarkerSize: StepBasic_SizeSelect) -> None: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...

class StepVisual_PreDefinedItem(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...

class StepVisual_PresentationLayerAssignment(Standard_Transient):
	def __init__(self) -> None: ...
	def AssignedItems(self) -> StepVisual_HArray1OfLayeredItem: ...
	def AssignedItemsValue(self, num: int) -> StepVisual_LayeredItem: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aAssignedItems: StepVisual_HArray1OfLayeredItem) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def NbAssignedItems(self) -> int: ...
	def SetAssignedItems(self, aAssignedItems: StepVisual_HArray1OfLayeredItem) -> None: ...
	def SetDescription(self, aDescription: TCollection_HAsciiString) -> None: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...

class StepVisual_PresentationLayerUsage(Standard_Transient):
	def __init__(self) -> None: ...
	def Assignment(self) -> StepVisual_PresentationLayerAssignment: ...
	def Init(self, aAssignment: StepVisual_PresentationLayerAssignment, aPresentation: StepVisual_PresentationRepresentation) -> None: ...
	def Presentation(self) -> StepVisual_PresentationRepresentation: ...
	def SetAssignment(self, aAssignment: StepVisual_PresentationLayerAssignment) -> None: ...
	def SetPresentation(self, aPresentation: StepVisual_PresentationRepresentation) -> None: ...

class StepVisual_PresentationRepresentation(StepRepr_Representation):
	def __init__(self) -> None: ...

class StepVisual_PresentationRepresentationSelect(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def PresentationRepresentation(self) -> StepVisual_PresentationRepresentation: ...
	def PresentationSet(self) -> StepVisual_PresentationSet: ...

class StepVisual_PresentationSet(Standard_Transient):
	def __init__(self) -> None: ...

class StepVisual_PresentationSize(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aUnit: StepVisual_PresentationSizeAssignmentSelect, aSize: StepVisual_PlanarBox) -> None: ...
	def SetSize(self, aSize: StepVisual_PlanarBox) -> None: ...
	def SetUnit(self, aUnit: StepVisual_PresentationSizeAssignmentSelect) -> None: ...
	def Size(self) -> StepVisual_PlanarBox: ...
	def Unit(self) -> StepVisual_PresentationSizeAssignmentSelect: ...

class StepVisual_PresentationSizeAssignmentSelect(StepData_SelectType):
	def __init__(self) -> None: ...
	def AreaInSet(self) -> StepVisual_AreaInSet: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def PresentationArea(self) -> StepVisual_PresentationArea: ...
	def PresentationView(self) -> StepVisual_PresentationView: ...

class StepVisual_PresentationStyleAssignment(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aStyles: StepVisual_HArray1OfPresentationStyleSelect) -> None: ...
	def NbStyles(self) -> int: ...
	def SetStyles(self, aStyles: StepVisual_HArray1OfPresentationStyleSelect) -> None: ...
	def Styles(self) -> StepVisual_HArray1OfPresentationStyleSelect: ...
	def StylesValue(self, num: int) -> StepVisual_PresentationStyleSelect: ...

class StepVisual_PresentationStyleSelect(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def CurveStyle(self) -> StepVisual_CurveStyle: ...
	def NullStyle(self) -> StepVisual_NullStyleMember: ...
	def PointStyle(self) -> StepVisual_PointStyle: ...
	def SurfaceStyleUsage(self) -> StepVisual_SurfaceStyleUsage: ...

class StepVisual_PresentedItem(Standard_Transient):
	pass

class StepVisual_PresentedItemRepresentation(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aPresentation: StepVisual_PresentationRepresentationSelect, aItem: StepVisual_PresentedItem) -> None: ...
	def Item(self) -> StepVisual_PresentedItem: ...
	def Presentation(self) -> StepVisual_PresentationRepresentationSelect: ...
	def SetItem(self, aItem: StepVisual_PresentedItem) -> None: ...
	def SetPresentation(self, aPresentation: StepVisual_PresentationRepresentationSelect) -> None: ...

class StepVisual_StyleContextSelect(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def PresentationSet(self) -> StepVisual_PresentationSet: ...
	def Representation(self) -> StepRepr_Representation: ...
	def RepresentationItem(self) -> StepRepr_RepresentationItem: ...

class StepVisual_StyledItem(StepRepr_RepresentationItem):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString, aStyles: StepVisual_HArray1OfPresentationStyleAssignment, aItem: Standard_Transient) -> None: ...
	def Item(self) -> StepRepr_RepresentationItem: ...
	def ItemAP242(self) -> StepVisual_StyledItemTarget: ...
	def NbStyles(self) -> int: ...
	def SetItem(self, aItem: StepRepr_RepresentationItem) -> None: ...
	def SetItem(self, aItem: StepVisual_StyledItemTarget) -> None: ...
	def SetStyles(self, aStyles: StepVisual_HArray1OfPresentationStyleAssignment) -> None: ...
	def Styles(self) -> StepVisual_HArray1OfPresentationStyleAssignment: ...
	def StylesValue(self, num: int) -> StepVisual_PresentationStyleAssignment: ...

class StepVisual_StyledItemTarget(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def GeometricRepresentationItem(self) -> StepGeom_GeometricRepresentationItem: ...
	def MappedItem(self) -> StepRepr_MappedItem: ...
	def Representation(self) -> StepRepr_Representation: ...
	def TopologicalRepresentationItem(self) -> StepShape_TopologicalRepresentationItem: ...

class StepVisual_SurfaceSideStyle(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString, aStyles: StepVisual_HArray1OfSurfaceStyleElementSelect) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def NbStyles(self) -> int: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...
	def SetStyles(self, aStyles: StepVisual_HArray1OfSurfaceStyleElementSelect) -> None: ...
	def Styles(self) -> StepVisual_HArray1OfSurfaceStyleElementSelect: ...
	def StylesValue(self, num: int) -> StepVisual_SurfaceStyleElementSelect: ...

class StepVisual_SurfaceStyleBoundary(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aStyleOfBoundary: StepVisual_CurveStyle) -> None: ...
	def SetStyleOfBoundary(self, aStyleOfBoundary: StepVisual_CurveStyle) -> None: ...
	def StyleOfBoundary(self) -> StepVisual_CurveStyle: ...

class StepVisual_SurfaceStyleControlGrid(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aStyleOfControlGrid: StepVisual_CurveStyle) -> None: ...
	def SetStyleOfControlGrid(self, aStyleOfControlGrid: StepVisual_CurveStyle) -> None: ...
	def StyleOfControlGrid(self) -> StepVisual_CurveStyle: ...

class StepVisual_SurfaceStyleElementSelect(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def SurfaceStyleBoundary(self) -> StepVisual_SurfaceStyleBoundary: ...
	def SurfaceStyleFillArea(self) -> StepVisual_SurfaceStyleFillArea: ...
	def SurfaceStyleParameterLine(self) -> StepVisual_SurfaceStyleParameterLine: ...

class StepVisual_SurfaceStyleFillArea(Standard_Transient):
	def __init__(self) -> None: ...
	def FillArea(self) -> StepVisual_FillAreaStyle: ...
	def Init(self, aFillArea: StepVisual_FillAreaStyle) -> None: ...
	def SetFillArea(self, aFillArea: StepVisual_FillAreaStyle) -> None: ...

class StepVisual_SurfaceStyleParameterLine(Standard_Transient):
	def __init__(self) -> None: ...
	def DirectionCounts(self) -> StepVisual_HArray1OfDirectionCountSelect: ...
	def DirectionCountsValue(self, num: int) -> StepVisual_DirectionCountSelect: ...
	def Init(self, aStyleOfParameterLines: StepVisual_CurveStyle, aDirectionCounts: StepVisual_HArray1OfDirectionCountSelect) -> None: ...
	def NbDirectionCounts(self) -> int: ...
	def SetDirectionCounts(self, aDirectionCounts: StepVisual_HArray1OfDirectionCountSelect) -> None: ...
	def SetStyleOfParameterLines(self, aStyleOfParameterLines: StepVisual_CurveStyle) -> None: ...
	def StyleOfParameterLines(self) -> StepVisual_CurveStyle: ...

class StepVisual_SurfaceStyleSegmentationCurve(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aStyleOfSegmentationCurve: StepVisual_CurveStyle) -> None: ...
	def SetStyleOfSegmentationCurve(self, aStyleOfSegmentationCurve: StepVisual_CurveStyle) -> None: ...
	def StyleOfSegmentationCurve(self) -> StepVisual_CurveStyle: ...

class StepVisual_SurfaceStyleSilhouette(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aStyleOfSilhouette: StepVisual_CurveStyle) -> None: ...
	def SetStyleOfSilhouette(self, aStyleOfSilhouette: StepVisual_CurveStyle) -> None: ...
	def StyleOfSilhouette(self) -> StepVisual_CurveStyle: ...

class StepVisual_SurfaceStyleUsage(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aSide: StepVisual_SurfaceSide, aStyle: StepVisual_SurfaceSideStyle) -> None: ...
	def SetSide(self, aSide: StepVisual_SurfaceSide) -> None: ...
	def SetStyle(self, aStyle: StepVisual_SurfaceSideStyle) -> None: ...
	def Side(self) -> StepVisual_SurfaceSide: ...
	def Style(self) -> StepVisual_SurfaceSideStyle: ...

class StepVisual_Template(StepRepr_Representation):
	def __init__(self) -> None: ...

class StepVisual_TemplateInstance(StepRepr_MappedItem):
	def __init__(self) -> None: ...

class StepVisual_TessellatedItem(StepGeom_GeometricRepresentationItem):
	def __init__(self) -> None: ...

class StepVisual_TextLiteral(StepGeom_GeometricRepresentationItem):
	def __init__(self) -> None: ...
	def Alignment(self) -> TCollection_HAsciiString: ...
	def Font(self) -> StepVisual_FontSelect: ...
	def Init(self, aName: TCollection_HAsciiString, aLiteral: TCollection_HAsciiString, aPlacement: StepGeom_Axis2Placement, aAlignment: TCollection_HAsciiString, aPath: StepVisual_TextPath, aFont: StepVisual_FontSelect) -> None: ...
	def Literal(self) -> TCollection_HAsciiString: ...
	def Path(self) -> StepVisual_TextPath: ...
	def Placement(self) -> StepGeom_Axis2Placement: ...
	def SetAlignment(self, aAlignment: TCollection_HAsciiString) -> None: ...
	def SetFont(self, aFont: StepVisual_FontSelect) -> None: ...
	def SetLiteral(self, aLiteral: TCollection_HAsciiString) -> None: ...
	def SetPath(self, aPath: StepVisual_TextPath) -> None: ...
	def SetPlacement(self, aPlacement: StepGeom_Axis2Placement) -> None: ...

class StepVisual_TextOrCharacter(StepData_SelectType):
	def __init__(self) -> None: ...
	def AnnotationText(self) -> StepVisual_AnnotationText: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def CompositeText(self) -> StepVisual_CompositeText: ...
	def TextLiteral(self) -> StepVisual_TextLiteral: ...

class StepVisual_TextStyle(Standard_Transient):
	def __init__(self) -> None: ...
	def CharacterAppearance(self) -> StepVisual_TextStyleForDefinedFont: ...
	def Init(self, aName: TCollection_HAsciiString, aCharacterAppearance: StepVisual_TextStyleForDefinedFont) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def SetCharacterAppearance(self, aCharacterAppearance: StepVisual_TextStyleForDefinedFont) -> None: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...

class StepVisual_TextStyleForDefinedFont(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aTextColour: StepVisual_Colour) -> None: ...
	def SetTextColour(self, aTextColour: StepVisual_Colour) -> None: ...
	def TextColour(self) -> StepVisual_Colour: ...

class StepVisual_ViewVolume(Standard_Transient):
	def __init__(self) -> None: ...
	def BackPlaneClipping(self) -> bool: ...
	def BackPlaneDistance(self) -> float: ...
	def FrontPlaneClipping(self) -> bool: ...
	def FrontPlaneDistance(self) -> float: ...
	def Init(self, aProjectionType: StepVisual_CentralOrParallel, aProjectionPoint: StepGeom_CartesianPoint, aViewPlaneDistance: float, aFrontPlaneDistance: float, aFrontPlaneClipping: bool, aBackPlaneDistance: float, aBackPlaneClipping: bool, aViewVolumeSidesClipping: bool, aViewWindow: StepVisual_PlanarBox) -> None: ...
	def ProjectionPoint(self) -> StepGeom_CartesianPoint: ...
	def ProjectionType(self) -> StepVisual_CentralOrParallel: ...
	def SetBackPlaneClipping(self, aBackPlaneClipping: bool) -> None: ...
	def SetBackPlaneDistance(self, aBackPlaneDistance: float) -> None: ...
	def SetFrontPlaneClipping(self, aFrontPlaneClipping: bool) -> None: ...
	def SetFrontPlaneDistance(self, aFrontPlaneDistance: float) -> None: ...
	def SetProjectionPoint(self, aProjectionPoint: StepGeom_CartesianPoint) -> None: ...
	def SetProjectionType(self, aProjectionType: StepVisual_CentralOrParallel) -> None: ...
	def SetViewPlaneDistance(self, aViewPlaneDistance: float) -> None: ...
	def SetViewVolumeSidesClipping(self, aViewVolumeSidesClipping: bool) -> None: ...
	def SetViewWindow(self, aViewWindow: StepVisual_PlanarBox) -> None: ...
	def ViewPlaneDistance(self) -> float: ...
	def ViewVolumeSidesClipping(self) -> bool: ...
	def ViewWindow(self) -> StepVisual_PlanarBox: ...

class StepVisual_AnnotationOccurrence(StepVisual_StyledItem):
	def __init__(self) -> None: ...

class StepVisual_BackgroundColour(StepVisual_Colour):
	def __init__(self) -> None: ...
	def Init(self, aPresentation: StepVisual_AreaOrView) -> None: ...
	def Presentation(self) -> StepVisual_AreaOrView: ...
	def SetPresentation(self, aPresentation: StepVisual_AreaOrView) -> None: ...

class StepVisual_CameraImage2dWithScale(StepVisual_CameraImage):
	def __init__(self) -> None: ...

class StepVisual_CameraImage3dWithScale(StepVisual_CameraImage):
	def __init__(self) -> None: ...

class StepVisual_CameraModelD2(StepVisual_CameraModel):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString, aViewWindow: StepVisual_PlanarBox, aViewWindowClipping: bool) -> None: ...
	def SetViewWindow(self, aViewWindow: StepVisual_PlanarBox) -> None: ...
	def SetViewWindowClipping(self, aViewWindowClipping: bool) -> None: ...
	def ViewWindow(self) -> StepVisual_PlanarBox: ...
	def ViewWindowClipping(self) -> bool: ...

class StepVisual_CameraModelD3(StepVisual_CameraModel):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString, aViewReferenceSystem: StepGeom_Axis2Placement3d, aPerspectiveOfVolume: StepVisual_ViewVolume) -> None: ...
	def PerspectiveOfVolume(self) -> StepVisual_ViewVolume: ...
	def SetPerspectiveOfVolume(self, aPerspectiveOfVolume: StepVisual_ViewVolume) -> None: ...
	def SetViewReferenceSystem(self, aViewReferenceSystem: StepGeom_Axis2Placement3d) -> None: ...
	def ViewReferenceSystem(self) -> StepGeom_Axis2Placement3d: ...

class StepVisual_CharacterizedObjectAndCharacterizedRepresentationAndDraughtingModelAndRepresentation(StepVisual_DraughtingModel):
	def __init__(self) -> None: ...

class StepVisual_ColourSpecification(StepVisual_Colour):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...

class StepVisual_CompositeTextWithExtent(StepVisual_CompositeText):
	def __init__(self) -> None: ...
	def Extent(self) -> StepVisual_PlanarExtent: ...
	def Init(self, aName: TCollection_HAsciiString, aCollectedText: StepVisual_HArray1OfTextOrCharacter, aExtent: StepVisual_PlanarExtent) -> None: ...
	def SetExtent(self, aExtent: StepVisual_PlanarExtent) -> None: ...

class StepVisual_ContextDependentInvisibility(StepVisual_Invisibility):
	def __init__(self) -> None: ...
	def Init(self, aInvisibleItems: StepVisual_HArray1OfInvisibleItem, aPresentationContext: StepVisual_InvisibilityContext) -> None: ...
	def PresentationContext(self) -> StepVisual_InvisibilityContext: ...
	def SetPresentationContext(self, aPresentationContext: StepVisual_InvisibilityContext) -> None: ...

class StepVisual_CoordinatesList(StepVisual_TessellatedItem):
	def __init__(self) -> None: ...
	def Init(self, theName: TCollection_HAsciiString, thePoints: TColgp_HArray1OfXYZ) -> None: ...
	def Points(self) -> TColgp_HArray1OfXYZ: ...

class StepVisual_MechanicalDesignGeometricPresentationRepresentation(StepVisual_PresentationRepresentation):
	def __init__(self) -> None: ...

class StepVisual_OverRidingStyledItem(StepVisual_StyledItem):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString, aStyles: StepVisual_HArray1OfPresentationStyleAssignment, aItem: Standard_Transient, aOverRiddenStyle: StepVisual_StyledItem) -> None: ...
	def OverRiddenStyle(self) -> StepVisual_StyledItem: ...
	def SetOverRiddenStyle(self, aOverRiddenStyle: StepVisual_StyledItem) -> None: ...

class StepVisual_PlanarBox(StepVisual_PlanarExtent):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString, aSizeInX: float, aSizeInY: float, aPlacement: StepGeom_Axis2Placement) -> None: ...
	def Placement(self) -> StepGeom_Axis2Placement: ...
	def SetPlacement(self, aPlacement: StepGeom_Axis2Placement) -> None: ...

class StepVisual_PreDefinedColour(StepVisual_Colour):
	def __init__(self) -> None: ...
	def GetPreDefinedItem(self) -> StepVisual_PreDefinedItem: ...
	def SetPreDefinedItem(self, item: StepVisual_PreDefinedItem) -> None: ...

class StepVisual_PreDefinedCurveFont(StepVisual_PreDefinedItem):
	def __init__(self) -> None: ...

class StepVisual_PreDefinedTextFont(StepVisual_PreDefinedItem):
	def __init__(self) -> None: ...

class StepVisual_PresentationArea(StepVisual_PresentationRepresentation):
	def __init__(self) -> None: ...

class StepVisual_PresentationStyleByContext(StepVisual_PresentationStyleAssignment):
	def __init__(self) -> None: ...
	def Init(self, aStyles: StepVisual_HArray1OfPresentationStyleSelect, aStyleContext: StepVisual_StyleContextSelect) -> None: ...
	def SetStyleContext(self, aStyleContext: StepVisual_StyleContextSelect) -> None: ...
	def StyleContext(self) -> StepVisual_StyleContextSelect: ...

class StepVisual_PresentationView(StepVisual_PresentationRepresentation):
	def __init__(self) -> None: ...

class StepVisual_TessellatedAnnotationOccurrence(StepVisual_StyledItem):
	def __init__(self) -> None: ...

class StepVisual_TessellatedCurveSet(StepVisual_TessellatedItem):
	def __init__(self) -> None: ...
	def CoordList(self) -> StepVisual_CoordinatesList: ...
	def Curves(self) -> False: ...

class StepVisual_TessellatedGeometricSet(StepVisual_TessellatedItem):
	def __init__(self) -> None: ...
	def Items(self) -> False: ...

class StepVisual_TextStyleWithBoxCharacteristics(StepVisual_TextStyle):
	def __init__(self) -> None: ...
	def Characteristics(self) -> StepVisual_HArray1OfBoxCharacteristicSelect: ...
	def CharacteristicsValue(self, num: int) -> StepVisual_BoxCharacteristicSelect: ...
	def Init(self, aName: TCollection_HAsciiString, aCharacterAppearance: StepVisual_TextStyleForDefinedFont, aCharacteristics: StepVisual_HArray1OfBoxCharacteristicSelect) -> None: ...
	def NbCharacteristics(self) -> int: ...
	def SetCharacteristics(self, aCharacteristics: StepVisual_HArray1OfBoxCharacteristicSelect) -> None: ...

class StepVisual_AnnotationCurveOccurrence(StepVisual_AnnotationOccurrence):
	def __init__(self) -> None: ...

class StepVisual_AnnotationFillAreaOccurrence(StepVisual_AnnotationOccurrence):
	def __init__(self) -> None: ...
	def FillStyleTarget(self) -> StepGeom_GeometricRepresentationItem: ...
	def Init(self, theName: TCollection_HAsciiString, theStyles: StepVisual_HArray1OfPresentationStyleAssignment, theItem: Standard_Transient, theFillStyleTarget: StepGeom_GeometricRepresentationItem) -> None: ...
	def SetFillStyleTarget(self, theTarget: StepGeom_GeometricRepresentationItem) -> None: ...

class StepVisual_AnnotationPlane(StepVisual_AnnotationOccurrence):
	def __init__(self) -> None: ...
	def Elements(self) -> StepVisual_HArray1OfAnnotationPlaneElement: ...
	def ElementsValue(self, theNum: int) -> StepVisual_AnnotationPlaneElement: ...
	def Init(self, theName: TCollection_HAsciiString, theStyles: StepVisual_HArray1OfPresentationStyleAssignment, theItem: Standard_Transient, theElements: StepVisual_HArray1OfAnnotationPlaneElement) -> None: ...
	def NbElements(self) -> int: ...
	def SetElements(self, theElements: StepVisual_HArray1OfAnnotationPlaneElement) -> None: ...
	def SetElementsValue(self, theNum: int, theItem: StepVisual_AnnotationPlaneElement) -> None: ...

class StepVisual_AnnotationTextOccurrence(StepVisual_AnnotationOccurrence):
	def __init__(self) -> None: ...

class StepVisual_CameraModelD3MultiClipping(StepVisual_CameraModelD3):
	def __init__(self) -> None: ...
	def Init(self, theName: TCollection_HAsciiString, theViewReferenceSystem: StepGeom_Axis2Placement3d, thePerspectiveOfVolume: StepVisual_ViewVolume, theShapeClipping: StepVisual_HArray1OfCameraModelD3MultiClippingInterectionSelect) -> None: ...
	def SetShapeClipping(self, theShapeClipping: StepVisual_HArray1OfCameraModelD3MultiClippingInterectionSelect) -> None: ...
	def ShapeClipping(self) -> StepVisual_HArray1OfCameraModelD3MultiClippingInterectionSelect: ...

class StepVisual_ColourRgb(StepVisual_ColourSpecification):
	def __init__(self) -> None: ...
	def Blue(self) -> float: ...
	def Green(self) -> float: ...
	def Init(self, aName: TCollection_HAsciiString, aRed: float, aGreen: float, aBlue: float) -> None: ...
	def Red(self) -> float: ...
	def SetBlue(self, aBlue: float) -> None: ...
	def SetGreen(self, aGreen: float) -> None: ...
	def SetRed(self, aRed: float) -> None: ...

class StepVisual_ContextDependentOverRidingStyledItem(StepVisual_OverRidingStyledItem):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString, aStyles: StepVisual_HArray1OfPresentationStyleAssignment, aItem: Standard_Transient, aOverRiddenStyle: StepVisual_StyledItem, aStyleContext: StepVisual_HArray1OfStyleContextSelect) -> None: ...
	def NbStyleContext(self) -> int: ...
	def SetStyleContext(self, aStyleContext: StepVisual_HArray1OfStyleContextSelect) -> None: ...
	def StyleContext(self) -> StepVisual_HArray1OfStyleContextSelect: ...
	def StyleContextValue(self, num: int) -> StepVisual_StyleContextSelect: ...

class StepVisual_DraughtingAnnotationOccurrence(StepVisual_AnnotationOccurrence):
	def __init__(self) -> None: ...

class StepVisual_DraughtingPreDefinedColour(StepVisual_PreDefinedColour):
	def __init__(self) -> None: ...

class StepVisual_DraughtingPreDefinedCurveFont(StepVisual_PreDefinedCurveFont):
	def __init__(self) -> None: ...

class StepVisual_MechanicalDesignGeometricPresentationArea(StepVisual_PresentationArea):
	def __init__(self) -> None: ...

class StepVisual_AnnotationCurveOccurrenceAndAnnotationOccurrenceAndGeomReprItemAndReprItemAndStyledItem(StepVisual_AnnotationCurveOccurrence):
	def __init__(self) -> None: ...