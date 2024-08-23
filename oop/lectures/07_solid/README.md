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
class UserManager:
    def authenticatie_user(self, eusername, password):
        # Authenticate login
        ...

    def update_user_profile(self, user_id, new_profile_data):
        # Profie update logic
        ...
    
    def send_email_notification(self, user_email, message):
        # Email sending logic
        ...
```

This class violates the SRP because it has multiple responsibilities: authentication, profile management, and email notifications.

If you need to change the way user authentication is handled, you might inadvertently affect the email notification logic, or vice versa.

To adhere to the SRP, we can split this class into three separate classes, each with a single responsibility:

```py
class UserManager:
    def authenticatie_user(self, eusername, password):
        # Authenticate login
        ...

    def update_user_profile(self, user_id, new_profile_data):
        # Profie update logic
        ...
    
    def send_email_notification(self, user_email, message):
        # Email sending logic
        ...
```

Now, each class has a single, well-defined responsibility. Changes to user authentication won't affect the email notification logic, and vice versa, improving maintainability and reducing the risk of unintended side effects.

</details>  


<details> <summary>O: Open/Closed Principle (OCP) </summary>
    
> Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

This means the design of a software entity should be such that you can introduce new functionality or behavior without modifying the existing code since changing the existing code might introduce bugs.

### Code Example:

Let's say you have a ShapeCalculator class that calculates the area and perimeter of different shapes like rectangles and circles.

```py
class ShapeCalculator:
    def calulate_area(self, shape):
        if shape.type == "rectangle":
            return shape.width * shape.height
        elif shape.type == "circle":
            return 3.14 * (shape.radius ** 2)
        
    def calculate_perimeter(self, shape):
        if shape.type == "rectangle":
            return 2 * (shape.width + shape.height)
        elif shape.type == "circle":
            return 2 * 3.14 * shape.radius
```

If we want to add support for a new shape, like a triangle, we would have to modify the calculate_area and calculate_perimeter methods, violating the Open/Closed Principle.

To adhere to the OCP, we can create an abstract base class for shapes and separate concrete classes for each shape type:

```py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.heigh = height
        
    def calculate_area(self):
        return self.width * self.heigh
    
    def calculate_perimeter(self):
        return (self.width + self.heigh) * 2
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return 3.14 *(self.radius **2)
    
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
    
    
# We can now add new sharpes like Triangle without modifying existing code

class Triangle(Shape):
    # Implementation for Triangle
```

By introducing an abstraction (Shape class) and separating the concrete implementations (Rectangle and Circle classes), we can add new shapes without modifying the existing code.

The ShapeCalculator class can now work with any shape that implements the Shape interface, allowing for easy extensibility.

</details> 


<details> <summary>L: Liskov Substitution Principle (LSP)</summary>
    
> Objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program.

This means if you have a base class and a derived class, you should be able to use instances of the derived class wherever instances of the base class are expected, without breaking the application.


### Code Example:

Let's consider a scenario where we have a base class Vehicle and two derived classes Car and Bicycle.
Without following the LSP, the code might look like this:

```py
class Vehicle:
    def start_engine(self):
        pass
    
class Car(Vehicle):
    def start_engine(self):
        print("Starting the car engine ...")
        
class Bicycle(Vehicle):
    def start_engine(self):
        # This doesn't make sense for a bicycle
        pass
```

In this example, the Bicycle class violates the LSP because it provides an implementation for the start_engine method, which doesn't make sense for a bicycle.

If we try to substitute a Bicycle instance where a Vehicle instance is expected, it might lead to unexpected behavior or errors.

To adhere to the LSP, we can restructure the code as follows:

```py
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        pass

class Engine:
    def start_engine(self):
        pass

class Car(Vehicle, Engine):
    def start_engine(self):
        print("Starting the car engine ...")

    def move(self):
        self.start_engine()
        print("Car is moving ...")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling the bicycle ...")
