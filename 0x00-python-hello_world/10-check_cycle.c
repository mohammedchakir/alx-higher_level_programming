#include "lists.h"

/**
 *  check_cycle - checks for a loop
 *  @list: list to be checked
 *  Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *fst = list;
	listint_t *scd = list;

	if (list == NULL)
		return (0);
	while (scd != NULL && scd->next != NULL && fst != NULL)
	{
		fst = fst->next;
		scd = scd->next->next;

		if (fst == scd)
			return (1);
	}
	return (0);
}
