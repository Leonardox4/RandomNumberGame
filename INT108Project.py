import random
def check_properties(num):
  # Check if the number is odd or even
  if num % 2 == 0:
    print(f"{num} is an even number.")
  else:
    print(f"{num} is an odd number.")

  # Check if the number is positive or negative
  if num >= 0:
    print(f"{num} is a positive number.")
  else:
    print(f"{num} is a negative number.")

  # Check if the number is prime or composite
  if num > 1:
    for i in range(2, num):
      if num % i == 0:
        print(f"{num} is a composite number.")
        break
    else:
      print(f"{num} is a prime number.")
  else:
    print(f"{num} is not a prime number.")

# Get the range from the user
range_start = int(input("Enter the start of the range: "))
range_end = int(input("Enter the end of the range: "))

# Pick a random number from the range
random_num = random.randint(range_start, range_end)

# Check the properties of the random number
print(f"Checking the properties of the randomly picked number: {random_num}")
check_properties(random_num)

m=input("Click anything to exit")
