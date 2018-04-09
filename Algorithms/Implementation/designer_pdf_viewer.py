#!/bin/python3

import sys

def designerPdfViewer(h, word):
    # Complete this function
    height_dict = {}
    for i in range(97, 123):
        height_dict[chr(i)] = h[i- 97]
    width, height = len(word), 0
    for char in word:
        char_height = height_dict[char]
        if char_height > height:
            height = char_height
    return width * height

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)

