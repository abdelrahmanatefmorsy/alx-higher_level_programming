#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t* list)
{
	listint_t* str, * nxt;

	if (list == NULL || list->next == NULL)
		return (0);

	str = list->next;
	nxt = list->next->next;

	while (str && nxt && nxt->next)
	{
		if (str == nxt)
			return (1);

		str = str->next;
		nxt = nxt->next->next;
	}

	return (0);
}
