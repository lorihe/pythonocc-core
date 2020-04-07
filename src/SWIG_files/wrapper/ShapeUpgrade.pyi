from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.TColGeom import *
from OCC.Core.Geom2d import *
from OCC.Core.TColGeom2d import *
from OCC.Core.TopoDS import *
from OCC.Core.TopAbs import *
from OCC.Core.ShapeBuild import *
from OCC.Core.ShapeExtend import *
from OCC.Core.Message import *
from OCC.Core.TColStd import *
from OCC.Core.BRepTools import *
from OCC.Core.TopTools import *
from OCC.Core.GeomAbs import *
from OCC.Core.ShapeAnalysis import *
from OCC.Core.TopLoc import *


class ShapeUpgrade:
	@staticmethod
	def C0BSplineToSequenceOfC1BSplineCurve(self, BS: Geom_BSplineCurve, seqBS: TColGeom_HSequenceOfBoundedCurve) -> bool: ...
	@staticmethod
	def C0BSplineToSequenceOfC1BSplineCurve(self, BS: Geom2d_BSplineCurve, seqBS: TColGeom2d_HSequenceOfBoundedCurve) -> bool: ...

class ShapeUpgrade_RemoveLocations(Standard_Transient):
	def __init__(self) -> None: ...
	def GetResult(self) -> TopoDS_Shape: ...
	def ModifiedShape(self, theInitShape: TopoDS_Shape) -> TopoDS_Shape: ...
	def Remove(self, theShape: TopoDS_Shape) -> bool: ...
	def RemoveLevel(self) -> TopAbs_ShapeEnum: ...
	def SetRemoveLevel(self, theLevel: TopAbs_ShapeEnum) -> None: ...

class ShapeUpgrade_ShapeDivide:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def GetContext(self) -> ShapeBuild_ReShape: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def MsgRegistrator(self) -> ShapeExtend_BasicMsgRegistrator: ...
	def Perform(self, newContext: Optional[bool]) -> bool: ...
	def Result(self) -> TopoDS_Shape: ...
	def SendMsg(self, shape: TopoDS_Shape, message: Message_Msg, gravity: Optional[Message_Gravity]) -> None: ...
	def SetContext(self, context: ShapeBuild_ReShape) -> None: ...
	def SetEdgeMode(self, aEdgeMode: int) -> None: ...
	def SetMaxTolerance(self, maxtol: float) -> None: ...
	def SetMinTolerance(self, mintol: float) -> None: ...
	def SetMsgRegistrator(self, msgreg: ShapeExtend_BasicMsgRegistrator) -> None: ...
	def SetPrecision(self, Prec: float) -> None: ...
	def SetSplitFaceTool(self, splitFaceTool: ShapeUpgrade_FaceDivide) -> None: ...
	def SetSurfaceSegmentMode(self, Segment: bool) -> None: ...
	def Status(self, status: ShapeExtend_Status) -> bool: ...

class ShapeUpgrade_ShellSewing:
	def __init__(self) -> None: ...
	def ApplySewing(self, shape: TopoDS_Shape, tol: Optional[float]) -> TopoDS_Shape: ...

class ShapeUpgrade_SplitCurve(Standard_Transient):
	def __init__(self) -> None: ...
	def Build(self, Segment: bool) -> None: ...
	def Compute(self) -> None: ...
	def Init(self, First: float, Last: float) -> None: ...
	def Perform(self, Segment: Optional[bool]) -> None: ...
	def SetSplitValues(self, SplitValues: TColStd_HSequenceOfReal) -> None: ...
	def SplitValues(self) -> TColStd_HSequenceOfReal: ...
	def Status(self, status: ShapeExtend_Status) -> bool: ...

