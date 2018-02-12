%module queue
%{
/* Includes the header in the wrapper code */
#include "queue.h"
%}

/* Parse the header file to generate wrappers */
%include "queue.h"
