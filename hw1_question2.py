def pali_check(num,dig_num):
    """
   Get a number and number of digits. 
   Return if the last number of digit of this number is a palindrome.

   """
    div_num =  10**dig_num
    first_digits = (num // div_num) * div_num 
    num = num - first_digits
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    
    hezka = 10**(dig_num-1)
    s_con = temp//hezka
    if(temp==rev) and (s_con>0 or temp==0):
        return True
    else:
        return False

def pali_check_middle(num,dig_num):
    """
   Get a number and number of digits. 
   Return if the middle number of digit of this number is a palindrome.

   """
    div_num1 =  10**(dig_num+1)
    div_num2 = 10
    first_digits = (num // div_num1) * div_num1
    num = (num - first_digits)//10
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    hezka = 10**(dig_num-1)
    s_con = temp//hezka
    if(temp==rev) and (s_con>0 or temp==0):
        return True
    else:
        return False

def check_palindrome():
   """
   Runs through all 6-digit numbers and checks the mentioned conditions.
   The function prints out the numbers that satisfy this condition.

   Note: It should print out the first number (with a palindrome in its last 4 digits),
   not all 4 "versions" of it.
   """
   for num in range(100000, 1000000):
        if pali_check(num,4) and pali_check(num+1,5) and pali_check_middle(num+2,4) and pali_check(num+3,6):
            print(num)
            
    
#check_palindrome()

if __name__ == '__main__':
    # Question 2
    return_value = check_palindrome()

    print(f"Question 2 solution: {return_value}")