class ShapeUpgrade_SplitSurface(Standard_Transient):
	def __init__(self) -> None: ...
	def Build(self, Segment: bool) -> None: ...
	def Compute(self, Segment: Optional[bool]) -> None: ...
	def Init(self, S: Geom_Surface) -> None: ...
	def Init(self, S: Geom_Surface, UFirst: float, ULast: float, VFirst: float, VLast: float) -> None: ...
	def Perform(self, Segment: Optional[bool]) -> None: ...
	def ResSurfaces(self) -> ShapeExtend_CompositeSurface: ...
	def SetUSplitValues(self, UValues: TColStd_HSequenceOfReal) -> None: ...
	def SetVSplitValues(self, VValues: TColStd_HSequenceOfReal) -> None: ...
	def Status(self, status: ShapeExtend_Status) -> bool: ...
	def USplitValues(self) -> TColStd_HSequenceOfReal: ...
	def VSplitValues(self) -> TColStd_HSequenceOfReal: ...

class ShapeUpgrade_Tool(Standard_Transient):
	def __init__(self) -> None: ...
	def Context(self) -> ShapeBuild_ReShape: ...
	def LimitTolerance(self, toler: float) -> float: ...
	def MaxTolerance(self) -> float: ...
	def MinTolerance(self) -> float: ...
	def Precision(self) -> float: ...
	def Set(self, tool: ShapeUpgrade_Tool) -> None: ...
	def SetContext(self, context: ShapeBuild_ReShape) -> None: ...
	def SetMaxTolerance(self, maxtol: float) -> None: ...
	def SetMinTolerance(self, mintol: float) -> None: ...
	def SetPrecision(self, preci: float) -> None: ...

class ShapeUpgrade_UnifySameDomain(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aShape: TopoDS_Shape, UnifyEdges: Optional[bool], UnifyFaces: Optional[bool], ConcatBSplines: Optional[bool]) -> None: ...
	def AllowInternalEdges(self, theValue: bool) -> None: ...
	def Build(self) -> None: ...
	def History(self) -> BRepTools_History: ...
	def History(self) -> BRepTools_History: ...
	def Initialize(self, aShape: TopoDS_Shape, UnifyEdges: Optional[bool], UnifyFaces: Optional[bool], ConcatBSplines: Optional[bool]) -> None: ...
	def KeepShape(self, theShape: TopoDS_Shape) -> None: ...
	def KeepShapes(self, theShapes: TopTools_MapOfShape) -> None: ...
	def SetAngularTolerance(self, theValue: float) -> None: ...
	def SetLinearTolerance(self, theValue: float) -> None: ...
	def SetSafeInputMode(self, theValue: bool) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...

class ShapeUpgrade_ConvertSurfaceToBezierBasis(ShapeUpgrade_SplitSurface):
	def __init__(self) -> None: ...
	def Build(self, Segment: bool) -> None: ...
	def Compute(self, Segment: bool) -> None: ...
	def GetBSplineMode(self) -> bool: ...
	def GetExtrusionMode(self) -> bool: ...
	def GetPlaneMode(self) -> bool: ...
	def GetRevolutionMode(self) -> bool: ...
	def Segments(self) -> ShapeExtend_CompositeSurface: ...
	def SetBSplineMode(self, mode: bool) -> None: ...
	def SetExtrusionMode(self, mode: bool) -> None: ...
	def SetPlaneMode(self, mode: bool) -> None: ...
	def SetRevolutionMode(self, mode: bool) -> None: ...

class ShapeUpgrade_EdgeDivide(ShapeUpgrade_Tool):
	def __init__(self) -> None: ...
	def Clear(self) -> None: ...
	def Compute(self, E: TopoDS_Edge) -> bool: ...
	def GetSplitCurve2dTool(self) -> ShapeUpgrade_SplitCurve2d: ...
	def GetSplitCurve3dTool(self) -> ShapeUpgrade_SplitCurve3d: ...
	def HasCurve2d(self) -> bool: ...
	def HasCurve3d(self) -> bool: ...
	def Knots2d(self) -> TColStd_HSequenceOfReal: ...
	def Knots3d(self) -> TColStd_HSequenceOfReal: ...
	def SetFace(self, F: TopoDS_Face) -> None: ...
	def SetSplitCurve2dTool(self, splitCurve2dTool: ShapeUpgrade_SplitCurve2d) -> None: ...
	def SetSplitCurve3dTool(self, splitCurve3dTool: ShapeUpgrade_SplitCurve3d) -> None: ...

