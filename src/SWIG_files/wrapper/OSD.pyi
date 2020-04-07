from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *

OSD_PThread = NewType('OSD_PThread', pthread_t)

class OSD_LockType(IntEnum):
	OSD_NoLock: int = ...
	OSD_ReadLock: int = ...
	OSD_WriteLock: int = ...
	OSD_ExclusiveLock: int = ...
OSD_NoLock = OSD_LockType.OSD_NoLock
OSD_ReadLock = OSD_LockType.OSD_ReadLock
OSD_WriteLock = OSD_LockType.OSD_WriteLock
OSD_ExclusiveLock = OSD_LockType.OSD_ExclusiveLock

class OSD_LoadMode(IntEnum):
	OSD_RTLD_LAZY: int = ...
	OSD_RTLD_NOW: int = ...
OSD_RTLD_LAZY = OSD_LoadMode.OSD_RTLD_LAZY
OSD_RTLD_NOW = OSD_LoadMode.OSD_RTLD_NOW

class OSD_OpenMode(IntEnum):
	OSD_ReadOnly: int = ...
	OSD_WriteOnly: int = ...
	OSD_ReadWrite: int = ...
OSD_ReadOnly = OSD_OpenMode.OSD_ReadOnly
OSD_WriteOnly = OSD_OpenMode.OSD_WriteOnly
OSD_ReadWrite = OSD_OpenMode.OSD_ReadWrite

class OSD_OEMType(IntEnum):
	OSD_Unavailable: int = ...
	OSD_SUN: int = ...
	OSD_DEC: int = ...
	OSD_SGI: int = ...
	OSD_NEC: int = ...
	OSD_MAC: int = ...
	OSD_PC: int = ...
	OSD_HP: int = ...
	OSD_IBM: int = ...
	OSD_VAX: int = ...
	OSD_LIN: int = ...
	OSD_AIX: int = ...
OSD_Unavailable = OSD_OEMType.OSD_Unavailable
OSD_SUN = OSD_OEMType.OSD_SUN
OSD_DEC = OSD_OEMType.OSD_DEC
OSD_SGI = OSD_OEMType.OSD_SGI
OSD_NEC = OSD_OEMType.OSD_NEC
OSD_MAC = OSD_OEMType.OSD_MAC
OSD_PC = OSD_OEMType.OSD_PC
OSD_HP = OSD_OEMType.OSD_HP
OSD_IBM = OSD_OEMType.OSD_IBM
OSD_VAX = OSD_OEMType.OSD_VAX
OSD_LIN = OSD_OEMType.OSD_LIN
OSD_AIX = OSD_OEMType.OSD_AIX

class OSD_WhoAmI(IntEnum):
	OSD_WDirectory: int = ...
	OSD_WDirectoryIterator: int = ...
	OSD_WEnvironment: int = ...
	OSD_WFile: int = ...
	OSD_WFileNode: int = ...
	OSD_WFileIterator: int = ...
	OSD_WPath: int = ...
	OSD_WProcess: int = ...
	OSD_WProtection: int = ...
	OSD_WHost: int = ...
	OSD_WDisk: int = ...
	OSD_WChronometer: int = ...
	OSD_WTimer: int = ...
	OSD_WPackage: int = ...
	OSD_WEnvironmentIterator: int = ...
OSD_WDirectory = OSD_WhoAmI.OSD_WDirectory
OSD_WDirectoryIterator = OSD_WhoAmI.OSD_WDirectoryIterator
OSD_WEnvironment = OSD_WhoAmI.OSD_WEnvironment
OSD_WFile = OSD_WhoAmI.OSD_WFile
OSD_WFileNode = OSD_WhoAmI.OSD_WFileNode
OSD_WFileIterator = OSD_WhoAmI.OSD_WFileIterator
OSD_WPath = OSD_WhoAmI.OSD_WPath
OSD_WProcess = OSD_WhoAmI.OSD_WProcess
OSD_WProtection = OSD_WhoAmI.OSD_WProtection
OSD_WHost = OSD_WhoAmI.OSD_WHost
OSD_WDisk = OSD_WhoAmI.OSD_WDisk
OSD_WChronometer = OSD_WhoAmI.OSD_WChronometer
OSD_WTimer = OSD_WhoAmI.OSD_WTimer
OSD_WPackage = OSD_WhoAmI.OSD_WPackage
OSD_WEnvironmentIterator = OSD_WhoAmI.OSD_WEnvironmentIterator

class OSD_SysType(IntEnum):
	OSD_Unknown: int = ...
	OSD_Default: int = ...
	OSD_UnixBSD: int = ...
	OSD_UnixSystemV: int = ...
	OSD_VMS: int = ...
	OSD_OS2: int = ...
	OSD_OSF: int = ...
	OSD_MacOs: int = ...
	OSD_Taligent: int = ...
	OSD_WindowsNT: int = ...
	OSD_LinuxREDHAT: int = ...
	OSD_Aix: int = ...
