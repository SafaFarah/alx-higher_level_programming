#include "lists.h"

/**
 * insert_node -  a function inserts a number into a sorted singly linked list.
 * @number: inserted number.
 * @head: pointer to pointer to head of list.
 *
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr;
	listint_t *temp;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	ptr = *head;
	temp->n = number;
	temp->next = NULL;
	while (ptr->next != NULL)
	{
		if (temp->n < ptr->next->n)
		{
			temp->next = ptr->next;
			ptr->next = temp;
			return (temp);
		}
		ptr = ptr->next;
	}
	return (NULL);
}
