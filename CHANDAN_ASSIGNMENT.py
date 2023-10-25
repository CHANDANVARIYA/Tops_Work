s="WELCOME TO CHANDAN VARIYA ASSIGNMENT PROJECT"
print(s.center(66,"*"))
print("Note:-")
print("All the Quetions And Answers of Assignment are in this Project")
print("Ask Any Quations Between")
print("Modual No.: 2 in 23 Quations")
print("Modual No.: 3 in 28 Quations")

a=int(input("ENTER MODUAL NO. :"))
b=int(input("ENTER QUE. NO. :"))

if a==2:
    if b==1:
        print("question:- Write a Python program to check if a number is positive, negative or zero.")
        print("Answer:-")
        a=int(input("Enter No. :"))
        if a>0:
            print(a,"Is Positive Number")
        elif a==0:
            print(a,"Is Zero")
        else:
            print(a,"Is Nagative Number")
                
    elif b==2:
        print("question:-  Write a Python program to get the Factorial number of given number.")
        print("Answer:-")
        n=int(input("Enter NO.:"))
        fact=1
        for i in range (1,n+1):
            fact=fact*i
        print(fact)
    elif b==3:
        print("question:- Write a Python program to get the Fibonacci series of given range.")
        print("Answer:-")
        n=int(input("Enter No.:"))
        a,b=0,1
        print(a,end=" ")
        while b<n:
            print (b,end=" ")
            a,b=b,a+b
    elif b==4:
        print("question:- How memory is managed in Python?")
        print("Answer:-")
        print("Memory management in Python is primarily managed by the Python Memory Manager, which includes several components responsible for various aspects of memory allocation and deallocation. Python's memory management is built on top of the memory management provided by the underlying operating system, but it adds a layer of abstraction to simplify memory management for the Python developer. Here are some key aspects of memory management in Python:")
        print("1. Automatic Memory Allocation")
        print("2. Reference Counting")
        print("3. Cycle Detector")
        print("4. Dynamic Typing")
        print("5. Memory Pools")
        print("6. GC Module")
        print("7. Memory Profiling and Optimization")
        print("8. Memory Efficiency")
    elif b==5:
        print("question:-  What is the purpose continue statement in python?")
        print("Answer:-")
        print("The continue statement in Python returns the control to the beginning of the while loop. The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.")
    elif b==6:
        print("question:- Write python program that swap two number with temp variable and without temp variable.")
        print("Answer:-")
        print("First We will try with using temp variable")
        a=input("Enter Value A :")
        b=input("Enter Value B :")
        temp=a
        print("Enter temp Value :",temp)
        a=b
        print("Enter Value A :",a)
        b=temp
        print("Enter Value B :",b)
        print("Now We will try without using temp variable")
        a=input("Enter Value A :")
        b=input("Enter Value B :")
        a,b=b,a
        print("Enter Value A :",a)
        print("Enter Value B :",b)
        
    elif b==7:
        print("question:- Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.")
        print("Answer:-")
        c=int(input("Enter No. :"))
        if c==0:
            print(c,"Is Zero")
        elif c%2!=0:
            print(c,"Is odd Number")
        else:
            print(c,"Is Even Number")
    elif b==8:
        print("question:- Write a Python program to test whether a passed letter is a vowel or not.")
        print("Answer:-")
        n=(input("Enter One Latter :"))
        if n=='a,' or n=='e' or n=='i' or n=='o' or n=='u'or n=='A,' or n=='E' or n=='I' or n=='O' or n=='U':
            print(n,"Is Vowel Latter")
        else:
            print(n,"Is not Vowel Latter")
    elif b==9:
        print("question:- Write a Python program to sum of three given integers.However, if two values are equal sum will be zero.")
        print("Answer:-")
        a=int(input("Enter No.:"))
        b=int(input("Enter NO.:"))
        c=int(input("Enter NO.:"))
        
        if a==b:
            print("two values are equal :0")
        elif a==c:
            print("two values are equal :0")
        elif b==c:
            print("two values are equal :0")
        else:
            n=a+b+c
            print("Addition",n)
    elif b==10:
        print("question:- Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.")
        print("Answer:-")
        def XYZ(x,y):
            if x==y or x-y==5 or x+y==5:
                return True
            else:
                return False
        x=int(input("Enter Value A :"))
        y=int(input("Enter Value B :"))
        print(XYZ(x,y))
    elif b==11:
        print("question:- Write a python program to sum of the first n positive integers")
        print("Answer:-")
        n=int(input("Enter Value :"))
        sum=(n*(n+1))/2
        print("Final Sum is :",sum)
    elif b==12:
        print("question:- Write a Python program to calculate the length of a string.")
        print("Answer:-")
        s=input("Enter String :")
        print("length of a string is :",len(s))
    elif b==13:
        print("question:- Write a Python program to count the number of characters (character frequency) in a string")
        print("Answer:-")
        s=input("Enter String :")
        s1=len(s)
        for i in s1:
            if i in s:
                print(i)
    elif b==14:
        print("question:- What are negative indexes and why are they used?")
        print("Answer:-")
        print("In Python, negative indexing allows you to access elements from the end of a sequence (such as a list, tuple, or string) rather than from the beginning. For instance, if you have a list my_list, the index -1 refers to the last element, -2 refers to the second-to-last element, and so on. Negative indexing can be useful in several scenarios")
    elif b==15:
        print("question:-  Write a Python program to count occurrences of a substring in a string.")
        print("Answer:-")
        s=input("Enter Your Sring :")
        s1=input("Enter your Substring :")
        print("Your Total Substrings Count Is :",s.count(s1))
    elif b==16:
        print("question:-   Write a Python program to count the occurrences of each word in a given sentence")
        print("Answer:-")
        s=input("Enter Your Sring :")
        for i in s:
            print(i,":",s.count(i))
    elif b==17:
        print("question:-   Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.")
        print("Answer:-")
        s1=input("Enter String :")
        s2=input("Enter String :")
        temp1=s1[0:2]
        temp2=s1[2:]
        temp3=s2[0:2]
        temp4=s2[2:]
        s=temp3+temp2+temp1+temp4
        print(s)
    elif b==18:
        print("question:- Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' insteadif the string length of the given string is less than 3, leave it unchanged.")
        print("Answer:-")
        s=input("Enter String :")
        s1=(len(s))
        s2=(s[-1:-4:-1])
        s3=(s2[::-1])
        if s1>=2:
            if s3=="ing":
                print(s+"ly")
            else:
                print(s+"ing")
        else:
            print(s)
    elif b==19:
        print("question:- Write a Python program to find the first appearance of the substring 'not' and 'poor' froma given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'substring with 'good'. Return the resulting string. ")
        print("Answer:-")
        s=input("Enter String :")
        print(s.replace("not poor","Good"))
    elif b==20:
        print("question:- Write a Python function that takes a list of words and returns the length of the longest one.")
        print("Answer:-")
        s=input("Enter Line String :")
        n=s.split()
        largest=len(n[0])
        for i in n:
            if len(i)>largest:
                largest=len(i)
        print("largest String length is :",largest)
    elif b==21:
        print("question:- Write a Python function to reverses a string if its length is a multiple of 4.")
        print("Answer:-")
        s=input("Enter String :")
        s1=len(s)
        if s1 >= 4:
            print(s[::-1])
        else:
            print(s)
    elif b==22:
        print("question:- Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. Ifthe string length islessthan 2,return instead of the empty string.")
        print(" o Sample String:w3resource'")
        print(" o Expected Result: 'w3ce'")
        print(" o Sample String: 'w3'")
        print(" o Expected Result: 'w3w3'")
        print(" o Sample String: ' w'")
        print(" o Expected Result: Empty String")
        print("Answer:-")
        s=input("Enter Your String Here:")
        s3=len(s)
        s1=(s[:2])
        s2=(s[-2:])
        if s3<2:
            print("empty string")
        else:
            print("Result is :",s1+s2)
    elif b==23:
        print("question:- Write a Python function to insert a string in the middle of a string.")
        print("Answer:-")
        s=input("Enter String :")
        s1=(s[:2])
        s2=(s[2:])
        print("String in String is:",s1+s+s2)
