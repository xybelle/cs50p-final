#include <cs50.h>
#include <stdio.h>

int get_size(void);
void print_pyramid(int size);

int main(void)
{
    // get height of pyramid
    int n = get_size();

    // print pyramid
    print_pyramid(n);
}

int get_size(void)
{
    int n;
    do
    {
        n = get_int("Height (1 - 8): ");
    }
    while (n < 1 || n > 8);
    return n;
}

void print_pyramid(int size)
{
    for (int i = 1; i <= size; i++)
    {
        for (int j = i; j < size; j++)
        {
            printf(" ");
        }

        for (int k = 1; k <= i; k++)
        {
            printf("#");
        }

        printf("\n");
    }
}
