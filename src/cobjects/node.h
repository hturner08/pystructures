#ifndef COLLECTIONS_C_NODE_H
#define COLLECTIONS_C_NODE_H

#include "common.h"
#include "array.h"

typedef struct node_s Node;

enum cc_stat  node_new             (Node **out);

void          node_destroy         (Node *ar);
void          node_destroy_cb      (Node *ar, void (*cb) (void*));

enum cc_stat  node_add_content      (Node *n, void *element);
enum cc_stat  node_get_content      (Node *n);
enum cc_stat  node_remove_content   (Node *n);

size_t        node_size            (Node *ar);
size_t        node_capacity        (Node *ar);
