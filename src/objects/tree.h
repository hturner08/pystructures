#ifndef COLLECTIONS_C_TREE_H
#define COLLECTIONS_C_TREE_H

typedef struct tree_s Tree;

typedef struct tree_conf_s{

}
typedef struct tree_iter_s{

}

enum cc_stat  tree_new             (Tree **out);

void          tree_destroy         (Tree *tr);

enum cc_stat  tree_add             (Tree *tr, void *element);

enum cc_stat  tree_remove          (Tree *tr, void *element, void **out);
enum cc_stat  tree_remove_at       (Tree *tr, size_t index, void **out);
enum cc_stat  tree_remove_last     (Tree *tr, void **out);
void          tree_remove_all      (Tree *tr); //Does not remove root


enum cc_stat  tree_get_at          (Tree *tr, size_t index, void **out);
enum cc_stat  tree_get_last        (Tree *tr, void **out);

enum cc_stat  tree_subtree        (Tree *tr, size_t from, size_t to, Tree **out);
enum cc_stat  tree_copy_shallow    (Tree *tr, Tree **out);
enum cc_stat  tree_copy_deep       (Tree *tr, void *(*cp) (void*), Tree **out);

size_t        tree_contains        (Array *ar, void *element);
size_t        tree_contains_value  (Array *ar, void *element, int (*cmp) (const void*, const void*));
size_t        tree_size            (Array *ar);

enum cc_stat  array_index_of        (Array *ar, void *element, size_t *index);
void          array_sort            (Array *ar, int (*cmp) (const void*, const void*));

void          array_map             (Array *ar, void (*fn) (void*));
void          array_reduce          (Array *ar, void (*fn) (void*, void*, void*), void *result);

enum cc_stat  array_filter_mut      (Array *ar, bool (*predicate) (const void*));
enum cc_stat  array_filter          (Array *ar, bool (*predicate) (const void*), Array **out);

void          tree_iter_init       (TreeIter *iter, Tree *tr);
enum cc_stat  tree_iter_next       (TreeIter *iter, void **out);
enum cc_stat  tree_iter_remove     (TreeIter *iter, void **out);
enum cc_stat  tree_iter_add        (TreeIter *iter, void *element);
enum cc_stat  tree_iter_replace    (TreeIter *iter, void *element, void **out);
size_t        tree_iter_index      (TreeIter *iter);
