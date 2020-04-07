from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BRepAdaptor import *
from OCC.Core.TopoDS import *
from OCC.Core.gp import *
from OCC.Core.Geom import *
from OCC.Core.TopAbs import *
from OCC.Core.Bnd import *
from OCC.Core.Geom2dHatch import *
from OCC.Core.GeomAPI import *
from OCC.Core.BRepClass3d import *
from OCC.Core.Geom2d import *
from OCC.Core.GeomAbs import *
from OCC.Core.IntSurf import *
from OCC.Core.TColStd import *
from OCC.Core.Adaptor3d import *
from OCC.Core.IntPatch import *
from OCC.Core.GeomAdaptor import *
from OCC.Core.GeomInt import *


class IntTools:
	@staticmethod
	def FindRootStates(self, aSeq: IntTools_SequenceOfRoots, anEpsNull: float) -> None: ...
	@staticmethod
	def GetRadius(self, C: BRepAdaptor_Curve, t1: float, t3: float) -> Tuple[int, float]: ...
	@staticmethod
	def Length(self, E: TopoDS_Edge) -> float: ...
	@staticmethod
	def Parameter(self, P: gp_Pnt, Curve: Geom_Curve) -> Tuple[int, float]: ...
	@staticmethod
	def PrepareArgs(self, C: BRepAdaptor_Curve, tMax: float, tMin: float, Discret: int, Deflect: float, anArgs: IntTools_CArray1OfReal) -> int: ...
	@staticmethod
	def RemoveIdenticalRoots(self, aSeq: IntTools_SequenceOfRoots, anEpsT: float) -> None: ...
	@staticmethod
	def SortRoots(self, aSeq: IntTools_SequenceOfRoots, anEpsT: float) -> None: ...

class IntTools_BaseRangeSample:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theDepth: int) -> None: ...
	def GetDepth(self) -> int: ...
	def SetDepth(self, theDepth: int) -> None: ...

class IntTools_BeanFaceIntersector:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theEdge: TopoDS_Edge, theFace: TopoDS_Face) -> None: ...
	@overload
	def __init__(self, theCurve: BRepAdaptor_Curve, theSurface: BRepAdaptor_Surface, theBeanTolerance: float, theFaceTolerance: float) -> None: ...
	@overload
	def __init__(self, theCurve: BRepAdaptor_Curve, theSurface: BRepAdaptor_Surface, theFirstParOnCurve: float, theLastParOnCurve: float, theUMinParameter: float, theUMaxParameter: float, theVMinParameter: float, theVMaxParameter: float, theBeanTolerance: float, theFaceTolerance: float) -> None: ...
	def Context(self) -> IntTools_Context: ...
	def Init(self, theEdge: TopoDS_Edge, theFace: TopoDS_Face) -> None: ...
	def Init(self, theCurve: BRepAdaptor_Curve, theSurface: BRepAdaptor_Surface, theBeanTolerance: float, theFaceTolerance: float) -> None: ...
	def Init(self, theCurve: BRepAdaptor_Curve, theSurface: BRepAdaptor_Surface, theFirstParOnCurve: float, theLastParOnCurve: float, theUMinParameter: float, theUMaxParameter: float, theVMinParameter: float, theVMaxParameter: float, theBeanTolerance: float, theFaceTolerance: float) -> None: ...
	def IsDone(self) -> bool: ...
	def Perform(self) -> None: ...
	def Result(self) -> IntTools_SequenceOfRanges: ...
	def Result(self, theResults: IntTools_SequenceOfRanges) -> None: ...
	def SetBeanParameters(self, theFirstParOnCurve: float, theLastParOnCurve: float) -> None: ...
	def SetContext(self, theContext: IntTools_Context) -> None: ...
	def SetSurfaceParameters(self, theUMinParameter: float, theUMaxParameter: float, theVMinParameter: float, theVMaxParameter: float) -> None: ...

