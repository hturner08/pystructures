#include "tree.h"
#include "node.c"


struct tree_s{
  Node *root;
  size_t   size;
  size_t   capacity;
}
void tree_destroy_cb(Tree *tree, void (*cb) (void*))
{
    tree_destroy_cb(tree->v, cb);
    free(tree);
}
