# ******* Exercise: Class and Static Methods ******* #

# *******  03_document_management  ******* #

# *******  TASK CONDITION  ******* #
"""
https://judge.softuni.org/Contests/2431/Static-and-Class-Methods-Exercise
- project
-- category
-- document
-- storage
-- topic

Class Topic

The Topic class should receive the following parameters upon initialization:
    id: int, topic: str, storage_folder: str

    It should have two methods:
    •	edit(new_topic: str, new_storage_folder: str)
            - change the topic and the storage folder

    •	__repr__()
            - returns a string representation of the topic in the format:
                "Topic {id}: {topic} in {storage_folder}"


Class Category
The Category class should receive the following parameters upon initialization: id: int, name: str.

The class should have two methods:
    •	edit(new_name: str) - edit the name of the category
    •	__repr__() - returns a string representation of the category in the following format: "Category {id}: {name}"


Class Document
The Document class should receive the following parameters upon initialization:
    id: int, category_id: int, topic_id: int, file_name: str.

    The class should also have one more attribute called tags (empty list). The class should also have 4 methods:

    •	from_instances(id: int, category: Category, topic: Topic, file_name: str)
            - create a new instance using the provided category and topic instances

    •	add_tag(tag_content: str)
        - if the tag is not already in the tags list, add it to the tags list

    •	remove_tag(tag_content: str)
        - if the tag is in the tags list, delete it

    •	edit(file_name: str)
            - change the file name with the given one

    •	__repr__()
            - returns a string representation of a document in the format: "Document {id}: {file_name}; category {category_id}, topic {topic_id}, tags: {tags joined by comma and space)}"


Class Storage
Upon initialization, the class Storage will not receive any parameters.

It should have 3 instance attributes:
        categories (empty list),
        topics (empty list), and
        documents (empty list).
    The class should have the following methods:
    •	add_category(category: Category)
        - add the category if it is not in the list
    •	add_topic(topic: Topic)
        - add the topic if it does not exist
    •	add_document(document: Document)
        - add the document if it does not exist
    •	edit_category(category_id: int, new_name: str)
        - edit the name of the category with the provided id
    •	edit_topic(topic_id: int, new_topic: str, new_storage_folder: str)
        - edit the topic with the given id
    •	edit_document(document_id: int, new_file_name: str)
        - edit the document with the given id
    •	delete_category(category_id)
        - delete the category with the provided id
    •	delete_topic(topic_id)
        - delete the topic with the provided id
    •	delete_document(document_id)
        - delete the document with the provided id
    •	get_document(document_id)
        - return the document with the provided id
    •	__repr__()
        - returns a string representation of each document on separate lines


"""

##########: SOLUTION :##########


##########: TEST CODE :##########
from project.category import Category
from project.document import Document
from project.storage import Storage
from project.topic import Topic

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)

"""
Output:

Category 1: work
Topic 1: daily tasks in C:\work_documents
Document 1: finilize project; category 1, topic 1, tags: urgent, work
Document 1: finilize project; category 1, topic 1, tags: urgent, work

 """
##########: UNITTEST :##########

from project.category import Category
from project.document import Document
from project.storage import Storage
from project.topic import Topic

import unittest


class TestDocumentManagement(unittest.TestCase):
    def setUp(self):
        self.c = Category(1, "C")
        self.t = Topic(1, "T", "C:\\user")
        self.d = Document(1, 1, 1, "D")
        self.s = Storage()

    def test_category_init(self):
        self.assertEqual(self.c.id, 1)
        self.assertEqual(self.c.name, "C")

    def test_category_edit(self):
        self.c.edit("new")
        self.assertEqual(self.c.name, "new")

    def test_category_repr(self):
        self.assertEqual(str(self.c), "Category 1: C")

    def test_document_init(self):
        self.assertEqual(self.d.id, 1)
        self.assertEqual(self.d.category_id, 1)
        self.assertEqual(self.d.topic_id, 1)
        self.assertEqual(self.d.file_name, "D")
        self.assertEqual(self.d.tags, [])

    def test_document_from_intsances(self):
        doc = Document.from_instances(1, self.c, self.t, "Doc")
        self.assertEqual(doc.id, 1)
        self.assertEqual(doc.category_id, 1)
        self.assertEqual(doc.topic_id, 1)
        self.assertEqual(doc.file_name, "Doc")
        self.assertEqual(doc.tags, [])

    def test_document_add_tag(self):
        self.d.add_tag("tag")
        self.d.add_tag("tag")
        self.assertEqual(self.d.tags, ["tag"])

    def test_document_remove_tag(self):
        self.d.add_tag("tag")
        self.d.add_tag("tag")
        self.d.remove_tag("tag")
        self.assertEqual(self.d.tags, [])

    def test_document_edit(self):
        self.d.edit("new")
        self.assertEqual(self.d.file_name, "new")

    def test_document_repr(self):
        self.d.add_tag("tag")
        self.assertEqual(str(self.d), 'Document 1: D; category 1, topic 1, tags: tag')

    def test_topic_init(self):
        self.assertEqual(self.t.id, 1)
        self.assertEqual(self.t.id, 1)
        self.assertEqual(self.t.storage_folder, "C:\\user")

    def test_topic_edit(self):
        self.t.edit("new topic", "new folder")
        self.assertEqual(self.t.topic, "new topic")
        self.assertEqual(self.t.storage_folder, "new folder")

    def test_topic_repr(self):
        self.assertEqual(str(self.t), "Topic 1: T in C:\\user")

    def test_storage_init(self):
        self.assertEqual(self.s.categories, [])
        self.assertEqual(self.s.topics, [])
        self.assertEqual(self.s.documents, [])

    def test_storage_add_category(self):
        self.s.add_category(self.c)
        self.s.add_category(self.c)
        self.assertEqual(self.s.categories, [self.c])

    def test_storage_add_topic(self):
        self.s.add_topic(self.t)
        self.s.add_topic(self.t)
        self.assertEqual(self.s.topics, [self.t])

    def test_storage_add_document(self):
        self.s.add_document(self.d)
        self.s.add_document(self.d)
        self.assertEqual(self.s.documents, [self.d])

    def test_storage_edit_category(self):
        self.s.add_category(self.c)
        self.s.edit_category(1, "new")
        self.assertEqual(self.s.categories[0].name, "new")

    def test_storage_edit_topic(self):
        self.s.add_topic(self.t)
        self.s.edit_topic(1, "new", "new storage")
        self.assertEqual(self.s.topics[0].topic, "new")
        self.assertEqual(self.s.topics[0].storage_folder, "new storage")

    def test_storage_edit_document(self):
        self.s.add_document(self.d)
        self.s.edit_document(1, "new")
        self.assertEqual(self.s.documents[0].file_name, "new")

    def test_storage_delete_category(self):
        self.s.add_category(self.c)
        self.s.delete_category(1)
        self.assertEqual(self.s.categories, [])

    def test_storage_delete_topic(self):
        self.s.add_topic(self.t)
        self.s.delete_topic(1)
        self.assertEqual(self.s.topics, [])

    def test_storage_delete_document(self):
        self.s.add_document(self.d)
        self.s.delete_document(1)
        self.assertEqual(self.s.documents, [])

    def test_storage_repr(self):
        self.s.add_category(self.c)
        self.s.add_topic(self.t)
        self.s.add_document(self.d)
        expected = str(self.s).strip('\n')
        self.assertEqual(expected, "Document 1: D; category 1, topic 1, tags: ")


if __name__ == "__main__":
    unittest.main()
