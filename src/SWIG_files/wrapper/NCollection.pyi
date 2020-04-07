from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *

NCollection_String = NewType('NCollection_String', NCollection_Utf8String)
Standard_Size = NewType('Standard_Size', int)

class NCollection_StdAllocator:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAlloc: NCollection_BaseAllocator) -> None: ...
	@overload
	def __init__(self, X: NCollection_StdAllocator) -> None: ...
	def Allocator(self) -> NCollection_BaseAllocator: ...

#classnotwrapped
class NCollection_Array1:
	pass

#classnotwrapped
class NCollection_AccAllocator:
	pass

#classnotwrapped
class NCollection_UtfString:
	pass

#classnotwrapped
class NCollection_Lerp:
	pass

#classnotwrapped
class NCollection_WinHeapAllocator:
	pass

#classnotwrapped
class NCollection_Mat4:
	pass

#classnotwrapped
class NCollection_AlignedAllocator:
	pass

#classnotwrapped
class NCollection_Map:
	pass

#classnotwrapped
class NCollection_SeqNode:
	pass

#classnotwrapped
class NCollection_BaseSequence:
	pass

#classnotwrapped
class NCollection_LocalArray:
	pass

#classnotwrapped
class NCollection_Comparator:
	pass

#classnotwrapped
class NCollection_TListNode:
	pass

#classnotwrapped
class NCollection_DataMap:
	pass

#classnotwrapped
class NCollection_ListNode:
	pass

#classnotwrapped
class NCollection_Vector:
	pass

#classnotwrapped
class NCollection_DoubleMap:
	pass

#classnotwrapped
class NCollection_UtfIterator:
	pass

#classnotwrapped
class NCollection_Vec3:
	pass

#classnotwrapped
class NCollection_UBTree:
	pass

#classnotwrapped
class NCollection_EBTree:
	pass

#classnotwrapped
class NCollection_Vec4:
	pass

#classnotwrapped
class NCollection_Handle:
	pass

#classnotwrapped
class NCollection_BaseList:
	pass

#classnotwrapped
class NCollection_SparseArray:
	pass

#classnotwrapped
class NCollection_BaseVector:
	pass

#classnotwrapped
class NCollection_IncAllocator:
	pass

#classnotwrapped
class NCollection_BaseAllocator:
	pass

#classnotwrapped
class NCollection_SparseArrayBase:
	pass

#classnotwrapped
class NCollection_IndexedMap:
	pass

#classnotwrapped
class NCollection_Vec2:
	pass

#classnotwrapped
class NCollection_List:
	pass

#classnotwrapped
class NCollection_TListIterator:
	pass

#classnotwrapped
class NCollection_BaseMap:
	pass

#classnotwrapped
class NCollection_Buffer:
	pass

#classnotwrapped
class NCollection_IndexedDataMap:
	pass

#classnotwrapped
class NCollection_StdAllocator:
	pass

#classnotwrapped
class NCollection_UBTreeFiller:
	pass

#classnotwrapped
class NCollection_DefaultHasher:
	pass

#classnotwrapped
class NCollection_Sequence:
	pass

#classnotwrapped
class NCollection_Array2:
	pass

#classnotwrapped
class NCollection_Shared:
	pass

#classnotwrapped
class NCollection_HeapAllocator:
	pass
