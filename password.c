// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);
bool lower(string password);
bool upper(string password);
bool digit(string password);
bool symbol(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below

bool valid(string password)
{
    int i = strlen(password);
    bool lower = false;
    bool upper = false;
    bool digit = false;
    bool symbol = false;

    for (int j = 0; j < i; j++)
    {
        if (islower(password[j]))
        {
            lower = true;
            break;
        }

    }
    for (int j = 0; j < i; j++)
    {
        if (isupper(password[j]))
        {
            upper = true;
            break;
        }
    }
    for (int j = 0; j < i; j++)
    {
        if (isdigit(password[j]))
        {
            digit = true;
            break;
        }
    }
    for (int j = 0; j < i; j++)
    {
        if ((password[j] > 32 && password[j] < 48) || (password[j] > 57 && password[j] < 65) || (password[j] > 90 && password[j] < 97) || (password[j] > 122 && password[j] < 127))
        {
            symbol = true;
            break;
        }
    }

    if ((lower == true) && (upper == true) && (digit == true) && (symbol == true))
    {
        return true;
    }
    else
    {
        return false;
    }
}
