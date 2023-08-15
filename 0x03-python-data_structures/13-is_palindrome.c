#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome -  a function checks if a singly linked list is a palindrome.
 * @head: pointer to pointer to head of list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *start;
	listint_t *end;
	listint_t *temp_e;

	if (*head == NULL)
		return (1);
	end = *head;
	start = *head;
	while (end->next != NULL)
	{
		end = end->next;
	}
	while (start->next != end)
	{
		if (end->n == start->n)
		{
			temp_e = end;
			end = start->next;
			while (end->next != temp_e)
			{
				end = end->next;
			}
			start = start->next;
		}
		if (end->n != start->n)
			return (0);
	}
	return (1);
}