class ShapeUpgrade_FaceDivide(ShapeUpgrade_Tool):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, F: TopoDS_Face) -> None: ...
	def GetSplitSurfaceTool(self) -> ShapeUpgrade_SplitSurface: ...
	def GetWireDivideTool(self) -> ShapeUpgrade_WireDivide: ...
	def Init(self, F: TopoDS_Face) -> None: ...
	def Perform(self) -> bool: ...
	def Result(self) -> TopoDS_Shape: ...
	def SetSplitSurfaceTool(self, splitSurfaceTool: ShapeUpgrade_SplitSurface) -> None: ...
	def SetSurfaceSegmentMode(self, Segment: bool) -> None: ...
	def SetWireDivideTool(self, wireDivideTool: ShapeUpgrade_WireDivide) -> None: ...
	def SplitCurves(self) -> bool: ...
	def SplitSurface(self) -> bool: ...
	def Status(self, status: ShapeExtend_Status) -> bool: ...

class ShapeUpgrade_FixSmallCurves(ShapeUpgrade_Tool):
	def __init__(self) -> None: ...
	def Approx(self, Curve3d: Geom_Curve, Curve2d: Geom2d_Curve, Curve2dR: Geom2d_Curve) -> Tuple[bool, float, float]: ...
	def Init(self, theEdge: TopoDS_Edge, theFace: TopoDS_Face) -> None: ...
	def SetSplitCurve2dTool(self, splitCurve2dTool: ShapeUpgrade_SplitCurve2d) -> None: ...
	def SetSplitCurve3dTool(self, splitCurve3dTool: ShapeUpgrade_SplitCurve3d) -> None: ...
	def Status(self, status: ShapeExtend_Status) -> bool: ...

class ShapeUpgrade_RemoveInternalWires(ShapeUpgrade_Tool):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theShape: TopoDS_Shape) -> None: ...
	def GetResult(self) -> TopoDS_Shape: ...
	def Init(self, theShape: TopoDS_Shape) -> None: ...
	def GetMinArea(self) -> float: ...
	def SetMinArea(self, value: float) -> None: ...
	def Perform(self) -> bool: ...
	def Perform(self, theSeqShapes: TopTools_SequenceOfShape) -> bool: ...
	def GetRemoveFaceMode(self) -> bool: ...
	def SetRemoveFaceMode(self, value: bool) -> None: ...
	def RemovedFaces(self) -> TopTools_SequenceOfShape: ...
	def RemovedWires(self) -> TopTools_SequenceOfShape: ...
	def Status(self, theStatus: ShapeExtend_Status) -> bool: ...

class ShapeUpgrade_ShapeConvertToBezier(ShapeUpgrade_ShapeDivide):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def Get2dConversion(self) -> bool: ...
	def Get3dCircleConversion(self) -> bool: ...
	def Get3dConicConversion(self) -> bool: ...
	def Get3dConversion(self) -> bool: ...
	def Get3dLineConversion(self) -> bool: ...
	def GetBSplineMode(self) -> bool: ...
	def GetExtrusionMode(self) -> bool: ...
	def GetPlaneMode(self) -> bool: ...
	def GetRevolutionMode(self) -> bool: ...
	def GetSurfaceConversion(self) -> bool: ...
	def Perform(self, newContext: Optional[bool]) -> bool: ...
	def Set2dConversion(self, mode: bool) -> None: ...
	def Set3dCircleConversion(self, mode: bool) -> None: ...
	def Set3dConicConversion(self, mode: bool) -> None: ...
	def Set3dConversion(self, mode: bool) -> None: ...
	def Set3dLineConversion(self, mode: bool) -> None: ...
	def SetBSplineMode(self, mode: bool) -> None: ...
	def SetExtrusionMode(self, mode: bool) -> None: ...
	def SetPlaneMode(self, mode: bool) -> None: ...
	def SetRevolutionMode(self, mode: bool) -> None: ...
	def SetSurfaceConversion(self, mode: bool) -> None: ...

