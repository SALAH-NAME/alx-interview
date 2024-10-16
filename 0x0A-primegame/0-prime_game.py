#!/usr/bin/python3
""" 0-prime_game.py """


def is_prime(n):
    """is_prime function
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def calculate_winner(n):
    """calculate_winner function
    """
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    maria_wins = 0
    ben_wins = 0
    for i in range(len(primes)):
        if i % 2 == 0:
            maria_wins += 1
        else:
            ben_wins += 1
    return maria_wins, ben_wins


def isWinner(x, nums):
    """isWinner function
    """
    maria_total = 0
    ben_total = 0
    for n in nums:
        maria_wins, ben_wins = calculate_winner(n)
        if maria_wins > ben_wins:
            maria_total += 1
        else:
            ben_total += 1
    if maria_total > ben_total:
        return "Maria"
    elif ben_total > maria_total:
        return "Ben"
    else:
        return None
