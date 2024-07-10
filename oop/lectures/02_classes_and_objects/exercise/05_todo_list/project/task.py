class Task:
    def __init__(self, task_name: str, task_date: str):
        self.name = task_name
        self.due_date = task_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        if new_name != self.name:
            self.name = new_name
            return self.name
        return "Name cannot be the same."

    def change_due_date(self, new_date: str):
        if new_date != self.due_date:
            self.due_date = new_date
            return self.due_date
        return "Date cannot be the same."

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if 0 <= comment_number < len(self.comments):
            self.comments[comment_number] = new_comment
            return ', '.join(self.comments)
        return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"