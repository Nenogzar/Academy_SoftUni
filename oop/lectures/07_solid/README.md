<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>

<body style="background-color: #0d1117; color: white; align-items: center; height: 100vh; margin: 0;">


## <a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/oop">Back to Python OOP</a>


Writing clean, maintainable code is just as important as writing code that works.

The SOLID principles provide a blueprint for writing code that’s easy to adjust, extend, and maintain over time.

<div id="badges" align="center">
<img src="https://github.com/Nenogzar/Academy_SoftUni/blob/main/oop/image/SOLID.jpg" alt="Nenogzar_Python" height="450"  >
</div>
It was introduced by Robert C. Martin (Uncle Bob) in the early 2000s.

In this article, we will explore each of the 5 principles with real world examples and code:

<details> <summary>S: Single Responsibility Principle (SRP) </summary>
    
> A class should have one, and only one, reason to change.

This means that a class must have only one responsibility.

When a class performs just one task, it contains a small number of methods and member variables making them more usable and easier to maintain.

If a class has multiple responsibilities, it becomes harder to understand, maintain, and modify and increases the potential for bugs because changes to one responsibility could affect the others.

### Code Example:

Imagine you have a class called UserManager that handles user authentication, user profile management, and email notifications.

```py

```

This class violates the SRP because it has multiple responsibilities: authentication, profile management, and email notifications.

If you need to change the way user authentication is handled, you might inadvertently affect the email notification logic, or vice versa.

To adhere to the SRP, we can split this class into three separate classes, each with a single responsibility:

```py

```

Now, each class has a single, well-defined responsibility. Changes to user authentication won't affect the email notification logic, and vice versa, improving maintainability and reducing the risk of unintended side effects.

</details>  


<details> <summary>O: Open/Closed Principle (OCP) </summary>
    
> Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

This means the design of a software entity should be such that you can introduce new functionality or behavior without modifying the existing code since changing the existing code might introduce bugs.

### Code Example:

Let's say you have a ShapeCalculator class that calculates the area and perimeter of different shapes like rectangles and circles.

```py

```

If we want to add support for a new shape, like a triangle, we would have to modify the calculate_area and calculate_perimeter methods, violating the Open/Closed Principle.

To adhere to the OCP, we can create an abstract base class for shapes and separate concrete classes for each shape type:

```py

```

By introducing an abstraction (Shape class) and separating the concrete implementations (Rectangle and Circle classes), we can add new shapes without modifying the existing code.

The ShapeCalculator class can now work with any shape that implements the Shape interface, allowing for easy extensibility.

</details> 


<details> <summary>L: Liskov Substitution Principle (LSP)</summary>
    
> 

```



```py

```

</details> 

<details> <summary>I: Interface Segregation Principle (ISP)</summary>
    
> 

```



```py

```

</details> 

<details> <summary>D: Dependency Inversion Principle (DIP)</summary>
    
> 

```



```py

```

</details> 
