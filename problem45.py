"""
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	T=n(n+1)/2	 	1, 3, 6, 10, 15,
Pentagonal	 	P=n(3n-1)/2	 	1, 5, 12, 22, 35,
Hexagonal       H=n(2n-1)	 	1, 6, 15, 28, 45,
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""
def isPentagonal(number, target):
    pentList = []
    while (number*(3*number-1)/2) >= target:
        pentList.append((number*(3*number-1)/2))
        number -= 1
    if target in pentList:
        return True
    else: return False
    
def isHexagonal(number, target):
    hexList = []
    while (number*(2*number-1)) >= target:
        hexList.append((number*(2*number-1)))
        number -= 1
    if target in hexList:
        return True
    else: return False
    
startval = 51000
while True:
    triangle = startval*(startval+1)/2
    print startval, triangle
    if isPentagonal(startval, triangle) and isHexagonal(startval, triangle):
        print triangle
        break
    startval += 1
    
# this code is fairly slow, but it works - answer is 1533776805
# this is n = 55385 for the triangle