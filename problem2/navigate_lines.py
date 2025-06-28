def read_file_lines(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            # Remove trailing newlines and return the list
            return [line.rstrip('\n') for line in lines]
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def main():
    # Prompt user for filepath
    filepath = input("Enter the filepath: ")
    lines = read_file_lines(filepath)
    
    # Check if the file was read successfully
    if not lines:
        print("No lines to display.")
        return
    
    # Main loop for navigation
    while True:
        print(f"\nThe file has {len(lines)} lines.")
        try:
            line_number = int(input("Enter a line number (1 to {} or 0 to quit): ".format(len(lines))))
            
            # Check for exit condition
            if line_number == 0:
                print("Exiting program.")
                break
            
            # Validate line number
            if 1 <= line_number <= len(lines):
                print(f"Line {line_number}: {lines[line_number - 1]}")
            else:
                print(f"Invalid line number. Please enter a number between 1 and {len(lines)} or 0 to quit.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()