elif a==3:
    if b==1:
        print("question:- What is List? How will you reverse a list?")
        print("Answer:-")
        print("List is Group of Differents types of Datas and we can Reverse it with Using Slicing Function. for Example ""l[::-1]"".")
    elif b==2:
        print("question:- How will you remove last object from a list?")
        print("Answer:-")
        print("with ussing Pop Function like (l.pop())")
    elif b==3:
        print("question:- Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?")
        print("Answer:-")
        l=[2,33,222,14,25]
        print("List1 Is:",l[-1])
    elif b==4:
        print("question:- Differentiate between append () and extend () methods?")
        print("Answer:-")
        print(" append() Use for add 1 Value in last. and extend() Use for add Multiple values in Last one.")
    elif b==5:
        print("question:- Write a Python function to get the largest number, smallest num and sum  of all from a list.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Number of list items :"))
        for i in range(n):
            l.append(int(input("Enter Value of list: ")))
        print("Your List Is :",l)
        largest=(l[0])
        for i in l:
            if i>largest:
                largest=(i)
        print("The largest number is :",largest)
        for i in l:
            if i<largest:
                largest=(i)
        print("The smallest number is :",largest)
        print("The SUM of List is :",sum(l))
    elif b==6:
        print("question:- How will you compare two lists?")
        print("Answer:-")
        print("In Python, you can compare two lists using various methods depending on the specific comparison you want to perform. Here are some common techniques to compare lists:")
        print("1: Comparing Equality")
        print("2: Comparing Identity")
        print("3: Comparing Element-wise")
        print("4: Comparing Length")
        print("5: Iterative Comparison")
    elif b==7:
        print("question:- Write a Python program to count the number of strings where the string  length is 2 or more and the first and last character are same from a given  list of strings.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Number of list items :"))
        for i in range(n):
            l.append(input("Enter Value of list: "))
        print("Your List Is :",l)
        a=0
        for i in l:
            if len(i)>1 and i[0]==i[-1]:
                print("The First and Last character are same of string is :",i)
                a=a+1
        print("Total Count of Strings is :",a)
    elif b==8:
        print("question:- Write a Python program to remove duplicates from a list.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Number of list items :"))
        for i in range(n):
            l.append(int(input("Enter Value of list: ")))
        print("Your List Is :",l)
        a=set(l)
        print("After Remove Dublicates Your List is :",a)
        
    elif b==9:
        print("question:-  Write a Python program to check a list is empty or not.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Number of list items :"))
        for i in range(n):
            l.append(int(input("Enter Value of list: ")))
        print("Your List Is :",l)
        a=len(l)
        if a<1:
            print("list is empty")
        else:
            print("list is not empty")
    elif b==10:
        print("question:- Write a Python function that takes two lists and returns true if they have at least one common member.")
        print("Answer:-")
        l1=[]
        n=int(input("Enter Number of list1 items :"))
        for i in range(n):
            l1.append(input("Enter Value of list: "))
        
        l2=[]
        n=int(input("Enter Number of list2 items :"))
        for i in range(n):
            l2.append(input("Enter Value of list: "))
        print("Your List1 Is :",l1)
        print("Your List2 Is :",l2)
        
        l3=[]
        for i in l1:
            if i in l2:
                print("They have at least one common member is :",i)
            else:
                print("They haven't at least one common member")
    elif b==11:
        print("question:- Write a Python program to generate and print a list of first and last 5  elements where the values are square of numbers between 1 and 30.")
        print("Answer:-")
        l=list()
        for i in range(1,31):
            l.append(i*i)
        print(l[:5])
        print(l[-5:])

    elif b==12:
        print("question:- Write a Python function that takes a list and returns a new list with unique elements of the first list.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Number of list items :"))
        for i in range(n):
            l.append(int(input("Enter Value of list: ")))
        print("Your List Is :",l)
        a=set(l)
        print("list with unique elements :",a)

    elif b==13:
        print("question:- Write a Python program to convert a list of characters into a string.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Number of list items :"))
        for i in range(n):
            l.append(int(input("Enter Value of list: ")))
        print("Your List Is :",l)
        for i in l:
            print("list of characters into a string is :",i,end="")
    elif b==14:
        print("question:- Write a Python program to select an item randomly from a list.")
        print("Answer:-")
        import random
        l=[]
        n=int(input("Enter Number of list items :"))
        for i in range(n):
            l.append(input("Enter Value of list: "))
        print("Your List Is :",l)
        print("selected an item randomly from a list :",random.choice(l))
    elif b==15:
        print("question:- Write a Python program to find the second smallest number in a list.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Number of list items :"))
        for i in range(n):
            l.append(input("Enter Value of list: "))
        print("Your List Is :",l)
        largest=(l[0])
        for i in l:
            if i<largest:
                largest=(i)
        print("The smallest number is :",largest)
        l.remove(largest)
        largest=(l[0])
        for i in l:
            if i<largest:
                largest=(i)
        print("The 2nd smallest number is :",largest)
    elif b==16:
        print("question:- Write a Python program to get unique values from a list")
        print("Answer:-")
        l=[]
        n=int(input("Enter Numbers of List items :"))
        for i in range(n):
            l.append(input("Enter value of list :"))
        print("Your List is :",l)
        a=set(l)
        print("unique Values are :")
        for i in a:
            print(i," ",end="")
    elif b==17:
        print("question:-  Write a Python program to check whether a list contains a sub list.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Numbers of List items :"))
        for i in range(n):
            l.append(input("Enter value of list :"))
        print("Your List is :",l)
        for i in l:
            if i==list:
                print(i,"sublist available in list")
                break
        else:
            print("sublist is not available in list")
    elif b==18:
        print("question:-   Write a Python program to split a list into different variables.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Number of List item :"))
        for i in range(n):
            l.append(input("Enter value of LIst :"))
        print("Your List is :",l)
        import random
        for i in l:
            print(random.choice(l),"=",i)
    elif b==19:
        print("question:- What is tuple? Difference between list and tuple.")
        print("Answer:-")
        print("tuple is groups of differents types of data...in List we can change values with using functions but in tuple we cant change tuple's value")
    elif b==20:
        print("question:-    Write a Python program to create a tuple with different data types.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Number of List item :"))
        for i in range(n):
            l.append(input("Enter value of LIst :"))
        tuple=tuple(l)
        print("Your tuple is :",tuple)
    elif b==21:
        print("question:-     Write a Python program to create a tuple with numbers.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Number if tuple items :"))
        for i in range(n):
            l.append(int(input("Enter Value of tuple :")))
        tuple=tuple(l)
        print("Your integer tuple is :",tuple)
    elif b==22:
        print("question:-  Write a Python program to convert a tuple to a string.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Number of List item :"))
        for i in range(n):
            l.append(input("Enter value of LIst :"))
        tuple=tuple(l)
        print("Your tuple is :",tuple)
        a=""
        for i in tuple:
            a+=i
        print("converted a tuple to a string is :",a)
    elif b==23:
        print("question:-   Write a Python program to check whether an element exists within a tuple.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Number of List item :"))
        for i in range(n):
            l.append(input("Enter value of LIst :"))
        tuple=tuple(l)
        print("Your tuple is :",tuple)
        a=input("which element you want find in tuple? :")
        if a in l:
            print(a,": Yes,an element exists in Your tuple.")
        else:
            print(a,": No,an element is not exists in Your tuple.")
    elif b==24:
        print("question:-   Write a Python program to find the length of a tuple.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Number of List item :"))
        for i in range(n):
            l.append(input("Enter value of LIst :"))
        tuple=tuple(l)
        print("Your tuple is :",tuple)
        print("length of a tuple is :",len(tuple))
    elif b==25:
        print("question:-  Write a Python program to convert a list to a tuple.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Number of List item :"))
        for i in range(n):
            l.append(input("Enter value of LIst :"))
        tuple=tuple(l)
        print("Your tuple is :",tuple)
        print("Your List is :",l)
    elif b==26:
        print("question:-   Write a Python program to reverse a tuple.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Number of List item :"))
        for i in range(n):
            l.append(input("Enter value of LIst :"))
        tuple=tuple(l)
        print("Your tuple is :",tuple)
        print("reverse a tuple is :",tuple[::-1])
    elif b==27:
        print("question:-  Write a Python program to replace last value of tuples in a list")
        print("Answer:-")
        l= [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        print("Your List is : l= [(1, 2, 3), (4, 5, 6), (7, 8, 9)]")
        n=input("Enter the value you want to replace with last elements :")
        a= [tup[:-1] + (n,) for tup in l]
        print("Modified List of Tuples:")
        for tup in a:
            print(tup)
    elif b==28:
        print("question:-   Write a Python program to find the repeated items of a tuple.")
        print("Answer:-")
        l=[]
        n=int(input("Enter Number of tuple item :"))
        for i in range(n):
            l.append(input("Enter value of tuple :"))
        t=tuple(l)
        print("Your tuple is :",t)
        for i in t:
            if t.count(i)>1:
                print("the repeated items of a tuple is :",i)
    elif b==29:
        print("question:-   Write a Python program to remove an empty tuple(s) from a list of tuples. ")
        print("Answer:-")
        l= [(1, 2, 3), (), (4, 5), (), (6,), (), (7, 8, 9)]
        print("Your List of tuple is : l= [(1, 2, 3), (), (4, 5), (), (6,), (), (7, 8, 9)]")
        a= [tup for tup in l if tup]
        print("Filtered List of Tuples:")
        for tup in a:
            print(tup)

    elif b==30:
        print("question:- Write a Python program to unzip a list of tuples into individual lists.")
        print("Answer:-")
        l= [(1, 'a'), (2, 'b'), (3, 'c')]
        print("Your :List is : l= [(1, 'a'), (2, 'b'), (3, 'c')]")
        a= list(zip(*l))
        print("Unzipped Lists:")
        for i in a:
            print(list(i))

    elif b==31:
        print("question:-  Write a Python program to convert a list of tuples into a dictionary.")
        print("Answer:-")
        l= [(1, 'a'), (2, 'b'), (3, 'c')]
        print(" Your List of tuple is : l= [(1, 'a'), (2, 'b'), (3, 'c')]")
        d= {t[0]: t[1] for t in l}
        print("Dictionary from list of tuples :", d)

        a = dict(l)
        print("Dictionary from list of tuples :", a)

    elif b==32:
        print("question:-  How will you create a dictionary using tuples in python? ")
        print("Answer:-")
    elif b==33:
        print("question:-  Write a Python script to sort (ascending and descending) a dictionary by value.")
        print("Answer:-")
        d= {'a': 4, 'b': 2, 'c': 1, 'd': 3}
        print("Your Dict is : d= {'a': 4, 'b': 2, 'c': 1, 'd': 3}")
        print("Dictionary sorted by values in ascending order:")
        a= dict(sorted(d.items(), key=lambda item: item[1]))
        print(a)
        print("\nDictionary sorted by values in descending order:")
        b= dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        print(b)
    elif b==34:
        print("question:- Write a Python script to concatenate following dictionaries to create a new one.")
        print("Answer:-")
        dict1 = {1: 'a', 2: 'b'}
        dict2 = {3: 'c', 4: 'd'}
        dict3 = {5: 'e', 6: 'f'}
        print("dict1 = {1: 'a', 2: 'b'}")
        print("dict2 = {3: 'c', 4: 'd'}")
        print("dict3 = {5: 'e', 6: 'f'}")
        
        concatenated_dict_1 = dict1.copy()
        concatenated_dict_1.update(dict2)
        concatenated_dict_1.update(dict3)
        print("Concatenated Dictionary using the update method :")
        print(concatenated_dict_1)
        concatenated_dict_2 = {**dict1, **dict2, **dict3}
        print("\nConcatenated Dictionary using the unpacking ** operator :")
        print(concatenated_dict_2)

    elif b==35:
        print("question:-")
        print("Answer:-")
    elif b==36:
        print("question:-")
        print("Answer:-")
    elif b==37:
        print("question:-")
        print("Answer:-")
    elif b==38:
        print("question:-")
        print("Answer:-")
    elif b==39:
        print("question:-")
        print("Answer:-")
    elif b==40:
        print("question:-")
        print("Answer:-")














        
