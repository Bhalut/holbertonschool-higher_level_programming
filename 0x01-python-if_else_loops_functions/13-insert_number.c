#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: singly linked list
 * @number: number content list
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *tmp = malloc(sizeof(listint_t));

	if (head == NULL || tmp == NULL)
		return (NULL);

	current = *head;
	while (current->next->n < number ||
	       current->next == NULL)
	{
		current = current->next;
	}

	tmp->n = number;
	tmp->next = current->next;
	current->next = tmp;

	return (tmp);
}
