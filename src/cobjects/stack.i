%module stack
%{
/* Includes the header in the wrapper code */
#include "stack.h"
%}

/* Parse the header file to generate wrappers */
%include "stack.h"
