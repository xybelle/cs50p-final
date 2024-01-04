#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string argv[1]);
char rotate (char c, int k);

int main(int argc, string argv[])
{
    // Check number of command-line argument
    if ((argc <= 1 ) || (argc > 2))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if (argc == '1')
    {
        return 0;
    }

    // Check if argv[1] is a digit
    if (only_digits(argv))
    {
        // Convert argv[1] to int
        int k = atoi(argv[1]);

        string plaintext = get_string("Plaintext:  ");
        int i = strlen(plaintext);
        for (int j = 0; j < i; j++)
        {
            plaintext[j] = rotate (plaintext[j], k);
        }

        printf("Ciphertext: ");
        for (int j = 0; j < i; j++)
        {
            printf("%c", plaintext[j]);
        }
        printf("\n");

    }
    else

    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}

bool only_digits(string argv[1])
{
    int i = strlen(argv[1]);
    for (int j = 0; j < i; j++)
    {
        if (isdigit(argv[1][j]))
        {
            return true;
        }
    }
    return false;
}

char rotate (char c, int k)
{
    if (isupper(c))
    {
        c = ((int) c - 65) + (k + 65);
    }
    else if (islower(c))
    {
        c = ((int) c - 97) + (k + 97);
    }
    return (char) c;
}
