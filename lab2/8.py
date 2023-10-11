import random
import math
import time


def calculate_pi_leibniz(n_terms=1000000):
    start = time.time()
    pi = 0
    sign = 1
    for i in range(n_terms):
        term = 1 / (2 * i + 1) * sign
        pi += term
        sign *= -1
    pi *= 4
    end = time.time()
    print(f"Leibniz method time: {end - start} seconds")
    print(f"pi: {round(pi, 10)}")
    return round(pi, 10)


def calculate_pi_monte_carlo(n_trials=1000000):
    start = time.time()
    points_in_circle = 0
    total_points = 0
    for _ in range(n_trials):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x ** 2 + y ** 2
        if distance <= 1:
            points_in_circle += 1
        total_points += 1
    pi_estimate = 4 * points_in_circle / total_points
    end = time.time()
    print(f"Monte Carlo method time: {end - start} seconds")
    print(f"pi: {round(pi_estimate, 10)}")
    return round(pi_estimate, 10)


def calculate_pi_math():
    start = time.time()
    pi = round(math.pi, 10)
    end = time.time()
    print(f"Math module time: {end - start} seconds")
    print(f"pi: {pi}")
    return pi


calculate_pi_leibniz()
calculate_pi_monte_carlo()
calculate_pi_math()
