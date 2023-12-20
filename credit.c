#include <cs50.h>
#include <stdio.h>

bool cardlengthcheck(long card);
int findlength(long card);
bool checksum(long card);
void firsttwo(long card);

int main()
{
    // Prompt for input
    long card;
    do
    {
        card = get_long("Number: ");
    }
    while (card <= 0);

    if (cardlengthcheck(card))
    {
        firsttwo(card);
    }
    else
    {
        printf("INVALID\n");
    }
}

bool cardlengthcheck(long card)
{
    int length = findlength(card);
    return ((length == 13 || length == 15 || length == 16) && checksum(card));
}

int findlength(long card)
{
    int count = 0;
    while (card != 0)
    {
        card = card / 10;
        count++;
    }
    return count;
}

bool checksum(long card)
{
    int sum = 0;
    long temp = card;

    while (temp > 0)
    {
        int last = temp % 10;
        sum = sum + last;
        temp = temp / 100;
    }

    temp = card / 10;
    while (temp > 0)
    {
        int seclast = (temp % 10);
        int multemp = seclast * 2;
        sum = sum + (multemp % 10) + (multemp / 10);
        temp = temp / 100;
    }
    return (sum % 10) == 0;
}

void firsttwo(long card)
{
    if ((card >= 34e13 && card < 35e13) || (card >= 37e13 && card < 38e13))
    {
        printf("AMEX\n");
    }
    else if ((card >= 51e14 && card < 56e14))
    {
        printf("MasterCard\n");
    }
    else if (card >= 4e12 || card >= 4e15)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