class ShapeUpgrade_ShapeDivideAngle(ShapeUpgrade_ShapeDivide):
	@overload
	def __init__(self, MaxAngle: float) -> None: ...
	@overload
	def __init__(self, MaxAngle: float, S: TopoDS_Shape) -> None: ...
	def InitTool(self, MaxAngle: float) -> None: ...
	def MaxAngle(self) -> float: ...
	def SetMaxAngle(self, MaxAngle: float) -> None: ...

class ShapeUpgrade_ShapeDivideArea(ShapeUpgrade_ShapeDivide):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def GetMaxArea(self) -> float: ...
	def SetMaxArea(self, value: float) -> None: ...

class ShapeUpgrade_ShapeDivideClosed(ShapeUpgrade_ShapeDivide):
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def SetNbSplitPoints(self, num: int) -> None: ...

class ShapeUpgrade_ShapeDivideClosedEdges(ShapeUpgrade_ShapeDivide):
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def SetNbSplitPoints(self, num: int) -> None: ...

class ShapeUpgrade_ShapeDivideContinuity(ShapeUpgrade_ShapeDivide):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def SetBoundaryCriterion(self, Criterion: Optional[GeomAbs_Shape]) -> None: ...
	def SetPCurveCriterion(self, Criterion: Optional[GeomAbs_Shape]) -> None: ...
	def SetSurfaceCriterion(self, Criterion: Optional[GeomAbs_Shape]) -> None: ...
	def SetTolerance(self, Tol: float) -> None: ...
	def SetTolerance2d(self, Tol: float) -> None: ...

class ShapeUpgrade_SplitCurve2d(ShapeUpgrade_SplitCurve):
	def __init__(self) -> None: ...
	def Build(self, Segment: bool) -> None: ...
	def GetCurves(self) -> TColGeom2d_HArray1OfCurve: ...
	def Init(self, C: Geom2d_Curve) -> None: ...
	def Init(self, C: Geom2d_Curve, First: float, Last: float) -> None: ...

class ShapeUpgrade_SplitCurve3d(ShapeUpgrade_SplitCurve):
	def __init__(self) -> None: ...
	def Build(self, Segment: bool) -> None: ...
	def GetCurves(self) -> TColGeom_HArray1OfCurve: ...
	def Init(self, C: Geom_Curve) -> None: ...
	def Init(self, C: Geom_Curve, First: float, Last: float) -> None: ...

class ShapeUpgrade_SplitSurfaceAngle(ShapeUpgrade_SplitSurface):
	def __init__(self, MaxAngle: float) -> None: ...
	def Compute(self, Segment: bool) -> None: ...
	def MaxAngle(self) -> float: ...
	def SetMaxAngle(self, MaxAngle: float) -> None: ...

class ShapeUpgrade_SplitSurfaceArea(ShapeUpgrade_SplitSurface):
	def __init__(self) -> None: ...
	def Compute(self, Segment: Optional[bool]) -> None: ...
	def GetNbParts(self) -> int: ...
	def SetNbParts(self, value: int) -> None: ...

class ShapeUpgrade_SplitSurfaceContinuity(ShapeUpgrade_SplitSurface):
	def __init__(self) -> None: ...
	def Compute(self, Segment: bool) -> None: ...
	def SetCriterion(self, Criterion: GeomAbs_Shape) -> None: ...
	def SetTolerance(self, Tol: float) -> None: ...

