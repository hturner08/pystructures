%module node
%{
/* Includes the header in the wrapper code */
#include "node.h"
%}

/* Parse the header file to generate wrappers */
%include "node.i"
