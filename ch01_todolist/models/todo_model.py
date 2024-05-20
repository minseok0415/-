class TodoList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)
        
    def get_tasks(self):
        return self.tasks
    
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
    
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True