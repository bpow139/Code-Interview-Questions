"""
Maybe investigate idea of using far most right car as the "end" 
of the road to toss out extra computation looping.

Also could be cool to visualize this!!!
"""
import time


def widestGap(s, f, n):

    # start = time.perf_counter()
    b = []
    for j in range(0, len(s)):
        for i in range(s[j] + 1, f[j]):
            b.append(i)

    car_space = s + f + b

    count = 0
    gap = [0]

    for k in range(1, n + 1):
        if k in car_space:
            if count == 0:
                pass
            else:
                gap.append(count)
                count = 0
        else:
            count += 1

    """ gap.append(count) this will add in
        all empty spaces not being used. 

        e.g. cars end at 10 but roads goes to 100

        ans is 90

    """
    max_gap = max(gap)

    print(f"The largest gap between vehicles is {max_gap}")


if __name__ == "__main__":

    start = time.perf_counter()
    s = [1, 3, 4, 9]
    f = [3, 7, 6, 15]
    n = 20
    widestGap(s, f, n)
    end = time.perf_counter()
    print(f"Compute Time: {end-start}")