class IntTools_CommonPrt:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aCPrt: IntTools_CommonPrt) -> None: ...
	def AllNullFlag(self) -> bool: ...
	def AppendRange2(self, aR: IntTools_Range) -> None: ...
	def AppendRange2(self, tf: float, tl: float) -> None: ...
	def Assign(self, Other: IntTools_CommonPrt) -> IntTools_CommonPrt: ...
	def BoundingPoints(self, aP1: gp_Pnt, aP2: gp_Pnt) -> None: ...
	def ChangeRanges2(self) -> IntTools_SequenceOfRanges: ...
	def Copy(self, anOther: IntTools_CommonPrt) -> None: ...
	def Edge1(self) -> TopoDS_Edge: ...
	def Edge2(self) -> TopoDS_Edge: ...
	def Range1(self) -> IntTools_Range: ...
	def Range1(self) -> Tuple[float, float]: ...
	def Ranges2(self) -> IntTools_SequenceOfRanges: ...
	def SetAllNullFlag(self, aFlag: bool) -> None: ...
	def SetBoundingPoints(self, aP1: gp_Pnt, aP2: gp_Pnt) -> None: ...
	def SetEdge1(self, anE: TopoDS_Edge) -> None: ...
	def SetEdge2(self, anE: TopoDS_Edge) -> None: ...
	def SetRange1(self, aR: IntTools_Range) -> None: ...
	def SetRange1(self, tf: float, tl: float) -> None: ...
	def SetType(self, aType: TopAbs_ShapeEnum) -> None: ...
	def SetVertexParameter1(self, tV: float) -> None: ...
	def SetVertexParameter2(self, tV: float) -> None: ...
	def Type(self) -> TopAbs_ShapeEnum: ...
	def VertexParameter1(self) -> float: ...
	def VertexParameter2(self) -> float: ...

