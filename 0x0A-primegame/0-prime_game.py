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


def generate_primes(limit):
    """generate_primes function
    """
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes


def count_primes(primes, n):
    """count_primes function
    """
    return sum(primes[:n + 1])


def isWinner(x, nums):
    """isWinner function
    """
    if x < 1 or not nums:
        return None

    maria_wins, ben_wins = 0, 0
    max_num = max(nums)
    primes = generate_primes(max_num)

    for _, current_num in zip(range(x), nums):
        prime_count = count_primes(primes, current_num)
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins == ben_wins:
        return None

    return 'Maria' if maria_wins > ben_wins else 'Ben'
