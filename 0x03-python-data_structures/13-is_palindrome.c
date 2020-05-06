#include "lists.h"

/**
 * reverse - reverse sigly linked list
 * @head: singly linked list
 * Return: void
 */
void reverse(listint_t **head)
{
	listint_t *current = *head, *next = NULL, *prev = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev = *head, *tmp = *head;

	if (!(*head) || !head)
		return (1);

	reverse(&rev);

	while (tmp->next != NULL)
	{
		if (rev->n != tmp->n)
			return (0);

		rev = rev->next;
		tmp = tmp->next;
	}

	return (1);
}
