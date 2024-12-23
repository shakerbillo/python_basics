first_name = input('Enter your first name: ')
days = input('How many days before your birthday: ')
print(f'Hi {first_name}, only {days} days before your birthday!')


''' 
Ask the user how many days until their birthday
and print an approx number of weeks until their birthday 

week is = 7 days 

decimal within the return is allowed

'''
days = input('How many days until your birthday? ')
print(round(int(days)/7))