/*
Copyright 2008-2020 Thomas Paviot (tpaviot@gmail.com)

This file is part of pythonOCC.
pythonOCC is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pythonOCC is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.
*/
%define BREPMESHDOCSTRING
"BRepMesh module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_brepmesh.html"
%enddef
%module (package="OCC.Core", docstring=BREPMESHDOCSTRING) BRepMesh


%{
#ifdef WNT
#pragma warning(disable : 4716)
#endif
%}

%include ../common/CommonIncludes.i
%include ../common/ExceptionCatcher.i
%include ../common/FunctionTransformers.i
%include ../common/Operators.i
%include ../common/OccHandle.i


%{
#include<BRepMesh_Delaun.hxx>
#include<BRepMesh_module.hxx>

//Dependencies
#include<Standard_module.hxx>
#include<NCollection_module.hxx>
#include<IMeshTools_module.hxx>
#include<gp_module.hxx>
#include<TopAbs_module.hxx>
#include<TopoDS_module.hxx>
#include<TCollection_module.hxx>
#include<TColStd_module.hxx>
#include<BRepAdaptor_module.hxx>
#include<GeomAbs_module.hxx>
#include<Adaptor3d_module.hxx>
#include<Poly_module.hxx>
#include<Bnd_module.hxx>
#include<TopLoc_module.hxx>
#include<Geom2d_module.hxx>
#include<Geom_module.hxx>
#include<IMeshData_module.hxx>
#include<TShort_module.hxx>
#include<Adaptor3d_module.hxx>
#include<Geom2dAdaptor_module.hxx>
#include<Message_module.hxx>
#include<Adaptor2d_module.hxx>
#include<GeomAdaptor_module.hxx>
#include<Geom_module.hxx>
#include<TopLoc_module.hxx>
#include<Geom2d_module.hxx>
#include<TColgp_module.hxx>
#include<TColStd_module.hxx>
#include<TCollection_module.hxx>
#include<Storage_module.hxx>
%};
%import Standard.i
%import NCollection.i
%import IMeshTools.i
%import gp.i
%import TopAbs.i
%import TopoDS.i
%import TCollection.i
%import TColStd.i
%import BRepAdaptor.i
%import GeomAbs.i
%import Adaptor3d.i
%import Poly.i
%import Bnd.i
%import TopLoc.i
%import Geom2d.i
%import Geom.i
%import IMeshData.i

%pythoncode {
from enum import IntEnum
from OCC.Core.Exception import *
};

/* public enums */
enum BRepMesh_FactoryError {
	BRepMesh_FE_NOERROR = 0,
	BRepMesh_FE_LIBRARYNOTFOUND = 1,
	BRepMesh_FE_FUNCTIONNOTFOUND = 2,
	BRepMesh_FE_CANNOTCREATEALGO = 3,
};

enum BRepMesh_DegreeOfFreedom {
	BRepMesh_Free = 0,
	BRepMesh_InVolume = 1,
	BRepMesh_OnSurface = 2,
	BRepMesh_OnCurve = 3,
	BRepMesh_Fixed = 4,
	BRepMesh_Frontier = 5,
	BRepMesh_Deleted = 6,
};

/* end public enums declaration */

/* python proy classes for enums */
%pythoncode {

class BRepMesh_FactoryError(IntEnum):
	BRepMesh_FE_NOERROR = 0
	BRepMesh_FE_LIBRARYNOTFOUND = 1
	BRepMesh_FE_FUNCTIONNOTFOUND = 2
	BRepMesh_FE_CANNOTCREATEALGO = 3
BRepMesh_FE_NOERROR = BRepMesh_FactoryError.BRepMesh_FE_NOERROR
BRepMesh_FE_LIBRARYNOTFOUND = BRepMesh_FactoryError.BRepMesh_FE_LIBRARYNOTFOUND
BRepMesh_FE_FUNCTIONNOTFOUND = BRepMesh_FactoryError.BRepMesh_FE_FUNCTIONNOTFOUND
BRepMesh_FE_CANNOTCREATEALGO = BRepMesh_FactoryError.BRepMesh_FE_CANNOTCREATEALGO

class BRepMesh_DegreeOfFreedom(IntEnum):
	BRepMesh_Free = 0
	BRepMesh_InVolume = 1
	BRepMesh_OnSurface = 2
	BRepMesh_OnCurve = 3
	BRepMesh_Fixed = 4
	BRepMesh_Frontier = 5
	BRepMesh_Deleted = 6
BRepMesh_Free = BRepMesh_DegreeOfFreedom.BRepMesh_Free
BRepMesh_InVolume = BRepMesh_DegreeOfFreedom.BRepMesh_InVolume
BRepMesh_OnSurface = BRepMesh_DegreeOfFreedom.BRepMesh_OnSurface
BRepMesh_OnCurve = BRepMesh_DegreeOfFreedom.BRepMesh_OnCurve
BRepMesh_Fixed = BRepMesh_DegreeOfFreedom.BRepMesh_Fixed
BRepMesh_Frontier = BRepMesh_DegreeOfFreedom.BRepMesh_Frontier
BRepMesh_Deleted = BRepMesh_DegreeOfFreedom.BRepMesh_Deleted
};
/* end python proxy for enums */

/* handles */
%wrap_handle(BRepMesh_Classifier)
%wrap_handle(BRepMesh_DataStructureOfDelaun)
%wrap_handle(BRepMesh_Deflection)
%wrap_handle(BRepMesh_DiscretRoot)
%wrap_handle(BRepMesh_FaceChecker)
%wrap_handle(BRepMesh_MeshTool)
%wrap_handle(BRepMesh_SelectorOfDataStructureOfDelaun)
%wrap_handle(BRepMesh_ShapeTool)
%wrap_handle(BRepMesh_VertexTool)
%wrap_handle(BRepMesh_IncrementalMesh)
/* end handles declaration */

/* templates */
/* end templates declaration */

/* typedefs */
typedef Standard_Integer ( * BRepMesh_PluginEntryType ) ( const TopoDS_Shape & theShape, const Standard_Real theLinDeflection, const Standard_Real theAngDeflection, BRepMesh_DiscretRoot * & theMeshAlgoInstance );
/* end typedefs declaration */

