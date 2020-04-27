#include "lists.h"

/**
 * check_cycle - hat checks if a singly linked list has a cycle in it
 * @list: singly list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *tmp;
	int e = 0;

	current = list;
	tmp = list;
	while (current != NULL)
	{
		current = current->next;
		while (tmp != NULL)
		{
			if (current == tmp)
			{
				e++;
				if (e > 1)
					return (1);
			}

			tmp = tmp->next;
		}
		e = 0;
	}

	return (0);
}
