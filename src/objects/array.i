%module array
%{
/* Includes the header in the wrapper code */
#include "array.h"
%}

/* Parse the header file to generate wrappers */
%include "array.h"
