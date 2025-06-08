#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle
 * @list: Pointer to the head of the list
 *
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;	/* Slow pointer */
	listint_t *hare = list;		/* Fast pointer */

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;	/* Move one step */
		hare = hare->next->next;	/* Move two steps */
		if (tortoise == hare)
			return (1);
	}
	return (0);	/* No cycle */
}
