# ******* Classes and Objects - Exercise ******* #

# *******  05_todo_list  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Compete/Index/1937#4
Create separate files for each class, as shown above.
You are tasked to create two classes: a Task class and a Section class.

The Task class should receive a name (string) and a due_date (str) upon initialization.
A task also has two attributes: comments (empty list) and completed set to False by default.
The Task class should also have five additional methods:
-	change_name(new_name: str)
    o	Changes the name of the task and returns the new name.
    o	If the new name is the same as the current name, return
        "Name cannot be the same."

-	change_due_date(new_date: str)
    o	Changes the due date of the task and returns the new date.
    o	If the new date is the same as the current date, return
        "Date cannot be the same."

-	add_comment(comment: str)
    o	Adds a comment to the task.

-	edit_comment(comment_number: int, new_comment: str)
    o	The comment number value represents the index of the comment we want to edit.
        The method should change the comment and
            return all the comments, separated by comma and space (", ")
    o	If the comment number is out of range,
    return "Cannot find comment."


-	details()
o	Returns the task's details in this format:
"Name: {task_name} - Due Date: {due_date}"


The Section class should receive a name (string) upon initialization.

The task also has one instance attribute: tasks (empty list)

The Section class should also have four methods:
-	add_task(new_task: Task)
    o	Adds a new task to the collection and returns
        "Task {task details} is added to the section"
    o	If the task is already in the collection, return
        "Task is already in the section {section_name}"


-	complete_task(task_name: str)
    o	Changes the task to completed (True) and returns
        "Completed task {task_name}"
    o	If the task is not found, returns
        "Could not find task with the name {task_name}"

-	clean_section()
    o	Removes all the completed tasks and returns "Cleared {amount of removed tasks} tasks."


-	view_section()
    o	Returns information about the section and its tasks in this format:
    "Section {section_name}:
     {details of the first task}
     {details of the second task}
     …
     {details of the n task}"

"""


##########: SOLUTION :##########



##########: TEST CODE :##########

from project.section import Section
from project.task import Task



task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())


"""
Outout:

Go to University
28.05.2020
Don't forget laptop and notebook
Name: Go to University - Due Date: 28.05.2020
Task Name: Go to University - Due Date: 28.05.2020 is added to the section
Cleared 0 tasks.
Section Daily tasks:
Name: Go to University - Due Date: 28.05.2020
Name: Make bed - Due Date: 27/05/2020

"""



##########: UNITTEST :##########

from project.task import Task
from project.section import Section

import unittest


class Test(unittest.TestCase):

    def test_task_init(self):
        task = Task("Tst", "27.04.2020")
        message = f"{task.name} - {task.due_date}"
        expected = "Tst - 27.04.2020"
        self.assertEqual(message, expected)

    def test_change_name_working(self):
        task = Task("Tst", "27.04.2020")
        task.change_name("New name")
        message = task.name
        expected = "New name"
        self.assertEqual(message, expected)

    def test_change_name_same_name(self):
        task = Task("Tst", "27.04.2020")
        message = task.change_name("Tst")
        expected = "Name cannot be the same."
        self.assertEqual(message, expected)

    def test_change_due_date_working(self):
        task = Task("Tst", "27.04.2020")
        task.change_due_date("21.05.2020")
        message = task.due_date
        expected = "21.05.2020"
        self.assertEqual(message, expected)

    def test_edit_comment_working(self):
        task = Task("Tst", "27.04.2020")
        task.add_comment("pay the bills")
        message = task.edit_comment(0, "finish my homework")
        expected = "finish my homework"
        self.assertEqual(message, expected)

    def test_edit_comment_not_found(self):
        task = Task("Tst", "27.04.2020")
        task.add_comment("pay the bills")
        message = task.edit_comment(1, "finish my homework")
        expected = "Cannot find comment."
        self.assertEqual(message, expected)

    def test_section_init(self):
        section = Section("New section")
        message = f"{section.name} - {len(section.tasks)}"
        expected = "New section - 0"
        self.assertEqual(message, expected)

    def test_add_task(self):
        section = Section("New section")
        task = Task("Tst", "27.04.2020")
        message = section.add_task(task)
        expected = "Task Name: Tst - Due Date: 27.04.2020 is added to the section"
        self.assertEqual(message, expected)

    def test_add_task_already_added(self):
        section = Section("New section")
        task = Task("Tst", "27.04.2020")
        section.add_task(task)
        message = section.add_task(task)
        expected = "Task is already in the section New section"
        self.assertEqual(message, expected)

    def test_complete_task(self):
        section = Section("New section")
        task = Task("Tst", "27.04.2020")
        section.add_task(task)
        section.complete_task("Tst")
        message = task.completed
        self.assertTrue(message)

    def test_complete_task_message(self):
        section = Section("New section")
        task = Task("Tst", "27.04.2020")
        section.add_task(task)
        message = section.complete_task("Tst")
        expected = "Completed task Tst"
        self.assertEqual(message, expected)

    def test_complete_not_found(self):
        section = Section("New section")
        message = section.complete_task("Tst")
        expected = "Could not find task with the name Tst"
        self.assertEqual(message, expected)

    def test_clean_section(self):
        section = Section("New section")
        task = Task("Tst", "27.04.2020")
        section.add_task(task)
        section.complete_task("Tst")
        message = section.clean_section()
        expected = "Cleared 1 tasks."
        self.assertEqual(message, expected)

    def test_view_section(self):
        section = Section("New section")
        message = section.view_section().strip()
        expected = "Section New section:"
        self.assertEqual(message, expected)


if __name__ == '__main__':
    unittest.main()