class IntTools_Context(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
	def BndBox(self, theS: TopoDS_Shape) -> Bnd_Box: ...
	def ComputePE(self, theP: gp_Pnt, theTolP: float, theE: TopoDS_Edge) -> Tuple[int, float, float]: ...
	def ComputeVE(self, theV: TopoDS_Vertex, theE: TopoDS_Edge, theFuzz: Optional[float]) -> Tuple[int, float, float]: ...
	def ComputeVF(self, theVertex: TopoDS_Vertex, theFace: TopoDS_Face, theFuzz: Optional[float]) -> Tuple[int, float, float, float]: ...
	def FClass2d(self, aF: TopoDS_Face) -> IntTools_FClass2d: ...
	def Hatcher(self, aF: TopoDS_Face) -> Geom2dHatch_Hatcher: ...
	def IsInfiniteFace(self, theFace: TopoDS_Face) -> bool: ...
	def IsPointInFace(self, aF: TopoDS_Face, aP2D: gp_Pnt2d) -> bool: ...
	def IsPointInFace(self, aP3D: gp_Pnt, aF: TopoDS_Face, aTol: float) -> bool: ...
	def IsPointInOnFace(self, aF: TopoDS_Face, aP2D: gp_Pnt2d) -> bool: ...
	def IsValidBlockForFace(self, aT1: float, aT2: float, aIC: IntTools_Curve, aF: TopoDS_Face, aTol: float) -> bool: ...
	def IsValidBlockForFaces(self, aT1: float, aT2: float, aIC: IntTools_Curve, aF1: TopoDS_Face, aF2: TopoDS_Face, aTol: float) -> bool: ...
	def IsValidPointForFace(self, aP3D: gp_Pnt, aF: TopoDS_Face, aTol: float) -> bool: ...
	def IsValidPointForFaces(self, aP3D: gp_Pnt, aF1: TopoDS_Face, aF2: TopoDS_Face, aTol: float) -> bool: ...
	def IsVertexOnLine(self, aV: TopoDS_Vertex, aIC: IntTools_Curve, aTolC: float) -> Tuple[bool, float]: ...
	def IsVertexOnLine(self, aV: TopoDS_Vertex, aTolV: float, aIC: IntTools_Curve, aTolC: float) -> Tuple[bool, float]: ...
	def OBB(self, theShape: TopoDS_Shape, theFuzzyValue: Optional[float]) -> Bnd_OBB: ...
	def ProjPC(self, aE: TopoDS_Edge) -> GeomAPI_ProjectPointOnCurve: ...
	def ProjPS(self, aF: TopoDS_Face) -> GeomAPI_ProjectPointOnSurf: ...
	def ProjPT(self, aC: Geom_Curve) -> GeomAPI_ProjectPointOnCurve: ...
	def ProjectPointOnEdge(self, aP: gp_Pnt, aE: TopoDS_Edge) -> Tuple[bool, float]: ...
	def SetPOnSProjectionTolerance(self, theValue: float) -> None: ...
	def SolidClassifier(self, aSolid: TopoDS_Solid) -> BRepClass3d_SolidClassifier: ...
	def StatePointFace(self, aF: TopoDS_Face, aP2D: gp_Pnt2d) -> TopAbs_State: ...
	def SurfaceAdaptor(self, theFace: TopoDS_Face) -> BRepAdaptor_Surface: ...
	def SurfaceData(self, aF: TopoDS_Face) -> IntTools_SurfaceRangeLocalizeData: ...
	def UVBounds(self, theFace: TopoDS_Face) -> Tuple[float, float, float, float]: ...

class IntTools_Curve:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, the3dCurve3d: Geom_Curve, the2dCurve1: Geom2d_Curve, the2dCurve2: Geom2d_Curve, theTolerance: Optional[float], theTangentialTolerance: Optional[float]) -> None: ...
	def Bounds(self, theFirstPnt: gp_Pnt, theLastPnt: gp_Pnt) -> Tuple[bool, float, float]: ...
	def Curve(self) -> Geom_Curve: ...
	def D0(self, thePar: float, thePnt: gp_Pnt) -> bool: ...
	def FirstCurve2d(self) -> Geom2d_Curve: ...
	def HasBounds(self) -> bool: ...
	def SecondCurve2d(self) -> Geom2d_Curve: ...
	def SetCurve(self, the3dCurve: Geom_Curve) -> None: ...
	def SetCurves(self, the3dCurve: Geom_Curve, the2dCurve1: Geom2d_Curve, the2dCurve2: Geom2d_Curve) -> None: ...
	def SetFirstCurve2d(self, the2dCurve1: Geom2d_Curve) -> None: ...
	def SetSecondCurve2d(self, the2dCurve2: Geom2d_Curve) -> None: ...
	def SetTangentialTolerance(self, theTangentialTolerance: float) -> None: ...
	def SetTolerance(self, theTolerance: float) -> None: ...
	def TangentialTolerance(self) -> float: ...
	def Tolerance(self) -> float: ...
	def Type(self) -> GeomAbs_CurveType: ...

class IntTools_CurveRangeLocalizeData:
	def __init__(self, theNbSample: int, theMinRange: float) -> None: ...
	def AddBox(self, theRange: IntTools_CurveRangeSample, theBox: Bnd_Box) -> None: ...
	def AddOutRange(self, theRange: IntTools_CurveRangeSample) -> None: ...
	def FindBox(self, theRange: IntTools_CurveRangeSample, theBox: Bnd_Box) -> bool: ...
	def GetMinRange(self) -> float: ...
	def GetNbSample(self) -> int: ...
	def IsRangeOut(self, theRange: IntTools_CurveRangeSample) -> bool: ...
	def ListRangeOut(self, theList: IntTools_ListOfCurveRangeSample) -> None: ...

