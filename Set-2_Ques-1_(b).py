# (b) Control Flow and Functions (10 Marks)
# Define a function is_prime(n) that checks if a given number n is a prime number. The function
# should return True if n is prime, and False otherwise.
# Use this function to print all prime numbers between 2 and 100.

# Answer-2

def is_prime(n):
    a = list()

    a[0:n+1] = (n+1)*[1]

    i = 2
    while i*i <= n:
        print ("I: ", i)

        a[0:n+1:i] = len(a[0:n+1:i])*[0]

        if a[n] == 0:
            return False

        while a[i] == 0:
            i+=1

    if a[n] == 0:
        return False
    else:
        return True

for x in range(2, 101):
    print(x, '=', is_prime(x))