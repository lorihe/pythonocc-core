from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *

BVH_Constants_MaxTreeDepth = .BVH_Constants_MaxTreeDepth
BVH_Constants_LeafNodeSizeSingle = .BVH_Constants_LeafNodeSizeSingle
BVH_Constants_LeafNodeSizeAverage = .BVH_Constants_LeafNodeSizeAverage
BVH_Constants_LeafNodeSizeDefault = .BVH_Constants_LeafNodeSizeDefault
BVH_Constants_LeafNodeSizeSmall = .BVH_Constants_LeafNodeSizeSmall
BVH_Constants_NbBinsOptimal = .BVH_Constants_NbBinsOptimal
BVH_Constants_NbBinsBest = .BVH_Constants_NbBinsBest

class BVH_AxisSelector:
	@staticmethod
	def MainAxis(self, theSize: BVH_VecNt) -> int: ...

class BVH_Tree():
	def __init__(self) -> None: ...
	def AddInnerNode(self, theMinPoint: BVH_VecNt, theMaxPoint: BVH_VecNt, theLftChild: int, theRghChild: int) -> False: ...
	def AddInnerNode(self, theLftChild: int, theRghChild: int) -> False: ...
	def AddLeafNode(self, theMinPoint: BVH_VecNt, theMaxPoint: BVH_VecNt, theBegElem: int, theEndElem: int) -> False: ...
	def AddLeafNode(self, theBegElem: int, theEndElem: int) -> False: ...
	def Clear(self) -> None: ...
	def CollapseToQuadTree(self) -> False: ...
	def EstimateSAH(self) -> False: ...
	def Reserve(self, theNbNodes: int) -> None: ...
	def SetInner(self, theNodeIndex: int) -> None: ...
	def SetOuter(self, theNodeIndex: int) -> None: ...

class BVH_Tree():
	def __init__(self) -> None: ...

#classnotwrapped
class BVH_Tools:
	pass

#classnotwrapped
class BVH_BuildTool:
	pass

#classnotwrapped
class BVH_BuildThread:
	pass

#classnotwrapped
class BVH_Sorter:
	pass

#classnotwrapped
class BVH_ObjectSet:
	pass

#classnotwrapped
class BVH_Box:
	pass

#classnotwrapped
class CenterAxis:
	pass

#classnotwrapped
class SurfaceCalculator:
	pass

#classnotwrapped
class BoxMinMax:
	pass

#classnotwrapped
class BVH_Distance:
	pass

#classnotwrapped
class BVH_ObjectTransient:
	pass

#classnotwrapped
class BVH_Object:
	pass

#classnotwrapped
class BVH_QuickSorter:
	pass

#classnotwrapped
class BVH_Set:
	pass

#classnotwrapped
class BVH_SpatialMedianBuilder:
	pass

#classnotwrapped
class BVH_Tree:
	pass

#classnotwrapped
class BVH_PrimitiveSet:
	pass

#classnotwrapped
class BVH_BuildQueue:
	pass

#classnotwrapped
class BVH_BuilderTransient:
	pass

#classnotwrapped
class BVH_Builder:
	pass

#classnotwrapped
class BVH_Properties:
	pass

#classnotwrapped
class BVH_Transform:
	pass

#classnotwrapped
class MatrixOp:
	pass

#classnotwrapped
class UnitVector:
	pass

#classnotwrapped
class BVH_RadixSorter:
	pass

#classnotwrapped
class BitPredicate:
	pass

#classnotwrapped
class BitComparator:
	pass

#classnotwrapped
class RadixSorter:
	pass

#classnotwrapped
class VectorType:
	pass

#classnotwrapped
class MatrixType:
	pass

#classnotwrapped
class ArrayType:
	pass

#classnotwrapped
class VecComp:
	pass

#classnotwrapped
class Array:
	pass

#classnotwrapped
class BVH_Triangulation:
	pass

#classnotwrapped
class BVH_PairDistance:
	pass

#classnotwrapped
class BVH_TreeBaseTransient:
	pass

#classnotwrapped
class BVH_TreeBase:
	pass

#classnotwrapped
class BVH_QuadTree:
	pass

#classnotwrapped
class BVH_BinaryTree:
	pass

#classnotwrapped
class BVH_SweepPlaneBuilder:
	pass

#classnotwrapped
class BVH_BaseTraverse:
	pass

#classnotwrapped
class BVH_Traverse:
	pass

#classnotwrapped
class BVH_PairTraverse:
	pass

#classnotwrapped
class BVH_BoxSet:
	pass

#classnotwrapped
class BVH_Geometry:
	pass

#classnotwrapped
class BVH_QueueBuilder:
	pass

#classnotwrapped
class BVH_DistanceField:
	pass

#classnotwrapped
class BVH_LinearBuilder:
	pass

#classnotwrapped
class BoundData:
	pass

#classnotwrapped
class UpdateBoundTask:
	pass

#classnotwrapped
class BVH_Bin:
	pass

#classnotwrapped
class BVH_BinnedBuilder:
	pass

#classnotwrapped
class BVH_AxisSelector:
	pass
