// #include <Python.h>
#include "stack.h"
static char module_docstring[] =
    "This module provides an interface for additional data structures.";
static char stack_docstring[] =
    "This is an array implementation of a stack.";
cdef extern from "stack.h":
    struct stack_s:
        pass
