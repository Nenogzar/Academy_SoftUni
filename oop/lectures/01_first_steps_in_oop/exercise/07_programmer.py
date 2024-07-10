# ******* First Steps in OOP - Exercise ******* #

# *******  07_programmer  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Compete/Index/1935


Create a class called Programmer.
Upon initialization, it should receive - name (string), language (string), and skills (integer).

The class should have two methods:

-	watch_course(course_name, language, skills_earned)
    o	If the programmer's language is the same as the one on the course,
        increase his skills with the given amount and return a message
            "{name} watched {course_name}"

    o	Otherwise return
            "{name} does not know {language}"

-	change_language(new_language, skills_needed)
    o	If the programmer has the skills and the new language is not the same as his,
        change his language to the new one and return
            "{name} switched from {previous_language} to {new_language}"

    o	If the programmer has the skills, but the given language is equal to his return
            "{name} already knows {language}".

    o	In the last case, the programmer does not have enough skills, so return
            "{name} needs {needed_skills} more skills"
        and do not change his language.

Submit only the class in the judge system.

Examples

Test Code:

programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))

Output:

John does not know Python
John already knows Java
John needs 50 more skills
John watched Java: zero to hero
John switched from Java to Python
John watched Python Masterclass



"""
##########: variant 1 :##########


class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, language: str, skills_earned: int) -> str:
        if self.language == language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        return f"{self.name} does not know {language}"

    def change_language(self, new_language: str, skills_needed: int) -> str:
        if self.language == new_language:
            return f"{self.name} already knows {new_language}"
        elif self.skills >= skills_needed:
            previous_language = self.language
            self.language = new_language
            self.skills -= skills_needed
            return f"{self.name} switched from {previous_language} to {new_language}"
        return f"{self.name} needs {skills_needed - self.skills} more skills"

# Test Code
programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))

##########: variant 2 :##########
class Programmer:

    def __init__(self, *args):
        [self.name,
         self.language,
         self.skills
         ] = args

    def watch_course(self, course_name, language, skills_earned):
        if language != self.language:
            return f"{self.name} does not know {language}"

        self.skills += skills_earned
        return f"{self.name} watched {course_name}"

    def change_language(self, new_language, skills_needed):
        if new_language == self.language:
            return f"{self.name} already knows {new_language}"

        if skills_needed > self.skills:
            needed_skills = skills_needed - self.skills
            return f"{self.name} needs {needed_skills} more skills"

        message = f"{self.name} switched from {self.language} to {new_language}"
        self.language = new_language
        return message


# Test Code
import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        programmer = Programmer("Lemmy", "Python", 100)
        self.assertEqual(programmer.name, "Lemmy")
        self.assertEqual(programmer.language, "Python")
        self.assertEqual(programmer.skills, 100)

    def test_watch_course_successfull(self):
        programmer = Programmer("Lemmy", "Python", 100)
        res = programmer.watch_course("Django Fundamentals", "Python", 50)
        self.assertEqual(res, "Lemmy watched Django Fundamentals")
        self.assertEqual(programmer.skills, 150)

    def test_watch_course_unsuccessfull(self):
        programmer = Programmer("Lemmy", "Python", 100)
        res = programmer.watch_course("Best C#", "C#", 20)
        self.assertEqual(res, "Lemmy does not know C#")
        self.assertEqual(programmer.skills, 100)

    def test_change_language_unsuccessful(self):
        programmer = Programmer("Lemmy", "Java", 100)
        res = programmer.change_language("Python", 150)
        self.assertEqual(res, "Lemmy needs 50 more skills")
        self.assertEqual(programmer.language, "Java")

    def test_change_language_successful(self):
        programmer = Programmer("Lemmy", "Java", 100)
        res = programmer.change_language("Python", 50)
        self.assertEqual(res, "Lemmy switched from Java to Python")
        self.assertEqual(programmer.language, "Python")

    def test_change_language_same_language(self):
        programmer = Programmer("Lemmy", "Python", 100)
        res = programmer.change_language("Python", 50)
        self.assertEqual(res, "Lemmy already knows Python")
        self.assertEqual(programmer.language, "Python")


if __name__ == "__main__":
    unittest.main()

##########: variant 3 solution SoftUni :##########


