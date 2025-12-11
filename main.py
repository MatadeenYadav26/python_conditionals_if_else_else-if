age = int(input('Enter Your Age: '))

if age >= 18 :
    print('You are eligible to vote')
else:
    print('Un-eligible to vote')

#ternary operators

print("Vote") if age >= 18 else print("cannot vote!")
