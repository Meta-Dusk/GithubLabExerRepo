def mean(numbers):
    """Return the mean (average) of a list of numbers."""
    if not numbers:
        raise ValueError("The list is empty.")
    return sum(numbers) / len(numbers)

def median(numbers):
    """Return the median (middle value) of a list of numbers."""
    if not numbers:
        raise ValueError("The list is empty.")

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2

    if n % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]

def mode(numbers):
    """Return the mode (most frequent value) of a list of numbers."""
    if not numbers:
        raise ValueError("The list is empty.")

    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]

    if len(modes) == 1:
        return modes[0]
    else:
        return modes  # return list if there are multiple modes

# Get user input
if __name__ == "__main__":
    try:
        input_str = input("Enter numbers separated by spaces: ")
        numbers = list(map(float, input_str.strip().split()))

        print("Mean:", mean(numbers))
        print("Median:", median(numbers))
        print("Mode:", mode(numbers))

    except ValueError as e:
        print("Error:", e)
