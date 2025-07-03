from stats import mean, median, mode

# Example usage of the stats functions
def main():
    # Sample lists of numbers
    numbers1 = [1, 2, 3, 4, 5]
    numbers2 = [1, 2, 2, 3, 4, 4, 4]
    numbers3 = []
    
    # Using mean function
    print("Mean of numbers1:", mean(numbers1))  # Expected: 3.0
    print("Mean of numbers2:", mean(numbers2))  # Expected: 2.7142857142857144
    print("Mean of empty list:", mean(numbers3))  # Expected: 0
    
    # Using median function
    print("Median of numbers1:", median(numbers1))  # Expected: 3
    print("Median of numbers2:", median(numbers2))  # Expected: 3
    print("Median of empty list:", median(numbers3))  # Expected: 0
    
    # Using mode function
    print("Mode of numbers1:", mode(numbers1))  # Expected: 1 (first number if all appear once)
    print("Mode of numbers2:", mode(numbers2))  # Expected: 4
    print("Mode of empty list:", mode(numbers3))  # Expected: 0

if __name__ == "__main__":
    main()