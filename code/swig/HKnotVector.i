%module hbspy

%{
#include "../HKnotVector.h"
%}

%include "std_vector.i"
namespace std {
    %template(IntVec)    vector<int>;
    %template(DoubleVec) vector<double>;
    %template(IntVecVec) vector<vector<int> >;
}

%import "../common.h"
%include "../HKnotVector.h"
