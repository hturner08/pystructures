
#include "node.h"

struct node_s{
  void *content;

  void *(*mem_alloc)  (size_t size);
  void *(*mem_calloc) (size_t blocks, size_t size);
  void  (*mem_free)   (void *block);
}
