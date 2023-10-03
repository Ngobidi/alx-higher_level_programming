#include "lists.h"

/**
 * insert_node - adds a new_nodes
 * @head: head of a node_list.
 * @num: index lists to add new_node
 *
 * Return: new_node address on successful, else Null
 */
listint_t *insert_node(listint_t **head, int num)
{
	listint_t *new;
	listint_t *h;
	listint_t *h_prev;

	h = *head;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > num)
			break;
		h_prev = h;
		h = h->next;
	}

	new->n = num;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = h;
		if (h == *head)
			*head = new;
		else
			h_prev->next = new;
	}

	return (new);
}