class IntTools_CurveRangeSampleMapHasher:
	@staticmethod
	def HashCode(self, theKey: IntTools_CurveRangeSample, theUpperBound: int) -> int: ...
	@staticmethod
	def IsEqual(self, S1: IntTools_CurveRangeSample, S2: IntTools_CurveRangeSample) -> bool: ...

class IntTools_EdgeEdge:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theEdge1: TopoDS_Edge, theEdge2: TopoDS_Edge) -> None: ...
	@overload
	def __init__(self, theEdge1: TopoDS_Edge, aT11: float, aT12: float, theEdge2: TopoDS_Edge, aT21: float, aT22: float) -> None: ...
	def CommonParts(self) -> IntTools_SequenceOfCommonPrts: ...
	def FuzzyValue(self) -> float: ...
	def IsCoincidenceCheckedQuickly(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def Perform(self) -> None: ...
	def SetEdge1(self, theEdge: TopoDS_Edge) -> None: ...
	def SetEdge1(self, theEdge: TopoDS_Edge, aT1: float, aT2: float) -> None: ...
	def SetEdge2(self, theEdge: TopoDS_Edge) -> None: ...
	def SetEdge2(self, theEdge: TopoDS_Edge, aT1: float, aT2: float) -> None: ...
	def SetFuzzyValue(self, theFuzz: float) -> None: ...
	def SetRange1(self, theRange1: IntTools_Range) -> None: ...
	def SetRange1(self, aT1: float, aT2: float) -> None: ...
	def SetRange2(self, theRange: IntTools_Range) -> None: ...
	def SetRange2(self, aT1: float, aT2: float) -> None: ...
	def UseQuickCoincidenceCheck(self, bFlag: bool) -> None: ...

class IntTools_EdgeFace:
	def __init__(self) -> None: ...
	def CommonParts(self) -> IntTools_SequenceOfCommonPrts: ...
	def Context(self) -> IntTools_Context: ...
	def Edge(self) -> TopoDS_Edge: ...
	def ErrorStatus(self) -> int: ...
	def Face(self) -> TopoDS_Face: ...
	def FuzzyValue(self) -> float: ...
	def IsCoincidenceCheckedQuickly(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def Perform(self) -> None: ...
	def Range(self) -> IntTools_Range: ...
	def SetContext(self, theContext: IntTools_Context) -> None: ...
	def SetEdge(self, theEdge: TopoDS_Edge) -> None: ...
	def SetFace(self, theFace: TopoDS_Face) -> None: ...
	def SetFuzzyValue(self, theFuzz: float) -> None: ...
	def SetRange(self, theRange: IntTools_Range) -> None: ...
	def SetRange(self, theFirst: float, theLast: float) -> None: ...
	def UseQuickCoincidenceCheck(self, theFlag: bool) -> None: ...

class IntTools_FClass2d:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, F: TopoDS_Face, Tol: float) -> None: ...
	def Destroy(self) -> None: ...
	def Init(self, F: TopoDS_Face, Tol: float) -> None: ...
	def IsHole(self) -> bool: ...
	def Perform(self, Puv: gp_Pnt2d, RecadreOnPeriodic: Optional[bool]) -> TopAbs_State: ...
	def PerformInfinitePoint(self) -> TopAbs_State: ...
	def TestOnRestriction(self, Puv: gp_Pnt2d, Tol: float, RecadreOnPeriodic: Optional[bool]) -> TopAbs_State: ...

class IntTools_FaceFace:
	def __init__(self) -> None: ...
	def Context(self) -> IntTools_Context: ...
	def Face1(self) -> TopoDS_Face: ...
	def Face2(self) -> TopoDS_Face: ...
	def FuzzyValue(self) -> float: ...
	def IsDone(self) -> bool: ...
	def Lines(self) -> IntTools_SequenceOfCurves: ...
	def Perform(self, F1: TopoDS_Face, F2: TopoDS_Face) -> None: ...
	def Points(self) -> IntTools_SequenceOfPntOn2Faces: ...
	def PrepareLines3D(self, bToSplit: Optional[bool]) -> None: ...
	def SetContext(self, aContext: IntTools_Context) -> None: ...
	def SetFuzzyValue(self, theFuzz: float) -> None: ...
	def SetList(self, ListOfPnts: IntSurf_ListOfPntOn2S) -> None: ...
	def SetParameters(self, ApproxCurves: bool, ComputeCurveOnS1: bool, ComputeCurveOnS2: bool, ApproximationTolerance: float) -> None: ...
	def TangentFaces(self) -> bool: ...

class IntTools_MarkedRangeSet:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theFirstBoundary: float, theLastBoundary: float, theInitFlag: int) -> None: ...
	@overload
	def __init__(self, theSortedArray: IntTools_CArray1OfReal, theInitFlag: int) -> None: ...
	def Flag(self, theIndex: int) -> int: ...
	def GetIndex(self, theValue: float) -> int: ...
	def GetIndex(self, theValue: float, UseLower: bool) -> int: ...
	def GetIndices(self, theValue: float) -> TColStd_SequenceOfInteger: ...
	def InsertRange(self, theFirstBoundary: float, theLastBoundary: float, theFlag: int) -> bool: ...
	def InsertRange(self, theRange: IntTools_Range, theFlag: int) -> bool: ...
	def InsertRange(self, theFirstBoundary: float, theLastBoundary: float, theFlag: int, theIndex: int) -> bool: ...
	def InsertRange(self, theRange: IntTools_Range, theFlag: int, theIndex: int) -> bool: ...
	def Length(self) -> int: ...
	def Range(self, theIndex: int) -> IntTools_Range: ...
	def SetBoundaries(self, theFirstBoundary: float, theLastBoundary: float, theInitFlag: int) -> None: ...
	def SetFlag(self, theIndex: int, theFlag: int) -> None: ...
	def SetRanges(self, theSortedArray: IntTools_CArray1OfReal, theInitFlag: int) -> None: ...

