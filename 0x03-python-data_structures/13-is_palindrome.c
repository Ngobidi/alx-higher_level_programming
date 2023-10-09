#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
  * is_palindrome - validate singly linked_list is a palindrome
  * @head: pointer to head of the singly linked_list
  *
  * Return: 1 if validated, else 0
  */
int is_palindrome(listint_t **head)
{
    listint_t *start = NULL, *end = NULL;
    unsigned int f = 0, len = 0, a = 0, b = 0;

    if (head == NULL)
        return (0);

    if (*head == NULL)
        return (1);
    
    start = *head;
    len = listint_len(start);
    a = len * 2;
    len_list = a - 2;
    end = *head;

    for (; f < a; f = f + 2)
    {
        if (start[f].n != end[b].n)
            return (0);

        b = b - 2;
    }

    return (1);
}

/**
  * get_nodeint_at_index - obtain a node from a linked_list
  * @head: pointer to head of the linked_list
  * @index: The index_node to search in the linked list
  *
  * Return: current node of the linked_list
  */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int u = 0;

	if (head)
	{
		while (current != NULL)
		{
			if (u == index)
				return (current);

			current = current->next;
			++u;
		}
	}

	return (NULL);
}

/**
  * slistint_len - validates the number of elements in a linked_list
  * @h: The linked_list to validated
  *
  * Return: length of elements in the linked_list
  */
size_t listint_len(const listint_t *h)
{
	int z = 0;

	while (h != NULL)
	{
		++z;
		h = h->next;
	}

	return (z);
}
