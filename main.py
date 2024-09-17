class ArmstrongChecker:
    def __init__(self, number):
        self.number = number  # Store the user input number
    
    def is_armstrong(self):
        # Convert the number to a string to get each digit
        digits = [int(digit) for digit in str(self.number)]
        power = len(digits)  # The power is the number of digits in the number
        
        # Calculate the sum of digits raised to the power
        armstrong_sum = sum([digit ** power for digit in digits])
        
        # Check if the sum equals the original number
        return armstrong_sum == self.number
    
    def display_result(self):
        if self.is_armstrong():
            print(f"{self.number} is an Armstrong number.")
        else:
            print(f"{self.number} is not an Armstrong number.")

# Example usage
if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        checker = ArmstrongChecker(number)
        checker.display_result()
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
