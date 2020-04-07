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
%define CONVERTDOCSTRING
"Convert module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_convert.html"
%enddef
%module (package="OCC.Core", docstring=CONVERTDOCSTRING) Convert


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
#include<Convert_module.hxx>

//Dependencies
#include<Standard_module.hxx>
#include<NCollection_module.hxx>
#include<TColgp_module.hxx>
#include<TColStd_module.hxx>
#include<gp_module.hxx>
#include<TColgp_module.hxx>
#include<TColStd_module.hxx>
#include<TCollection_module.hxx>
#include<Storage_module.hxx>
%};
%import Standard.i
%import NCollection.i
%import TColgp.i
%import TColStd.i
%import gp.i

%pythoncode {
from enum import IntEnum
from OCC.Core.Exception import *
};

/* public enums */
enum Convert_ParameterisationType {
	Convert_TgtThetaOver2 = 0,
	Convert_TgtThetaOver2_1 = 1,
	Convert_TgtThetaOver2_2 = 2,
	Convert_TgtThetaOver2_3 = 3,
	Convert_TgtThetaOver2_4 = 4,
	Convert_QuasiAngular = 5,
	Convert_RationalC1 = 6,
	Convert_Polynomial = 7,
};

/* end public enums declaration */

/* python proy classes for enums */
%pythoncode {

class Convert_ParameterisationType(IntEnum):
	Convert_TgtThetaOver2 = 0
	Convert_TgtThetaOver2_1 = 1
	Convert_TgtThetaOver2_2 = 2
	Convert_TgtThetaOver2_3 = 3
	Convert_TgtThetaOver2_4 = 4
	Convert_QuasiAngular = 5
	Convert_RationalC1 = 6
	Convert_Polynomial = 7
Convert_TgtThetaOver2 = Convert_ParameterisationType.Convert_TgtThetaOver2
Convert_TgtThetaOver2_1 = Convert_ParameterisationType.Convert_TgtThetaOver2_1
Convert_TgtThetaOver2_2 = Convert_ParameterisationType.Convert_TgtThetaOver2_2
Convert_TgtThetaOver2_3 = Convert_ParameterisationType.Convert_TgtThetaOver2_3
Convert_TgtThetaOver2_4 = Convert_ParameterisationType.Convert_TgtThetaOver2_4
Convert_QuasiAngular = Convert_ParameterisationType.Convert_QuasiAngular
Convert_RationalC1 = Convert_ParameterisationType.Convert_RationalC1
Convert_Polynomial = Convert_ParameterisationType.Convert_Polynomial
};
/* end python proxy for enums */

/* handles */
/* end handles declaration */

/* templates */
%template(Convert_SequenceOfArray1OfPoles) NCollection_Sequence<opencascade::handle<TColgp_HArray1OfPnt>>;
/* end templates declaration */

/* typedefs */
typedef void Convert_CosAndSinEvalFunction ( Standard_Real, const Standard_Integer, const TColgp_Array1OfPnt2d &, const TColStd_Array1OfReal &, const TColStd_Array1OfInteger *, Standard_Real Result [ 2 ] );
typedef NCollection_Sequence<opencascade::handle<TColgp_HArray1OfPnt>> Convert_SequenceOfArray1OfPoles;
typedef TColgp_SequenceOfArray1OfPnt2d Convert_SequenceOfArray1OfPoles2d;
/* end typedefs declaration */

