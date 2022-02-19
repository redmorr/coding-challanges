import pytest

import factorial
import fibonacci

testdata = [(1, 1),
            (2, 2),
            (3, 3),
            (4, 5),
            (5, 8),
            (6, 13),
            (10, 89),
            (20, 10946),
            (30, 1346269),
            (45, 1836311903),
            (500, 225591516161936330872512695036072072046011324913758190588638866418474627738686883405015987052796968498626)]


@pytest.mark.parametrize('n_of_stairs, expected', testdata)
@pytest.mark.parametrize('solution_class', [factorial.Solution, fibonacci.Solution], ids=["Factorial", "Fibonacci"])
def test_climbing_stairs(solution_class, expected, n_of_stairs):
    assert expected == solution_class().climbStairs(n_of_stairs)
