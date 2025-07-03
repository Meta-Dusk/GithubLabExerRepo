def main():
    
    filename = input("Enter the filename: ")

    try:
        
        with open(filename, 'r') as file:
            lines = file.readlines()

        
        lines = [line.rstrip('\n') for line in lines]

       
        while True:
            print(f"\nThe file has {len(lines)} lines.")
            try:
                line_number = int(input("Enter a line number (0 to quit): "))
                if line_number == 0:
                    print("Exiting program.")
                    break
                elif 1 <= line_number <= len(lines):
                    print(f"Line {line_number}: {lines[line_number - 1]}")
                else:
                    print("Invalid line number. Try again.")
            except ValueError:
                print("Please enter a valid integer.")

    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

if __name__ == "__main__":
    main()
