#include "lists.h"
#include <stdlib.h>

/**
 * isPalindrome - checks if a singly linked lis    t is a palindrome.
 * @start: pointer to pointer to head of list.
 * @end:  pointer to head of list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindr    ome.
 */
int isPalindrome(listint_t **start, listint_t *end)
{
	int r;
	int r1;

	if (end == NULL)
		return (1);
	r = isPalindrome(start, end->next);
	if (r == 0)
		return (0);
	if (end->n == (*start)->n)
		r1 = 1;
	else
		r1 = 0;
	*start = (*start)->next;
	return (r1);
}

/**
 * is_palindrome -  a function checks if a singly linked list is a palindrome.
 * @head: pointer to pointer to head of list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	return (isPalindrome(head, *head));
}