class ShapeUpgrade_WireDivide(ShapeUpgrade_Tool):
	def __init__(self) -> None: ...
	def GetEdgeDivideTool(self) -> ShapeUpgrade_EdgeDivide: ...
	def GetFixSmallCurveTool(self) -> ShapeUpgrade_FixSmallCurves: ...
	def GetTransferParamTool(self) -> ShapeAnalysis_TransferParameters: ...
	def Init(self, W: TopoDS_Wire, F: TopoDS_Face) -> None: ...
	def Init(self, W: TopoDS_Wire, S: Geom_Surface) -> None: ...
	def Load(self, W: TopoDS_Wire) -> None: ...
	def Load(self, E: TopoDS_Edge) -> None: ...
	def Perform(self) -> None: ...
	def SetEdgeDivideTool(self, edgeDivideTool: ShapeUpgrade_EdgeDivide) -> None: ...
	def SetEdgeMode(self, EdgeMode: int) -> None: ...
	def SetFace(self, F: TopoDS_Face) -> None: ...
	def SetFixSmallCurveTool(self, FixSmallCurvesTool: ShapeUpgrade_FixSmallCurves) -> None: ...
	def SetSplitCurve2dTool(self, splitCurve2dTool: ShapeUpgrade_SplitCurve2d) -> None: ...
	def SetSplitCurve3dTool(self, splitCurve3dTool: ShapeUpgrade_SplitCurve3d) -> None: ...
	def SetSurface(self, S: Geom_Surface) -> None: ...
	def SetSurface(self, S: Geom_Surface, L: TopLoc_Location) -> None: ...
	def SetTransferParamTool(self, TransferParam: ShapeAnalysis_TransferParameters) -> None: ...
	def Status(self, status: ShapeExtend_Status) -> bool: ...
	def Wire(self) -> TopoDS_Wire: ...

class ShapeUpgrade_ClosedEdgeDivide(ShapeUpgrade_EdgeDivide):
	def __init__(self) -> None: ...
	def Compute(self, anEdge: TopoDS_Edge) -> bool: ...

class ShapeUpgrade_ClosedFaceDivide(ShapeUpgrade_FaceDivide):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, F: TopoDS_Face) -> None: ...
	def GetNbSplitPoints(self) -> int: ...
	def SetNbSplitPoints(self, num: int) -> None: ...
	def SplitSurface(self) -> bool: ...

class ShapeUpgrade_ConvertCurve2dToBezier(ShapeUpgrade_SplitCurve2d):
	def __init__(self) -> None: ...
	def Build(self, Segment: bool) -> None: ...
	def Compute(self) -> None: ...
	def SplitParams(self) -> TColStd_HSequenceOfReal: ...

class ShapeUpgrade_ConvertCurve3dToBezier(ShapeUpgrade_SplitCurve3d):
	def __init__(self) -> None: ...
	def Build(self, Segment: bool) -> None: ...
	def Compute(self) -> None: ...
	def GetCircleMode(self) -> bool: ...
	def GetConicMode(self) -> bool: ...
	def GetLineMode(self) -> bool: ...
	def SetCircleMode(self, mode: bool) -> None: ...
	def SetConicMode(self, mode: bool) -> None: ...
	def SetLineMode(self, mode: bool) -> None: ...
	def SplitParams(self) -> TColStd_HSequenceOfReal: ...

class ShapeUpgrade_FaceDivideArea(ShapeUpgrade_FaceDivide):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, F: TopoDS_Face) -> None: ...
	def GetMaxArea(self) -> float: ...
	def SetMaxArea(self, value: float) -> None: ...
	def Perform(self) -> bool: ...

class ShapeUpgrade_FixSmallBezierCurves(ShapeUpgrade_FixSmallCurves):
	def __init__(self) -> None: ...
	def Approx(self, Curve3d: Geom_Curve, Curve2d: Geom2d_Curve, Curve2dR: Geom2d_Curve) -> Tuple[bool, float, float]: ...

class ShapeUpgrade_SplitCurve2dContinuity(ShapeUpgrade_SplitCurve2d):
	def __init__(self) -> None: ...
	def Compute(self) -> None: ...
	def SetCriterion(self, Criterion: GeomAbs_Shape) -> None: ...
	def SetTolerance(self, Tol: float) -> None: ...

class ShapeUpgrade_SplitCurve3dContinuity(ShapeUpgrade_SplitCurve3d):
	def __init__(self) -> None: ...
	def Compute(self) -> None: ...
	def GetCurve(self) -> Geom_Curve: ...
	def SetCriterion(self, Criterion: GeomAbs_Shape) -> None: ...
	def SetTolerance(self, Tol: float) -> None: ...
