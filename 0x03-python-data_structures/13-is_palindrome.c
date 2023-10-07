#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
  * is_palindrome - validates singly linked_list is a palindrome
  * @head: The begining of the singly linked_list
  *
  * Return: 1 if validated, else 0
  */
int is_palindrome(listint_t **head)
{
    listint_t *begin = NULL, *stop = NULL;
    unsigned int x = 0, length = 0, length_cyc = 0, length_list = 0;

    if (head == NULL)
        return (0);

    if (*head == NULL)
        return (1);
    
    begin = *head;
    length = listint_len(begin);
    length_cyc = length * 2;
    length_list = length_cyc - 2;
    stop = *head;

    for (; x < length_cyc; x = x + 2)
    {
        if (begin[x].n != end[length_list].n)
            return (0);

        length_list = length_list - 2;
    }

    return (1);
}

/**
  * get_nodeint_at_index - obtain node at index from a linked_list
  * @head: The node_head
  * @index: The index to obtain in the linked_list
  *
  * Return: The required node of the linked_list
  */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int p = 0;

	if (head)
	{
		while (current != NULL)
		{
			if (p == index)
				return (current);

			current = current->next;
			++p;
		}
	}

	return (NULL);
}

/**
  * slistint_len - Count the num of element in a linked_list
  * @h: The linked_list to counts
  *
  * Return: length of elements in the linked_list
  */
size_t listint_len(const listint_t *h)
{
	int l = 0;

	while (h != NULL)
	{
		++l;
		h = h->next;
	}

	return (l);
}