class IntTools_PntOn2Faces:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aP1: IntTools_PntOnFace, aP2: IntTools_PntOnFace) -> None: ...
	def IsValid(self) -> bool: ...
	def P1(self) -> IntTools_PntOnFace: ...
	def P2(self) -> IntTools_PntOnFace: ...
	def SetP1(self, aP1: IntTools_PntOnFace) -> None: ...
	def SetP2(self, aP2: IntTools_PntOnFace) -> None: ...
	def SetValid(self, bF: bool) -> None: ...

class IntTools_PntOnFace:
	def __init__(self) -> None: ...
	def Face(self) -> TopoDS_Face: ...
	def Init(self, aF: TopoDS_Face, aP: gp_Pnt, U: float, V: float) -> None: ...
	def Parameters(self) -> Tuple[float, float]: ...
	def Pnt(self) -> gp_Pnt: ...
	def SetFace(self, aF: TopoDS_Face) -> None: ...
	def SetParameters(self, U: float, V: float) -> None: ...
	def SetPnt(self, aP: gp_Pnt) -> None: ...
	def SetValid(self, bF: bool) -> None: ...
	def Valid(self) -> bool: ...

class IntTools_Range:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aFirst: float, aLast: float) -> None: ...
	def First(self) -> float: ...
	def Last(self) -> float: ...
	def Range(self) -> Tuple[float, float]: ...
	def SetFirst(self, aFirst: float) -> None: ...
	def SetLast(self, aLast: float) -> None: ...

