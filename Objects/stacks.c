#include <stdio.h>
#include <stdlib.h>
#include "stacks.h"
#include <limits.h>
/*
This is an implementation of a stack
using a LinkedList. Using a LinkedList in
place of an array, allows size to be determined
at runtime.

*/
typedef struct Node{
  Node *next;
  int* contents;
  void (*add)(int* added, );
};
void add_Contents(int* added, int* contents){
  contents = added;
};
typedef struct Stack{
  Node *head;
  void (*push)(Node *pushed);
  Node* (*pop);
  Node* (*peek);
};
