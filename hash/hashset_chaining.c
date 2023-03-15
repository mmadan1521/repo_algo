#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>

#define HASH_CAPACITY 11

typedef struct hash_node {
   int               data;
   struct hash_node   *next; // for chaining during hash collision
} hash_node_t;

typedef struct hash_set {
   int capacity;
   hash_node_t **elements; // basically array of pointers "*elements[]"
} hash_set_t;

int hash_code(int data)
{
   int key = abs(data) % HASH_CAPACITY;
   printf("\t\thash key for %d ==> %d\n", data, key);
   return key;
}

bool hash_set_contains(hash_set_t *hash_set, int data)
{
   int index = hash_code(data);

   hash_node_t *curr_ptr = hash_set->elements[index];
   while (curr_ptr != NULL) {
      if (curr_ptr->data == data) {
         printf("node %d is present in hash set\n", data);
         return true; // found
      }
      curr_ptr = curr_ptr->next;
   }
   printf("node %d is not present in hash set\n", data);
   return false;
}

void hash_set_add(hash_set_t *hash_set, int data)
{
   if (hash_set_contains(hash_set, data) == false) { // not already present
      int index = hash_code(data);
      hash_node_t *hash_node = calloc(1, sizeof(hash_node_t));
      hash_node->data = data;

      if (hash_set->elements[index] == NULL) {
         hash_set->elements[index] = hash_node;
      } else {
         hash_node->next = hash_set->elements[index]; 
         hash_set->elements[index] = hash_node; 
      }
      printf("+++++ Hash Set added: %d\n", data);
   } else {
      printf("!!!!! Hash Set duplicates not allowed: %d\n", data);
   }
}

void hash_set_print(hash_set_t *hash_set)
{
   for (int i = 0; i < HASH_CAPACITY; i++) {
      if (hash_set->elements[i]) {
         printf("%d: ", i);
         hash_node_t *curr_ptr = hash_set->elements[i];
         while (curr_ptr != NULL) {
            printf(" ==> %d", curr_ptr->data);
            curr_ptr = curr_ptr->next;
         }
         printf("\n");
      }
   }
}

void hash_set_free(hash_set_t *hash_set)
{
   for (int i = 0; i < HASH_CAPACITY; i++) {
      if (hash_set->elements[i]) {
         printf("%d: ", i);
         hash_node_t *curr_ptr = hash_set->elements[i];
         while (curr_ptr != NULL) {
            printf(" ==> free(%d)", curr_ptr->data);
            hash_node_t *temp_ptr = curr_ptr;
            curr_ptr = curr_ptr->next;
            free(temp_ptr);
         }
         printf("\n");
      }
   }
}

int main()
{
   hash_set_t hash_set;
   hash_set.capacity = HASH_CAPACITY;
   hash_set.elements = calloc(HASH_CAPACITY, sizeof(hash_node_t *));

   printf("(HASH_CAPACITY * sizeof(hash_node_t *)) ==> %lu\n", (HASH_CAPACITY * sizeof(hash_node_t *)));
   printf("address off hash_set.elements: %p\n", hash_set.elements);

   for (int i = 0; i < HASH_CAPACITY; i++) {
      printf("address of elements[%d]: %p, %p\n", i, &hash_set.elements[i], hash_set.elements[i]);
   }

   hash_set_add(&hash_set, 0);
   hash_set_add(&hash_set, 10);
   hash_set_add(&hash_set, 11);
   hash_set_add(&hash_set, 12);
   hash_set_add(&hash_set, 20);
   hash_set_add(&hash_set, 21);
   hash_set_add(&hash_set, 22);
   hash_set_add(&hash_set, 30);
   hash_set_add(&hash_set, 31);
   hash_set_add(&hash_set, 32);
   hash_set_add(&hash_set, 20);

   hash_set_print(&hash_set);

   printf("\n ===== Check for node presence ===== \n");
   hash_set_contains(&hash_set, 0);
   hash_set_contains(&hash_set, 21);
   hash_set_contains(&hash_set, 91);

   /*
   TODO:
   hash_set_remove(&hash_set, 0);
   hash_set_remove(&hash_set, 22);
   hash_set_remove(&hash_set, 32);
   */

   // free memory
   hash_set_free(&hash_set);
   free(hash_set.elements);
}