class IntTools_Root:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aRoot: float, aType: int) -> None: ...
	def Interval(self) -> Tuple[float, float, float, float]: ...
	def IsValid(self) -> bool: ...
	def LayerHeight(self) -> float: ...
	def Root(self) -> float: ...
	def SetInterval(self, t1: float, t2: float, f1: float, f2: float) -> None: ...
	def SetLayerHeight(self, aHeight: float) -> None: ...
	def SetRoot(self, aRoot: float) -> None: ...
	def SetStateAfter(self, aState: TopAbs_State) -> None: ...
	def SetStateBefore(self, aState: TopAbs_State) -> None: ...
	def SetType(self, aType: int) -> None: ...
	def StateAfter(self) -> TopAbs_State: ...
	def StateBefore(self) -> TopAbs_State: ...
	def Type(self) -> int: ...

class IntTools_ShrunkRange:
	def __init__(self) -> None: ...
	def BndBox(self) -> Bnd_Box: ...
	def Context(self) -> IntTools_Context: ...
	def Edge(self) -> TopoDS_Edge: ...
	def IsDone(self) -> bool: ...
	def IsSplittable(self) -> bool: ...
	def Length(self) -> float: ...
	def Perform(self) -> None: ...
	def SetContext(self, aCtx: IntTools_Context) -> None: ...
	def SetData(self, aE: TopoDS_Edge, aT1: float, aT2: float, aV1: TopoDS_Vertex, aV2: TopoDS_Vertex) -> None: ...
	def SetShrunkRange(self, aT1: float, aT2: float) -> None: ...
	def ShrunkRange(self) -> Tuple[float, float]: ...

class IntTools_SurfaceRangeLocalizeData:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theNbSampleU: int, theNbSampleV: int, theMinRangeU: float, theMinRangeV: float) -> None: ...
	@overload
	def __init__(self, Other: IntTools_SurfaceRangeLocalizeData) -> None: ...
	def AddBox(self, theRange: IntTools_SurfaceRangeSample, theBox: Bnd_Box) -> None: ...
	def AddOutRange(self, theRange: IntTools_SurfaceRangeSample) -> None: ...
	def Assign(self, Other: IntTools_SurfaceRangeLocalizeData) -> IntTools_SurfaceRangeLocalizeData: ...
	def ClearGrid(self) -> None: ...
	def FindBox(self, theRange: IntTools_SurfaceRangeSample, theBox: Bnd_Box) -> bool: ...
	def GetGridDeflection(self) -> float: ...
	def GetGridPoint(self, theUIndex: int, theVIndex: int) -> gp_Pnt: ...
	def GetMinRangeU(self) -> float: ...
	def GetMinRangeV(self) -> float: ...
	def GetNBUPointsInFrame(self) -> int: ...
	def GetNBVPointsInFrame(self) -> int: ...
	def GetNbSampleU(self) -> int: ...
	def GetNbSampleV(self) -> int: ...
	def GetPointInFrame(self, theUIndex: int, theVIndex: int) -> gp_Pnt: ...
	def GetRangeUGrid(self) -> int: ...
	def GetRangeVGrid(self) -> int: ...
	def GetUParam(self, theIndex: int) -> float: ...
	def GetUParamInFrame(self, theIndex: int) -> float: ...
	def GetVParam(self, theIndex: int) -> float: ...
	def GetVParamInFrame(self, theIndex: int) -> float: ...
	def IsRangeOut(self, theRange: IntTools_SurfaceRangeSample) -> bool: ...
	def ListRangeOut(self, theList: IntTools_ListOfSurfaceRangeSample) -> None: ...
	def RemoveRangeOutAll(self) -> None: ...
	def SetFrame(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float) -> None: ...
	def SetGridDeflection(self, theDeflection: float) -> None: ...
	def SetGridPoint(self, theUIndex: int, theVIndex: int, thePoint: gp_Pnt) -> None: ...
	def SetRangeUGrid(self, theNbUGrid: int) -> None: ...
	def SetRangeVGrid(self, theNbVGrid: int) -> None: ...
	def SetUParam(self, theIndex: int, theUParam: float) -> None: ...
	def SetVParam(self, theIndex: int, theVParam: float) -> None: ...

