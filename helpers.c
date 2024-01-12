#include "helpers.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

float min(float *a, int *b);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop through all pixels
    float avergb;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Get average of r, g, b
            avergb = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0;

            // Update pixel values
            image[i][j].rgbtRed = round(avergb);
            image[i][j].rgbtGreen = round(avergb);
            image[i][j].rgbtBlue = round(avergb);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    float sepiaRed, sepiaGreen, sepiaBlue;
    int max = 255;
    // Loop through all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Get sepia values
            sepiaRed = (.393 * image[i][j].rgbtRed) + (.769 * image[i][j].rgbtGreen)
                 + (.189 * image[i][j].rgbtBlue);
            sepiaGreen = (.349 * image[i][j].rgbtRed) + (.686 * image[i][j].rgbtGreen)
                 + (.168 * image[i][j].rgbtBlue);
            sepiaBlue = (.272 * image[i][j].rgbtRed) + (.534 * image[i][j].rgbtGreen)
                 + (.131 * image[i][j].rgbtBlue);

            // Update pixel values
            image[i][j].rgbtRed = round(min(&sepiaRed, &max));
            image[i][j].rgbtGreen = round(min(&sepiaGreen, &max));
            image[i][j].rgbtBlue = round(min(&sepiaBlue, &max));
        }
    }
    return;
}

// Return which is lower
float min(float *a, int *b)
{
    return (*a < *b) ? *a : *b;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int h = height, w = width;
    RGBTRIPLE tmp;

    // Swap
    for (int i = 0; i < height; i++)
    {
        for (int j = 0, n = width/2; j < n; j++)
        {
            tmp = image[i][w];
            image[i][w] = image[i][j];
            image[i][j] = tmp;
            w--;
        }
        w = width;
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int counter = 0;

            // Edge and corner
            if (((i == 0 && j == 0) || ((i == height) && j == 0) || (i == 0 && (j == width)) || ((i == height) && (j == width))))
            {
                for (int x = -1; x < 2; x++)
                {
                    for (int y = -1; y < 2; y++)
                    {
                        copy[i][j].rgbtRed += copy[i + x][j + y].rgbtRed;
                        copy[i][j].rgbtGreen += copy[i + x][j + y].rgbtGreen;
                        copy[i][j].rgbtBlue += copy[i + x][j + y].rgbtBlue;
                        counter++;
                    }
                }
                image[i][j].rgbtRed = copy[i][j].rgbtRed / counter;
                image[i][j].rgbtGreen = copy[i][j].rgbtGreen / counter;
                image[i][j].rgbtBlue = copy[i][j].rgbtBlue / counter;

                break;
            }

            // Middle part
            if (((i > 1) && (i == (height - 1))) || ((j > 1) && (j == (width - 1))))
            {

                for (int x = -1; x < 2; x++)
                {
                    for (int y = -1; y < 2; y++)
                    {
                        copy[i][j].rgbtRed += copy[i + x][j + y].rgbtRed;
                        copy[i][j].rgbtGreen += copy[i + x][j + y].rgbtGreen;
                        copy[i][j].rgbtBlue += copy[i + x][j + y].rgbtBlue;
                        counter++;
                    }
                }
                image[i][j].rgbtRed = copy[i][j].rgbtRed / counter;
                image[i][j].rgbtGreen = copy[i][j].rgbtGreen / counter;
                image[i][j].rgbtBlue = copy[i][j].rgbtBlue / counter;

                break;
            }
        }
    }
    return;
}