```

Explanation of the new design:
Vehicle: A base class that contains common characteristics for all vehicles, such as the brand.
Engine: A class that represents all vehicles with engines. This defines the start_engine method, which can be implemented by specific engine vehicles.
Car: Inherits from both Vehicle and Engine. This is where the start_engine method is implemented, as well as the behavior of the car when moving (move).
Bicycle: Inherits only Vehicle, since bicycle has no engine and therefore does not implement the start_engine method.

How this improves the code:
Now the Bicycle class does not have to implement the start_engine method, which is more logical and follows Liskov's substitution principle.
Each vehicle can have its own specific methods and functionalities without being forced to inherit inappropriate methods.
This approach is more consistent with the solid principles of object-oriented programming, including the Liskow principle.


</details> 

<details> <summary>I: Interface Segregation Principle (ISP)</summary>
    
>  No client should be forced to depend on interfaces they don't use.

The main idea behind ISP is to prevent the creation of "fat" or "bloated" interfaces that include methods that are not required by all clients.
By segregating interfaces into smaller, more specific ones, clients only depend on the methods they actually need, promoting loose coupling and better code organization.

### Code Example:

Let's consider a scenario where we have a media player application that supports different types of media files, such as audio files (MP3, WAV) and video files (MP4, AVI).

Without applying the ISP, we might have a single interface like this:

```py
class MediaPlayer:
    def play_audio(self, audio_file):
        raise NotImplementedError
    
    def play_video(selfself, video_file):
        raise NotImplementedError
    
    def stop_audio(self):
        raise NotImplementedError
    
    def stop_video(self):
        raise NotImplementedError
    
    def adjust_audio_volume(self, volume):
        raise NotImplementedError
        
    def adjust_video_brightness(self, brightness):
        raise NotImplementedError
```

In this case, any class that implements the MediaPlayer interface would be forced to implement all the methods, even if it doesn't need them.
For example, an audio player would have to implement the play_video, stop_video, and adjust_video_brightness methods, even though they are not relevant for audio playback.
To adhere to the ISP, we can segregate the interface into smaller, more focused interfaces:


```py
class AudioPlayer:
    def play_audio(self, audio_file):
        raise NotImplementedError

    def stop_audio(self):
        raise NotImplementedError

    def adjust_audio_volume(self, volume):
        raise NotImplementedError


class VideoPlayer:
    def play_video(selfself, video_file):
        raise NotImplementedError

    def stop_video(self):
        raise NotImplementedError

    def adjust_video_brightness(self, brightness):
        raise NotImplementedError
```
Now, we can have separate implementations for audio and video players:

```py
class MP3Player(AudioPlayer):
    def play_audio(self, audio_file):
        # play MP3 file
        ...

    def stop_audio(self):
        # stop audio file
        ...

    def adjust_audio_volume(self, volume):
        # adjust volume
        ...


class AviVideoPlayer(VideoPlayer):
    def play_video(selfself, video_file):
        # play AVI video file
        ...

    def stop_video(self):
        # stop Avi fideo file
        ...

    def adjust_video_brightness(self, brightness):
        # adjust video brighttness
        ...
```

By segregating the interfaces, each class only needs to implement the methods it actually requires. This not only makes the code more maintainable but also prevents clients from being forced to depend on methods they don't use.

If we need a class that supports both audio and video playback, we can create a new class that implements both interfaces:

```py
class MulstimediaPlayer(AudioPlayer,VideoPlayer):
    # implement methods from AudioPlayer adn VideoPlayer interfaces

```

</details> 

<details> <summary>D: Dependency Inversion Principle (DIP)</summary>
    
> High-level modules should not depend on low-level modules; both should depend on abstractions.

This means that a particular class should not depend directly on another class, but on an abstraction (interface) of this class.
Applying this principle reduces dependency on specific implementations and makes our code more reusable.

### Code Example:

Let's consider a example where we have a EmailService class that sends emails using a specific email provider (e.g., Gmail).

```py

```
In this example, the EmailService class directly depends on the GmailClient class, a low-level module that implements the details of sending emails using the Gmail API.

This violates the DIP because the high-level EmailService module is tightly coupled to the low-level GmailClient module.

To adhere to the DIP, we can introduce an abstraction (interface) for email clients:

```py

```

Now, the EmailService class depends on the EmailClient abstraction, and the low-level email client implementations (GmailClient and OutlookClient) depend on the abstraction.

This follows the DIP, resulting in a more flexible and extensible design.

</details> 
