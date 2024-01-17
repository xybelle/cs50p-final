#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check if single command-line is entered
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open memory card
    FILE *card = fopen(argv[1], "rb");
    if (card == NULL)
    {
        printf("Could not open input file\n");
        return 2;
    }

    const int BLOCK_SIZE = 512;
    uint8_t buffer[BLOCK_SIZE];
    int counter = 0;
    char filename[8];

    FILE *img = NULL; // Initialize to NULL

    bool firstjpg = false;
    bool newjpg = true;

    // Read from memory card while there is still data left
    while (fread(buffer, 1, BLOCK_SIZE, card) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (!firstjpg)
            {
                firstjpg = true;
                sprintf(filename, "%03i.jpg", counter);
                counter++;

                img = fopen(filename, "wb");
                if (img == NULL)
                {
                    printf("Could not create image file\n");
                    fclose(card);
                    return 6;
                }

                fwrite(buffer, 1, BLOCK_SIZE, img);
            }
            else
            {
                if (img != NULL)
                {
                    fclose(img);
                }
                sprintf(filename, "%03i.jpg", counter);
                counter++;

                img = fopen(filename, "wb");
                if (img == NULL)
                {
                    printf("Could not create image file\n");
                    fclose(card);
                    return 6;
                }
                fwrite(buffer, 1, BLOCK_SIZE, img);
            }
        }
        else
        {
            if (img != NULL && counter >= 1)
            {
                fwrite(buffer, 1, BLOCK_SIZE, img);
            }
        }
    }

    if (img != NULL)
    {
        fclose(img);
    }
    fclose(card);
    return 0;
}
