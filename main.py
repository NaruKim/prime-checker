def prime_checker(number):
  i=2
  while i<number:
    if number%i==0:
      print ("It's not a prime number")
      return False
    i+=1
  print ("It's a prime number")
  return True


n = int(input("Check this number: "))
prime_checker(number=n)



