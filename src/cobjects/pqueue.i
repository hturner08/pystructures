%module pqueue
%{
/* Includes the header in the wrapper code */
#include "pqueue.h"
%}

/* Parse the header file to generate wrappers */
%include "pqueue.h"
