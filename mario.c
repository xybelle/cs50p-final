#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int size, i, j, k, l;

    do
    {
        size = get_int("Height: ");
    }
    while (size < 1 || size > 8);

    for (i = 1; i <= size; i++)
    {
        for (j = i; j < size; j++)
        {
            printf(" ");
        }

        for (k = 1; k <= i; k++)
        {
            printf("#");
        }

        printf("  ");

        for (l = 1; l <= i; l++)
        {
            printf("#");
        }

        printf("\n");
    }

}
