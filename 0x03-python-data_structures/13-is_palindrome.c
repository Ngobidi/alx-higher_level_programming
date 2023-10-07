#include "lists.h"

/**
  * is_palindrome - validates singly linked_list is a palindrome
  * @head: The begining of the singly linked_list
  *
  * Return: 1 if validated, else 0
  */
int is_palindrome(listint_t **head)
{
    listint_t *start = NULL, *end = NULL;
    unsigned int x = 0, len = 0, len_cyc = 0, len_list = 0;

    if (head == NULL)
        return (0);

    if (*head == NULL)
        return (1);
    
    start = *head;
    len = listint_len(start);
    len_cyc = len * 2;
    len_list = len_cyc - 2;
    end = *head;

    for (; x < len_cyc; x = x + 2)
    {
        if (start[x].b != end[len_list].b)
            return (0);

        len_list = len_list - 2;
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
	int y = 0;

	while (h != NULL)
	{
		++y;
		h = h->next;
	}

	return (y);
}
