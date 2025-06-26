#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - cheks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, otherwise 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;	/* Pointer to travese the list */
	int *values;		/* Array to store the values */
	int len = 0, i = 0;
	int start, end;

	if (head == NULL || *head == NULL)
		return (1);
	/* Count the number of nodes */
	current = *head;
	while (current != NULL)
	{
		len++;
		current = current->next;
	}
	/* Allocate memory for the array */
	values = malloc(sizeof(int) * len);
	if (values == NULL)
		return (0);
	/* Fill the array with list values */
	current = *head;
	while (current != NULL)
	{
		values[i] = current->n;
		i++;
		current = current->next;
	}
	/* Check if the array is a palindrome */
	for (start = 0, end = len - 1; start < end; start++, end--)
	{
		if (values[start] != values[end])
		{
			free(values);
			return (0);
		}
	}
	/* Clean up and return */
	free(values);
	return (1);
}
