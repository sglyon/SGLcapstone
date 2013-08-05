#ifndef _H_KNOT_VECTOR_H_
#define _H_KNOT_VECTOR_H_

#include "common.h"
#include <vector>
#include <iostream>

using namespace std;
using namespace util;

namespace hsf
{
  class HKnotVector
  {
    /// A one-dimensional object which stores a knot vector of any degree.
    /// No geometric operations are performed using a knot vector, only basis
    /// function queries. This class is best used in connection with a HNURBS object which
    /// stores the geometric information. We do store the extra knot for open
    /// knot vectors. So a degree p knot vector will have p + 1 knots at the beginning
    /// and end of the knot vector. We currently don't support periodic knot
    /// vectors although this could be added pretty easily.
    public:

    /// Default constructor
    HKnotVector() : mDeg( 0 ) {}

    /// construct a knot vector from a vector of knots. We assume that p + 1 repeated
    /// knots exists at the beginning and end of the knot vector.
    HKnotVector( uint degree, const DoubleVec &knots )
      : mDeg( degree ), mKnots( knots )
    {
      getKVecData( mKnots, mGroups, mReverseGroups, mMultipleCount );
    }

    /// A destructor
    ~HKnotVector() {}

    /// Returns the degree of this knot vector.
    uint degree() const { return mDeg; }

    /// Returns true if the knot vector is even.
    bool isEven() const { return degree() % 2 == 0; }

    /// Returns true if the knot vector is odd.
    bool isOdd() const { return !isEven(); }

    protected:

    uint mDeg;
    DoubleVec mKnots;
    IntVec mGroups;
    IntVecVec mReverseGroups;
    IntVec mMultipleCount;

    /// Returns group, multiplicity, zcount data for a vector of knots.
    void getKVecData( const DoubleVec &knots, IntVec &knot_groups,
              IntVecVec &reverse_knot_groups, IntVec &multiple_counts ) const
    {
      knot_groups.clear();
      reverse_knot_groups.clear();
      multiple_counts.clear();
      knot_groups.push_back( 0 );
      multiple_counts.push_back( 0 );
      uint group_index = 0;
      uint multiple_count = 0;
      IntVec group;
      group.push_back( 0 );
      for( uint iknot = 1; iknot < knots.size(); ++iknot )
      {
        if( equals( knots[ iknot - 1 ], knots[ iknot ], 1e-8 ) )
        {
          group.push_back( iknot );
          ++multiple_count;
        }
        else
        {
          ++group_index;
          multiple_count = 0;
          reverse_knot_groups.push_back( group );
          group.clear();
          group.push_back( iknot );
        }
        knot_groups.push_back( group_index );
        multiple_counts.push_back( multiple_count );
      }
      reverse_knot_groups.push_back( group );
    }
  };
}
#endif
