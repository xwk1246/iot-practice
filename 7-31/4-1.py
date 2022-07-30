secret = 7
guess = int(input())
if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")
