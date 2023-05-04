from solution import Solution
import random


def main():
    s = Solution()
    arr = [random.randint(1, 10000000) for _ in range(10000000)]

    answer = s.naive_approach(nums=arr)
    print(answer)

    answer2 = s.better_approach(nums=arr)
    print(answer2)


if __name__ == "__main__":
    main()