class IntTools_SurfaceRangeSample:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theIndexU: int, theDepthU: int, theIndexV: int, theDepthV: int) -> None: ...
	@overload
	def __init__(self, theRangeU: IntTools_CurveRangeSample, theRangeV: IntTools_CurveRangeSample) -> None: ...
	@overload
	def __init__(self, Other: IntTools_SurfaceRangeSample) -> None: ...
	def Assign(self, Other: IntTools_SurfaceRangeSample) -> IntTools_SurfaceRangeSample: ...
	def GetDepthU(self) -> int: ...
	def GetDepthV(self) -> int: ...
	def GetDepths(self) -> Tuple[int, int]: ...
	def GetIndexU(self) -> int: ...
	def GetIndexV(self) -> int: ...
	def GetIndexes(self) -> Tuple[int, int]: ...
	def GetRangeIndexUDeeper(self, theNbSampleU: int) -> int: ...
	def GetRangeIndexVDeeper(self, theNbSampleV: int) -> int: ...
	def GetRangeU(self, theFirstU: float, theLastU: float, theNbSampleU: int) -> IntTools_Range: ...
	def GetRangeV(self, theFirstV: float, theLastV: float, theNbSampleV: int) -> IntTools_Range: ...
	def GetRanges(self, theRangeU: IntTools_CurveRangeSample, theRangeV: IntTools_CurveRangeSample) -> None: ...
	def GetSampleRangeU(self) -> IntTools_CurveRangeSample: ...
	def GetSampleRangeV(self) -> IntTools_CurveRangeSample: ...
	def IsEqual(self, Other: IntTools_SurfaceRangeSample) -> bool: ...
	def SetDepthU(self, theDepthU: int) -> None: ...
	def SetDepthV(self, theDepthV: int) -> None: ...
	def SetIndexU(self, theIndexU: int) -> None: ...
	def SetIndexV(self, theIndexV: int) -> None: ...
	def SetIndexes(self, theIndexU: int, theIndexV: int) -> None: ...
	def SetRanges(self, theRangeU: IntTools_CurveRangeSample, theRangeV: IntTools_CurveRangeSample) -> None: ...
	def SetSampleRangeU(self, theRangeSampleU: IntTools_CurveRangeSample) -> None: ...
	def SetSampleRangeV(self, theRangeSampleV: IntTools_CurveRangeSample) -> None: ...

class IntTools_SurfaceRangeSampleMapHasher:
	@staticmethod
	def HashCode(self, theKey: IntTools_SurfaceRangeSample, theUpperBound: int) -> int: ...
	@staticmethod
	def IsEqual(self, S1: IntTools_SurfaceRangeSample, S2: IntTools_SurfaceRangeSample) -> bool: ...

