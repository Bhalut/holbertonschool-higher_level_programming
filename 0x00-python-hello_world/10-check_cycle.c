#include "lists.h"

/**
 * check_cycle - hat checks if a singly linked list has a cycle in it
 * @list: singly list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	int i = 0;

	current = list;

	if (current == NULL)
		return (i);

	while (current != NULL)
	{
		current = current->next;
		if (current == list)
		{
			i = 1;
			break;
		}
	}

	return (i);
}
