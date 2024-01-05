#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool all_alpha(string key);
bool all_unique(string key);
bool key_count(string key);
char ciphertext(char plaintext, char key[]);

int main(int argc, string argv[])
{
    // Check the number of command-line argument
    string key = argv[1];
    if ((argc <= 1) || (argc > 2))
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    if (key_count(key))
    {
        if (all_unique(key))
        {
            // Prompt user for plaintext
            string plaintext = get_string("plaintext:  ");

            int len = strlen(plaintext);

            // Call function to rotate each character
            for (int i = 0; i < len; i++)
            {
                plaintext[i] = ciphertext(plaintext[i], key);
            }
            printf("ciphertext: ");
            for (int i = 0; i < len; i++)
            {
                printf("%c", plaintext[i]);
            }
            printf("\n");
        }
        else
        {
            printf("Key has duplicates\n");
            return 1;
        }
    }
    else
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
}

// Check if key contains 26 characters
bool key_count(string key)
{
    int count = strlen(key);
    if (count != 26)
    {
        printf("Key must contain 26 characters.\n");
    }
    return count && all_alpha(key);
}

// Check if key contains anything but alphabet
bool all_alpha(string key)
{
    int digit = 0;
    for (int i = 0; i < 26; i++)
    {
        if (isdigit(key[i]))
        {
            digit++;
        }
    }
    if (digit >= 1)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    return 0;
}

// Check if each key is unique
bool all_unique(string key)
{
    for (int i = 0; i < 26; i++)
    {
        for (int j = i + 1; j < 26; j++)
        {
            if (key[i] == key[j])
            {
                return false;
            }
        }
    }
    return true;
}

// Ciphertext
char ciphertext(char plaintext, char key[])
{
    int ci = 0;
    char cipher = 0;
    if (isalpha(plaintext))
    {
        if (isupper(plaintext))
        {
            ci = plaintext - 65;
            cipher = key[ci];
            return cipher;
        }
        else if (islower(plaintext))
        {
            ci = plaintext - 97;
            cipher = key[ci];
            return cipher + 32;
        }
    }
    return plaintext;
}
