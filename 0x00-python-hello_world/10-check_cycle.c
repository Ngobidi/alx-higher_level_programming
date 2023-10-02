#include "lists.h"

/**
 * check_cycle - validates whelter a singly linked_list contained a circle
 * @list: linked_list
 * Return: a int value 1 on sucessfull, else 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *abc = list;
	listint_t *cba = list;

	while (abc && cba && abc->next)
	{
		cba = cba->next;
		abc = abc->next->next;
		if (cba == abc)
			return (1);
	}
	return (0);
}
