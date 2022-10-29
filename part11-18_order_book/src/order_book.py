# Write your solution here:

class Task:
    id = 0

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        Task.id += 1
        self.id = Task.id
        self._finished = False
    
    def is_finished(self):
        return self._finished
    
    def mark_finished(self):
        self._finished = True
    
    def __str__(self) -> str:
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} " + ("FINISHED" if self.is_finished() else "NOT FINISHED")
    

class OrderBook:
    def __init__(self):
        self._orders = []

    def add_order(self, description, programmer, workload):
        self._orders.append(Task(description, programmer, workload))
    
    def all_orders(self):
        return self._orders

    def programmers(self):
        return list(set([task.programmer for task in self._orders]))


    def mark_finished(self, id: int):
        for order in self.all_orders():
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError("ID not found")

    def finished_orders(self):
        return [order for order in self.all_orders() if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self.all_orders() if not order.is_finished()]

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("Programmer not found")
        finished_tasks = [task for task in self.all_orders() if task.programmer == programmer and task.is_finished()]
        unfinished_tasks = [task for task in self.all_orders() if task.programmer == programmer and not task.is_finished()]
        finished_workload = sum(task.workload for task in finished_tasks)
        unfinished_workload = sum(task.workload for task in unfinished_tasks)
        
        return (len(finished_tasks), len(unfinished_tasks), finished_workload, unfinished_workload)