#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks for a loop in a linked list
 * @list: a ptr to the list head
 * Return: 0 with no loop, 1 with a loop
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (fast != NULL)
	{
		fast = fast->next;
		if (fast->next == NULL)
			return (0);
		slow = slow->next;
		fast = fast->next;
		if (fast == slow)
			return (1);
		i++;
	}
	return (0);
}
