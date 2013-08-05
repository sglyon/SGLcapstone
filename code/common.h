#ifndef _UTIL_COMMON_H_
#define _UTIL_COMMON_H_

#include <climits>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <assert.h>

/// common definitions needed throughout the hsf library

typedef unsigned int uint;
typedef unsigned long ulong;
typedef unsigned short ushort;
typedef unsigned char uchar;

using namespace std;

namespace util
{
  /// Clamps the values to a determined range. The values
  /// 'minimum' and 'maxmimum' must be of a type that can be
  /// cast to the same type as 'value', and must be less-than
  /// comparable with value's type as well.
  template< typename T, typename T2, typename T3 >
  inline T numClamp( T value, T2 minimum, T3 maximum )
  {
    if( value < minimum )
      return minimum;
    if( maximum < value )
      return maximum;
    return value;
  }

  /// This form is a little inconvenient, but is the basis of most other
  /// ways of measuring equality.
  inline bool equals( double a, double b, double tolerance )
  {
    // This method has been benchmarked, and it's pretty fast.
    return ( a == b ) ||
      ( ( a <= ( b + tolerance ) ) &&
      ( a >= ( b - tolerance ) ) );
  }

  typedef std::vector< double > DoubleVec;
  typedef std::vector< int > IntVec;
  typedef std::vector< IntVec > IntVecVec;
}
#endif
