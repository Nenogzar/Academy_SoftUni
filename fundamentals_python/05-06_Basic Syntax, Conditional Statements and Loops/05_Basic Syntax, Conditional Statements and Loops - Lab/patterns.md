# Star Pattern Programs In Python
1. Write a python program to print following star pattern: 

         *  *  *  *  *
         *  *  *  *  *
         *  *  *  *  *
         *  *  *  *  *
         *  *  *  *  *

        
Code:

    n=5
    for i in range(n):
        for j in range(n):
            print('*', end=' ')
        print()

1.1. Hollow Square of Stars Pattern 5 in Python

      
      *  *  *  *  * 
      *           * 
      *           *
      *           *
      *  *  *  *  *

Please Enter any Side of a Square  :5
Hollow Square Star Pattern

Code: 

      side = int(input("Please Enter any Side of a Square  : "))
      
      print("Hollow Square Star Pattern")
      for i in range(side):
          for j in range(side):
              if(i == 0 or i == side-1 or j == 0 or j == side-1):
                  print('*', end = ' ')
              else:
                  print(' ', end = ' ')
          print()




2. Write a python program to print following pattern: 

         *
         *  *
         *  *  *
         *  *  *  *        
         *  *  *  *  *

Code:

    n = 5 
    for i in range(n): 
       for j in range(i+1): 
          print('*', end=' ')
       print()

3. Write a python code to print following star pattern: 

         *  *  *  *  *
         *  *  *  *
         *  *  *
         *  *
         *

Code:    

    n = 5 
    for i in range(n): 
       for j in range(i, n): 
          print('*', end=' ')
       print()

4. Write a python code to print following pattern: 

                        *
                    *   *
                *   *   *
            *   *   *   *
        *   *   *   *   *

Code:

    n = 5 
    for i in range(n): 
      for j in range(i, n): 
         print(' ', end=' ') 
      for j in range(i+1):
         print('*', end=' ')
      print()

5. Write a python program to print following star pattern: 

        *   *   *   *   *
            *   *   *   *
                *   *   *
                    *   *
                        *
Code:

        n = 5 
        for i in range(n): 
           for j in range(i+1): 
              print(' ', end=' ') 
           for j in range(i, n):
              print('*', end=' ')
           print()



6. Write a python program to print following hill star pattern: 


                    *
                *   *   *
            *   *   *   *   *
        *   *   *   *   *   *   *
    *   *   *   *   *   *   *   *   *

Code:

        n = 5 
        for i in range(n): 
           for j in range(i, n): 
              print(' ', end=' ') 
           for j in range(i):
              print('*', end=' ')
           for j in range(i+1):
              print('*', end=' ')
           print()


7. Write a python program to print revers hill star pattern: 


    *   *   *   *   *   *   *   *   *
        *   *   *   *   *   *   *   
            *   *   *   *   * 
                *   *   *
                    *
Code:

        n = 5 
        for i in range(n): 
           for j in range(i+1): 
              print(' ', end=' ') 
           for j in range(i, n-1):
              print('*', end=' ')
           for j in range(i, n):
              print('*', end=' ')
           print()

8. Write a python code to print Dimond pattern with star: 


                    *
                *   *   *
            *   *   *   *   *
        *   *   *   *   *   *   *
    *   *   *   *   *   *   *   *   *
        *   *   *   *   *   *   *   
            *   *   *   *   * 
                *   *   *
                    *

Code:

    n = 5 
    for i in range(n-1): 
       for j in range(i, n): 
          print(' ', end=' ') 
       for j in range(i):
          print('*', end=' ')
       for j in range(i+1): 
          print('*', end=' ')
       print() 
    for i in range(n): 
       for j in range(i+1): 
          print(' ', end=' ') 
       for j in range(i, n-1):
          print('*', end=' ')
       for j in range(i, n):
          print('*', end=' ')
       print()

8.1. Python Hollow Star Diamond

   
                  *
               *     *
            *           *
         *                 *
      *                       *
         *                 *
            *           *
               *     *
                  * 



9. Print Trouser Style Pattern


      ****************
      *******  *******
      ******    ******
      *****      *****
      ****        ****
      ***          ***
      **            **
      *              *

Code: 

      n = 16
      print("*" * n, end="\n")
      i = (n // 2) - 1
      j = 2
      while i != 0:
          while j <= (n - 2):
              print("*" * i, end="")
      
              print(" " * j, end="")
              print("*" * i)
              i = i - 1
              j = j + 2

9.1. Python Pyramid Program to Display Trouser Line Star Pattern

      ****************
      *******--*******
      ******----******
      *****------*****
      ****--------****
      ***----------***
      **------------**
      *--------------*

Code: 

      n = 16
      print("*" * n, end="\n")
      i = (n // 2) - 1
      j = 2
      while i != 0:
          while j <= (n - 2):
              print("*" * i, end="")
      
              print("-" * j, end="")
              print("*" * i)
              i = i - 1
              j = j + 2

10. Sand Glass star pattern 10 in Python Programming
Write a Python program
to display Sand glass
star pattern 10
Enter number of Rows:5

         * * * * * 
          * * * * 
           * * * 
            * * 
             * 
            * * 
           * * * 
          * * * * 
         * * * * * 

