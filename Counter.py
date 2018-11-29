#!/usr/bin/env python

from collections import defaultdict

lines = open('strings.csv').read().splitlines()

def identify_duplicates(phrase):
    word_count = defaultdict(lambda : 0)
    words = phrase.strip().split()
    for w in words:
        word_count[w] += 1
    return word_count

def annotate_duplicates(phrase):
    word_count = identify_duplicates(phrase)
    words = phrase.strip().split()
    response = []
    for w in words:
        count = word_count[w]
        word_count[w] -= 1
        response.append(f"{w}:{count}")

    return " ".join(response)

if __name__ == "__main__":
    for line in lines:
        print(annotate_duplicates(line))




