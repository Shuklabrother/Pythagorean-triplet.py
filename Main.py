a = int(input("Write bigger number:\n"))
b = int(input("Write first remaining number:\n"))
c = int(input("Write Second remaining number:\n"))
A = a*a
B = b*b
C = c*c
D = B+C
E = {a, b, c}

if A==D:
  print("This is Pythagorean triplets", E)

else:
  print("This is not Pythagorean triplets", E)