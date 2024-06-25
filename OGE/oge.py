def find_max_sum_pair_divisible_by_t(numbers, t):
    """
    Finds the pair of elements with maximum sum divisible by t in the given sequence.

    Args:
        numbers (list[int]): The sequence of positive integers.
        t (int): The divisor value.

    Returns:
        tuple[int, int]: The pair of elements with maximum sum divisible by t, or an empty tuple if no such pair exists.
    """

    max_sum, max_pair = 0, (-1, -1)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            current_sum = numbers[i] + numbers[j]
            if current_sum % t == 0 and current_sum > max_sum:
                max_sum = current_sum
                max_pair = (numbers[i], numbers[j])

    return max_pair


if __name__ == "__main__":
    # Read the input
    n = int(input())
    numbers = [int(input()) for _ in range(n)]

    # Find the maximum sum pair divisible by t = 107
    max_pair = find_max_sum_pair_divisible_by_t(numbers, 107)
    # Print the result
    if max_pair == (-1, -1):
        print("No pair with maximum sum divisible by 107 exists.")
    else:
        print(f"Maximum sum pair divisible by 107: {max_pair}")
