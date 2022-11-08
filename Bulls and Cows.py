'''You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.'''

class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        bulls = 0
        cows = 0
        secret_dict = {}

        guess_dict = {}

        for i in range(len(secret)):

            if secret[i] not in secret_dict.keys():
                secret_dict[secret[i]] = set([i])
            else:
                secret_dict[secret[i]].add(i)
        
        for i in range(len(guess)):

            if guess[i] not in guess_dict.keys():
                guess_dict[guess[i]] = set([i])
            else:
                guess_dict[guess[i]].add(i)

        for key in secret_dict.keys():

            if key not in guess_dict.keys():
                continue

            secret_indices = secret_dict[key]
            guess_indices = guess_dict[key]

            bull_indices = secret_indices & guess_indices
            bulls += len(bull_indices)

            secret_indices = secret_indices - bull_indices
            guess_indices = guess_indices - bull_indices

            cows += min(len(secret_indices), len(guess_indices))


        return str(bulls) + 'A' + str(cows) + 'B'

        

