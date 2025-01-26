def fibonacci_gen():
    """This function generates a fibonacci series..."""
    try:
        count = int(input("\tHow many Fibonacci numbers do you want to generate: "))
        if count <= 0:
            print("Invalid Input! Please enter a positive number.")
            return
        
        series = [0, 1]
        while len(series) < count:
            next_term = series[-1] + series[-2]
            series.append(next_term)
        
        # Trim series for cases where count is 1
        series = series[:count]
        print(f"\tGenerated Fibonacci series ({count} numbers): {series}")
    except ValueError:
        print("Invalid input! Please enter an integer.")

def main():
    while True:
        print("\n\t\t---- FIBONACCI GENERATOR ----")
        print("\tThis app generates Fibonacci numbers as directed by the user.")
        start = input("\tPress Enter to start the app or type 'exit' to quit: ").strip().lower()
        if start == 'exit':
            print("\t\t\tEXITED!!")
            break
        fibonacci_gen()

if __name__ == "__main__":
    main()