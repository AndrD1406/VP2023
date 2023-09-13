while True:
    try:    
        a, b, c = map(int, input("Enter the values split:").split())

        while 1 > a or a > 106 or 1 > b or b > 106 or 1 > c or c > 106 or not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int) :
            print('''Wrong value!
        All the values must be in the range between 1 and 106 inclusively!
        (Which naturally means they need to be integers)''')
            program_continue = str(input('''If you want to quit press "-"
        if you want to continue press anything else:'''));
            if program_continue != "-":
                a, b, c = map(int, input("Enter the values split:").split())
            else:
                break;   
        else:
            def calculate_sum(x, y, z):
                return x + y + z
            orders = [(a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)]
            results = [calculate_sum(x, y, z) for x, y, z in orders]
    
            if len(set(results)) > 1:
                print("YES")  
            else:
                print("NO DIFFENCE BETWEEN THE RESULTS")
    except:
        print("You should have put 3 numbers, first two followed by an indentation!")
    while True:
        choice = input('Do you want to continue (+/-)? ').strip().lower()
        if choice in ('+', '-'):
            break
        else:
            print('Please enter a valid response ("+" or "-").')

    if choice == '-':
        break