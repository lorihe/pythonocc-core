from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *

Storage_Position = NewType('Storage_Position', long)

class Storage_SolveMode(IntEnum):
	Storage_AddSolve: int = ...
	Storage_WriteSolve: int = ...
	Storage_ReadSolve: int = ...
Storage_AddSolve = Storage_SolveMode.Storage_AddSolve
Storage_WriteSolve = Storage_SolveMode.Storage_WriteSolve
Storage_ReadSolve = Storage_SolveMode.Storage_ReadSolve

class Storage_Error(IntEnum):
	Storage_VSOk: int = ...
	Storage_VSOpenError: int = ...
	Storage_VSModeError: int = ...
	Storage_VSCloseError: int = ...
	Storage_VSAlreadyOpen: int = ...
	Storage_VSNotOpen: int = ...
	Storage_VSSectionNotFound: int = ...
	Storage_VSWriteError: int = ...
	Storage_VSFormatError: int = ...
	Storage_VSUnknownType: int = ...
	Storage_VSTypeMismatch: int = ...
	Storage_VSInternalError: int = ...
	Storage_VSExtCharParityError: int = ...
	Storage_VSWrongFileDriver: int = ...
Storage_VSOk = Storage_Error.Storage_VSOk
Storage_VSOpenError = Storage_Error.Storage_VSOpenError
Storage_VSModeError = Storage_Error.Storage_VSModeError
Storage_VSCloseError = Storage_Error.Storage_VSCloseError
Storage_VSAlreadyOpen = Storage_Error.Storage_VSAlreadyOpen
Storage_VSNotOpen = Storage_Error.Storage_VSNotOpen
Storage_VSSectionNotFound = Storage_Error.Storage_VSSectionNotFound
Storage_VSWriteError = Storage_Error.Storage_VSWriteError
Storage_VSFormatError = Storage_Error.Storage_VSFormatError
Storage_VSUnknownType = Storage_Error.Storage_VSUnknownType
Storage_VSTypeMismatch = Storage_Error.Storage_VSTypeMismatch
Storage_VSInternalError = Storage_Error.Storage_VSInternalError
Storage_VSExtCharParityError = Storage_Error.Storage_VSExtCharParityError
Storage_VSWrongFileDriver = Storage_Error.Storage_VSWrongFileDriver

class Storage_OpenMode(IntEnum):
	Storage_VSNone: int = ...
	Storage_VSRead: int = ...
	Storage_VSWrite: int = ...
	Storage_VSReadWrite: int = ...
Storage_VSNone = Storage_OpenMode.Storage_VSNone
Storage_VSRead = Storage_OpenMode.Storage_VSRead
Storage_VSWrite = Storage_OpenMode.Storage_VSWrite
Storage_VSReadWrite = Storage_OpenMode.Storage_VSReadWrite

#classnotwrapped
class Storage_Bucket:
	pass

#classnotwrapped
class Storage_BucketOfPersistent:
	pass

#classnotwrapped
class Storage_BucketIterator:
	pass

#classnotwrapped
class Storage_RootData:
	pass

#classnotwrapped
class Storage_TypeData:
	pass

#classnotwrapped
class Storage_Root:
	pass

#classnotwrapped
class Storage_Schema:
	pass

#classnotwrapped
class Storage_DefaultCallBack:
	pass

#classnotwrapped
class Storage_TypedCallBack:
	pass

#classnotwrapped
class Storage_CallBack:
	pass

#classnotwrapped
class Storage_HeaderData:
	pass

#classnotwrapped
class Storage_BaseDriver:
	pass

#classnotwrapped
class Storage_InternalData:
	pass

#classnotwrapped
class Storage_Data:
	pass

#classnotwrapped
class Storage:
	pass
