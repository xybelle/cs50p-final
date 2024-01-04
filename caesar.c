#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string argv[1]);
char rotate(char c, int k);

int main(int argc, string argv[])
{
    // Check number of command-line argument
    if ((argc <= 1) || (argc > 2))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if (only_digits(argv))
    {
        // Convert argv[1] to int
        int k = atoi(argv[1]);

        // Prompt user for plaintext
        string plaintext = get_string("Plaintext:  ");
        int i = strlen(plaintext);

        // Call function to rotate each character
        for (int j = 0; j < i; j++)
        {
            plaintext[j] = rotate(plaintext[j], k);
        }

        // Print ciphertext
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

// Check if argv[1] is a digit
bool only_digits(string argv[1])
{
    int i = strlen(argv[1]);
    int c = 0;
    for (int j = 0; j < i; j++)
    {
        if (isdigit(argv[1][j]))
        {
            c++;
        }
    }
    if (c == i)
    {
        return true;
    }
    return false;
}

// Rotate character if it's a letter
char rotate(char c, int k)
{
    if (isalpha(c))
    {
        int ci = 0;
        if (isupper(c))
        {
            ci = c - 65;
            c = (ci + k) % 26;
            return c + 65;
        }
        else if (islower(c))
        {
            ci = c - 97;
            c = (ci + k) % 26;
            return c + 97;
        }
    }
    return c;
}
