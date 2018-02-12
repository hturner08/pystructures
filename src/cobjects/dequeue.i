%module dequeue
%{
/* Includes the header in the wrapper code */
#include "dequeue.h"
%}

/* Parse the header file to generate wrappers */
%include "dequeue.h"