/***********************
* class <anon-class-1> *
***********************/
/******************************
* class BRepMesh_BaseMeshAlgo *
******************************/
%nodefaultctor BRepMesh_BaseMeshAlgo;
class BRepMesh_BaseMeshAlgo : public IMeshTools_MeshAlgo {
	public:
typedef NCollection_Shared<NCollection_Vector<gp_Pnt>> VectorOfPnt;
		/****************** Perform ******************/
		%feature("compactdefaultargs") Perform;
		%feature("autodoc", "Performs processing of the given face.

Parameters
----------
theDFace: IMeshData::IFaceHandle
theParameters: IMeshTools_Parameters

Returns
-------
None
") Perform;
		virtual void Perform(const IMeshData::IFaceHandle & theDFace, const IMeshTools_Parameters & theParameters);

};


%extend BRepMesh_BaseMeshAlgo {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/************************
* class BRepMesh_Circle *
************************/
class BRepMesh_Circle {
	public:
		/****************** BRepMesh_Circle ******************/
		%feature("compactdefaultargs") BRepMesh_Circle;
		%feature("autodoc", "Default constructor.

Returns
-------
None
") BRepMesh_Circle;
		 BRepMesh_Circle();

		/****************** BRepMesh_Circle ******************/
		%feature("compactdefaultargs") BRepMesh_Circle;
		%feature("autodoc", "Constructor. @param thelocation location of a circle. @param theradius radius of a circle.

Parameters
----------
theLocation: gp_XY
theRadius: float

Returns
-------
None
") BRepMesh_Circle;
		 BRepMesh_Circle(const gp_XY & theLocation, const Standard_Real theRadius);

		/****************** Location ******************/
		%feature("compactdefaultargs") Location;
		%feature("autodoc", "Returns location of a circle.

Returns
-------
gp_XY
") Location;
		const gp_XY Location();

		/****************** Radius ******************/
		%feature("compactdefaultargs") Radius;
		%feature("autodoc", "Returns radius of a circle.

Returns
-------
float
") Radius;
		const Standard_Real & Radius();

		/****************** SetLocation ******************/
		%feature("compactdefaultargs") SetLocation;
		%feature("autodoc", "Sets location of a circle. @param thelocation location of a circle.

Parameters
----------
theLocation: gp_XY

Returns
-------
None
") SetLocation;
		void SetLocation(const gp_XY & theLocation);

		/****************** SetRadius ******************/
		%feature("compactdefaultargs") SetRadius;
		%feature("autodoc", "Sets radius of a circle. @param theradius radius of a circle.

Parameters
----------
theRadius: float

Returns
-------
None
") SetRadius;
		void SetRadius(const Standard_Real theRadius);

};


%extend BRepMesh_Circle {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*********************************
* class BRepMesh_CircleInspector *
*********************************/
class BRepMesh_CircleInspector : public NCollection_CellFilter_InspectorXY {
	public:
typedef Standard_Integer Target;
		/****************** BRepMesh_CircleInspector ******************/
		%feature("compactdefaultargs") BRepMesh_CircleInspector;
		%feature("autodoc", "Constructor. @param thetolerance tolerance to be used for identification of shot circles. @param thereservedsize size to be reserved for vector of circles. @param theallocator memory allocator to be used by internal collections.

Parameters
----------
theTolerance: float
theReservedSize: int
theAllocator: NCollection_IncAllocator

Returns
-------
None
") BRepMesh_CircleInspector;
		 BRepMesh_CircleInspector(const Standard_Real theTolerance, const Standard_Integer theReservedSize, const opencascade::handle<NCollection_IncAllocator> & theAllocator);

		/****************** Bind ******************/
		%feature("compactdefaultargs") Bind;
		%feature("autodoc", "Adds the circle to vector of circles at the given position. @param theindex position of circle in the vector. @param thecircle circle to be added.

Parameters
----------
theIndex: int
theCircle: BRepMesh_Circle

Returns
-------
None
") Bind;
		void Bind(const Standard_Integer theIndex, const BRepMesh_Circle & theCircle);

		/****************** Circle ******************/
		%feature("compactdefaultargs") Circle;
		%feature("autodoc", "Returns circle with the given index. @param theindex index of circle. returns circle with the given index.

Parameters
----------
theIndex: int

Returns
-------
BRepMesh_Circle
") Circle;
		BRepMesh_Circle & Circle(const Standard_Integer theIndex);

		/****************** Circles ******************/
		%feature("compactdefaultargs") Circles;
		%feature("autodoc", "Resutns vector of registered circles.

Returns
-------
IMeshData::VectorOfCircle
") Circles;
		const IMeshData::VectorOfCircle & Circles();

		/****************** GetShotCircles ******************/
		%feature("compactdefaultargs") GetShotCircles;
		%feature("autodoc", "Returns list of circles shot by the reference point.

Returns
-------
IMeshData::ListOfInteger
") GetShotCircles;
		IMeshData::ListOfInteger & GetShotCircles();

		/****************** Inspect ******************/
		%feature("compactdefaultargs") Inspect;
		%feature("autodoc", "Performs inspection of a circle with the given index. @param thetargetindex index of a circle to be checked. returns status of the check.

Parameters
----------
theTargetIndex: int

Returns
-------
NCollection_CellFilter_Action
") Inspect;
		NCollection_CellFilter_Action Inspect(const Standard_Integer theTargetIndex);

		/****************** IsEqual ******************/
		%feature("compactdefaultargs") IsEqual;
		%feature("autodoc", "Checks indices for equlity.

Parameters
----------
theIndex: int
theTargetIndex: int

Returns
-------
bool
") IsEqual;
		static Standard_Boolean IsEqual(const Standard_Integer theIndex, const Standard_Integer theTargetIndex);

		/****************** SetPoint ******************/
		%feature("compactdefaultargs") SetPoint;
		%feature("autodoc", "Set reference point to be checked. @param thepoint bullet point.

Parameters
----------
thePoint: gp_XY

Returns
-------
None
") SetPoint;
		void SetPoint(const gp_XY & thePoint);

};


%extend BRepMesh_CircleInspector {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/****************************
* class BRepMesh_CircleTool *
****************************/
class BRepMesh_CircleTool {
	public:
		/****************** BRepMesh_CircleTool ******************/
		%feature("compactdefaultargs") BRepMesh_CircleTool;
		%feature("autodoc", "Constructor. @param theallocator memory allocator to be used by internal structures.

Parameters
----------
theAllocator: NCollection_IncAllocator

Returns
-------
None
") BRepMesh_CircleTool;
		 BRepMesh_CircleTool(const opencascade::handle<NCollection_IncAllocator> & theAllocator);

		/****************** BRepMesh_CircleTool ******************/
		%feature("compactdefaultargs") BRepMesh_CircleTool;
		%feature("autodoc", "Constructor. @param thereservedsize size to be reserved for vector of circles. @param theallocator memory allocator to be used by internal structures.

Parameters
----------
theReservedSize: int
theAllocator: NCollection_IncAllocator

Returns
-------
None
") BRepMesh_CircleTool;
		 BRepMesh_CircleTool(const Standard_Integer theReservedSize, const opencascade::handle<NCollection_IncAllocator> & theAllocator);

		/****************** Bind ******************/
		%feature("compactdefaultargs") Bind;
		%feature("autodoc", "Binds the circle to the tool. @param theindex index a circle should be bound with. @param thecircle circle to be bound.

Parameters
----------
theIndex: int
theCircle: gp_Circ2d

Returns
-------
None
") Bind;
		void Bind(const Standard_Integer theIndex, const gp_Circ2d & theCircle);

		/****************** Bind ******************/
		%feature("compactdefaultargs") Bind;
		%feature("autodoc", "Computes circle on three points and bind it to the tool. @param theindex index a circle should be bound with. @param thepoint1 first point. @param thepoint2 second point. @param thepoint3 third point. returns false in case of impossibility to build a circle on the given points, true elsewhere.

Parameters
----------
theIndex: int
thePoint1: gp_XY
thePoint2: gp_XY
thePoint3: gp_XY

Returns
-------
bool
") Bind;
		Standard_Boolean Bind(const Standard_Integer theIndex, const gp_XY & thePoint1, const gp_XY & thePoint2, const gp_XY & thePoint3);

		/****************** Delete ******************/
		%feature("compactdefaultargs") Delete;
		%feature("autodoc", "Deletes a circle from the tool. @param theindex index of a circle to be removed.

Parameters
----------
theIndex: int

Returns
-------
None
") Delete;
		void Delete(const Standard_Integer theIndex);

		/****************** Init ******************/
		%feature("compactdefaultargs") Init;
		%feature("autodoc", "Initializes the tool. @param thereservedsize size to be reserved for vector of circles.

Parameters
----------
Standard_Integer: 

Returns
-------
None
") Init;
		void Init(const Standard_Integer);

		/****************** IsEmpty ******************/
		%feature("compactdefaultargs") IsEmpty;
		%feature("autodoc", "Retruns true if cell filter contains no circle.

Returns
-------
bool
") IsEmpty;
		Standard_Boolean IsEmpty();

		/****************** MakeCircle ******************/
		%feature("compactdefaultargs") MakeCircle;
		%feature("autodoc", "Computes circle on three points. @param thepoint1 first point. @param thepoint2 second point. @param thepoint3 third point. @param[out] thelocation center of computed circle. @param[out] theradius radius of computed circle. returns false in case of impossibility to build a circle on the given points, true elsewhere.

Parameters
----------
thePoint1: gp_XY
thePoint2: gp_XY
thePoint3: gp_XY
theLocation: gp_XY

Returns
-------
theRadius: float
") MakeCircle;
		static Standard_Boolean MakeCircle(const gp_XY & thePoint1, const gp_XY & thePoint2, const gp_XY & thePoint3, gp_XY & theLocation, Standard_Real &OutValue);

		/****************** MocBind ******************/
		%feature("compactdefaultargs") MocBind;
		%feature("autodoc", "Binds implicit zero circle. @param theindex index a zero circle should be bound with.

Parameters
----------
theIndex: int

Returns
-------
None
") MocBind;
		void MocBind(const Standard_Integer theIndex);

		/****************** Select ******************/
		%feature("compactdefaultargs") Select;
		%feature("autodoc", "Select the circles shot by the given point. @param thepoint bullet point.

Parameters
----------
thePoint: gp_XY

Returns
-------
IMeshData::ListOfInteger
") Select;
		IMeshData::ListOfInteger & Select(const gp_XY & thePoint);

		/****************** SetCellSize ******************/
		%feature("compactdefaultargs") SetCellSize;
		%feature("autodoc", "Sets new size for cell filter. @param thesize cell size to be set for x and y dimensions.

Parameters
----------
theSize: float

Returns
-------
None
") SetCellSize;
		void SetCellSize(const Standard_Real theSize);

		/****************** SetCellSize ******************/
		%feature("compactdefaultargs") SetCellSize;
		%feature("autodoc", "Sets new size for cell filter. @param thesizex cell size to be set for x dimension. @param thesizey cell size to be set for y dimension.

Parameters
----------
theSizeX: float
theSizeY: float

Returns
-------
None
") SetCellSize;
		void SetCellSize(const Standard_Real theSizeX, const Standard_Real theSizeY);

		/****************** SetMinMaxSize ******************/
		%feature("compactdefaultargs") SetMinMaxSize;
		%feature("autodoc", "Sets limits of inspection area. @param themin bottom left corner of inspection area. @param themax top right corner of inspection area.

Parameters
----------
theMin: gp_XY
theMax: gp_XY

Returns
-------
None
") SetMinMaxSize;
		void SetMinMaxSize(const gp_XY & theMin, const gp_XY & theMax);

};


%extend BRepMesh_CircleTool {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/****************************
* class BRepMesh_Classifier *
****************************/
class BRepMesh_Classifier : public Standard_Transient {
	public:
		/****************** BRepMesh_Classifier ******************/
		%feature("compactdefaultargs") BRepMesh_Classifier;
		%feature("autodoc", "Constructor.

Returns
-------
None
") BRepMesh_Classifier;
		 BRepMesh_Classifier();

		/****************** Perform ******************/
		%feature("compactdefaultargs") Perform;
		%feature("autodoc", "Performs classification of the given point regarding to face internals. @param thepoint point in parametric space to be classified. returns topabs_in if point lies within face boundaries and topabs_out elsewhere.

Parameters
----------
thePoint: gp_Pnt2d

Returns
-------
TopAbs_State
") Perform;
		TopAbs_State Perform(const gp_Pnt2d & thePoint);

		/****************** RegisterWire ******************/
		%feature("compactdefaultargs") RegisterWire;
		%feature("autodoc", "Registers wire specified by sequence of points for further classification of points. @param thewire wire to be registered. specified by sequence of points. @param thetoluv tolerance to be used for calculations in parametric space. @param theumin lower u boundary of the face in parametric space. @param theumax upper u boundary of the face in parametric space. @param thevmin lower v boundary of the face in parametric space. @param thevmax upper v boundary of the face in parametric space.

Parameters
----------
theWire: NCollection_Sequence< gp_Pnt2d *>
theTolUV: std::pair<float, float>
theRangeU: std::pair<float, float>
theRangeV: std::pair<float, float>

Returns
-------
None
") RegisterWire;
		void RegisterWire(const NCollection_Sequence<const gp_Pnt2d *> & theWire, const std::pair<Standard_Real, Standard_Real> & theTolUV, const std::pair<Standard_Real, Standard_Real> & theRangeU, const std::pair<Standard_Real, Standard_Real> & theRangeV);

};


%make_alias(BRepMesh_Classifier)

%extend BRepMesh_Classifier {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*************************
* class BRepMesh_Context *
*************************/
class BRepMesh_Context : public IMeshTools_Context {
	public:
		/****************** BRepMesh_Context ******************/
		%feature("compactdefaultargs") BRepMesh_Context;
		%feature("autodoc", "Constructor.

Returns
-------
None
") BRepMesh_Context;
		 BRepMesh_Context();

};


%extend BRepMesh_Context {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**********************************
* class BRepMesh_CurveTessellator *
**********************************/
class BRepMesh_CurveTessellator : public IMeshTools_CurveTessellator {
	public:
		/****************** BRepMesh_CurveTessellator ******************/
		%feature("compactdefaultargs") BRepMesh_CurveTessellator;
		%feature("autodoc", "Constructor.

Parameters
----------
theEdge: IMeshData::IEdgeHandle
theParameters: IMeshTools_Parameters

Returns
-------
None
") BRepMesh_CurveTessellator;
		 BRepMesh_CurveTessellator(const IMeshData::IEdgeHandle & theEdge, const IMeshTools_Parameters & theParameters);

		/****************** BRepMesh_CurveTessellator ******************/
		%feature("compactdefaultargs") BRepMesh_CurveTessellator;
		%feature("autodoc", "Constructor.

Parameters
----------
theEdge: IMeshData::IEdgeHandle
theOrientation: TopAbs_Orientation
theFace: IMeshData::IFaceHandle
theParameters: IMeshTools_Parameters

Returns
-------
None
") BRepMesh_CurveTessellator;
		 BRepMesh_CurveTessellator(const IMeshData::IEdgeHandle & theEdge, const TopAbs_Orientation theOrientation, const IMeshData::IFaceHandle & theFace, const IMeshTools_Parameters & theParameters);

		/****************** PointsNb ******************/
		%feature("compactdefaultargs") PointsNb;
		%feature("autodoc", "Returns number of tessellation points.

Returns
-------
int
") PointsNb;
		virtual Standard_Integer PointsNb();

		/****************** Value ******************/
		%feature("compactdefaultargs") Value;
		%feature("autodoc", "Returns parameters of solution with the given index. @param theindex index of tessellation point. @param theparameter parameters on pcurve corresponded to the solution. @param thepoint tessellation point. returns true in case of valid result, false elewhere.

Parameters
----------
theIndex: int
thePoint: gp_Pnt

Returns
-------
theParameter: float
") Value;
		virtual Standard_Boolean Value(const Standard_Integer theIndex, gp_Pnt & thePoint, Standard_Real &OutValue);

};


%extend BRepMesh_CurveTessellator {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/********************************************
* class BRepMesh_CustomDelaunayBaseMeshAlgo *
********************************************/
/***************************************
* class BRepMesh_DataStructureOfDelaun *
***************************************/
class BRepMesh_DataStructureOfDelaun : public Standard_Transient {
	public:
		/****************** BRepMesh_DataStructureOfDelaun ******************/
		%feature("compactdefaultargs") BRepMesh_DataStructureOfDelaun;
		%feature("autodoc", "Constructor. @param theallocator memory allocator to be used by internal structures. @param thereservednodesize presumed number of nodes in this mesh.

Parameters
----------
theAllocator: NCollection_IncAllocator
theReservedNodeSize: int,optional
	default value is 100

Returns
-------
None
") BRepMesh_DataStructureOfDelaun;
		 BRepMesh_DataStructureOfDelaun(const opencascade::handle<NCollection_IncAllocator> & theAllocator, const Standard_Integer theReservedNodeSize = 100);

		/****************** AddElement ******************/
		%feature("compactdefaultargs") AddElement;
		%feature("autodoc", "Adds element to the mesh if it is not already in the mesh. @param theelement element to be added to the mesh. returns index of the element in the structure.

Parameters
----------
theElement: BRepMesh_Triangle

Returns
-------
int
") AddElement;
		Standard_Integer AddElement(const BRepMesh_Triangle & theElement);

		/****************** AddLink ******************/
		%feature("compactdefaultargs") AddLink;
		%feature("autodoc", "Adds link to the mesh if it is not already in the mesh. @param thelink link to be added to the mesh. returns index of the link in the structure.

Parameters
----------
theLink: BRepMesh_Edge

Returns
-------
int
") AddLink;
		Standard_Integer AddLink(const BRepMesh_Edge & theLink);

		/****************** AddNode ******************/
		%feature("compactdefaultargs") AddNode;
		%feature("autodoc", "Adds node to the mesh if it is not already in the mesh. @param thenode node to be added to the mesh. @param isforceadd adds the given node to structure without checking on coincidence with other nodes. returns index of the node in the structure.

Parameters
----------
theNode: BRepMesh_Vertex
isForceAdd: bool,optional
	default value is Standard_False

Returns
-------
int
") AddNode;
		Standard_Integer AddNode(const BRepMesh_Vertex & theNode, const Standard_Boolean isForceAdd = Standard_False);

		/****************** Allocator ******************/
		%feature("compactdefaultargs") Allocator;
		%feature("autodoc", "Returns memory allocator used by the structure.

Returns
-------
opencascade::handle<NCollection_IncAllocator>
") Allocator;
		const opencascade::handle<NCollection_IncAllocator> & Allocator();

		/****************** ClearDeleted ******************/
		%feature("compactdefaultargs") ClearDeleted;
		%feature("autodoc", "Substitutes deleted items by the last one from corresponding map to have only non-deleted elements, links or nodes in the structure.

Returns
-------
None
") ClearDeleted;
		void ClearDeleted();

		/****************** ClearDomain ******************/
		%feature("compactdefaultargs") ClearDomain;
		%feature("autodoc", "Removes all elements.

Returns
-------
None
") ClearDomain;
		void ClearDomain();

		/****************** Data ******************/
		%feature("compactdefaultargs") Data;
		%feature("autodoc", "Gives the data structure for initialization of cell size and tolerance.

Returns
-------
opencascade::handle<BRepMesh_VertexTool>
") Data;
		const opencascade::handle<BRepMesh_VertexTool> & Data();

		/****************** Dump ******************/
		%feature("compactdefaultargs") Dump;
		%feature("autodoc", "No available documentation.

Parameters
----------
theFileNameStr: char *

Returns
-------
None
") Dump;
		void Dump(const char * theFileNameStr);

		/****************** ElementNodes ******************/
		%feature("compactdefaultargs") ElementNodes;
		%feature("autodoc", "Returns indices of nodes forming the given element. @param theelement element which nodes should be retrieved. @param[out] thenodes nodes of the given element.

Parameters
----------
theElement: BRepMesh_Triangle
): int (  theNodes

Returns
-------
None
") ElementNodes;
		void ElementNodes(const BRepMesh_Triangle & theElement, Standard_Integer ( & theNodes )[3]);

		/****************** ElementsConnectedTo ******************/
		%feature("compactdefaultargs") ElementsConnectedTo;
		%feature("autodoc", "Returns indices of elements conected to the link with the given index. @param thelinkindex index of link whose data should be retrieved. returns indices of elements conected to the link.

Parameters
----------
theLinkIndex: int

Returns
-------
BRepMesh_PairOfIndex
") ElementsConnectedTo;
		const BRepMesh_PairOfIndex & ElementsConnectedTo(const Standard_Integer theLinkIndex);

		/****************** ElementsOfDomain ******************/
		%feature("compactdefaultargs") ElementsOfDomain;
		%feature("autodoc", "Returns map of indices of elements registered in mesh.

Returns
-------
IMeshData::MapOfInteger
") ElementsOfDomain;
		const IMeshData::MapOfInteger & ElementsOfDomain();

		/****************** GetElement ******************/
		%feature("compactdefaultargs") GetElement;
		%feature("autodoc", "Get element by the index. @param theindex index of an element. returns element with the given index.

Parameters
----------
theIndex: int

Returns
-------
BRepMesh_Triangle
") GetElement;
		const BRepMesh_Triangle & GetElement(const Standard_Integer theIndex);

		/****************** GetLink ******************/
		%feature("compactdefaultargs") GetLink;
		%feature("autodoc", "Get link by the index. @param theindex index of a link. returns link with the given index.

Parameters
----------
theIndex: int

Returns
-------
BRepMesh_Edge
") GetLink;
		const BRepMesh_Edge & GetLink(const Standard_Integer theIndex);

		/****************** GetNode ******************/
		%feature("compactdefaultargs") GetNode;
		%feature("autodoc", "Get node by the index. @param theindex index of a node. returns node with the given index.

Parameters
----------
theIndex: int

Returns
-------
BRepMesh_Vertex
") GetNode;
		const BRepMesh_Vertex & GetNode(const Standard_Integer theIndex);

		/****************** IndexOf ******************/
		%feature("compactdefaultargs") IndexOf;
		%feature("autodoc", "Finds the index of the given node. @param thenode node to find. returns index of the given element of zero if node is not in the mesh.

Parameters
----------
theNode: BRepMesh_Vertex

Returns
-------
int
") IndexOf;
		Standard_Integer IndexOf(const BRepMesh_Vertex & theNode);

		/****************** IndexOf ******************/
		%feature("compactdefaultargs") IndexOf;
		%feature("autodoc", "Finds the index of the given link. @param thelink link to find. returns index of the given element of zero if link is not in the mesh.

Parameters
----------
theLink: BRepMesh_Edge

Returns
-------
int
") IndexOf;
		Standard_Integer IndexOf(const BRepMesh_Edge & theLink);

		/****************** LinksConnectedTo ******************/
		%feature("compactdefaultargs") LinksConnectedTo;
		%feature("autodoc", "Get list of links attached to the node with the given index. @param theindex index of node whose links should be retrieved. returns list of links attached to the node.

Parameters
----------
theIndex: int

Returns
-------
IMeshData::ListOfInteger
") LinksConnectedTo;
		const IMeshData::ListOfInteger & LinksConnectedTo(const Standard_Integer theIndex);

		/****************** LinksOfDomain ******************/
		%feature("compactdefaultargs") LinksOfDomain;
		%feature("autodoc", "Returns map of indices of links registered in mesh.

Returns
-------
IMeshData::MapOfInteger
") LinksOfDomain;
		const IMeshData::MapOfInteger & LinksOfDomain();

		/****************** NbElements ******************/
		%feature("compactdefaultargs") NbElements;
		%feature("autodoc", "Returns number of links.

Returns
-------
int
") NbElements;
		Standard_Integer NbElements();

		/****************** NbLinks ******************/
		%feature("compactdefaultargs") NbLinks;
		%feature("autodoc", "Returns number of links.

Returns
-------
int
") NbLinks;
		Standard_Integer NbLinks();

		/****************** NbNodes ******************/
		%feature("compactdefaultargs") NbNodes;
		%feature("autodoc", "Returns number of nodes.

Returns
-------
int
") NbNodes;
		Standard_Integer NbNodes();

		/****************** RemoveElement ******************/
		%feature("compactdefaultargs") RemoveElement;
		%feature("autodoc", "Removes element from the mesh. @param theindex index of element to be removed.

Parameters
----------
theIndex: int

Returns
-------
None
") RemoveElement;
		void RemoveElement(const Standard_Integer theIndex);

		/****************** RemoveLink ******************/
		%feature("compactdefaultargs") RemoveLink;
		%feature("autodoc", "Removes link from the mesh in case if it has no connected elements and its type is free. @param theindex index of link to be removed. @param isforce if true link will be removed even if movability is not free.

Parameters
----------
theIndex: int
isForce: bool,optional
	default value is Standard_False

Returns
-------
None
") RemoveLink;
		void RemoveLink(const Standard_Integer theIndex, const Standard_Boolean isForce = Standard_False);

		/****************** RemoveNode ******************/
		%feature("compactdefaultargs") RemoveNode;
		%feature("autodoc", "Removes node from the mesh in case if it has no connected links and its type is free. @param theindex index of node to be removed. @param isforce if true node will be removed even if movability is not free.

Parameters
----------
theIndex: int
isForce: bool,optional
	default value is Standard_False

Returns
-------
None
") RemoveNode;
		void RemoveNode(const Standard_Integer theIndex, const Standard_Boolean isForce = Standard_False);


        %feature("autodoc", "1");
        %extend{
            std::string StatisticsToString() {
            std::stringstream s;
            self->Statistics(s);
            return s.str();}
        };
		/****************** SubstituteElement ******************/
		%feature("compactdefaultargs") SubstituteElement;
		%feature("autodoc", "Substitutes the element with the given index by new one. @param theindex index of element to be substituted. @param thenewlink substituting element. returns false in case if new element is already in the structure, true elsewhere.

Parameters
----------
theIndex: int
theNewElement: BRepMesh_Triangle

Returns
-------
bool
") SubstituteElement;
		Standard_Boolean SubstituteElement(const Standard_Integer theIndex, const BRepMesh_Triangle & theNewElement);

		/****************** SubstituteLink ******************/
		%feature("compactdefaultargs") SubstituteLink;
		%feature("autodoc", "Substitutes the link with the given index by new one. @param theindex index of link to be substituted. @param thenewlink substituting link. returns false in case if new link is already in the structure, true elsewhere.

Parameters
----------
theIndex: int
theNewLink: BRepMesh_Edge

Returns
-------
bool
") SubstituteLink;
		Standard_Boolean SubstituteLink(const Standard_Integer theIndex, const BRepMesh_Edge & theNewLink);

		/****************** SubstituteNode ******************/
		%feature("compactdefaultargs") SubstituteNode;
		%feature("autodoc", "Substitutes the node with the given index by new one. @param theindex index of node to be substituted. @param thenewnode substituting node. returns false in case if new node is already in the structure, true elsewhere.

Parameters
----------
theIndex: int
theNewNode: BRepMesh_Vertex

Returns
-------
bool
") SubstituteNode;
		Standard_Boolean SubstituteNode(const Standard_Integer theIndex, const BRepMesh_Vertex & theNewNode);

};


%make_alias(BRepMesh_DataStructureOfDelaun)

%extend BRepMesh_DataStructureOfDelaun {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/****************************
* class BRepMesh_Deflection *
****************************/
class BRepMesh_Deflection : public Standard_Transient {
	public:
		/****************** ComputeAbsoluteDeflection ******************/
		%feature("compactdefaultargs") ComputeAbsoluteDeflection;
		%feature("autodoc", "Returns absolute deflection for theshape with respect to the relative deflection and themaxshapesize. @param theshape shape for that the deflection should be computed. @param therelativedeflection relative deflection. @param themaxshapesize maximum size of the whole shape. returns absolute deflection for the shape.

Parameters
----------
theShape: TopoDS_Shape
theRelativeDeflection: float
theMaxShapeSize: float

Returns
-------
float
") ComputeAbsoluteDeflection;
		static Standard_Real ComputeAbsoluteDeflection(const TopoDS_Shape & theShape, const Standard_Real theRelativeDeflection, const Standard_Real theMaxShapeSize);

		/****************** ComputeDeflection ******************/
		%feature("compactdefaultargs") ComputeDeflection;
		%feature("autodoc", "Computes and updates deflection of the given discrete edge.

Parameters
----------
theDEdge: IMeshData::IEdgeHandle
theMaxShapeSize: float
theParameters: IMeshTools_Parameters

Returns
-------
None
") ComputeDeflection;
		static void ComputeDeflection(const IMeshData::IEdgeHandle & theDEdge, const Standard_Real theMaxShapeSize, const IMeshTools_Parameters & theParameters);

		/****************** ComputeDeflection ******************/
		%feature("compactdefaultargs") ComputeDeflection;
		%feature("autodoc", "Computes and updates deflection of the given discrete wire.

Parameters
----------
theDWire: IMeshData::IWireHandle
theParameters: IMeshTools_Parameters

Returns
-------
None
") ComputeDeflection;
		static void ComputeDeflection(const IMeshData::IWireHandle & theDWire, const IMeshTools_Parameters & theParameters);

		/****************** ComputeDeflection ******************/
		%feature("compactdefaultargs") ComputeDeflection;
		%feature("autodoc", "Computes and updates deflection of the given discrete face.

Parameters
----------
theDFace: IMeshData::IFaceHandle
theParameters: IMeshTools_Parameters

Returns
-------
None
") ComputeDeflection;
		static void ComputeDeflection(const IMeshData::IFaceHandle & theDFace, const IMeshTools_Parameters & theParameters);

};


%make_alias(BRepMesh_Deflection)

%extend BRepMesh_Deflection {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/************************
* class BRepMesh_Delaun *
************************/
class BRepMesh_Delaun {
	public:
		/****************** BRepMesh_Delaun ******************/
		%feature("compactdefaultargs") BRepMesh_Delaun;
		%feature("autodoc", "Creates instance of triangulator, but do not run the algorithm automatically.

Parameters
----------
theOldMesh: BRepMesh_DataStructureOfDelaun
theCellsCountU: int
theCellsCountV: int
isFillCircles: bool

Returns
-------
None
") BRepMesh_Delaun;
		 BRepMesh_Delaun(const opencascade::handle<BRepMesh_DataStructureOfDelaun> & theOldMesh, const Standard_Integer theCellsCountU, const Standard_Integer theCellsCountV, const Standard_Boolean isFillCircles);

		/****************** BRepMesh_Delaun ******************/
		%feature("compactdefaultargs") BRepMesh_Delaun;
		%feature("autodoc", "Creates the triangulation with an empty mesh data structure.

Parameters
----------
theVertices: IMeshData::Array1OfVertexOfDelaun

Returns
-------
None
") BRepMesh_Delaun;
		 BRepMesh_Delaun(IMeshData::Array1OfVertexOfDelaun & theVertices);

		/****************** BRepMesh_Delaun ******************/
		%feature("compactdefaultargs") BRepMesh_Delaun;
		%feature("autodoc", "Creates the triangulation with an existent mesh data structure.

Parameters
----------
theOldMesh: BRepMesh_DataStructureOfDelaun
theVertices: IMeshData::Array1OfVertexOfDelaun

Returns
-------
None
") BRepMesh_Delaun;
		 BRepMesh_Delaun(const opencascade::handle<BRepMesh_DataStructureOfDelaun> & theOldMesh, IMeshData::Array1OfVertexOfDelaun & theVertices);

		/****************** BRepMesh_Delaun ******************/
		%feature("compactdefaultargs") BRepMesh_Delaun;
		%feature("autodoc", "Creates the triangulation with an existant mesh data structure.

Parameters
----------
theOldMesh: BRepMesh_DataStructureOfDelaun
theVertexIndices: IMeshData::VectorOfInteger

Returns
-------
None
") BRepMesh_Delaun;
		 BRepMesh_Delaun(const opencascade::handle<BRepMesh_DataStructureOfDelaun> & theOldMesh, IMeshData::VectorOfInteger & theVertexIndices);

		/****************** BRepMesh_Delaun ******************/
		%feature("compactdefaultargs") BRepMesh_Delaun;
		%feature("autodoc", "Creates the triangulation with an existant mesh data structure.

Parameters
----------
theOldMesh: Handle ( BRepMesh_DataStructureOfDelaun )
theVertexIndices: IMeshData::VectorOfInteger
theCellsCountU: int
theCellsCountV: int

Returns
-------
None
") BRepMesh_Delaun;
		 BRepMesh_Delaun(const Handle ( BRepMesh_DataStructureOfDelaun ) & theOldMesh, IMeshData::VectorOfInteger & theVertexIndices, const Standard_Integer theCellsCountU, const Standard_Integer theCellsCountV);

		/****************** AddVertices ******************/
		%feature("compactdefaultargs") AddVertices;
		%feature("autodoc", "Adds some vertices into the triangulation.

Parameters
----------
theVerticesIndices: IMeshData::VectorOfInteger

Returns
-------
None
") AddVertices;
		void AddVertices(IMeshData::VectorOfInteger & theVerticesIndices);

		/****************** Circles ******************/
		%feature("compactdefaultargs") Circles;
		%feature("autodoc", "Returns tool used to build mesh consistent to delaunay criteria.

Returns
-------
BRepMesh_CircleTool
") Circles;
		const BRepMesh_CircleTool & Circles();

		/****************** Contains ******************/
		%feature("compactdefaultargs") Contains;
		%feature("autodoc", "Test is the given triangle contains the given vertex. @param thesqtolerance square tolerance to check closeness to some edge @param theedgeon if it is != 0 the vertex lies onto the edge index returned through this parameter.

Parameters
----------
theTriangleId: int
theVertex: BRepMesh_Vertex
theSqTolerance: float

Returns
-------
theEdgeOn: int
") Contains;
		Standard_Boolean Contains(const Standard_Integer theTriangleId, const BRepMesh_Vertex & theVertex, const Standard_Real theSqTolerance, Standard_Integer &OutValue);

		/****************** GetEdge ******************/
		%feature("compactdefaultargs") GetEdge;
		%feature("autodoc", "Gives edge with the given index.

Parameters
----------
theIndex: int

Returns
-------
BRepMesh_Edge
") GetEdge;
		const BRepMesh_Edge & GetEdge(const Standard_Integer theIndex);

		/****************** GetTriangle ******************/
		%feature("compactdefaultargs") GetTriangle;
		%feature("autodoc", "Gives triangle with the given index.

Parameters
----------
theIndex: int

Returns
-------
BRepMesh_Triangle
") GetTriangle;
		const BRepMesh_Triangle & GetTriangle(const Standard_Integer theIndex);

		/****************** GetVertex ******************/
		%feature("compactdefaultargs") GetVertex;
		%feature("autodoc", "Gives vertex with the given index.

Parameters
----------
theIndex: int

Returns
-------
BRepMesh_Vertex
") GetVertex;
		const BRepMesh_Vertex & GetVertex(const Standard_Integer theIndex);

		/****************** Init ******************/
		%feature("compactdefaultargs") Init;
		%feature("autodoc", "Initializes the triangulation with an array of vertices.

Parameters
----------
theVertices: IMeshData::Array1OfVertexOfDelaun

Returns
-------
None
") Init;
		void Init(IMeshData::Array1OfVertexOfDelaun & theVertices);

		/****************** InitCirclesTool ******************/
		%feature("compactdefaultargs") InitCirclesTool;
		%feature("autodoc", "Forces initialization of circles cell filter using working structure.

Parameters
----------
theCellsCountU: int
theCellsCountV: int

Returns
-------
None
") InitCirclesTool;
		void InitCirclesTool(const Standard_Integer theCellsCountU, const Standard_Integer theCellsCountV);

		/****************** RemoveVertex ******************/
		%feature("compactdefaultargs") RemoveVertex;
		%feature("autodoc", "Removes a vertex from the triangulation.

Parameters
----------
theVertex: BRepMesh_Vertex

Returns
-------
None
") RemoveVertex;
		void RemoveVertex(const BRepMesh_Vertex & theVertex);

		/****************** Result ******************/
		%feature("compactdefaultargs") Result;
		%feature("autodoc", "Gives the mesh data structure.

Returns
-------
opencascade::handle<BRepMesh_DataStructureOfDelaun>
") Result;
		const opencascade::handle<BRepMesh_DataStructureOfDelaun> & Result();

		/****************** UseEdge ******************/
		%feature("compactdefaultargs") UseEdge;
		%feature("autodoc", "Modify mesh to use the edge. returns true if done.

Parameters
----------
theEdge: int

Returns
-------
bool
") UseEdge;
		Standard_Boolean UseEdge(const Standard_Integer theEdge);

};


%extend BRepMesh_Delaun {
	%pythoncode {
	__repr__ = _dumps_object

	@methodnotwrapped
	def Frontier(self):
		pass

	@methodnotwrapped
	def InternalEdges(self):
		pass

	@methodnotwrapped
	def FreeEdges(self):
		pass

	@methodnotwrapped
	def ProcessConstraints(self):
		pass
	}
};

/********************************
* class BRepMesh_DiscretFactory *
********************************/
%nodefaultctor BRepMesh_DiscretFactory;
%ignore BRepMesh_DiscretFactory::~BRepMesh_DiscretFactory();
class BRepMesh_DiscretFactory {
	public:
		/****************** DefaultName ******************/
		%feature("compactdefaultargs") DefaultName;
		%feature("autodoc", "Returns name for current meshing algorithm.

Returns
-------
TCollection_AsciiString
") DefaultName;
		const TCollection_AsciiString & DefaultName();

		/****************** Discret ******************/
		%feature("compactdefaultargs") Discret;
		%feature("autodoc", "Returns triangulation algorithm instance. @param theshape shape to be meshed. @param thelindeflection linear deflection to be used for meshing. @param theangdeflection angular deflection to be used for meshing.

Parameters
----------
theShape: TopoDS_Shape
theLinDeflection: float
theAngDeflection: float

Returns
-------
opencascade::handle<BRepMesh_DiscretRoot>
") Discret;
		opencascade::handle<BRepMesh_DiscretRoot> Discret(const TopoDS_Shape & theShape, const Standard_Real theLinDeflection, const Standard_Real theAngDeflection);

		/****************** ErrorStatus ******************/
		%feature("compactdefaultargs") ErrorStatus;
		%feature("autodoc", "Returns error status for last meshing algorithm switch.

Returns
-------
BRepMesh_FactoryError
") ErrorStatus;
		BRepMesh_FactoryError ErrorStatus();

		/****************** FunctionName ******************/
		%feature("compactdefaultargs") FunctionName;
		%feature("autodoc", "Returns function name that should be exported by plugin.

Returns
-------
TCollection_AsciiString
") FunctionName;
		const TCollection_AsciiString & FunctionName();

		/****************** Get ******************/
		%feature("compactdefaultargs") Get;
		%feature("autodoc", "Returns the global factory instance.

Returns
-------
BRepMesh_DiscretFactory
") Get;
		static BRepMesh_DiscretFactory & Get();

		/****************** Names ******************/
		%feature("compactdefaultargs") Names;
		%feature("autodoc", "Returns the list of registered meshing algorithms.

Returns
-------
TColStd_MapOfAsciiString
") Names;
		const TColStd_MapOfAsciiString & Names();

		/****************** SetDefault ******************/
		%feature("compactdefaultargs") SetDefault;
		%feature("autodoc", "Setup meshing algorithm that should be created by this factory. returns true if requested tool is available. on fail factory will continue to use previous algo. call ::errorstatus() method to retrieve fault reason.

Parameters
----------
theName: TCollection_AsciiString
theFuncName: TCollection_AsciiString,optional
	default value is 'DISCRETALGO'

Returns
-------
bool
") SetDefault;
		Standard_Boolean SetDefault(const TCollection_AsciiString & theName, const TCollection_AsciiString & theFuncName = "DISCRETALGO");

		/****************** SetDefaultName ******************/
		%feature("compactdefaultargs") SetDefaultName;
		%feature("autodoc", "Setup meshing algorithm by name. returns true if requested tool is available. on fail factory will continue to use previous algo.

Parameters
----------
theName: TCollection_AsciiString

Returns
-------
bool
") SetDefaultName;
		Standard_Boolean SetDefaultName(const TCollection_AsciiString & theName);

		/****************** SetFunctionName ******************/
		%feature("compactdefaultargs") SetFunctionName;
		%feature("autodoc", "Advanced function. changes function name to retrieve from plugin. returns true if requested tool is available. on fail factory will continue to use previous algo.

Parameters
----------
theFuncName: TCollection_AsciiString

Returns
-------
bool
") SetFunctionName;
		Standard_Boolean SetFunctionName(const TCollection_AsciiString & theFuncName);

};


%extend BRepMesh_DiscretFactory {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*****************************
* class BRepMesh_DiscretRoot *
*****************************/
%nodefaultctor BRepMesh_DiscretRoot;
class BRepMesh_DiscretRoot : public Standard_Transient {
	public:
		/****************** IsDone ******************/
		%feature("compactdefaultargs") IsDone;
		%feature("autodoc", "Returns true if triangualtion was performed and has success.

Returns
-------
bool
") IsDone;
		Standard_Boolean IsDone();

		/****************** Perform ******************/
		%feature("compactdefaultargs") Perform;
		%feature("autodoc", "Compute triangulation for set shape.

Returns
-------
None
") Perform;
		virtual void Perform();

		/****************** SetShape ******************/
		%feature("compactdefaultargs") SetShape;
		%feature("autodoc", "Set the shape to triangulate.

Parameters
----------
theShape: TopoDS_Shape

Returns
-------
None
") SetShape;
		void SetShape(const TopoDS_Shape & theShape);

		/****************** Shape ******************/
		%feature("compactdefaultargs") Shape;
		%feature("autodoc", "No available documentation.

Returns
-------
TopoDS_Shape
") Shape;
		const TopoDS_Shape Shape();

};


%make_alias(BRepMesh_DiscretRoot)

%extend BRepMesh_DiscretRoot {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*****************************
* class BRepMesh_EdgeDiscret *
*****************************/
class BRepMesh_EdgeDiscret : public IMeshTools_ModelAlgo {
	public:
		/****************** BRepMesh_EdgeDiscret ******************/
		%feature("compactdefaultargs") BRepMesh_EdgeDiscret;
		%feature("autodoc", "Constructor.

Returns
-------
None
") BRepMesh_EdgeDiscret;
		 BRepMesh_EdgeDiscret();

		/****************** CreateEdgeTessellationExtractor ******************/
		%feature("compactdefaultargs") CreateEdgeTessellationExtractor;
		%feature("autodoc", "Creates instance of tessellation extractor.

Parameters
----------
theDEdge: IMeshData::IEdgeHandle
theDFace: IMeshData::IFaceHandle

Returns
-------
opencascade::handle<IMeshTools_CurveTessellator>
") CreateEdgeTessellationExtractor;
		static opencascade::handle<IMeshTools_CurveTessellator> CreateEdgeTessellationExtractor(const IMeshData::IEdgeHandle & theDEdge, const IMeshData::IFaceHandle & theDFace);

		/****************** CreateEdgeTessellator ******************/
		%feature("compactdefaultargs") CreateEdgeTessellator;
		%feature("autodoc", "Creates instance of free edge tessellator.

Parameters
----------
theDEdge: IMeshData::IEdgeHandle
theParameters: IMeshTools_Parameters

Returns
-------
opencascade::handle<IMeshTools_CurveTessellator>
") CreateEdgeTessellator;
		static opencascade::handle<IMeshTools_CurveTessellator> CreateEdgeTessellator(const IMeshData::IEdgeHandle & theDEdge, const IMeshTools_Parameters & theParameters);

		/****************** CreateEdgeTessellator ******************/
		%feature("compactdefaultargs") CreateEdgeTessellator;
		%feature("autodoc", "Creates instance of edge tessellator.

Parameters
----------
theDEdge: IMeshData::IEdgeHandle
theOrientation: TopAbs_Orientation
theDFace: IMeshData::IFaceHandle
theParameters: IMeshTools_Parameters

Returns
-------
opencascade::handle<IMeshTools_CurveTessellator>
") CreateEdgeTessellator;
		static opencascade::handle<IMeshTools_CurveTessellator> CreateEdgeTessellator(const IMeshData::IEdgeHandle & theDEdge, const TopAbs_Orientation theOrientation, const IMeshData::IFaceHandle & theDFace, const IMeshTools_Parameters & theParameters);

		/****************** Tessellate2d ******************/
		%feature("compactdefaultargs") Tessellate2d;
		%feature("autodoc", "Updates 2d discrete edge model using tessellation of 3d curve.

Parameters
----------
theDEdge: IMeshData::IEdgeHandle
theUpdateEnds: bool

Returns
-------
None
") Tessellate2d;
		static void Tessellate2d(const IMeshData::IEdgeHandle & theDEdge, const Standard_Boolean theUpdateEnds);

		/****************** Tessellate3d ******************/
		%feature("compactdefaultargs") Tessellate3d;
		%feature("autodoc", "Updates 3d discrete edge model using the given tessellation tool.

Parameters
----------
theDEdge: IMeshData::IEdgeHandle
theTessellator: IMeshTools_CurveTessellator
theUpdateEnds: bool

Returns
-------
None
") Tessellate3d;
		static void Tessellate3d(const IMeshData::IEdgeHandle & theDEdge, const opencascade::handle<IMeshTools_CurveTessellator> & theTessellator, const Standard_Boolean theUpdateEnds);

};


%extend BRepMesh_EdgeDiscret {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***************************************
* class BRepMesh_EdgeParameterProvider *
***************************************/
/*******************************************
* class BRepMesh_EdgeTessellationExtractor *
*******************************************/
/*****************************
* class BRepMesh_FaceChecker *
*****************************/
class BRepMesh_FaceChecker : public Standard_Transient {
	public:
typedef NCollection_Shared<NCollection_Vector<Segment>> Segments;
typedef NCollection_Shared<NCollection_Array1<opencascade ::handle<Segments>>> ArrayOfSegments;
		class Segment {};
		/****************** BRepMesh_FaceChecker ******************/
		%feature("compactdefaultargs") BRepMesh_FaceChecker;
		%feature("autodoc", "Default constructor.

Parameters
----------
theFace: IMeshData::IFaceHandle
theParameters: IMeshTools_Parameters

Returns
-------
None
") BRepMesh_FaceChecker;
		 BRepMesh_FaceChecker(const IMeshData::IFaceHandle & theFace, const IMeshTools_Parameters & theParameters);

		/****************** Perform ******************/
		%feature("compactdefaultargs") Perform;
		%feature("autodoc", "Performs check wires of the face for intersections. returns true if there is no intersection, false elsewhere.

Returns
-------
bool
") Perform;
		Standard_Boolean Perform();

};


%make_alias(BRepMesh_FaceChecker)

%extend BRepMesh_FaceChecker {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*****************************
* class BRepMesh_FaceDiscret *
*****************************/
class BRepMesh_FaceDiscret : public IMeshTools_ModelAlgo {
	public:
		/****************** BRepMesh_FaceDiscret ******************/
		%feature("compactdefaultargs") BRepMesh_FaceDiscret;
		%feature("autodoc", "Constructor.

Parameters
----------
theAlgoFactory: IMeshTools_MeshAlgoFactory

Returns
-------
None
") BRepMesh_FaceDiscret;
		 BRepMesh_FaceDiscret(const opencascade::handle<IMeshTools_MeshAlgoFactory> & theAlgoFactory);

};


%extend BRepMesh_FaceDiscret {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**************************
* class BRepMesh_GeomTool *
**************************/
class BRepMesh_GeomTool {
	public:
/* public enums */
enum IntFlag {
	NoIntersection = 0,
	Cross = 1,
	EndPointTouch = 2,
	PointOnSegment = 3,
	Glued = 4,
	Same = 5,
};

/* end public enums declaration */

/* python proy classes for enums */
%pythoncode {

class IntFlag(IntEnum):
	NoIntersection = 0
	Cross = 1
	EndPointTouch = 2
	PointOnSegment = 3
	Glued = 4
	Same = 5
NoIntersection = IntFlag.NoIntersection
Cross = IntFlag.Cross
EndPointTouch = IntFlag.EndPointTouch
PointOnSegment = IntFlag.PointOnSegment
Glued = IntFlag.Glued
Same = IntFlag.Same
};
/* end python proxy for enums */

		/****************** BRepMesh_GeomTool ******************/
		%feature("compactdefaultargs") BRepMesh_GeomTool;
		%feature("autodoc", "Constructor. initiates discretization of the given geometric curve. @param thecurve curve to be discretized. @param thefirstparam first parameter of the curve. @param thelastparam last parameter of the curve. @param thelindeflection linear deflection. @param theangdeflection angular deflection. @param theminpointsnb minimum nuber of points to be produced.

Parameters
----------
theCurve: BRepAdaptor_Curve
theFirstParam: float
theLastParam: float
theLinDeflection: float
theAngDeflection: float
theMinPointsNb: int,optional
	default value is 2
theMinSize: float,optional
	default value is Precision::Confusion()

Returns
-------
None
") BRepMesh_GeomTool;
		 BRepMesh_GeomTool(const BRepAdaptor_Curve & theCurve, const Standard_Real theFirstParam, const Standard_Real theLastParam, const Standard_Real theLinDeflection, const Standard_Real theAngDeflection, const Standard_Integer theMinPointsNb = 2, const Standard_Real theMinSize = Precision::Confusion());

		/****************** BRepMesh_GeomTool ******************/
		%feature("compactdefaultargs") BRepMesh_GeomTool;
		%feature("autodoc", "Constructor. initiates discretization of geometric curve corresponding to iso curve of the given surface. @param thesurface surface the iso curve to be taken from. @param theisotype type of iso curve to be used, u or v. @param theparamiso parameter on the surface specifying the iso curve. @param thefirstparam first parameter of the curve. @param thelastparam last parameter of the curve. @param thelindeflection linear deflection. @param theangdeflection angular deflection. @param theminpointsnb minimum nuber of points to be produced.

Parameters
----------
theSurface: BRepAdaptor_HSurface
theIsoType: GeomAbs_IsoType
theParamIso: float
theFirstParam: float
theLastParam: float
theLinDeflection: float
theAngDeflection: float
theMinPointsNb: int,optional
	default value is 2
theMinSize: float,optional
	default value is Precision::Confusion()

Returns
-------
None
") BRepMesh_GeomTool;
		 BRepMesh_GeomTool(const opencascade::handle<BRepAdaptor_HSurface> & theSurface, const GeomAbs_IsoType theIsoType, const Standard_Real theParamIso, const Standard_Real theFirstParam, const Standard_Real theLastParam, const Standard_Real theLinDeflection, const Standard_Real theAngDeflection, const Standard_Integer theMinPointsNb = 2, const Standard_Real theMinSize = Precision::Confusion());

		/****************** AddPoint ******************/
		%feature("compactdefaultargs") AddPoint;
		%feature("autodoc", "Adds point to already calculated points (or replaces existing). @param thepoint point to be added. @param theparam parameter on the curve corresponding to the given point. @param theisreplace if true replaces existing point lying within parameteric tolerance of the given point. returns index of new added point or found with parametric tolerance.

Parameters
----------
thePoint: gp_Pnt
theParam: float
theIsReplace: bool,optional
	default value is Standard_True

Returns
-------
int
") AddPoint;
		Standard_Integer AddPoint(const gp_Pnt & thePoint, const Standard_Real theParam, const Standard_Boolean theIsReplace = Standard_True);

		/****************** CellsCount ******************/
		%feature("compactdefaultargs") CellsCount;
		%feature("autodoc", "No available documentation.

Parameters
----------
theSurface: Handle ( Adaptor3d_HSurface )
theVerticesNb: int
theDeflection: float
theRangeSplitter: BRepMesh_DefaultRangeSplitter *

Returns
-------
std::pair<int, int >
") CellsCount;
		static std::pair<Standard_Integer, Standard_Integer > CellsCount(const Handle ( Adaptor3d_HSurface ) & theSurface, const Standard_Integer theVerticesNb, const Standard_Real theDeflection, const BRepMesh_DefaultRangeSplitter * theRangeSplitter);

		/****************** NbPoints ******************/
		%feature("compactdefaultargs") NbPoints;
		%feature("autodoc", "Returns number of discretization points.

Returns
-------
int
") NbPoints;
		Standard_Integer NbPoints();

		/****************** SquareDeflectionOfSegment ******************/
		%feature("compactdefaultargs") SquareDeflectionOfSegment;
		%feature("autodoc", "Compute deflection of the given segment.

Parameters
----------
theFirstPoint: gp_Pnt
theLastPoint: gp_Pnt
theMidPoint: gp_Pnt

Returns
-------
float
") SquareDeflectionOfSegment;
		static Standard_Real SquareDeflectionOfSegment(const gp_Pnt & theFirstPoint, const gp_Pnt & theLastPoint, const gp_Pnt & theMidPoint);

		/****************** Value ******************/
		%feature("compactdefaultargs") Value;
		%feature("autodoc", "Gets parameters of discretization point with the given index. @param theindex index of discretization point. @param theisoparam parameter on surface to be used as second coordinate of resulting 2d point. @param theparam[out] parameter of the point on the iso curve. @param thepoint[out] discretization point. @param theuv[out] discretization point in parametric space of the surface. returns true on success, false elsewhere.

Parameters
----------
theIndex: int
theIsoParam: float
thePoint: gp_Pnt
theUV: gp_Pnt2d

Returns
-------
theParam: float
") Value;
		Standard_Boolean Value(const Standard_Integer theIndex, const Standard_Real theIsoParam, Standard_Real &OutValue, gp_Pnt & thePoint, gp_Pnt2d & theUV);

		/****************** Value ******************/
		%feature("compactdefaultargs") Value;
		%feature("autodoc", "Gets parameters of discretization point with the given index. @param theindex index of discretization point. @param thesurface surface the curve is lying onto. @param theparam[out] parameter of the point on the curve. @param thepoint[out] discretization point. @param theuv[out] discretization point in parametric space of the surface. returns true on success, false elsewhere.

Parameters
----------
theIndex: int
theSurface: BRepAdaptor_HSurface
thePoint: gp_Pnt
theUV: gp_Pnt2d

Returns
-------
theParam: float
") Value;
		Standard_Boolean Value(const Standard_Integer theIndex, const opencascade::handle<BRepAdaptor_HSurface> & theSurface, Standard_Real &OutValue, gp_Pnt & thePoint, gp_Pnt2d & theUV);

};


%extend BRepMesh_GeomTool {
	%pythoncode {
	__repr__ = _dumps_object

	@methodnotwrapped
	def IntLinLin(self):
		pass

	@methodnotwrapped
	def Normal(self):
		pass

	@methodnotwrapped
	def IntSegSeg(self):
		pass
	}
};

/*********************************
* class BRepMesh_MeshAlgoFactory *
*********************************/
class BRepMesh_MeshAlgoFactory : public IMeshTools_MeshAlgoFactory {
	public:
		/****************** BRepMesh_MeshAlgoFactory ******************/
		%feature("compactdefaultargs") BRepMesh_MeshAlgoFactory;
		%feature("autodoc", "Constructor.

Returns
-------
None
") BRepMesh_MeshAlgoFactory;
		 BRepMesh_MeshAlgoFactory();

		/****************** GetAlgo ******************/
		%feature("compactdefaultargs") GetAlgo;
		%feature("autodoc", "Creates instance of meshing algorithm for the given type of surface.

Parameters
----------
theSurfaceType: GeomAbs_SurfaceType
theParameters: IMeshTools_Parameters

Returns
-------
opencascade::handle<IMeshTools_MeshAlgo>
") GetAlgo;
		virtual opencascade::handle<IMeshTools_MeshAlgo> GetAlgo(const GeomAbs_SurfaceType theSurfaceType, const IMeshTools_Parameters & theParameters);

};


%extend BRepMesh_MeshAlgoFactory {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**************************
* class BRepMesh_MeshTool *
**************************/
class BRepMesh_MeshTool : public Standard_Transient {
	public:
		class NodeClassifier {};
		/****************** BRepMesh_MeshTool ******************/
		%feature("compactdefaultargs") BRepMesh_MeshTool;
		%feature("autodoc", "Constructor. initializes tool by the given data structure.

Parameters
----------
theStructure: BRepMesh_DataStructureOfDelaun

Returns
-------
None
") BRepMesh_MeshTool;
		 BRepMesh_MeshTool(const opencascade::handle<BRepMesh_DataStructureOfDelaun> & theStructure);

		/****************** AddAndLegalizeTriangle ******************/
		%feature("compactdefaultargs") AddAndLegalizeTriangle;
		%feature("autodoc", "Adds new triangle with specified nodes to mesh. legalizes triangle in case if it violates circle criteria.

Parameters
----------
thePoint1: int
thePoint2: int
thePoint3: int

Returns
-------
None
") AddAndLegalizeTriangle;
		void AddAndLegalizeTriangle(const Standard_Integer thePoint1, const Standard_Integer thePoint2, const Standard_Integer thePoint3);

		/****************** AddLink ******************/
		%feature("compactdefaultargs") AddLink;
		%feature("autodoc", "Adds new link to mesh. updates link index and link orientaion parameters.

Parameters
----------
theFirstNode: int
theLastNode: int

Returns
-------
theLinkIndex: int
theLinkOri: bool
") AddLink;
		void AddLink(const Standard_Integer theFirstNode, const Standard_Integer theLastNode, Standard_Integer &OutValue, Standard_Boolean &OutValue);

		/****************** AddTriangle ******************/
		%feature("compactdefaultargs") AddTriangle;
		%feature("autodoc", "Adds new triangle with specified nodes to mesh.

Parameters
----------
thePoint1: int
thePoint2: int
thePoint3: int
): int (  theEdges

Returns
-------
None
") AddTriangle;
		void AddTriangle(const Standard_Integer thePoint1, const Standard_Integer thePoint2, const Standard_Integer thePoint3, Standard_Integer ( & theEdges )[3]);

		/****************** CleanFrontierLinks ******************/
		%feature("compactdefaultargs") CleanFrontierLinks;
		%feature("autodoc", "Cleans frontier links from triangles to the right.

Returns
-------
None
") CleanFrontierLinks;
		void CleanFrontierLinks();

		/****************** EraseFreeLinks ******************/
		%feature("compactdefaultargs") EraseFreeLinks;
		%feature("autodoc", "Erases all links that have no elements connected to them.

Returns
-------
None
") EraseFreeLinks;
		void EraseFreeLinks();

		/****************** EraseFreeLinks ******************/
		%feature("compactdefaultargs") EraseFreeLinks;
		%feature("autodoc", "Erases links from the specified map that have no elements connected to them.

Parameters
----------
theLinks: IMeshData::MapOfIntegerInteger

Returns
-------
None
") EraseFreeLinks;
		void EraseFreeLinks(const IMeshData::MapOfIntegerInteger & theLinks);

		/****************** EraseItemsConnectedTo ******************/
		%feature("compactdefaultargs") EraseItemsConnectedTo;
		%feature("autodoc", "Erases all elements connected to the specified artificial node. in addition, erases the artificial node itself.

Parameters
----------
theNodeIndex: int

Returns
-------
None
") EraseItemsConnectedTo;
		void EraseItemsConnectedTo(const Standard_Integer theNodeIndex);

		/****************** EraseTriangle ******************/
		%feature("compactdefaultargs") EraseTriangle;
		%feature("autodoc", "Erases triangle with the given index and adds the free edges into the map. when an edge is suppressed more than one time it is destroyed.

Parameters
----------
theTriangleIndex: int
theLoopEdges: IMeshData::MapOfIntegerInteger

Returns
-------
None
") EraseTriangle;
		void EraseTriangle(const Standard_Integer theTriangleIndex, IMeshData::MapOfIntegerInteger & theLoopEdges);

		/****************** GetStructure ******************/
		%feature("compactdefaultargs") GetStructure;
		%feature("autodoc", "Returns data structure manipulated by this tool.

Returns
-------
opencascade::handle<BRepMesh_DataStructureOfDelaun>
") GetStructure;
		const opencascade::handle<BRepMesh_DataStructureOfDelaun> & GetStructure();

		/****************** Legalize ******************/
		%feature("compactdefaultargs") Legalize;
		%feature("autodoc", "Performs legalization of triangles connected to the specified link.

Parameters
----------
theLinkIndex: int

Returns
-------
None
") Legalize;
		void Legalize(const Standard_Integer theLinkIndex);

};


%make_alias(BRepMesh_MeshTool)

%extend BRepMesh_MeshTool {
	%pythoncode {
	__repr__ = _dumps_object

	@methodnotwrapped
	def DumpTriangles(self):
		pass

	@methodnotwrapped
	def EraseTriangles(self):
		pass
	}
};

/******************************
* class BRepMesh_ModelBuilder *
******************************/
class BRepMesh_ModelBuilder : public IMeshTools_ModelBuilder {
	public:
		/****************** BRepMesh_ModelBuilder ******************/
		%feature("compactdefaultargs") BRepMesh_ModelBuilder;
		%feature("autodoc", "Constructor.

Returns
-------
None
") BRepMesh_ModelBuilder;
		 BRepMesh_ModelBuilder();

};


%extend BRepMesh_ModelBuilder {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*****************************
* class BRepMesh_ModelHealer *
*****************************/
class BRepMesh_ModelHealer : public IMeshTools_ModelAlgo {
	public:
		/****************** BRepMesh_ModelHealer ******************/
		%feature("compactdefaultargs") BRepMesh_ModelHealer;
		%feature("autodoc", "Constructor.

Returns
-------
None
") BRepMesh_ModelHealer;
		 BRepMesh_ModelHealer();

};


%extend BRepMesh_ModelHealer {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/************************************
* class BRepMesh_ModelPostProcessor *
************************************/
class BRepMesh_ModelPostProcessor : public IMeshTools_ModelAlgo {
	public:
		/****************** BRepMesh_ModelPostProcessor ******************/
		%feature("compactdefaultargs") BRepMesh_ModelPostProcessor;
		%feature("autodoc", "Constructor.

Returns
-------
None
") BRepMesh_ModelPostProcessor;
		 BRepMesh_ModelPostProcessor();

};


%extend BRepMesh_ModelPostProcessor {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***********************************
* class BRepMesh_ModelPreProcessor *
***********************************/
class BRepMesh_ModelPreProcessor : public IMeshTools_ModelAlgo {
	public:
		/****************** BRepMesh_ModelPreProcessor ******************/
		%feature("compactdefaultargs") BRepMesh_ModelPreProcessor;
		%feature("autodoc", "Constructor.

Returns
-------
None
") BRepMesh_ModelPreProcessor;
		 BRepMesh_ModelPreProcessor();

};


%extend BRepMesh_ModelPreProcessor {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***************************************
* class BRepMesh_NodeInsertionMeshAlgo *
***************************************/
/******************************
* class BRepMesh_OrientedEdge *
******************************/
class BRepMesh_OrientedEdge {
	public:
		/****************** BRepMesh_OrientedEdge ******************/
		%feature("compactdefaultargs") BRepMesh_OrientedEdge;
		%feature("autodoc", "Default constructor.

Returns
-------
None
") BRepMesh_OrientedEdge;
		 BRepMesh_OrientedEdge();

		/****************** BRepMesh_OrientedEdge ******************/
		%feature("compactdefaultargs") BRepMesh_OrientedEdge;
		%feature("autodoc", "Constructs a link between two vertices.

Parameters
----------
theFirstNode: int
theLastNode: int

Returns
-------
None
") BRepMesh_OrientedEdge;
		 BRepMesh_OrientedEdge(const Standard_Integer theFirstNode, const Standard_Integer theLastNode);

		/****************** FirstNode ******************/
		%feature("compactdefaultargs") FirstNode;
		%feature("autodoc", "Returns index of first node of the link.

Returns
-------
int
") FirstNode;
		Standard_Integer FirstNode();

		/****************** HashCode ******************/
		%feature("compactdefaultargs") HashCode;
		%feature("autodoc", "Computes a hash code for this oriented edge, in the range [1, theupperbound] @param theupperbound the upper bound of the range a computing hash code must be within returns a computed hash code, in the range [1, theupperbound].

Parameters
----------
theUpperBound: int

Returns
-------
int
") HashCode;
		Standard_Integer HashCode(const Standard_Integer theUpperBound);

        %extend {
            Standard_Integer __hash__() {
            return $self->HashCode(2147483647);
            }
        };

		/****************** IsEqual ******************/
		%feature("compactdefaultargs") IsEqual;
		%feature("autodoc", "Checks this and other edge for equality. @param theother edge to be checked against this one. @retrun true if edges have the same orientation, false if not.

Parameters
----------
theOther: BRepMesh_OrientedEdge

Returns
-------
bool
") IsEqual;
		Standard_Boolean IsEqual(const BRepMesh_OrientedEdge & theOther);

		/****************** LastNode ******************/
		%feature("compactdefaultargs") LastNode;
		%feature("autodoc", "Returns index of last node of the link.

Returns
-------
int
") LastNode;
		Standard_Integer LastNode();


            %extend{
                bool __eq_wrapper__(const BRepMesh_OrientedEdge other) {
                if (*self==other) return true;
                else return false;
                }
            }
            %pythoncode {
            def __eq__(self, right):
                try:
                    return self.__eq_wrapper__(right)
                except:
                    return False
            }
};


%extend BRepMesh_OrientedEdge {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*****************************
* class BRepMesh_PairOfIndex *
*****************************/
class BRepMesh_PairOfIndex {
	public:
		/****************** BRepMesh_PairOfIndex ******************/
		%feature("compactdefaultargs") BRepMesh_PairOfIndex;
		%feature("autodoc", "Default constructor.

Returns
-------
None
") BRepMesh_PairOfIndex;
		 BRepMesh_PairOfIndex();

		/****************** Append ******************/
		%feature("compactdefaultargs") Append;
		%feature("autodoc", "Appends index to the pair.

Parameters
----------
theIndex: int

Returns
-------
None
") Append;
		void Append(const Standard_Integer theIndex);

		/****************** Clear ******************/
		%feature("compactdefaultargs") Clear;
		%feature("autodoc", "Clears indices.

Returns
-------
None
") Clear;
		void Clear();

		/****************** Extent ******************/
		%feature("compactdefaultargs") Extent;
		%feature("autodoc", "Returns number of initialized indeces.

Returns
-------
int
") Extent;
		Standard_Integer Extent();

		/****************** FirstIndex ******************/
		%feature("compactdefaultargs") FirstIndex;
		%feature("autodoc", "Returns first index of pair.

Returns
-------
int
") FirstIndex;
		Standard_Integer FirstIndex();

		/****************** Index ******************/
		%feature("compactdefaultargs") Index;
		%feature("autodoc", "Returns index corresponding to the given position in the pair. @param thepairpos position of index in the pair (1 or 2).

Parameters
----------
thePairPos: int

Returns
-------
int
") Index;
		Standard_Integer Index(const Standard_Integer thePairPos);

		/****************** IsEmpty ******************/
		%feature("compactdefaultargs") IsEmpty;
		%feature("autodoc", "Returns is pair is empty.

Returns
-------
bool
") IsEmpty;
		Standard_Boolean IsEmpty();

		/****************** LastIndex ******************/
		%feature("compactdefaultargs") LastIndex;
		%feature("autodoc", "Returns last index of pair.

Returns
-------
int
") LastIndex;
		Standard_Integer LastIndex();

		/****************** Prepend ******************/
		%feature("compactdefaultargs") Prepend;
		%feature("autodoc", "Prepends index to the pair.

Parameters
----------
theIndex: int

Returns
-------
None
") Prepend;
		void Prepend(const Standard_Integer theIndex);

		/****************** RemoveIndex ******************/
		%feature("compactdefaultargs") RemoveIndex;
		%feature("autodoc", "Remove index from the given position. @param thepairpos position of index in the pair (1 or 2).

Parameters
----------
thePairPos: int

Returns
-------
None
") RemoveIndex;
		void RemoveIndex(const Standard_Integer thePairPos);

		/****************** SetIndex ******************/
		%feature("compactdefaultargs") SetIndex;
		%feature("autodoc", "Sets index corresponding to the given position in the pair. @param thepairpos position of index in the pair (1 or 2). @param theindex index to be stored.

Parameters
----------
thePairPos: int
theIndex: int

Returns
-------
None
") SetIndex;
		void SetIndex(const Standard_Integer thePairPos, const Standard_Integer theIndex);

};


%extend BRepMesh_PairOfIndex {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*************************************************
* class BRepMesh_SelectorOfDataStructureOfDelaun *
*************************************************/
class BRepMesh_SelectorOfDataStructureOfDelaun : public Standard_Transient {
	public:
		/****************** BRepMesh_SelectorOfDataStructureOfDelaun ******************/
		%feature("compactdefaultargs") BRepMesh_SelectorOfDataStructureOfDelaun;
		%feature("autodoc", "Default constructor.

Returns
-------
None
") BRepMesh_SelectorOfDataStructureOfDelaun;
		 BRepMesh_SelectorOfDataStructureOfDelaun();

		/****************** BRepMesh_SelectorOfDataStructureOfDelaun ******************/
		%feature("compactdefaultargs") BRepMesh_SelectorOfDataStructureOfDelaun;
		%feature("autodoc", "Constructor. initializes selector by the mesh.

Parameters
----------
theMesh: BRepMesh_DataStructureOfDelaun

Returns
-------
None
") BRepMesh_SelectorOfDataStructureOfDelaun;
		 BRepMesh_SelectorOfDataStructureOfDelaun(const opencascade::handle<BRepMesh_DataStructureOfDelaun> & theMesh);

		/****************** AddNeighbours ******************/
		%feature("compactdefaultargs") AddNeighbours;
		%feature("autodoc", "Adds a level of neighbours by edge the selector.

Returns
-------
None
") AddNeighbours;
		void AddNeighbours();

		/****************** Elements ******************/
		%feature("compactdefaultargs") Elements;
		%feature("autodoc", "Returns selected elements.

Returns
-------
IMeshData::MapOfInteger
") Elements;
		const IMeshData::MapOfInteger & Elements();

		/****************** FrontierLinks ******************/
		%feature("compactdefaultargs") FrontierLinks;
		%feature("autodoc", "Gives the list of incices of frontier links.

Returns
-------
IMeshData::MapOfInteger
") FrontierLinks;
		const IMeshData::MapOfInteger & FrontierLinks();

		/****************** Initialize ******************/
		%feature("compactdefaultargs") Initialize;
		%feature("autodoc", "Initializes selector by the mesh.

Parameters
----------
theMesh: BRepMesh_DataStructureOfDelaun

Returns
-------
None
") Initialize;
		void Initialize(const opencascade::handle<BRepMesh_DataStructureOfDelaun> & theMesh);

		/****************** Links ******************/
		%feature("compactdefaultargs") Links;
		%feature("autodoc", "Returns selected links.

Returns
-------
IMeshData::MapOfInteger
") Links;
		const IMeshData::MapOfInteger & Links();

		/****************** NeighboursByEdgeOf ******************/
		%feature("compactdefaultargs") NeighboursByEdgeOf;
		%feature("autodoc", "Selects all neighboring elements by links of the given element.

Parameters
----------
theElement: BRepMesh_Triangle

Returns
-------
None
") NeighboursByEdgeOf;
		void NeighboursByEdgeOf(const BRepMesh_Triangle & theElement);

		/****************** NeighboursOf ******************/
		%feature("compactdefaultargs") NeighboursOf;
		%feature("autodoc", "Selects all neighboring elements of the given node.

Parameters
----------
theNode: BRepMesh_Vertex

Returns
-------
None
") NeighboursOf;
		void NeighboursOf(const BRepMesh_Vertex & theNode);

		/****************** NeighboursOf ******************/
		%feature("compactdefaultargs") NeighboursOf;
		%feature("autodoc", "Selects all neighboring elements of the given link.

Parameters
----------
theLink: BRepMesh_Edge

Returns
-------
None
") NeighboursOf;
		void NeighboursOf(const BRepMesh_Edge & theLink);

		/****************** NeighboursOf ******************/
		%feature("compactdefaultargs") NeighboursOf;
		%feature("autodoc", "Selects all neighboring elements of the given element.

Parameters
----------
theElement: BRepMesh_Triangle

Returns
-------
None
") NeighboursOf;
		void NeighboursOf(const BRepMesh_Triangle & theElement);

		/****************** NeighboursOf ******************/
		%feature("compactdefaultargs") NeighboursOf;
		%feature("autodoc", "Adds a level of neighbours by edge to the selector.

Parameters
----------
&: BRepMesh_SelectorOfDataStructureOfDelaun

Returns
-------
None
") NeighboursOf;
		void NeighboursOf(const BRepMesh_SelectorOfDataStructureOfDelaun &);

		/****************** NeighboursOfElement ******************/
		%feature("compactdefaultargs") NeighboursOfElement;
		%feature("autodoc", "Selects all neighboring elements by nodes of the given element.

Parameters
----------
theElementIndex: int

Returns
-------
None
") NeighboursOfElement;
		void NeighboursOfElement(const Standard_Integer theElementIndex);

		/****************** NeighboursOfLink ******************/
		%feature("compactdefaultargs") NeighboursOfLink;
		%feature("autodoc", "Selects all neighboring elements of link with the given index.

Parameters
----------
theLinkIndex: int

Returns
-------
None
") NeighboursOfLink;
		void NeighboursOfLink(const Standard_Integer theLinkIndex);

		/****************** NeighboursOfNode ******************/
		%feature("compactdefaultargs") NeighboursOfNode;
		%feature("autodoc", "Selects all neighboring elements of node with the given index.

Parameters
----------
theNodeIndex: int

Returns
-------
None
") NeighboursOfNode;
		void NeighboursOfNode(const Standard_Integer theNodeIndex);

		/****************** Nodes ******************/
		%feature("compactdefaultargs") Nodes;
		%feature("autodoc", "Returns selected nodes.

Returns
-------
IMeshData::MapOfInteger
") Nodes;
		const IMeshData::MapOfInteger & Nodes();

};


%make_alias(BRepMesh_SelectorOfDataStructureOfDelaun)

%extend BRepMesh_SelectorOfDataStructureOfDelaun {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***************************
* class BRepMesh_ShapeTool *
***************************/
class BRepMesh_ShapeTool : public Standard_Transient {
	public:
		/****************** AddInFace ******************/
		%feature("compactdefaultargs") AddInFace;
		%feature("autodoc", "Stores the given triangulation into the given face. @param theface face to be updated by triangulation. @param thetriangulation triangulation to be stored into the face.

Parameters
----------
theFace: TopoDS_Face
theTriangulation: Poly_Triangulation

Returns
-------
None
") AddInFace;
		static void AddInFace(const TopoDS_Face & theFace, opencascade::handle<Poly_Triangulation> & theTriangulation);

		/****************** BoxMaxDimension ******************/
		%feature("compactdefaultargs") BoxMaxDimension;
		%feature("autodoc", "Gets the maximum dimension of the given bounding box. if the given bounding box is void leaves the resulting value unchanged. @param thebox bounding box to be processed. @param themaxdimension maximum dimension of the given box.

Parameters
----------
theBox: Bnd_Box

Returns
-------
theMaxDimension: float
") BoxMaxDimension;
		static void BoxMaxDimension(const Bnd_Box & theBox, Standard_Real &OutValue);

		/****************** CheckAndUpdateFlags ******************/
		%feature("compactdefaultargs") CheckAndUpdateFlags;
		%feature("autodoc", "Checks same parameter, same range and degenerativity attributes using geometrical data of the given edge and updates edge model by computed parameters in case of worst case - it can drop flags same parameter and same range to false but never to true if it is already set to false. in contrary, it can also drop degenerated flag to true, but never to false if it is already set to true.

Parameters
----------
theEdge: IMeshData::IEdgeHandle
thePCurve: IMeshData::IPCurveHandle

Returns
-------
None
") CheckAndUpdateFlags;
		static void CheckAndUpdateFlags(const IMeshData::IEdgeHandle & theEdge, const IMeshData::IPCurveHandle & thePCurve);

		/****************** MaxFaceTolerance ******************/
		%feature("compactdefaultargs") MaxFaceTolerance;
		%feature("autodoc", "Returns maximum tolerance of the given face. considers tolerances of edges and vertices contained in the given face.

Parameters
----------
theFace: TopoDS_Face

Returns
-------
float
") MaxFaceTolerance;
		static Standard_Real MaxFaceTolerance(const TopoDS_Face & theFace);

		/****************** NullifyEdge ******************/
		%feature("compactdefaultargs") NullifyEdge;
		%feature("autodoc", "Nullifies polygon on triangulation stored in the edge. @param theedge edge to be updated by null polygon. @param thetriangulation triangulation the given edge is associated to. @param thelocation face location.

Parameters
----------
theEdge: TopoDS_Edge
theTriangulation: Handle ( Poly_Triangulation )
theLocation: TopLoc_Location

Returns
-------
None
") NullifyEdge;
		static void NullifyEdge(const TopoDS_Edge & theEdge, const Handle ( Poly_Triangulation ) & theTriangulation, const TopLoc_Location & theLocation);

		/****************** NullifyEdge ******************/
		%feature("compactdefaultargs") NullifyEdge;
		%feature("autodoc", "Nullifies 3d polygon stored in the edge. @param theedge edge to be updated by null polygon. @param thelocation face location.

Parameters
----------
theEdge: TopoDS_Edge
theLocation: TopLoc_Location

Returns
-------
None
") NullifyEdge;
		static void NullifyEdge(const TopoDS_Edge & theEdge, const TopLoc_Location & theLocation);

		/****************** NullifyFace ******************/
		%feature("compactdefaultargs") NullifyFace;
		%feature("autodoc", "Nullifies triangulation stored in the face. @param theface face to be updated by null triangulation.

Parameters
----------
theFace: TopoDS_Face

Returns
-------
None
") NullifyFace;
		static void NullifyFace(const TopoDS_Face & theFace);

		/****************** Range ******************/
		%feature("compactdefaultargs") Range;
		%feature("autodoc", "Gets the parametric range of the given edge on the given face.

Parameters
----------
theEdge: TopoDS_Edge
theFace: TopoDS_Face
thePCurve: Handle ( Geom2d_Curve )
isConsiderOrientation: bool,optional
	default value is Standard_False

Returns
-------
theFirstParam: float
theLastParam: float
") Range;
		static Standard_Boolean Range(const TopoDS_Edge & theEdge, const TopoDS_Face & theFace, Handle ( Geom2d_Curve ) & thePCurve, Standard_Real &OutValue, Standard_Real &OutValue, const Standard_Boolean isConsiderOrientation = Standard_False);

		/****************** Range ******************/
		%feature("compactdefaultargs") Range;
		%feature("autodoc", "Gets the 3d range of the given edge.

Parameters
----------
theEdge: TopoDS_Edge
theCurve: Handle ( Geom_Curve )
isConsiderOrientation: bool,optional
	default value is Standard_False

Returns
-------
theFirstParam: float
theLastParam: float
") Range;
		static Standard_Boolean Range(const TopoDS_Edge & theEdge, Handle ( Geom_Curve ) & theCurve, Standard_Real &OutValue, Standard_Real &OutValue, const Standard_Boolean isConsiderOrientation = Standard_False);

		/****************** UVPoints ******************/
		%feature("compactdefaultargs") UVPoints;
		%feature("autodoc", "Gets the strict uv locations of the extremities of the edge using pcurve.

Parameters
----------
theEdge: TopoDS_Edge
theFace: TopoDS_Face
theFirstPoint2d: gp_Pnt2d
theLastPoint2d: gp_Pnt2d
isConsiderOrientation: bool,optional
	default value is Standard_False

Returns
-------
bool
") UVPoints;
		static Standard_Boolean UVPoints(const TopoDS_Edge & theEdge, const TopoDS_Face & theFace, gp_Pnt2d & theFirstPoint2d, gp_Pnt2d & theLastPoint2d, const Standard_Boolean isConsiderOrientation = Standard_False);

		/****************** UpdateEdge ******************/
		%feature("compactdefaultargs") UpdateEdge;
		%feature("autodoc", "Updates the given edge by the given tessellated representation. @param theedge edge to be updated. @param thepolygon tessellated representation of the edge to be stored. @param thetriangulation triangulation the given edge is associated to. @param thelocation face location.

Parameters
----------
theEdge: TopoDS_Edge
thePolygon: Handle ( Poly_PolygonOnTriangulation )
theTriangulation: Handle ( Poly_Triangulation )
theLocation: TopLoc_Location

Returns
-------
None
") UpdateEdge;
		static void UpdateEdge(const TopoDS_Edge & theEdge, const Handle ( Poly_PolygonOnTriangulation ) & thePolygon, const Handle ( Poly_Triangulation ) & theTriangulation, const TopLoc_Location & theLocation);

		/****************** UpdateEdge ******************/
		%feature("compactdefaultargs") UpdateEdge;
		%feature("autodoc", "Updates the given edge by the given tessellated representation. @param theedge edge to be updated. @param thepolygon tessellated representation of the edge to be stored.

Parameters
----------
theEdge: TopoDS_Edge
thePolygon: Poly_Polygon3D

Returns
-------
None
") UpdateEdge;
		static void UpdateEdge(const TopoDS_Edge & theEdge, const opencascade::handle<Poly_Polygon3D> & thePolygon);

		/****************** UpdateEdge ******************/
		%feature("compactdefaultargs") UpdateEdge;
		%feature("autodoc", "Updates the given seam edge by the given tessellated representations. @param theedge edge to be updated. @param thepolygon1 tessellated representation corresponding to forward direction of the seam edge. @param thepolygon2 tessellated representation corresponding to reversed direction of the seam edge. @param thetriangulation triangulation the given edge is associated to. @param thelocation face location.

Parameters
----------
theEdge: TopoDS_Edge
thePolygon1: Handle ( Poly_PolygonOnTriangulation )
thePolygon2: Handle ( Poly_PolygonOnTriangulation )
theTriangulation: Handle ( Poly_Triangulation )
theLocation: TopLoc_Location

Returns
-------
None
") UpdateEdge;
		static void UpdateEdge(const TopoDS_Edge & theEdge, const Handle ( Poly_PolygonOnTriangulation ) & thePolygon1, const Handle ( Poly_PolygonOnTriangulation ) & thePolygon2, const Handle ( Poly_Triangulation ) & theTriangulation, const TopLoc_Location & theLocation);

		/****************** UseLocation ******************/
		%feature("compactdefaultargs") UseLocation;
		%feature("autodoc", "Applies location to the given point and return result. @param thepnt point to be transformed. @param theloc location to be applied.

Parameters
----------
thePnt: gp_Pnt
theLoc: TopLoc_Location

Returns
-------
gp_Pnt
") UseLocation;
		static gp_Pnt UseLocation(const gp_Pnt & thePnt, const TopLoc_Location & theLoc);

};


%make_alias(BRepMesh_ShapeTool)

%extend BRepMesh_ShapeTool {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/******************************
* class BRepMesh_ShapeVisitor *
******************************/
class BRepMesh_ShapeVisitor : public IMeshTools_ShapeVisitor {
	public:
		/****************** BRepMesh_ShapeVisitor ******************/
		%feature("compactdefaultargs") BRepMesh_ShapeVisitor;
		%feature("autodoc", "Constructor.

Parameters
----------
theModel: Handle ( IMeshData_Model )

Returns
-------
None
") BRepMesh_ShapeVisitor;
		 BRepMesh_ShapeVisitor(const Handle ( IMeshData_Model ) & theModel);

		/****************** Visit ******************/
		%feature("compactdefaultargs") Visit;
		%feature("autodoc", "Handles topods_face object.

Parameters
----------
theFace: TopoDS_Face

Returns
-------
None
") Visit;
		virtual void Visit(const TopoDS_Face & theFace);

		/****************** Visit ******************/
		%feature("compactdefaultargs") Visit;
		%feature("autodoc", "Handles topods_edge object.

Parameters
----------
theEdge: TopoDS_Edge

Returns
-------
None
") Visit;
		virtual void Visit(const TopoDS_Edge & theEdge);

};


%extend BRepMesh_ShapeVisitor {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**************************
* class BRepMesh_Triangle *
**************************/
class BRepMesh_Triangle {
	public:
		int myEdges[3];
		bool myOrientations[3];
		BRepMesh_DegreeOfFreedom myMovability;
		/****************** BRepMesh_Triangle ******************/
		%feature("compactdefaultargs") BRepMesh_Triangle;
		%feature("autodoc", "Default constructor.

Returns
-------
None
") BRepMesh_Triangle;
		 BRepMesh_Triangle();

		/****************** BRepMesh_Triangle ******************/
		%feature("compactdefaultargs") BRepMesh_Triangle;
		%feature("autodoc", "Constructor. @param theedges array of edges of triangle. @param theorientations array of edge's orientations. @param themovability movability of triangle.

Parameters
----------
): int (  theEdges
): bool (  theOrientations
theMovability: BRepMesh_DegreeOfFreedom

Returns
-------
None
") BRepMesh_Triangle;
		 BRepMesh_Triangle(const Standard_Integer ( & theEdges )[3], const Standard_Boolean ( & theOrientations )[3], const BRepMesh_DegreeOfFreedom theMovability);

		/****************** Edges ******************/
		%feature("compactdefaultargs") Edges;
		%feature("autodoc", "Gets edges with orientations composing the triangle. @param[out] theedges array edges are stored to. @param[out] theorientations array orientations are stored to.

Parameters
----------
): int (  theEdges
): bool (  theOrientations

Returns
-------
None
") Edges;
		void Edges(Standard_Integer ( & theEdges )[3], Standard_Boolean ( & theOrientations )[3]);

		/****************** HashCode ******************/
		%feature("compactdefaultargs") HashCode;
		%feature("autodoc", "Computes a hash code for this triangle, in the range [1, theupperbound] @param theupperbound the upper bound of the range a computing hash code must be within returns a computed hash code, in the range [1, theupperbound].

Parameters
----------
theUpperBound: int

Returns
-------
int
") HashCode;
		Standard_Integer HashCode(const Standard_Integer theUpperBound);

        %extend {
            Standard_Integer __hash__() {
            return $self->HashCode(2147483647);
            }
        };

		/****************** Initialize ******************/
		%feature("compactdefaultargs") Initialize;
		%feature("autodoc", "Initializes the triangle by the given parameters. @param theedges array of edges of triangle. @param theorientations array of edge's orientations. @param themovability movability of triangle.

Parameters
----------
): int (  theEdges
): bool (  theOrientations
theMovability: BRepMesh_DegreeOfFreedom

Returns
-------
None
") Initialize;
		void Initialize(const Standard_Integer ( & theEdges )[3], const Standard_Boolean ( & theOrientations )[3], const BRepMesh_DegreeOfFreedom theMovability);

		/****************** IsEqual ******************/
		%feature("compactdefaultargs") IsEqual;
		%feature("autodoc", "Checks for equality with another triangle. @param theother triangle to be checked against this one. returns true if equal, false if not.

Parameters
----------
theOther: BRepMesh_Triangle

Returns
-------
bool
") IsEqual;
		Standard_Boolean IsEqual(const BRepMesh_Triangle & theOther);

		/****************** Movability ******************/
		%feature("compactdefaultargs") Movability;
		%feature("autodoc", "Returns movability of the triangle.

Returns
-------
BRepMesh_DegreeOfFreedom
") Movability;
		BRepMesh_DegreeOfFreedom Movability();

		/****************** SetMovability ******************/
		%feature("compactdefaultargs") SetMovability;
		%feature("autodoc", "Sets movability of the triangle.

Parameters
----------
theMovability: BRepMesh_DegreeOfFreedom

Returns
-------
None
") SetMovability;
		void SetMovability(const BRepMesh_DegreeOfFreedom theMovability);


            %extend{
                bool __eq_wrapper__(const BRepMesh_Triangle other) {
                if (*self==other) return true;
                else return false;
                }
            }
            %pythoncode {
            def __eq__(self, right):
                try:
                    return self.__eq_wrapper__(right)
                except:
                    return False
            }
};


%extend BRepMesh_Triangle {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/************************
* class BRepMesh_Vertex *
************************/
class BRepMesh_Vertex {
	public:
		/****************** BRepMesh_Vertex ******************/
		%feature("compactdefaultargs") BRepMesh_Vertex;
		%feature("autodoc", "Default constructor.

Returns
-------
None
") BRepMesh_Vertex;
		 BRepMesh_Vertex();

		/****************** BRepMesh_Vertex ******************/
		%feature("compactdefaultargs") BRepMesh_Vertex;
		%feature("autodoc", "Creates vertex associated with point in 3d space. @param theuv position of vertex in parametric space. @param thelocation3d index of 3d point to be associated with vertex. @param themovability movability of the vertex.

Parameters
----------
theUV: gp_XY
theLocation3d: int
theMovability: BRepMesh_DegreeOfFreedom

Returns
-------
None
") BRepMesh_Vertex;
		 BRepMesh_Vertex(const gp_XY & theUV, const Standard_Integer theLocation3d, const BRepMesh_DegreeOfFreedom theMovability);

		/****************** BRepMesh_Vertex ******************/
		%feature("compactdefaultargs") BRepMesh_Vertex;
		%feature("autodoc", "Creates vertex without association with point in 3d space. @param theu u position of vertex in parametric space. @param thev v position of vertex in parametric space. @param themovability movability of the vertex.

Parameters
----------
theU: float
theV: float
theMovability: BRepMesh_DegreeOfFreedom

Returns
-------
None
") BRepMesh_Vertex;
		 BRepMesh_Vertex(const Standard_Real theU, const Standard_Real theV, const BRepMesh_DegreeOfFreedom theMovability);

		/****************** ChangeCoord ******************/
		%feature("compactdefaultargs") ChangeCoord;
		%feature("autodoc", "Returns position of the vertex in parametric space for modification.

Returns
-------
gp_XY
") ChangeCoord;
		gp_XY ChangeCoord();

		/****************** Coord ******************/
		%feature("compactdefaultargs") Coord;
		%feature("autodoc", "Returns position of the vertex in parametric space.

Returns
-------
gp_XY
") Coord;
		const gp_XY Coord();

		/****************** HashCode ******************/
		%feature("compactdefaultargs") HashCode;
		%feature("autodoc", "Computes a hash code for this vertex, in the range [1, theupperbound] @param theupperbound the upper bound of the range a computing hash code must be within returns a computed hash code, in the range [1, theupperbound].

Parameters
----------
theUpperBound: int

Returns
-------
int
") HashCode;
		Standard_Integer HashCode(const Standard_Integer theUpperBound);

        %extend {
            Standard_Integer __hash__() {
            return $self->HashCode(2147483647);
            }
        };

		/****************** Initialize ******************/
		%feature("compactdefaultargs") Initialize;
		%feature("autodoc", "Initializes vertex associated with point in 3d space. @param theuv position of vertex in parametric space. @param thelocation3d index of 3d point to be associated with vertex. @param themovability movability of the vertex.

Parameters
----------
theUV: gp_XY
theLocation3d: int
theMovability: BRepMesh_DegreeOfFreedom

Returns
-------
None
") Initialize;
		void Initialize(const gp_XY & theUV, const Standard_Integer theLocation3d, const BRepMesh_DegreeOfFreedom theMovability);

		/****************** IsEqual ******************/
		%feature("compactdefaultargs") IsEqual;
		%feature("autodoc", "Checks for equality with another vertex. @param theother vertex to be checked against this one. returns true if equal, false if not.

Parameters
----------
theOther: BRepMesh_Vertex

Returns
-------
bool
") IsEqual;
		Standard_Boolean IsEqual(const BRepMesh_Vertex & theOther);

		/****************** Location3d ******************/
		%feature("compactdefaultargs") Location3d;
		%feature("autodoc", "Returns index of 3d point associated with the vertex.

Returns
-------
int
") Location3d;
		Standard_Integer Location3d();

		/****************** Movability ******************/
		%feature("compactdefaultargs") Movability;
		%feature("autodoc", "Returns movability of the vertex.

Returns
-------
BRepMesh_DegreeOfFreedom
") Movability;
		BRepMesh_DegreeOfFreedom Movability();

		/****************** SetMovability ******************/
		%feature("compactdefaultargs") SetMovability;
		%feature("autodoc", "Sets movability of the vertex.

Parameters
----------
theMovability: BRepMesh_DegreeOfFreedom

Returns
-------
None
") SetMovability;
		void SetMovability(const BRepMesh_DegreeOfFreedom theMovability);


            %extend{
                bool __eq_wrapper__(const BRepMesh_Vertex other) {
                if (*self==other) return true;
                else return false;
                }
            }
            %pythoncode {
            def __eq__(self, right):
                try:
                    return self.__eq_wrapper__(right)
                except:
                    return False
            }
};


%extend BRepMesh_Vertex {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*********************************
* class BRepMesh_VertexInspector *
*********************************/
class BRepMesh_VertexInspector : public NCollection_CellFilter_InspectorXY {
	public:
typedef Standard_Integer Target;
		/****************** BRepMesh_VertexInspector ******************/
		%feature("compactdefaultargs") BRepMesh_VertexInspector;
		%feature("autodoc", "Constructor. @param theallocator memory allocator to be used by internal collections.

Parameters
----------
theAllocator: NCollection_IncAllocator

Returns
-------
None
") BRepMesh_VertexInspector;
		 BRepMesh_VertexInspector(const opencascade::handle<NCollection_IncAllocator> & theAllocator);

		/****************** Add ******************/
		%feature("compactdefaultargs") Add;
		%feature("autodoc", "Registers the given vertex. @param thevertex vertex to be registered.

Parameters
----------
theVertex: BRepMesh_Vertex

Returns
-------
int
") Add;
		Standard_Integer Add(const BRepMesh_Vertex & theVertex);

		/****************** Clear ******************/
		%feature("compactdefaultargs") Clear;
		%feature("autodoc", "Clear inspector's internal data structures.

Returns
-------
None
") Clear;
		void Clear();

		/****************** Delete ******************/
		%feature("compactdefaultargs") Delete;
		%feature("autodoc", "Deletes vertex with the given index. @param theindex index of vertex to be removed.

Parameters
----------
theIndex: int

Returns
-------
None
") Delete;
		void Delete(const Standard_Integer theIndex);

		/****************** GetCoincidentPoint ******************/
		%feature("compactdefaultargs") GetCoincidentPoint;
		%feature("autodoc", "Returns index of point coinciding with regerence one.

Returns
-------
int
") GetCoincidentPoint;
		Standard_Integer GetCoincidentPoint();

		/****************** GetListOfDelPoints ******************/
		%feature("compactdefaultargs") GetListOfDelPoints;
		%feature("autodoc", "Returns list with indexes of vertices that have movability attribute equal to brepmesh_deleted and can be replaced with another node.

Returns
-------
IMeshData::ListOfInteger
") GetListOfDelPoints;
		const IMeshData::ListOfInteger & GetListOfDelPoints();

		/****************** GetVertex ******************/
		%feature("compactdefaultargs") GetVertex;
		%feature("autodoc", "Returns vertex with the given index.

Parameters
----------
theIndex: int

Returns
-------
BRepMesh_Vertex
") GetVertex;
		BRepMesh_Vertex & GetVertex(Standard_Integer theIndex);

		/****************** Inspect ******************/
		%feature("compactdefaultargs") Inspect;
		%feature("autodoc", "Performs inspection of a point with the given index. @param thetargetindex index of a circle to be checked. returns status of the check.

Parameters
----------
theTargetIndex: int

Returns
-------
NCollection_CellFilter_Action
") Inspect;
		NCollection_CellFilter_Action Inspect(const Standard_Integer theTargetIndex);

		/****************** IsEqual ******************/
		%feature("compactdefaultargs") IsEqual;
		%feature("autodoc", "Checks indices for equlity.

Parameters
----------
theIndex: int
theTargetIndex: int

Returns
-------
bool
") IsEqual;
		static Standard_Boolean IsEqual(const Standard_Integer theIndex, const Standard_Integer theTargetIndex);

		/****************** NbVertices ******************/
		%feature("compactdefaultargs") NbVertices;
		%feature("autodoc", "Returns number of registered vertices.

Returns
-------
int
") NbVertices;
		Standard_Integer NbVertices();

		/****************** SetPoint ******************/
		%feature("compactdefaultargs") SetPoint;
		%feature("autodoc", "Set reference point to be checked.

Parameters
----------
thePoint: gp_XY

Returns
-------
None
") SetPoint;
		void SetPoint(const gp_XY & thePoint);

		/****************** SetTolerance ******************/
		%feature("compactdefaultargs") SetTolerance;
		%feature("autodoc", "Sets the tolerance to be used for identification of coincident vertices equal for both dimensions.

Parameters
----------
theTolerance: float

Returns
-------
None
") SetTolerance;
		void SetTolerance(const Standard_Real theTolerance);

		/****************** SetTolerance ******************/
		%feature("compactdefaultargs") SetTolerance;
		%feature("autodoc", "Sets the tolerance to be used for identification of coincident vertices. @param thetolerancex tolerance for x dimension. @param thetolerancey tolerance for y dimension.

Parameters
----------
theToleranceX: float
theToleranceY: float

Returns
-------
None
") SetTolerance;
		void SetTolerance(const Standard_Real theToleranceX, const Standard_Real theToleranceY);

};


%extend BRepMesh_VertexInspector {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/****************************
* class BRepMesh_VertexTool *
****************************/
class BRepMesh_VertexTool : public Standard_Transient {
	public:
		/****************** BRepMesh_VertexTool ******************/
		%feature("compactdefaultargs") BRepMesh_VertexTool;
		%feature("autodoc", "Constructor. @param theallocator memory allocator to be used by internal collections.

Parameters
----------
theAllocator: NCollection_IncAllocator

Returns
-------
None
") BRepMesh_VertexTool;
		 BRepMesh_VertexTool(const opencascade::handle<NCollection_IncAllocator> & theAllocator);

		/****************** Add ******************/
		%feature("compactdefaultargs") Add;
		%feature("autodoc", "Adds vertex with empty data to the tool. @param thevertex node to be added to the mesh. @param isforceadd adds the given node to structure without checking on coincidence with other nodes. returns index of the node in the structure.

Parameters
----------
theVertex: BRepMesh_Vertex
isForceAdd: bool

Returns
-------
int
") Add;
		Standard_Integer Add(const BRepMesh_Vertex & theVertex, const Standard_Boolean isForceAdd);

		/****************** DeleteVertex ******************/
		%feature("compactdefaultargs") DeleteVertex;
		%feature("autodoc", "Deletes vertex with the given index from the tool.

Parameters
----------
theIndex: int

Returns
-------
None
") DeleteVertex;
		void DeleteVertex(const Standard_Integer theIndex);

		/****************** Extent ******************/
		%feature("compactdefaultargs") Extent;
		%feature("autodoc", "Returns a number of vertices.

Returns
-------
int
") Extent;
		Standard_Integer Extent();

		/****************** FindIndex ******************/
		%feature("compactdefaultargs") FindIndex;
		%feature("autodoc", "Returns index of the given vertex.

Parameters
----------
theVertex: BRepMesh_Vertex

Returns
-------
int
") FindIndex;
		Standard_Integer FindIndex(const BRepMesh_Vertex & theVertex);

		/****************** FindKey ******************/
		%feature("compactdefaultargs") FindKey;
		%feature("autodoc", "Returns vertex by the given index.

Parameters
----------
theIndex: int

Returns
-------
BRepMesh_Vertex
") FindKey;
		const BRepMesh_Vertex & FindKey(const Standard_Integer theIndex);

		/****************** GetListOfDelNodes ******************/
		%feature("compactdefaultargs") GetListOfDelNodes;
		%feature("autodoc", "Returns the list with indexes of vertices that have movability attribute equal to brepmesh_deleted and can be replaced with another node.

Returns
-------
IMeshData::ListOfInteger
") GetListOfDelNodes;
		const IMeshData::ListOfInteger & GetListOfDelNodes();

		/****************** GetTolerance ******************/
		%feature("compactdefaultargs") GetTolerance;
		%feature("autodoc", "Gets the tolerance to be used for identification of coincident vertices. @param thetolerancex tolerance for x dimension. @param thetolerancey tolerance for y dimension.

Parameters
----------

Returns
-------
theToleranceX: float
theToleranceY: float
") GetTolerance;
		void GetTolerance(Standard_Real &OutValue, Standard_Real &OutValue);

		/****************** IsEmpty ******************/
		%feature("compactdefaultargs") IsEmpty;
		%feature("autodoc", "Returns true when the map contains no keys. .

Returns
-------
bool
") IsEmpty;
		Standard_Boolean IsEmpty();

		/****************** RemoveLast ******************/
		%feature("compactdefaultargs") RemoveLast;
		%feature("autodoc", "Remove last node from the structure.

Returns
-------
None
") RemoveLast;
		void RemoveLast();

		/****************** SetCellSize ******************/
		%feature("compactdefaultargs") SetCellSize;
		%feature("autodoc", "Sets new size of cell for cellfilter equal in both directions.

Parameters
----------
theSize: float

Returns
-------
None
") SetCellSize;
		void SetCellSize(const Standard_Real theSize);

		/****************** SetCellSize ******************/
		%feature("compactdefaultargs") SetCellSize;
		%feature("autodoc", "Sets new size of cell for cellfilter. @param thesizex size for x dimension. @param thesizey size for y dimension.

Parameters
----------
theSizeX: float
theSizeY: float

Returns
-------
None
") SetCellSize;
		void SetCellSize(const Standard_Real theSizeX, const Standard_Real theSizeY);

		/****************** SetTolerance ******************/
		%feature("compactdefaultargs") SetTolerance;
		%feature("autodoc", "Sets the tolerance to be used for identification of coincident vertices equal for both dimensions.

Parameters
----------
theTolerance: float

Returns
-------
None
") SetTolerance;
		void SetTolerance(const Standard_Real theTolerance);

		/****************** SetTolerance ******************/
		%feature("compactdefaultargs") SetTolerance;
		%feature("autodoc", "Sets the tolerance to be used for identification of coincident vertices. @param thetolerancex tolerance for x dimension. @param thetolerancey tolerance for y dimension.

Parameters
----------
theToleranceX: float
theToleranceY: float

Returns
-------
None
") SetTolerance;
		void SetTolerance(const Standard_Real theToleranceX, const Standard_Real theToleranceY);


        %feature("autodoc", "1");
        %extend{
            std::string StatisticsToString() {
            std::stringstream s;
            self->Statistics(s);
            return s.str();}
        };
		/****************** Substitute ******************/
		%feature("compactdefaultargs") Substitute;
		%feature("autodoc", "Substitutes vertex with the given by the given vertex with attributes. @param theindex index of vertex to be substituted. @param thevertex replacement vertex.

Parameters
----------
theIndex: int
theVertex: BRepMesh_Vertex

Returns
-------
None
") Substitute;
		void Substitute(const Standard_Integer theIndex, const BRepMesh_Vertex & theVertex);

};


%make_alias(BRepMesh_VertexTool)

%extend BRepMesh_VertexTool {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*****************************************
* class BRepMesh_ConstrainedBaseMeshAlgo *
*****************************************/
/***************************************************
* class BRepMesh_DelaunayDeflectionControlMeshAlgo *
***************************************************/
/***********************************************
* class BRepMesh_DelaunayNodeInsertionMeshAlgo *
***********************************************/
/**********************
* class BRepMesh_Edge *
**********************/
class BRepMesh_Edge : public BRepMesh_OrientedEdge {
	public:
		/****************** BRepMesh_Edge ******************/
		%feature("compactdefaultargs") BRepMesh_Edge;
		%feature("autodoc", "Default constructor.

Returns
-------
None
") BRepMesh_Edge;
		 BRepMesh_Edge();

		/****************** BRepMesh_Edge ******************/
		%feature("compactdefaultargs") BRepMesh_Edge;
		%feature("autodoc", "Constructs a link between two vertices.

Parameters
----------
theFirstNode: int
theLastNode: int
theMovability: BRepMesh_DegreeOfFreedom

Returns
-------
None
") BRepMesh_Edge;
		 BRepMesh_Edge(const Standard_Integer theFirstNode, const Standard_Integer theLastNode, const BRepMesh_DegreeOfFreedom theMovability);

		/****************** IsEqual ******************/
		%feature("compactdefaultargs") IsEqual;
		%feature("autodoc", "Checks for equality with another edge. @param theother edge to be checked against this one. returns true if equal, false if not.

Parameters
----------
theOther: BRepMesh_Edge

Returns
-------
bool
") IsEqual;
		Standard_Boolean IsEqual(const BRepMesh_Edge & theOther);

		/****************** IsSameOrientation ******************/
		%feature("compactdefaultargs") IsSameOrientation;
		%feature("autodoc", "Checks if the given edge and this one have the same orientation. @param theother edge to be checked against this one. etrun true if edges have the same orientation, false if not.

Parameters
----------
theOther: BRepMesh_Edge

Returns
-------
bool
") IsSameOrientation;
		Standard_Boolean IsSameOrientation(const BRepMesh_Edge & theOther);

		/****************** Movability ******************/
		%feature("compactdefaultargs") Movability;
		%feature("autodoc", "Returns movability flag of the link.

Returns
-------
BRepMesh_DegreeOfFreedom
") Movability;
		BRepMesh_DegreeOfFreedom Movability();

		/****************** SetMovability ******************/
		%feature("compactdefaultargs") SetMovability;
		%feature("autodoc", "Sets movability flag of the link. @param themovability flag to be set.

Parameters
----------
theMovability: BRepMesh_DegreeOfFreedom

Returns
-------
None
") SetMovability;
		void SetMovability(const BRepMesh_DegreeOfFreedom theMovability);


            %extend{
                bool __eq_wrapper__(const BRepMesh_Edge other) {
                if (*self==other) return true;
                else return false;
                }
            }
            %pythoncode {
            def __eq__(self, right):
                try:
                    return self.__eq_wrapper__(right)
                except:
                    return False
            }
};


%extend BRepMesh_Edge {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*********************************
* class BRepMesh_IncrementalMesh *
*********************************/
class BRepMesh_IncrementalMesh : public BRepMesh_DiscretRoot {
	public:
		/****************** BRepMesh_IncrementalMesh ******************/
		%feature("compactdefaultargs") BRepMesh_IncrementalMesh;
		%feature("autodoc", "Default constructor.

Returns
-------
None
") BRepMesh_IncrementalMesh;
		 BRepMesh_IncrementalMesh();

		/****************** BRepMesh_IncrementalMesh ******************/
		%feature("compactdefaultargs") BRepMesh_IncrementalMesh;
		%feature("autodoc", "Constructor. automatically calls method perform. @param theshape shape to be meshed. @param thelindeflection linear deflection. @param isrelative if true deflection used for discretization of each edge will be <thelindeflection> * <size of edge>. deflection used for the faces will be the maximum deflection of their edges. @param theangdeflection angular deflection. @param isinparallel if true shape will be meshed in parallel.

Parameters
----------
theShape: TopoDS_Shape
theLinDeflection: float
isRelative: bool,optional
	default value is Standard_False
theAngDeflection: float,optional
	default value is 0.5
isInParallel: bool,optional
	default value is Standard_False

Returns
-------
None
") BRepMesh_IncrementalMesh;
		 BRepMesh_IncrementalMesh(const TopoDS_Shape & theShape, const Standard_Real theLinDeflection, const Standard_Boolean isRelative = Standard_False, const Standard_Real theAngDeflection = 0.5, const Standard_Boolean isInParallel = Standard_False);

		/****************** BRepMesh_IncrementalMesh ******************/
		%feature("compactdefaultargs") BRepMesh_IncrementalMesh;
		%feature("autodoc", "Constructor. automatically calls method perform. @param theshape shape to be meshed. @param theparameters - parameters of meshing.

Parameters
----------
theShape: TopoDS_Shape
theParameters: IMeshTools_Parameters

Returns
-------
None
") BRepMesh_IncrementalMesh;
		 BRepMesh_IncrementalMesh(const TopoDS_Shape & theShape, const IMeshTools_Parameters & theParameters);

		/****************** ChangeParameters ******************/
		%feature("compactdefaultargs") ChangeParameters;
		%feature("autodoc", "Returns modifiable meshing parameters.

Returns
-------
IMeshTools_Parameters
") ChangeParameters;
		IMeshTools_Parameters & ChangeParameters();

		/****************** Discret ******************/
		%feature("compactdefaultargs") Discret;
		%feature("autodoc", "Plugin interface for the mesh factories. initializes meshing algorithm with the given parameters. @param theshape shape to be meshed. @param thelindeflection linear deflection. @param theangdeflection angular deflection. @param[out] thealgo pointer to initialized algorithm.

Parameters
----------
theShape: TopoDS_Shape
theLinDeflection: float
theAngDeflection: float
theAlgo: BRepMesh_DiscretRoot *

Returns
-------
int
") Discret;
		static Standard_Integer Discret(const TopoDS_Shape & theShape, const Standard_Real theLinDeflection, const Standard_Real theAngDeflection, BRepMesh_DiscretRoot * & theAlgo);

		/****************** GetStatusFlags ******************/
		%feature("compactdefaultargs") GetStatusFlags;
		%feature("autodoc", "Returns accumulated status flags faced during meshing.

Returns
-------
int
") GetStatusFlags;
		Standard_Integer GetStatusFlags();

		/****************** IsModified ******************/
		%feature("compactdefaultargs") IsModified;
		%feature("autodoc", "Returns modified flag.

Returns
-------
bool
") IsModified;
		Standard_Boolean IsModified();

		/****************** IsParallelDefault ******************/
		%feature("compactdefaultargs") IsParallelDefault;
		%feature("autodoc", "Returns multi-threading usage flag set by default in discret() static method (thus applied only to mesh factories).

Returns
-------
bool
") IsParallelDefault;
		static Standard_Boolean IsParallelDefault();

		/****************** Parameters ******************/
		%feature("compactdefaultargs") Parameters;
		%feature("autodoc", "Returns meshing parameters.

Returns
-------
IMeshTools_Parameters
") Parameters;
		const IMeshTools_Parameters & Parameters();

		/****************** Perform ******************/
		%feature("compactdefaultargs") Perform;
		%feature("autodoc", "Performs meshing ot the shape.

Returns
-------
None
") Perform;
		virtual void Perform();

		/****************** Perform ******************/
		%feature("compactdefaultargs") Perform;
		%feature("autodoc", "Performs meshing using custom context;.

Parameters
----------
theContext: IMeshTools_Context

Returns
-------
None
") Perform;
		void Perform(const opencascade::handle<IMeshTools_Context> & theContext);

		/****************** SetParallelDefault ******************/
		%feature("compactdefaultargs") SetParallelDefault;
		%feature("autodoc", "Setup multi-threading usage flag set by default in discret() static method (thus applied only to mesh factories).

Parameters
----------
isInParallel: bool

Returns
-------
None
") SetParallelDefault;
		static void SetParallelDefault(const Standard_Boolean isInParallel);

};


%make_alias(BRepMesh_IncrementalMesh)

%extend BRepMesh_IncrementalMesh {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**************************************
* class BRepMesh_DelaunayBaseMeshAlgo *
**************************************/
class BRepMesh_DelaunayBaseMeshAlgo : public BRepMesh_ConstrainedBaseMeshAlgo {
	public:
		/****************** BRepMesh_DelaunayBaseMeshAlgo ******************/
		%feature("compactdefaultargs") BRepMesh_DelaunayBaseMeshAlgo;
		%feature("autodoc", "Constructor.

Returns
-------
None
") BRepMesh_DelaunayBaseMeshAlgo;
		 BRepMesh_DelaunayBaseMeshAlgo();

};


%extend BRepMesh_DelaunayBaseMeshAlgo {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/* python proxy for excluded classes */
%pythoncode {
@classnotwrapped
class BRepMesh_WireInterferenceChecker:
	pass

@classnotwrapped
class BRepMesh_EdgeTessellator:
	pass

@classnotwrapped
class BRepMesh_EdgeTessellationExtractor:
	pass

@classnotwrapped
class BRepMesh_EdgeParameterProvider:
	pass

@classnotwrapped
class BRepMesh_FastDiscret:
	pass

@classnotwrapped
class BRepMesh_CustomDelaunayBaseMeshAlgo:
	pass

@classnotwrapped
class BRepMesh_NodeInsertionMeshAlgo:
	pass

@classnotwrapped
class BRepMesh_ConstrainedBaseMeshAlgo:
	pass

@classnotwrapped
class BRepMesh_CustomBaseMeshAlgo:
	pass

@classnotwrapped
class BRepMesh_DelaunayDeflectionControlMeshAlgo:
	pass

@classnotwrapped
class BRepMesh_DelaunayNodeInsertionMeshAlgo:
	pass

}
/* end python proxy for excluded classes */
/* harray1 classes */
/* harray2 classes */
/* hsequence classes */
