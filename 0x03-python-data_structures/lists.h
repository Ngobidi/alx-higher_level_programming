#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

/**
 * struct listint_s - singly linked_list typed defined
 * @b: int value
 * @next: pointers to the next_node
 *
 * Description: singly linked_list nodes structure defined
 */
typedef struct listint_s
{
	    int b;
	        struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int b);
void free_listint(listint_t *head);
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index);
int is_palindrome(listint_t **head);
size_t listint_len(const listint_t *h);

#endif /* LISTS_H */
