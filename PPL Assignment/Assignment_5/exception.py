#ASSIGNMENT NO 5 ON EXCEPTIONS

try:
    fh = open("testfile", "r")
    fh.write("This is my testfile!")
except IOError:
    print("Not able to write data in the file!")
else:
    print("Content written")
finally:
    print("File closed!")
    fh.close()
	
i = input("Enter 1st number : ")
j = input("Enter 2nd number : ")
try:
    k = int(i) / int(j)
    print(k)
    print("inside try block before m")
    m = int(i) / int(j)
    print("Division : ")
    print(m)
    print("inside try block after m")
except(ZeroDivisionError):
    print("divisor 0")
except:
    print("except")
finally:
    print("Inside finally ")

print("guess the number")
class Error(Exception):
   pass

class ValueTooSmallError(Error):
   
   pass

class ValueTooLargeError(Error):
   
   pass


number = 22

while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This is small")
       print()
   except ValueTooLargeError:
       print("This is large")
       print()

print("Correct!")