class IntTools_Tools:
	@staticmethod
	def CheckCurve(self, theCurve: IntTools_Curve, theBox: Bnd_Box) -> bool: ...
	@staticmethod
	def ClassifyPointByFace(self, aF: TopoDS_Face, P: gp_Pnt2d) -> TopAbs_State: ...
	@staticmethod
	def ComputeIntRange(self, theTol1: float, theTol2: float, theAngle: float) -> float: ...
	@staticmethod
	def ComputeTolerance(self, theCurve3D: Geom_Curve, theCurve2D: Geom2d_Curve, theSurf: Geom_Surface, theFirst: float, theLast: float, theTolRange: Optional[float]) -> Tuple[bool, float, float]: ...
	@staticmethod
	def ComputeVV(self, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> int: ...
	@staticmethod
	def CurveTolerance(self, aC: Geom_Curve, aTolBase: float) -> float: ...
	@staticmethod
	def HasInternalEdge(self, aW: TopoDS_Wire) -> bool: ...
	@staticmethod
	def IntermediatePoint(self, aFirst: float, aLast: float) -> float: ...
	@staticmethod
	def IsClosed(self, aC: Geom_Curve) -> bool: ...
	@staticmethod
	def IsDirsCoinside(self, D1: gp_Dir, D2: gp_Dir) -> bool: ...
	@staticmethod
	def IsDirsCoinside(self, D1: gp_Dir, D2: gp_Dir, aTol: float) -> bool: ...
	@staticmethod
	def IsInRange(self, theRRef: IntTools_Range, theR: IntTools_Range, theTol: float) -> bool: ...
	@staticmethod
	def IsMiddlePointsEqual(self, E1: TopoDS_Edge, E2: TopoDS_Edge) -> bool: ...
	@staticmethod
	def IsOnPave(self, theT: float, theRange: IntTools_Range, theTol: float) -> bool: ...
	@staticmethod
	def IsOnPave1(self, theT: float, theRange: IntTools_Range, theTol: float) -> bool: ...
	@staticmethod
	def IsVertex(self, E: TopoDS_Edge, t: float) -> bool: ...
	@staticmethod
	def IsVertex(self, E: TopoDS_Edge, V: TopoDS_Vertex, t: float) -> bool: ...
	@staticmethod
	def IsVertex(self, aCmnPrt: IntTools_CommonPrt) -> bool: ...
	@staticmethod
	def IsVertex(self, aP: gp_Pnt, aTolPV: float, aV: TopoDS_Vertex) -> bool: ...
	@staticmethod
	def MakeFaceFromWireAndFace(self, aW: TopoDS_Wire, aF: TopoDS_Face, aFNew: TopoDS_Face) -> None: ...
	@staticmethod
	def RejectLines(self, aSIn: IntTools_SequenceOfCurves, aSOut: IntTools_SequenceOfCurves) -> None: ...
	@staticmethod
	def SegPln(self, theLin: gp_Lin, theTLin1: float, theTLin2: float, theTolLin: float, thePln: gp_Pln, theTolPln: float, theP: gp_Pnt) -> Tuple[int, float, float, float, float]: ...
	@staticmethod
	def SplitCurve(self, aC: IntTools_Curve, aS: IntTools_SequenceOfCurves) -> int: ...
	@staticmethod
	def VertexParameter(self, theCP: IntTools_CommonPrt) -> float: ...
	@staticmethod
	def VertexParameters(self, theCP: IntTools_CommonPrt) -> Tuple[float, float]: ...

class IntTools_TopolTool(Adaptor3d_TopolTool):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theSurface: Adaptor3d_HSurface) -> None: ...
	def ComputeSamplePoints(self) -> None: ...
	def Initialize(self) -> None: ...
	def Initialize(self, theSurface: Adaptor3d_HSurface) -> None: ...
	def NbSamples(self) -> int: ...
	def NbSamplesU(self) -> int: ...
	def NbSamplesV(self) -> int: ...
	def SamplePnts(self, theDefl: float, theNUmin: int, theNVmin: int) -> None: ...
	def SamplePoint(self, Index: int, P2d: gp_Pnt2d, P3d: gp_Pnt) -> None: ...

class IntTools_WLineTool:
	@staticmethod
	def NotUseSurfacesForApprox(self, aF1: TopoDS_Face, aF2: TopoDS_Face, WL: IntPatch_WLine, ifprm: int, ilprm: int) -> bool: ...

class IntTools_CurveRangeSample(IntTools_BaseRangeSample):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theIndex: int) -> None: ...
	def GetRange(self, theFirst: float, theLast: float, theNbSample: int) -> IntTools_Range: ...
	def GetRangeIndex(self) -> int: ...
	def GetRangeIndexDeeper(self, theNbSample: int) -> int: ...
	def IsEqual(self, Other: IntTools_CurveRangeSample) -> bool: ...
	def SetRangeIndex(self, theIndex: int) -> None: ...

#classnotwrapped
class IntTools_CArray1OfInteger:
	pass

#classnotwrapped
class IntTools_CArray1OfReal:
	pass
