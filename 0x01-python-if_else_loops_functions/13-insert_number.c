#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserts a new node into an ordered linked list
 * @head: ptr to a ptr of the head node
 * @number: the value to be placed into the new node
 * Return: the address of the new node or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *newnode, *oldnode = NULL;

	if (head == NULL)
		return (NULL);

	newnode = malloc(sizeof(*newnode));
	if (newnode == NULL)
		return (NULL);

	newnode->n = number;
	newnode->next = NULL;
	if (*head == NULL)
	{
		*head = newnode;
		return (newnode);
	}

	current = *head;
	while (current != NULL)
	{
		if (number < current->n)
		{
			if (oldnode == NULL)
			{
				*head = newnode;
				newnode->next = current;
				return (newnode);
			}
			else
			{
				oldnode->next = newnode;
				newnode->next = current;
				return (newnode);
			}
		}
		oldnode = current;
		current = current->next;
	}
	oldnode->next = newnode;
	return (newnode);
}
