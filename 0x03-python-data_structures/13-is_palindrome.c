#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks for whether a linked list is a palindrome
 * @head: a ptr to the head node
 * Return: 1 if yes, 0 if no
 */

int is_palindrome(listint_t **head)
{
	listint_t *tail = NULL, *temp = NULL, *top = NULL;
	int length = 0, i = 0, j = 0, k = 0;

	if (head == NULL || *head == NULL)
		return (1);

	tail = *head;
	top = *head;
	while (tail != NULL)
	{
		length++;
		if (tail->next == NULL)
			break;
		tail = tail->next;
	}
	length = length - 1;
	i = 0;
	j = length - i;
	while (i <= j)
	{
		if (tail->n != top->n)
			return (0);
		k = i;
		j--;
		temp = top;
		while (k < j)
		{
			temp = temp->next;
			k++;
		}
		tail = temp;
		top = top->next;
		i++;
	}
	return (1);
}
