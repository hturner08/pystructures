%module pystructures
%{
/* Includes the header in the wrapper code */
#include "array.h"
#include "queue.h"
#include "common.h"
#include "dequeue.h"
#include "pqueue.h"
#include "stack.h"
/*#include"tree.h*/
/*#include "node.h"*/
%}

/* Parse the header file to generate wrappers */
%include "array.h"
%include "array.h"
%include "queue.h"
%include "common.h"
%include "dequeue.h"
%include "pqueue.h"
%include "stack.h"