OSD_Unknown = OSD_SysType.OSD_Unknown
OSD_Default = OSD_SysType.OSD_Default
OSD_UnixBSD = OSD_SysType.OSD_UnixBSD
OSD_UnixSystemV = OSD_SysType.OSD_UnixSystemV
OSD_VMS = OSD_SysType.OSD_VMS
OSD_OS2 = OSD_SysType.OSD_OS2
OSD_OSF = OSD_SysType.OSD_OSF
OSD_MacOs = OSD_SysType.OSD_MacOs
OSD_Taligent = OSD_SysType.OSD_Taligent
OSD_WindowsNT = OSD_SysType.OSD_WindowsNT
OSD_LinuxREDHAT = OSD_SysType.OSD_LinuxREDHAT
OSD_Aix = OSD_SysType.OSD_Aix

class OSD_KindFile(IntEnum):
	OSD_FILE: int = ...
	OSD_DIRECTORY: int = ...
	OSD_LINK: int = ...
	OSD_SOCKET: int = ...
	OSD_UNKNOWN: int = ...
OSD_FILE = OSD_KindFile.OSD_FILE
OSD_DIRECTORY = OSD_KindFile.OSD_DIRECTORY
OSD_LINK = OSD_KindFile.OSD_LINK
OSD_SOCKET = OSD_KindFile.OSD_SOCKET
OSD_UNKNOWN = OSD_KindFile.OSD_UNKNOWN

class OSD_SignalMode(IntEnum):
	OSD_SignalMode_AsIs: int = ...
	OSD_SignalMode_Set: int = ...
	OSD_SignalMode_SetUnhandled: int = ...
	OSD_SignalMode_Unset: int = ...
OSD_SignalMode_AsIs = OSD_SignalMode.OSD_SignalMode_AsIs
OSD_SignalMode_Set = OSD_SignalMode.OSD_SignalMode_Set
OSD_SignalMode_SetUnhandled = OSD_SignalMode.OSD_SignalMode_SetUnhandled
OSD_SignalMode_Unset = OSD_SignalMode.OSD_SignalMode_Unset

class OSD_FromWhere(IntEnum):
	OSD_FromBeginning: int = ...
	OSD_FromHere: int = ...
	OSD_FromEnd: int = ...
OSD_FromBeginning = OSD_FromWhere.OSD_FromBeginning
OSD_FromHere = OSD_FromWhere.OSD_FromHere
OSD_FromEnd = OSD_FromWhere.OSD_FromEnd

class OSD_SingleProtection(IntEnum):
	OSD_None: int = ...
	OSD_R: int = ...
	OSD_W: int = ...
	OSD_RW: int = ...
	OSD_X: int = ...
	OSD_RX: int = ...
	OSD_WX: int = ...
	OSD_RWX: int = ...
	OSD_D: int = ...
	OSD_RD: int = ...
	OSD_WD: int = ...
	OSD_RWD: int = ...
	OSD_XD: int = ...
	OSD_RXD: int = ...
	OSD_WXD: int = ...
	OSD_RWXD: int = ...
OSD_None = OSD_SingleProtection.OSD_None
OSD_R = OSD_SingleProtection.OSD_R
OSD_W = OSD_SingleProtection.OSD_W
OSD_RW = OSD_SingleProtection.OSD_RW
OSD_X = OSD_SingleProtection.OSD_X
OSD_RX = OSD_SingleProtection.OSD_RX
OSD_WX = OSD_SingleProtection.OSD_WX
OSD_RWX = OSD_SingleProtection.OSD_RWX
OSD_D = OSD_SingleProtection.OSD_D
OSD_RD = OSD_SingleProtection.OSD_RD
OSD_WD = OSD_SingleProtection.OSD_WD
OSD_RWD = OSD_SingleProtection.OSD_RWD
OSD_XD = OSD_SingleProtection.OSD_XD
OSD_RXD = OSD_SingleProtection.OSD_RXD
OSD_WXD = OSD_SingleProtection.OSD_WXD
OSD_RWXD = OSD_SingleProtection.OSD_RWXD

#classnotwrapped
class OSD_Timer:
	pass

#classnotwrapped
class OSD_PerfMeter:
	pass

#classnotwrapped
class OSD_Disk:
	pass

#classnotwrapped
class OSD_Protection:
	pass

#classnotwrapped
class OSD_MemInfo:
	pass

#classnotwrapped
class OSD_DirectoryIterator:
	pass

#classnotwrapped
class OSD_Chronometer:
	pass

#classnotwrapped
class OSD_ThreadPool:
	pass

#classnotwrapped
class OSD_SharedLibrary:
	pass

#classnotwrapped
class OSD_Error:
	pass

#classnotwrapped
class OSD_Host:
	pass

#classnotwrapped
class OSD_Parallel:
	pass

#classnotwrapped
class OSD_Directory:
	pass

#classnotwrapped
class OSD_Path:
	pass

#classnotwrapped
class OSD_Process:
	pass

#classnotwrapped
class OSD_MAllocHook:
	pass

#classnotwrapped
class OSD_FileNode:
	pass

#classnotwrapped
class OSD_File:
	pass

#classnotwrapped
class OSD_FileIterator:
	pass

#classnotwrapped
class OSD_Thread:
	pass

#classnotwrapped
class OSD_Environment:
	pass

#classnotwrapped
class OSD:
	pass
