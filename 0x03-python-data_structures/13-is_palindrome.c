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
	listint_t *temp = NULL;
	int *top;
	int length = 0, i = 0, j = 0;

	if (head == NULL || *head == NULL)
		return (1);

	temp = *head;
	while (temp != NULL)
	{
		length++;
		if (temp->next == NULL)
			break;
		temp = temp->next;
	}
	length = length - 1;
	temp = *head;
	top = malloc(sizeof(*top) * length);
	for (i = 0; i <= length; i++)
	{
		top[i] = temp->n;
		temp = temp->next;
	}
	i = 0;
	j = length;
	while (i < j)
	{
		if (top[i] != top[j])
		{
			free(top);
			return (0);
		}
		i++;
		j--;
	}
	free(top);
	return (1);
}