/***************************************************
* class Convert_CompBezierCurves2dToBSplineCurve2d *
***************************************************/
class Convert_CompBezierCurves2dToBSplineCurve2d {
	public:
		/****************** Convert_CompBezierCurves2dToBSplineCurve2d ******************/
		%feature("compactdefaultargs") Convert_CompBezierCurves2dToBSplineCurve2d;
		%feature("autodoc", "Constructs a framework for converting a sequence of adjacent non-rational bezier curves into a bspline curve. knots will be created on the computed bspline curve at each junction point of two consecutive bezier curves. the degree of continuity of the bspline curve will be increased at the junction point of two consecutive bezier curves if their tangent vectors at this point are parallel. angulartolerance (given in radians, and defaulted to 1.0 e-4) will be used to check the parallelism of the two tangent vectors. use the following functions: - addcurve to define in sequence the adjacent bezier curves to be converted, - perform to compute the data needed to build the bspline curve, - and the available consultation functions to access the computed data. this data may be used to construct the bspline curve.

Parameters
----------
AngularTolerance: float,optional
	default value is 1.0e-4

Returns
-------
None
") Convert_CompBezierCurves2dToBSplineCurve2d;
		 Convert_CompBezierCurves2dToBSplineCurve2d(const Standard_Real AngularTolerance = 1.0e-4);

		/****************** AddCurve ******************/
		%feature("compactdefaultargs") AddCurve;
		%feature("autodoc", "Adds the bezier curve defined by the table of poles poles, to the sequence (still contained in this framework) of adjacent bezier curves to be converted into a bspline curve. only polynomial (i.e. non-rational) bezier curves are converted using this framework. if this is not the first call to the function (i.e. if this framework still contains data in its sequence of bezier curves), the degree of continuity of the bspline curve will be increased at the time of computation at the first point of the added bezier curve (i.e. the first point of the poles table). this will be the case if the tangent vector of the curve at this point is parallel to the tangent vector at the end point of the preceding bezier curve in the sequence of bezier curves still contained in this framework. an angular tolerance given at the time of construction of this framework, will be used to check the parallelism of the two tangent vectors. this checking procedure, and all the relative computations will be performed by the function perform. when the sequence of adjacent bezier curves is complete, use the following functions: - perform to compute the data needed to build the bspline curve, - and the available consultation functions to access the computed data. this data may be used to construct the bspline curve. warning the sequence of bezier curves treated by this framework is automatically initialized with the first bezier curve when the function is first called. during subsequent use of this function, ensure that the first point of the added bezier curve (i.e. the first point of the poles table) is coincident with the last point of the sequence (i.e. the last point of the preceding bezier curve in the sequence) of bezier curves still contained in this framework. an error may occur at the time of computation if this condition is not satisfied. particular care must be taken with respect to the above, as this condition is not checked either when defining the sequence of bezier curves or at the time of computation.

Parameters
----------
Poles: TColgp_Array1OfPnt2d

Returns
-------
None
") AddCurve;
		void AddCurve(const TColgp_Array1OfPnt2d & Poles);

		/****************** Degree ******************/
		%feature("compactdefaultargs") Degree;
		%feature("autodoc", "Returns the degree of the bspline curve whose data is computed in this framework. warning take particular care not to use this function before the computation is performed (perform function), as this condition is not checked and an error may therefore occur.

Returns
-------
int
") Degree;
		Standard_Integer Degree();

		/****************** KnotsAndMults ******************/
		%feature("compactdefaultargs") KnotsAndMults;
		%feature("autodoc", "Loads the knots table with the knots and the mults table with the corresponding multiplicities of the bspline curve whose data is computed in this framework. warning - do not use this function before the computation is performed (perform function). - the length of the knots and mults arrays must be equal to the number of knots in the bspline curve whose data is computed in this framework. particular care must be taken with respect to the above as these conditions are not checked, and an error may occur.

Parameters
----------
Knots: TColStd_Array1OfReal
Mults: TColStd_Array1OfInteger

Returns
-------
None
") KnotsAndMults;
		void KnotsAndMults(TColStd_Array1OfReal & Knots, TColStd_Array1OfInteger & Mults);

		/****************** NbKnots ******************/
		%feature("compactdefaultargs") NbKnots;
		%feature("autodoc", "Returns the number of knots of the bspline curve whose data is computed in this framework. warning take particular care not to use this function before the computation is performed (perform function), as this condition is not checked and an error may therefore occur.

Returns
-------
int
") NbKnots;
		Standard_Integer NbKnots();

		/****************** NbPoles ******************/
		%feature("compactdefaultargs") NbPoles;
		%feature("autodoc", "Returns the number of poles of the bspline curve whose data is computed in this framework. warning take particular care not to use this function before the computation is performed (perform function), as this condition is not checked and an error may therefore occur.

Returns
-------
int
") NbPoles;
		Standard_Integer NbPoles();

		/****************** Perform ******************/
		%feature("compactdefaultargs") Perform;
		%feature("autodoc", "Computes all the data needed to build a bspline curve equivalent to the sequence of adjacent bezier curves still contained in this framework. a knot is inserted on the computed bspline curve at the junction point of two consecutive bezier curves. the degree of continuity of the bspline curve will be increased at the junction point of two consecutive bezier curves if their tangent vectors at this point are parallel. an angular tolerance given at the time of construction of this framework is used to check the parallelism of the two tangent vectors. use the available consultation functions to access the computed data. this data may then be used to construct the bspline curve. warning ensure that the curves in the sequence of bezier curves contained in this framework are adjacent. an error may occur at the time of computation if this condition is not satisfied. particular care must be taken with respect to the above as this condition is not checked, either when defining the bezier curve sequence or at the time of computation.

Returns
-------
None
") Perform;
		void Perform();

		/****************** Poles ******************/
		%feature("compactdefaultargs") Poles;
		%feature("autodoc", "Loads the poles table with the poles of the bspline curve whose data is computed in this framework. warning - do not use this function before the computation is performed (perform function). - the length of the poles array must be equal to the number of poles of the bspline curve whose data is computed in this framework. particular care must be taken with respect to the above, as these conditions are not checked, and an error may occur.

Parameters
----------
Poles: TColgp_Array1OfPnt2d

Returns
-------
None
") Poles;
		void Poles(TColgp_Array1OfPnt2d & Poles);

};


%extend Convert_CompBezierCurves2dToBSplineCurve2d {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***********************************************
* class Convert_CompBezierCurvesToBSplineCurve *
***********************************************/
class Convert_CompBezierCurvesToBSplineCurve {
	public:
		/****************** Convert_CompBezierCurvesToBSplineCurve ******************/
		%feature("compactdefaultargs") Convert_CompBezierCurvesToBSplineCurve;
		%feature("autodoc", "Constructs a framework for converting a sequence of adjacent non-rational bezier curves into a bspline curve. knots will be created on the computed bspline curve at each junction point of two consecutive bezier curves. the degree of continuity of the bspline curve will be increased at the junction point of two consecutive bezier curves if their tangent vectors at this point are parallel. angulartolerance (given in radians, and defaulted to 1.0 e-4) will be used to check the parallelism of the two tangent vectors. use the following functions: - addcurve to define in sequence the adjacent bezier curves to be converted, - perform to compute the data needed to build the bspline curve, - and the available consultation functions to access the computed data. this data may be used to construct the bspline curve.

Parameters
----------
AngularTolerance: float,optional
	default value is 1.0e-4

Returns
-------
None
") Convert_CompBezierCurvesToBSplineCurve;
		 Convert_CompBezierCurvesToBSplineCurve(const Standard_Real AngularTolerance = 1.0e-4);

		/****************** AddCurve ******************/
		%feature("compactdefaultargs") AddCurve;
		%feature("autodoc", "Adds the bezier curve defined by the table of poles poles, to the sequence (still contained in this framework) of adjacent bezier curves to be converted into a bspline curve. only polynomial (i.e. non-rational) bezier curves are converted using this framework. if this is not the first call to the function (i.e. if this framework still contains data in its bezier curve sequence), the degree of continuity of the bspline curve will be increased at the time of computation at the first point of the added bezier curve (i.e. the first point of the poles table). this will be the case if the tangent vector of the curve at this point is parallel to the tangent vector at the end point of the preceding bezier curve in the bezier curve sequence still contained in this framework. an angular tolerance given at the time of construction of this framework will be used to check the parallelism of the two tangent vectors. this checking procedure and all related computations will be performed by the perform function. when the adjacent bezier curve sequence is complete, use the following functions: - perform to compute the data needed to build the bspline curve, - and the available consultation functions to access the computed data. this data may be used to construct the bspline curve. warning the bezier curve sequence treated by this framework is automatically initialized with the first bezier curve when the function is first called. during subsequent use of this function, ensure that the first point of the added bezier curve (i.e. the first point of the poles table) is coincident with the last point of the bezier curve sequence (i.e. the last point of the preceding bezier curve in the sequence) still contained in this framework. an error may occur at the time of computation if this condition is not satisfied. particular care must be taken with respect to the above, as this condition is not checked either when defining the bezier curve sequence or at the time of computation.

Parameters
----------
Poles: TColgp_Array1OfPnt

Returns
-------
None
") AddCurve;
		void AddCurve(const TColgp_Array1OfPnt & Poles);

		/****************** Degree ******************/
		%feature("compactdefaultargs") Degree;
		%feature("autodoc", "Returns the degree of the bspline curve whose data is computed in this framework. warning take particular care not to use this function before the computation is performed (perform function), as this condition is not checked and an error may therefore occur.

Returns
-------
int
") Degree;
		Standard_Integer Degree();

		/****************** KnotsAndMults ******************/
		%feature("compactdefaultargs") KnotsAndMults;
		%feature("autodoc", "- loads the knots table with the knots, - and loads the mults table with the corresponding multiplicities of the bspline curve whose data is computed in this framework. warning - do not use this function before the computation is performed (perform function). - the length of the knots and mults arrays must be equal to the number of knots in the bspline curve whose data is computed in this framework. particular care must be taken with respect to the above as these conditions are not checked, and an error may occur.

Parameters
----------
Knots: TColStd_Array1OfReal
Mults: TColStd_Array1OfInteger

Returns
-------
None
") KnotsAndMults;
		void KnotsAndMults(TColStd_Array1OfReal & Knots, TColStd_Array1OfInteger & Mults);

		/****************** NbKnots ******************/
		%feature("compactdefaultargs") NbKnots;
		%feature("autodoc", "Returns the number of knots of the bspline curve whose data is computed in this framework. warning take particular care not to use this function before the computation is performed (perform function), as this condition is not checked and an error may therefore occur.

Returns
-------
int
") NbKnots;
		Standard_Integer NbKnots();

		/****************** NbPoles ******************/
		%feature("compactdefaultargs") NbPoles;
		%feature("autodoc", "Returns the number of poles of the bspline curve whose data is computed in this framework. warning take particular care not to use this function before the computation is performed (perform function), as this condition is not checked and an error may therefore occur.

Returns
-------
int
") NbPoles;
		Standard_Integer NbPoles();

		/****************** Perform ******************/
		%feature("compactdefaultargs") Perform;
		%feature("autodoc", "Computes all the data needed to build a bspline curve equivalent to the adjacent bezier curve sequence still contained in this framework. a knot is inserted on the computed bspline curve at the junction point of two consecutive bezier curves. the degree of continuity of the bspline curve will be increased at the junction point of two consecutive bezier curves if their tangent vectors at this point are parallel. an angular tolerance given at the time of construction of this framework is used to check the parallelism of the two tangent vectors. use the available consultation functions to access the computed data. this data may then be used to construct the bspline curve. warning make sure that the curves in the bezier curve sequence contained in this framework are adjacent. an error may occur at the time of computation if this condition is not satisfied. particular care must be taken with respect to the above as this condition is not checked, either when defining the bezier curve sequence or at the time of computation.

Returns
-------
None
") Perform;
		void Perform();

		/****************** Poles ******************/
		%feature("compactdefaultargs") Poles;
		%feature("autodoc", "Loads the poles table with the poles of the bspline curve whose data is computed in this framework. warning - do not use this function before the computation is performed (perform function). - the length of the poles array must be equal to the number of poles of the bspline curve whose data is computed in this framework. particular care must be taken with respect to the above, as these conditions are not checked, and an error may occur.

Parameters
----------
Poles: TColgp_Array1OfPnt

Returns
-------
None
") Poles;
		void Poles(TColgp_Array1OfPnt & Poles);

};


%extend Convert_CompBezierCurvesToBSplineCurve {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**************************************
* class Convert_CompPolynomialToPoles *
**************************************/
class Convert_CompPolynomialToPoles {
	public:
		/****************** Convert_CompPolynomialToPoles ******************/
		%feature("compactdefaultargs") Convert_CompPolynomialToPoles;
		%feature("autodoc", "Warning! continuity can be at most the maximum degree of the polynomial functions trueintervals : this is the true parameterisation for the composite curve that is : the curve has mycontinuity if the nth curve is parameterized between mytrueintervals(n) and mytrueintervals(n+1) //! coefficients have to be the implicit 'c form': coefficients[numcurves][maxdegree+1][dimension] //! warning! the numberofcoefficient of an polynome is his degree + 1 example: to convert the linear function f(x) = 2*x + 1 on the domaine [2,5] to bspline with the bound [-1,1]. arguments are : numcurves = 1; continuity = 1; dimension = 1; maxdegree = 1; numcoeffpercurve [1] = {2}; coefficients[2] = {1, 2}; polynomialintervals[1,2] = {{2,5}} trueintervals[2] = {-1, 1}.

Parameters
----------
NumCurves: int
Continuity: int
Dimension: int
MaxDegree: int
NumCoeffPerCurve: TColStd_HArray1OfInteger
Coefficients: TColStd_HArray1OfReal
PolynomialIntervals: TColStd_HArray2OfReal
TrueIntervals: TColStd_HArray1OfReal

Returns
-------
None
") Convert_CompPolynomialToPoles;
		 Convert_CompPolynomialToPoles(const Standard_Integer NumCurves, const Standard_Integer Continuity, const Standard_Integer Dimension, const Standard_Integer MaxDegree, const opencascade::handle<TColStd_HArray1OfInteger> & NumCoeffPerCurve, const opencascade::handle<TColStd_HArray1OfReal> & Coefficients, const opencascade::handle<TColStd_HArray2OfReal> & PolynomialIntervals, const opencascade::handle<TColStd_HArray1OfReal> & TrueIntervals);

		/****************** Convert_CompPolynomialToPoles ******************/
		%feature("compactdefaultargs") Convert_CompPolynomialToPoles;
		%feature("autodoc", "To convert sevral span with different order of continuity. warning: the length of continuity have to be numcurves-1.

Parameters
----------
NumCurves: int
Dimension: int
MaxDegree: int
Continuity: TColStd_Array1OfInteger
NumCoeffPerCurve: TColStd_Array1OfInteger
Coefficients: TColStd_Array1OfReal
PolynomialIntervals: TColStd_Array2OfReal
TrueIntervals: TColStd_Array1OfReal

Returns
-------
None
") Convert_CompPolynomialToPoles;
		 Convert_CompPolynomialToPoles(const Standard_Integer NumCurves, const Standard_Integer Dimension, const Standard_Integer MaxDegree, const TColStd_Array1OfInteger & Continuity, const TColStd_Array1OfInteger & NumCoeffPerCurve, const TColStd_Array1OfReal & Coefficients, const TColStd_Array2OfReal & PolynomialIntervals, const TColStd_Array1OfReal & TrueIntervals);

		/****************** Convert_CompPolynomialToPoles ******************/
		%feature("compactdefaultargs") Convert_CompPolynomialToPoles;
		%feature("autodoc", "To convert only one span.

Parameters
----------
Dimension: int
MaxDegree: int
Degree: int
Coefficients: TColStd_Array1OfReal
PolynomialIntervals: TColStd_Array1OfReal
TrueIntervals: TColStd_Array1OfReal

Returns
-------
None
") Convert_CompPolynomialToPoles;
		 Convert_CompPolynomialToPoles(const Standard_Integer Dimension, const Standard_Integer MaxDegree, const Standard_Integer Degree, const TColStd_Array1OfReal & Coefficients, const TColStd_Array1OfReal & PolynomialIntervals, const TColStd_Array1OfReal & TrueIntervals);

		/****************** Degree ******************/
		%feature("compactdefaultargs") Degree;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") Degree;
		Standard_Integer Degree();

		/****************** IsDone ******************/
		%feature("compactdefaultargs") IsDone;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsDone;
		Standard_Boolean IsDone();

		/****************** Knots ******************/
		%feature("compactdefaultargs") Knots;
		%feature("autodoc", "Knots of the n-dimensional bspline.

Parameters
----------
K: TColStd_HArray1OfReal

Returns
-------
None
") Knots;
		void Knots(opencascade::handle<TColStd_HArray1OfReal> & K);

		/****************** Multiplicities ******************/
		%feature("compactdefaultargs") Multiplicities;
		%feature("autodoc", "Multiplicities of the knots in the bspline.

Parameters
----------
M: TColStd_HArray1OfInteger

Returns
-------
None
") Multiplicities;
		void Multiplicities(opencascade::handle<TColStd_HArray1OfInteger> & M);

		/****************** NbKnots ******************/
		%feature("compactdefaultargs") NbKnots;
		%feature("autodoc", "Degree of the n-dimensional bspline.

Returns
-------
int
") NbKnots;
		Standard_Integer NbKnots();

		/****************** NbPoles ******************/
		%feature("compactdefaultargs") NbPoles;
		%feature("autodoc", "Number of poles of the n-dimensional bspline.

Returns
-------
int
") NbPoles;
		Standard_Integer NbPoles();

		/****************** Poles ******************/
		%feature("compactdefaultargs") Poles;
		%feature("autodoc", "Returns the poles of the n-dimensional bspline in the following format : [1..numpoles][1..dimension].

Parameters
----------
Poles: TColStd_HArray2OfReal

Returns
-------
None
") Poles;
		void Poles(opencascade::handle<TColStd_HArray2OfReal> & Poles);

};


%extend Convert_CompPolynomialToPoles {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/************************************
* class Convert_ConicToBSplineCurve *
************************************/
%nodefaultctor Convert_ConicToBSplineCurve;
class Convert_ConicToBSplineCurve {
	public:
		/****************** BuildCosAndSin ******************/
		%feature("compactdefaultargs") BuildCosAndSin;
		%feature("autodoc", "No available documentation.

Parameters
----------
Parametrisation: Convert_ParameterisationType
CosNumerator: TColStd_HArray1OfReal
SinNumerator: TColStd_HArray1OfReal
Denominator: TColStd_HArray1OfReal
Knots: TColStd_HArray1OfReal
Mults: TColStd_HArray1OfInteger

Returns
-------
Degree: int
") BuildCosAndSin;
		void BuildCosAndSin(const Convert_ParameterisationType Parametrisation, opencascade::handle<TColStd_HArray1OfReal> & CosNumerator, opencascade::handle<TColStd_HArray1OfReal> & SinNumerator, opencascade::handle<TColStd_HArray1OfReal> & Denominator, Standard_Integer &OutValue, opencascade::handle<TColStd_HArray1OfReal> & Knots, opencascade::handle<TColStd_HArray1OfInteger> & Mults);

		/****************** BuildCosAndSin ******************/
		%feature("compactdefaultargs") BuildCosAndSin;
		%feature("autodoc", "No available documentation.

Parameters
----------
Parametrisation: Convert_ParameterisationType
UFirst: float
ULast: float
CosNumerator: TColStd_HArray1OfReal
SinNumerator: TColStd_HArray1OfReal
Denominator: TColStd_HArray1OfReal
Knots: TColStd_HArray1OfReal
Mults: TColStd_HArray1OfInteger

Returns
-------
Degree: int
") BuildCosAndSin;
		void BuildCosAndSin(const Convert_ParameterisationType Parametrisation, const Standard_Real UFirst, const Standard_Real ULast, opencascade::handle<TColStd_HArray1OfReal> & CosNumerator, opencascade::handle<TColStd_HArray1OfReal> & SinNumerator, opencascade::handle<TColStd_HArray1OfReal> & Denominator, Standard_Integer &OutValue, opencascade::handle<TColStd_HArray1OfReal> & Knots, opencascade::handle<TColStd_HArray1OfInteger> & Mults);

		/****************** Degree ******************/
		%feature("compactdefaultargs") Degree;
		%feature("autodoc", "Returns the degree of the bspline curve whose data is computed in this framework.

Returns
-------
int
") Degree;
		Standard_Integer Degree();

		/****************** IsPeriodic ******************/
		%feature("compactdefaultargs") IsPeriodic;
		%feature("autodoc", "Returns true if the bspline curve whose data is computed in this framework is periodic.

Returns
-------
bool
") IsPeriodic;
		Standard_Boolean IsPeriodic();

		/****************** Knot ******************/
		%feature("compactdefaultargs") Knot;
		%feature("autodoc", "Returns the knot of index index to the knots table of the bspline curve whose data is computed in this framework. exceptions standard_outofrange if index is outside the bounds of the knots table of the bspline curve whose data is computed in this framework.

Parameters
----------
Index: int

Returns
-------
float
") Knot;
		Standard_Real Knot(const Standard_Integer Index);

		/****************** Multiplicity ******************/
		%feature("compactdefaultargs") Multiplicity;
		%feature("autodoc", "Returns the multiplicity of the knot of index index to the knots table of the bspline curve whose data is computed in this framework. exceptions standard_outofrange if index is outside the bounds of the knots table of the bspline curve whose data is computed in this framework.

Parameters
----------
Index: int

Returns
-------
int
") Multiplicity;
		Standard_Integer Multiplicity(const Standard_Integer Index);

		/****************** NbKnots ******************/
		%feature("compactdefaultargs") NbKnots;
		%feature("autodoc", "Returns the number of knots of the bspline curve whose data is computed in this framework.

Returns
-------
int
") NbKnots;
		Standard_Integer NbKnots();

		/****************** NbPoles ******************/
		%feature("compactdefaultargs") NbPoles;
		%feature("autodoc", "Returns the number of poles of the bspline curve whose data is computed in this framework.

Returns
-------
int
") NbPoles;
		Standard_Integer NbPoles();

		/****************** Pole ******************/
		%feature("compactdefaultargs") Pole;
		%feature("autodoc", "Returns the pole of index index to the poles table of the bspline curve whose data is computed in this framework. exceptions standard_outofrange if index is outside the bounds of the poles table of the bspline curve whose data is computed in this framework.

Parameters
----------
Index: int

Returns
-------
gp_Pnt2d
") Pole;
		gp_Pnt2d Pole(const Standard_Integer Index);

		/****************** Weight ******************/
		%feature("compactdefaultargs") Weight;
		%feature("autodoc", "Returns the weight of the pole of index index to the poles table of the bspline curve whose data is computed in this framework. exceptions standard_outofrange if index is outside the bounds of the poles table of the bspline curve whose data is computed in this framework.

Parameters
----------
Index: int

Returns
-------
float
") Weight;
		Standard_Real Weight(const Standard_Integer Index);

};


%extend Convert_ConicToBSplineCurve {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**************************************************
* class Convert_ElementarySurfaceToBSplineSurface *
**************************************************/
%nodefaultctor Convert_ElementarySurfaceToBSplineSurface;
class Convert_ElementarySurfaceToBSplineSurface {
	public:
		/****************** IsUPeriodic ******************/
		%feature("compactdefaultargs") IsUPeriodic;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsUPeriodic;
		Standard_Boolean IsUPeriodic();

		/****************** IsVPeriodic ******************/
		%feature("compactdefaultargs") IsVPeriodic;
		%feature("autodoc", "Returns true if the bspline surface whose data is computed in this framework is periodic in the u or v parametric direction.

Returns
-------
bool
") IsVPeriodic;
		Standard_Boolean IsVPeriodic();

		/****************** NbUKnots ******************/
		%feature("compactdefaultargs") NbUKnots;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbUKnots;
		Standard_Integer NbUKnots();

		/****************** NbUPoles ******************/
		%feature("compactdefaultargs") NbUPoles;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbUPoles;
		Standard_Integer NbUPoles();

		/****************** NbVKnots ******************/
		%feature("compactdefaultargs") NbVKnots;
		%feature("autodoc", "Returns the number of knots for the u or v parametric direction of the bspline surface whose data is computed in this framework .

Returns
-------
int
") NbVKnots;
		Standard_Integer NbVKnots();

		/****************** NbVPoles ******************/
		%feature("compactdefaultargs") NbVPoles;
		%feature("autodoc", "Returns the number of poles for the u or v parametric direction of the bspline surface whose data is computed in this framework.

Returns
-------
int
") NbVPoles;
		Standard_Integer NbVPoles();

		/****************** Pole ******************/
		%feature("compactdefaultargs") Pole;
		%feature("autodoc", "Returns the pole of index (uindex,vindex) to the poles table of the bspline surface whose data is computed in this framework. exceptions standard_outofrange if, for the bspline surface whose data is computed in this framework: - uindex is outside the bounds of the poles table in the u parametric direction, or - vindex is outside the bounds of the poles table in the v parametric direction.

Parameters
----------
UIndex: int
VIndex: int

Returns
-------
gp_Pnt
") Pole;
		gp_Pnt Pole(const Standard_Integer UIndex, const Standard_Integer VIndex);

		/****************** UDegree ******************/
		%feature("compactdefaultargs") UDegree;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") UDegree;
		Standard_Integer UDegree();

		/****************** UKnot ******************/
		%feature("compactdefaultargs") UKnot;
		%feature("autodoc", "Returns the u-knot of range uindex. raised if uindex < 1 or uindex > nbuknots.

Parameters
----------
UIndex: int

Returns
-------
float
") UKnot;
		Standard_Real UKnot(const Standard_Integer UIndex);

		/****************** UMultiplicity ******************/
		%feature("compactdefaultargs") UMultiplicity;
		%feature("autodoc", "Returns the multiplicity of the u-knot of range uindex. raised if uindex < 1 or uindex > nbuknots.

Parameters
----------
UIndex: int

Returns
-------
int
") UMultiplicity;
		Standard_Integer UMultiplicity(const Standard_Integer UIndex);

		/****************** VDegree ******************/
		%feature("compactdefaultargs") VDegree;
		%feature("autodoc", "Returns the degree for the u or v parametric direction of the bspline surface whose data is computed in this framework.

Returns
-------
int
") VDegree;
		Standard_Integer VDegree();

		/****************** VKnot ******************/
		%feature("compactdefaultargs") VKnot;
		%feature("autodoc", "Returns the v-knot of range vindex. raised if vindex < 1 or vindex > nbvknots.

Parameters
----------
UIndex: int

Returns
-------
float
") VKnot;
		Standard_Real VKnot(const Standard_Integer UIndex);

		/****************** VMultiplicity ******************/
		%feature("compactdefaultargs") VMultiplicity;
		%feature("autodoc", "Returns the multiplicity of the v-knot of range vindex. raised if vindex < 1 or vindex > nbvknots.

Parameters
----------
VIndex: int

Returns
-------
int
") VMultiplicity;
		Standard_Integer VMultiplicity(const Standard_Integer VIndex);

		/****************** Weight ******************/
		%feature("compactdefaultargs") Weight;
		%feature("autodoc", "Returns the weight of the pole of index (uindex,vindex) to the poles table of the bspline surface whose data is computed in this framework. exceptions standard_outofrange if, for the bspline surface whose data is computed in this framework: - uindex is outside the bounds of the poles table in the u parametric direction, or - vindex is outside the bounds of the poles table in the v parametric direction.

Parameters
----------
UIndex: int
VIndex: int

Returns
-------
float
") Weight;
		Standard_Real Weight(const Standard_Integer UIndex, const Standard_Integer VIndex);

};


%extend Convert_ElementarySurfaceToBSplineSurface {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**************************************
* class Convert_GridPolynomialToPoles *
**************************************/
class Convert_GridPolynomialToPoles {
	public:
		/****************** Convert_GridPolynomialToPoles ******************/
		%feature("compactdefaultargs") Convert_GridPolynomialToPoles;
		%feature("autodoc", "To only one polynomial surface. the length of <polynomialuintervals> and <polynomialvintervals> have to be 2. this values defined the parametric domain of the polynomial equation. //! coefficients : the <coefficients> have to be formated than an 'c array' [maxudegree+1] [maxvdegree+1] [3].

Parameters
----------
MaxUDegree: int
MaxVDegree: int
NumCoeff: TColStd_HArray1OfInteger
Coefficients: TColStd_HArray1OfReal
PolynomialUIntervals: TColStd_HArray1OfReal
PolynomialVIntervals: TColStd_HArray1OfReal

Returns
-------
None
") Convert_GridPolynomialToPoles;
		 Convert_GridPolynomialToPoles(const Standard_Integer MaxUDegree, const Standard_Integer MaxVDegree, const opencascade::handle<TColStd_HArray1OfInteger> & NumCoeff, const opencascade::handle<TColStd_HArray1OfReal> & Coefficients, const opencascade::handle<TColStd_HArray1OfReal> & PolynomialUIntervals, const opencascade::handle<TColStd_HArray1OfReal> & PolynomialVIntervals);

		/****************** Convert_GridPolynomialToPoles ******************/
		%feature("compactdefaultargs") Convert_GridPolynomialToPoles;
		%feature("autodoc", "To one grid of polynomial surface. warning! continuity in each parametric direction can be at most the maximum degree of the polynomial functions. //! <trueuintervals>, <truevintervals> : this is the true parameterisation for the composite surface //! coefficients : the coefficients have to be formated than an 'c array' [nbvsurfaces] [nbusurfaces] [maxudegree+1] [maxvdegree+1] [3] raises domainerror if <numcoeffpersurface> is not a [1, nbvsurfaces*nbusurfaces, 1,2] array. if <coefficients> is not a.

Parameters
----------
NbUSurfaces: int
NBVSurfaces: int
UContinuity: int
VContinuity: int
MaxUDegree: int
MaxVDegree: int
NumCoeffPerSurface: TColStd_HArray2OfInteger
Coefficients: TColStd_HArray1OfReal
PolynomialUIntervals: TColStd_HArray1OfReal
PolynomialVIntervals: TColStd_HArray1OfReal
TrueUIntervals: TColStd_HArray1OfReal
TrueVIntervals: TColStd_HArray1OfReal

Returns
-------
None
") Convert_GridPolynomialToPoles;
		 Convert_GridPolynomialToPoles(const Standard_Integer NbUSurfaces, const Standard_Integer NBVSurfaces, const Standard_Integer UContinuity, const Standard_Integer VContinuity, const Standard_Integer MaxUDegree, const Standard_Integer MaxVDegree, const opencascade::handle<TColStd_HArray2OfInteger> & NumCoeffPerSurface, const opencascade::handle<TColStd_HArray1OfReal> & Coefficients, const opencascade::handle<TColStd_HArray1OfReal> & PolynomialUIntervals, const opencascade::handle<TColStd_HArray1OfReal> & PolynomialVIntervals, const opencascade::handle<TColStd_HArray1OfReal> & TrueUIntervals, const opencascade::handle<TColStd_HArray1OfReal> & TrueVIntervals);

		/****************** IsDone ******************/
		%feature("compactdefaultargs") IsDone;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsDone;
		Standard_Boolean IsDone();

		/****************** NbUKnots ******************/
		%feature("compactdefaultargs") NbUKnots;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbUKnots;
		Standard_Integer NbUKnots();

		/****************** NbUPoles ******************/
		%feature("compactdefaultargs") NbUPoles;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbUPoles;
		Standard_Integer NbUPoles();

		/****************** NbVKnots ******************/
		%feature("compactdefaultargs") NbVKnots;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbVKnots;
		Standard_Integer NbVKnots();

		/****************** NbVPoles ******************/
		%feature("compactdefaultargs") NbVPoles;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbVPoles;
		Standard_Integer NbVPoles();

		/****************** Perform ******************/
		%feature("compactdefaultargs") Perform;
		%feature("autodoc", "No available documentation.

Parameters
----------
UContinuity: int
VContinuity: int
MaxUDegree: int
MaxVDegree: int
NumCoeffPerSurface: TColStd_HArray2OfInteger
Coefficients: TColStd_HArray1OfReal
PolynomialUIntervals: TColStd_HArray1OfReal
PolynomialVIntervals: TColStd_HArray1OfReal
TrueUIntervals: TColStd_HArray1OfReal
TrueVIntervals: TColStd_HArray1OfReal

Returns
-------
None
") Perform;
		void Perform(const Standard_Integer UContinuity, const Standard_Integer VContinuity, const Standard_Integer MaxUDegree, const Standard_Integer MaxVDegree, const opencascade::handle<TColStd_HArray2OfInteger> & NumCoeffPerSurface, const opencascade::handle<TColStd_HArray1OfReal> & Coefficients, const opencascade::handle<TColStd_HArray1OfReal> & PolynomialUIntervals, const opencascade::handle<TColStd_HArray1OfReal> & PolynomialVIntervals, const opencascade::handle<TColStd_HArray1OfReal> & TrueUIntervals, const opencascade::handle<TColStd_HArray1OfReal> & TrueVIntervals);

		/****************** Poles ******************/
		%feature("compactdefaultargs") Poles;
		%feature("autodoc", "Returns the poles of the bspline surface.

Returns
-------
opencascade::handle<TColgp_HArray2OfPnt>
") Poles;
		const opencascade::handle<TColgp_HArray2OfPnt> & Poles();

		/****************** UDegree ******************/
		%feature("compactdefaultargs") UDegree;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") UDegree;
		Standard_Integer UDegree();

		/****************** UKnots ******************/
		%feature("compactdefaultargs") UKnots;
		%feature("autodoc", "Knots in the u direction.

Returns
-------
opencascade::handle<TColStd_HArray1OfReal>
") UKnots;
		const opencascade::handle<TColStd_HArray1OfReal> & UKnots();

		/****************** UMultiplicities ******************/
		%feature("compactdefaultargs") UMultiplicities;
		%feature("autodoc", "Multiplicities of the knots in the u direction.

Returns
-------
opencascade::handle<TColStd_HArray1OfInteger>
") UMultiplicities;
		const opencascade::handle<TColStd_HArray1OfInteger> & UMultiplicities();

		/****************** VDegree ******************/
		%feature("compactdefaultargs") VDegree;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") VDegree;
		Standard_Integer VDegree();

		/****************** VKnots ******************/
		%feature("compactdefaultargs") VKnots;
		%feature("autodoc", "Knots in the v direction.

Returns
-------
opencascade::handle<TColStd_HArray1OfReal>
") VKnots;
		const opencascade::handle<TColStd_HArray1OfReal> & VKnots();

		/****************** VMultiplicities ******************/
		%feature("compactdefaultargs") VMultiplicities;
		%feature("autodoc", "Multiplicities of the knots in the v direction.

Returns
-------
opencascade::handle<TColStd_HArray1OfInteger>
") VMultiplicities;
		const opencascade::handle<TColStd_HArray1OfInteger> & VMultiplicities();

};


%extend Convert_GridPolynomialToPoles {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*************************************
* class Convert_CircleToBSplineCurve *
*************************************/
class Convert_CircleToBSplineCurve : public Convert_ConicToBSplineCurve {
	public:
		/****************** Convert_CircleToBSplineCurve ******************/
		%feature("compactdefaultargs") Convert_CircleToBSplineCurve;
		%feature("autodoc", "The equivalent b-spline curve has the same orientation as the circle c.

Parameters
----------
C: gp_Circ2d
Parameterisation: Convert_ParameterisationType,optional
	default value is Convert_TgtThetaOver2

Returns
-------
None
") Convert_CircleToBSplineCurve;
		 Convert_CircleToBSplineCurve(const gp_Circ2d & C, const Convert_ParameterisationType Parameterisation = Convert_TgtThetaOver2);

		/****************** Convert_CircleToBSplineCurve ******************/
		%feature("compactdefaultargs") Convert_CircleToBSplineCurve;
		%feature("autodoc", "The circle c is limited between the parametric values u1, u2 in radians. u1 and u2 [0.0, 2*pi] . the equivalent b-spline curve is oriented from u1 to u2 and has the same orientation as the circle c. //! raised if u1 = u2 or u1 = u2 + 2.0 * pi.

Parameters
----------
C: gp_Circ2d
U1: float
U2: float
Parameterisation: Convert_ParameterisationType,optional
	default value is Convert_TgtThetaOver2

Returns
-------
None
") Convert_CircleToBSplineCurve;
		 Convert_CircleToBSplineCurve(const gp_Circ2d & C, const Standard_Real U1, const Standard_Real U2, const Convert_ParameterisationType Parameterisation = Convert_TgtThetaOver2);

};


%extend Convert_CircleToBSplineCurve {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*************************************
* class Convert_ConeToBSplineSurface *
*************************************/
class Convert_ConeToBSplineSurface : public Convert_ElementarySurfaceToBSplineSurface {
	public:
		/****************** Convert_ConeToBSplineSurface ******************/
		%feature("compactdefaultargs") Convert_ConeToBSplineSurface;
		%feature("autodoc", "The equivalent b-spline surface as the same orientation as the cone in the u and v parametric directions. //! raised if u1 = u2 or u1 = u2 + 2.0 * pi raised if v1 = v2.

Parameters
----------
C: gp_Cone
U1: float
U2: float
V1: float
V2: float

Returns
-------
None
") Convert_ConeToBSplineSurface;
		 Convert_ConeToBSplineSurface(const gp_Cone & C, const Standard_Real U1, const Standard_Real U2, const Standard_Real V1, const Standard_Real V2);

		/****************** Convert_ConeToBSplineSurface ******************/
		%feature("compactdefaultargs") Convert_ConeToBSplineSurface;
		%feature("autodoc", "The equivalent b-spline surface as the same orientation as the cone in the u and v parametric directions. //! raised if v1 = v2.

Parameters
----------
C: gp_Cone
V1: float
V2: float

Returns
-------
None
") Convert_ConeToBSplineSurface;
		 Convert_ConeToBSplineSurface(const gp_Cone & C, const Standard_Real V1, const Standard_Real V2);

};


%extend Convert_ConeToBSplineSurface {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*****************************************
* class Convert_CylinderToBSplineSurface *
*****************************************/
class Convert_CylinderToBSplineSurface : public Convert_ElementarySurfaceToBSplineSurface {
	public:
		/****************** Convert_CylinderToBSplineSurface ******************/
		%feature("compactdefaultargs") Convert_CylinderToBSplineSurface;
		%feature("autodoc", "The equivalent b-splinesurface as the same orientation as the cylinder in the u and v parametric directions. //! raised if u1 = u2 or u1 = u2 + 2.0 * pi raised if v1 = v2.

Parameters
----------
Cyl: gp_Cylinder
U1: float
U2: float
V1: float
V2: float

Returns
-------
None
") Convert_CylinderToBSplineSurface;
		 Convert_CylinderToBSplineSurface(const gp_Cylinder & Cyl, const Standard_Real U1, const Standard_Real U2, const Standard_Real V1, const Standard_Real V2);

		/****************** Convert_CylinderToBSplineSurface ******************/
		%feature("compactdefaultargs") Convert_CylinderToBSplineSurface;
		%feature("autodoc", "The equivalent b-splinesurface as the same orientation as the cylinder in the u and v parametric directions. //! raised if v1 = v2.

Parameters
----------
Cyl: gp_Cylinder
V1: float
V2: float

Returns
-------
None
") Convert_CylinderToBSplineSurface;
		 Convert_CylinderToBSplineSurface(const gp_Cylinder & Cyl, const Standard_Real V1, const Standard_Real V2);

};


%extend Convert_CylinderToBSplineSurface {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**************************************
* class Convert_EllipseToBSplineCurve *
**************************************/
class Convert_EllipseToBSplineCurve : public Convert_ConicToBSplineCurve {
	public:
		/****************** Convert_EllipseToBSplineCurve ******************/
		%feature("compactdefaultargs") Convert_EllipseToBSplineCurve;
		%feature("autodoc", "The equivalent b-spline curve has the same orientation as the ellipse e.

Parameters
----------
E: gp_Elips2d
Parameterisation: Convert_ParameterisationType,optional
	default value is Convert_TgtThetaOver2

Returns
-------
None
") Convert_EllipseToBSplineCurve;
		 Convert_EllipseToBSplineCurve(const gp_Elips2d & E, const Convert_ParameterisationType Parameterisation = Convert_TgtThetaOver2);

		/****************** Convert_EllipseToBSplineCurve ******************/
		%feature("compactdefaultargs") Convert_EllipseToBSplineCurve;
		%feature("autodoc", "The ellipse e is limited between the parametric values u1, u2. the equivalent b-spline curve is oriented from u1 to u2 and has the same orientation as e. //! raised if u1 = u2 or u1 = u2 + 2.0 * pi.

Parameters
----------
E: gp_Elips2d
U1: float
U2: float
Parameterisation: Convert_ParameterisationType,optional
	default value is Convert_TgtThetaOver2

Returns
-------
None
") Convert_EllipseToBSplineCurve;
		 Convert_EllipseToBSplineCurve(const gp_Elips2d & E, const Standard_Real U1, const Standard_Real U2, const Convert_ParameterisationType Parameterisation = Convert_TgtThetaOver2);

};


%extend Convert_EllipseToBSplineCurve {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/****************************************
* class Convert_HyperbolaToBSplineCurve *
****************************************/
class Convert_HyperbolaToBSplineCurve : public Convert_ConicToBSplineCurve {
	public:
		/****************** Convert_HyperbolaToBSplineCurve ******************/
		%feature("compactdefaultargs") Convert_HyperbolaToBSplineCurve;
		%feature("autodoc", "The hyperbola h is limited between the parametric values u1, u2 and the equivalent b-spline curve has the same orientation as the hyperbola.

Parameters
----------
H: gp_Hypr2d
U1: float
U2: float

Returns
-------
None
") Convert_HyperbolaToBSplineCurve;
		 Convert_HyperbolaToBSplineCurve(const gp_Hypr2d & H, const Standard_Real U1, const Standard_Real U2);

};


%extend Convert_HyperbolaToBSplineCurve {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***************************************
* class Convert_ParabolaToBSplineCurve *
***************************************/
class Convert_ParabolaToBSplineCurve : public Convert_ConicToBSplineCurve {
	public:
		/****************** Convert_ParabolaToBSplineCurve ******************/
		%feature("compactdefaultargs") Convert_ParabolaToBSplineCurve;
		%feature("autodoc", "The parabola prb is limited between the parametric values u1, u2 and the equivalent b-spline curve as the same orientation as the parabola prb.

Parameters
----------
Prb: gp_Parab2d
U1: float
U2: float

Returns
-------
None
") Convert_ParabolaToBSplineCurve;
		 Convert_ParabolaToBSplineCurve(const gp_Parab2d & Prb, const Standard_Real U1, const Standard_Real U2);

};


%extend Convert_ParabolaToBSplineCurve {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***************************************
* class Convert_SphereToBSplineSurface *
***************************************/
class Convert_SphereToBSplineSurface : public Convert_ElementarySurfaceToBSplineSurface {
	public:
		/****************** Convert_SphereToBSplineSurface ******************/
		%feature("compactdefaultargs") Convert_SphereToBSplineSurface;
		%feature("autodoc", "The equivalent b-spline surface as the same orientation as the sphere in the u and v parametric directions. //! raised if u1 = u2 or u1 = u2 + 2.0 * pi raised if v1 = v2.

Parameters
----------
Sph: gp_Sphere
U1: float
U2: float
V1: float
V2: float

Returns
-------
None
") Convert_SphereToBSplineSurface;
		 Convert_SphereToBSplineSurface(const gp_Sphere & Sph, const Standard_Real U1, const Standard_Real U2, const Standard_Real V1, const Standard_Real V2);

		/****************** Convert_SphereToBSplineSurface ******************/
		%feature("compactdefaultargs") Convert_SphereToBSplineSurface;
		%feature("autodoc", "The equivalent b-spline surface as the same orientation as the sphere in the u and v parametric directions. //! raised if utrim = true and param1 = param2 or param1 = param2 + 2.0 * pi raised if utrim = false and param1 = param2.

Parameters
----------
Sph: gp_Sphere
Param1: float
Param2: float
UTrim: bool,optional
	default value is Standard_True

Returns
-------
None
") Convert_SphereToBSplineSurface;
		 Convert_SphereToBSplineSurface(const gp_Sphere & Sph, const Standard_Real Param1, const Standard_Real Param2, const Standard_Boolean UTrim = Standard_True);

		/****************** Convert_SphereToBSplineSurface ******************/
		%feature("compactdefaultargs") Convert_SphereToBSplineSurface;
		%feature("autodoc", "The equivalent b-spline surface as the same orientation as the sphere in the u and v parametric directions.

Parameters
----------
Sph: gp_Sphere

Returns
-------
None
") Convert_SphereToBSplineSurface;
		 Convert_SphereToBSplineSurface(const gp_Sphere & Sph);

};


%extend Convert_SphereToBSplineSurface {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**************************************
* class Convert_TorusToBSplineSurface *
**************************************/
class Convert_TorusToBSplineSurface : public Convert_ElementarySurfaceToBSplineSurface {
	public:
		/****************** Convert_TorusToBSplineSurface ******************/
		%feature("compactdefaultargs") Convert_TorusToBSplineSurface;
		%feature("autodoc", "The equivalent b-spline surface as the same orientation as the torus in the u and v parametric directions. //! raised if u1 = u2 or u1 = u2 + 2.0 * pi raised if v1 = v2 or v1 = v2 + 2.0 * pi.

Parameters
----------
T: gp_Torus
U1: float
U2: float
V1: float
V2: float

Returns
-------
None
") Convert_TorusToBSplineSurface;
		 Convert_TorusToBSplineSurface(const gp_Torus & T, const Standard_Real U1, const Standard_Real U2, const Standard_Real V1, const Standard_Real V2);

		/****************** Convert_TorusToBSplineSurface ******************/
		%feature("compactdefaultargs") Convert_TorusToBSplineSurface;
		%feature("autodoc", "The equivalent b-spline surface as the same orientation as the torus in the u and v parametric directions. //! raised if param1 = param2 or param1 = param2 + 2.0 * pi.

Parameters
----------
T: gp_Torus
Param1: float
Param2: float
UTrim: bool,optional
	default value is Standard_True

Returns
-------
None
") Convert_TorusToBSplineSurface;
		 Convert_TorusToBSplineSurface(const gp_Torus & T, const Standard_Real Param1, const Standard_Real Param2, const Standard_Boolean UTrim = Standard_True);

		/****************** Convert_TorusToBSplineSurface ******************/
		%feature("compactdefaultargs") Convert_TorusToBSplineSurface;
		%feature("autodoc", "The equivalent b-spline surface as the same orientation as the torus in the u and v parametric directions.

Parameters
----------
T: gp_Torus

Returns
-------
None
") Convert_TorusToBSplineSurface;
		 Convert_TorusToBSplineSurface(const gp_Torus & T);

};


%extend Convert_TorusToBSplineSurface {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/* harray1 classes */
/* harray2 classes */
/* hsequence classes */
