#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to the pointer of the first node
 * @number: The number to insert
 *
 * Return: Address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;

	/* Create the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	/* If list is empty or num < head, insert at start */
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	/* Find the right spot in the list */
	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
	/* Insert the new node */
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
