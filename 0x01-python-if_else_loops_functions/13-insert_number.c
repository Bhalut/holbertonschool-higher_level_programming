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
	listint_t *current = *head, *tmp;
	
	tmp = malloc(sizeof(listint_t));
	if (tmp == NULL)
		return (NULL);

	tmp->n = number;
	if (*head == NULL || current->n >= number)
	{
		tmp->next = current;
		*head = tmp;
		return (tmp);
	}

	while (current->next->n <= number && current->next)
		current = current->next;

	tmp->next = current->next;
	current->next = tmp;

	return (tmp);
}
