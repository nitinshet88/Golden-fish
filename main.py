# use of filter and map functions --------------------------------------------------------
a= [1,2,3,4,5,6,7,8,9,10]
odds = lambda  i: i%2 !=0
evens = lambda i: i%2==0

re = list(filter(evens,a))
ro=list(filter(odds,a))
# print(ro)
doubles = list(map(lambda i:i*2, a))
# print(doubles)

ce = [i*2 for i in a]
co = [i*10 for i in a if (i%2!=0)]
ce_co = [i if (i%2==0) else ("odd") for i in a]
# print(co)

# reversing the integer -------------------------------------------------------------
number = 123456
n=123456
rev =0
while n >0:
    rev = rev *10 +n%10
    n=n//10
# print(rev)

# To check the number is armstrong or not----------------------------------------
# num = 370
# n=num
# cube = 0
# while (n):
#     digit = n%10
#     cube += digit*digit*digit
#     n=n//10
# if cube==num:
#     print("armstrong")
# else:
#     print("not an armstrong")

# To check the number is prime or not--------------------------------------------

def is_prime (n):
    for i in range (2,n):
        if n%i == 0:
            print("non prime")
            break
    else:
        print("prime")

# is_prime(71)

# To check the range of number is prime or not--------------------------------------------
def primes (n):
    for i in range (1,n+1):
        for j in range (2, i):
            if i%j ==0:
                break
        else:
            print(i, end=" ,")
# primes(100)

#fibonassi series -----------------------------------------------------------------
# a=0
# b=5
# for i in range (0,11):
#     print(a, end=", ")
#     c=a+b
#     a,b=b,c

# count =0
# def fibonassi (a,b,d):
#     global count
#     while count <=d:
#         print(a, end=", ")
#         c=a+b
#         count +=1
#         fibonassi(b,c,d)
# fibonassi(0,5,10)

# To check palindrome or not using recursion ---------------------------------------
def is_pal (n):
    rev =0
    def pal(n):
        nonlocal rev
        if n >0:
            rev = rev *10 + n%10
            pal(n//10)
        return rev
    print(rev)
    a = pal(n)
    if a == n:
        print("yes it is palindrome")
    else:
        print("not a palindrome")
# is_pal(1233215)

# To check binary or not  ------------------------------------------------------------
def is_binary (n):
    def check_digits (n):
        while (n):
            if n%10==0 or n%10==1:
                pass
            else:
                return False
            n=n//10
        return True
    if check_digits(n) == True:
        print("yes binary")
    else:
        print("not binary")
# is_binary(110010201010)

# Wap to get sum of digits -----------------------------------------------------------

def sumOfDigits (n):
    sum =0
    while n:
        sum += n%10
        n= n//10
    return sum

# print(sumOfDigits(123456))

# Wap to get average of sequence -------------------------------------------------------

def average (l):
    sum = 0
    for i in l:
        sum += i
    avg = sum/len(l)
    return avg
m=[1,2,3,4,5,6,7,8,9,10]
# print(average(m))

# Pectorial of number----------------------------------------------------------------
def pactorial (m):
    if m==0:
        return 1
    return  m*(pactorial(m-1))
# print (pactorial(5))

# pact=1
# for i in range (1,7):
#     pact=pact*i
# print(pact)

# To find lcm of 2 numbers ---------------------------------------------------------
def LCM(l,m):
    if l>m:
        greater = l
    else:
        greater =m
    while True:
        if greater%l==0 and greater %m ==0:
            lcm = greater
            break
        greater+=1
    return lcm

# print(LCM(30,40))

# find HCF---------------------------------------------------------------------------
def HCF(n,m):
    if n<m:
        smaller = n
    else:
        smaller = m
    for i in  range (smaller+1,2,-1):
        if n%i==0 and m%i ==0:
            hcf =  i
            return hcf

# print(HCF(50,15))

# Leap year or not------------------------------------------------------------------
'''year =2022
if ((year % 400 ==0) or (year % 100 !=0) and (year %4==0)):
     print("leap year")
else:
     print("not")'''

#Move hash to forward--------------------------------------------------------------
'move#hash#to#front'

def nonHash (s):
    m = " "
    n= " "
    for i in s:
        if i== '#':
            n+=i
            m+=" "
        else:
            m+=i
    print(m+n)
# nonHash('move#hash#to#front')

# String operations to find the number of repeatation of charactors------------
# a='aaaabbbccccdddde'
# d = { }
# for i in a:
#     d[i]=0
# for j in a:
#     d[j]+=1
# print(d)
#
# s=" "
# for k,v in d.items():
#     s+= k
#     s+=str(v)
# print(s)

#  Generators ------------
# def produce ():
#     for i in range (1, 5):
#         yield i
#
# a = produce()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

#  word matching -------------------------------------------------------------------------
# a=['I5', 'ho2w', '4you', 'lo6ve', 'you8', 'a3re', 'hell0o']
# d = {}
# for i in a:
#     key = 0
#     value = " "
#     for j in i:
#         if j.isdigit():
#             key+=int(j)
#         else:
#             value+=j
#     d[key]=value
# print(d)
#
# l= sorted(d.items())
# str = " "
# for i in l:
#     str +=(i[1])
# print(str)

# Linear search -----------------------------------------------------
# def find(l,v):
#     position =0
#     def search(l,v):
#         for i in range (0, len(l)):
#             if l[i]==v:
#                 nonlocal position
#                 position = i
#                 return True
#         return False
#     if search(l,v):
#         print(f"found at {position}")
#     else:
#         print("not found go home")
#
# lis = [3,4,2,1,6,90,56]
# find(lis,90)

'''
# linear search using while loop -----------------------------------------
def find(l,v):
    position =0
    i=0
    def search(l,v):
        nonlocal position, i
        while i <= len(l):
            if l[i]==v:
                position = i
                return True
            i+=1
        return False
    if search(l,v):
        print(f"found at {position}")
    else:
        print("not found go home")

lis = [3,4,2,1,6,90,56]
find(lis,90)'''
'''logic for binary search is first the list should be sorted,
then we find the mid index of the list, the value in the mid index is matches 
it returns found, if it not matches mid index will become lower boundary,
 .............
'''

def binarySearch (lis, n):
    pos = 0
    def bsearch (list, n):
        lb=0
        ub = len(list)-1
        nonlocal pos
        while lb<=ub:
            mid = (lb+ub)//2
            if list[mid] ==n:
                pos = mid+1
                return True
            else:
                if list[mid] < n:
                    lb=mid+1
                else:
                    ub=mid-1
        return False
    if bsearch(lis,n):
        print(f"found at {pos}")
    else:
        print("not found go home")

lis = [2,3,5,6,7,14,25]
n= 7
# binarySearch(lis,n)

# Bubble sort --------------------------------------------------------
# def sort(nums):
#     for i in range (len(nums)-1,0,-1):
#         for j in range (i):
#             if nums[j]> nums [j+1]:
#                 temp = nums [j]
#                 nums [j] =nums[j+1]
#                 nums [j+1] =temp
#
#
# nums = [5, 3, 8, 6, 7, 2]
# sort(nums)
# print(nums)

#  Selection sort ---------------------------------

def selectionSort (nums):
    for i in range (len(nums)-1):
        minpos = i
        for j in range (i,(len(nums))):
            if nums [j] <nums [minpos]:
                minpos = j
        temp = nums [i]
        nums [i] = nums [minpos]
        nums [minpos] = temp
        print(nums)

nums = [5,13,8,6,7,2]
# selectionSort(nums)
# print (nums)
































