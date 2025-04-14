def main():
    # Prompt the user for temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert Fahrenheit to Celsius
    celcius = (fahrenheit- 32) * 5.0/9.0
    
    # Print the result
    print(f"Temperature: {fahrenheit}F = {celcius}C")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()