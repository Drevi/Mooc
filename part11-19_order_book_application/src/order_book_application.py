# Write your solution here
# If you use the classes made in the previous exercise, copy them here

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


class OrderBookApplication:
    def __init__(self):
        self._order_book = OrderBook()

    def help(self):
        print("commands:\n0 exit\n1 add order\n2 list finished tasks\n3 list unfinished tasks\n4 mark task as finished\n5 programmers\n6 status of programmer")

    def add_order(self):
        description = input("description: ")
        programmer_workload = input("programmer and workload estimate: ").split()
        try:
            self._order_book.add_order(description, programmer_workload[0], int(programmer_workload[1]))
            print("added!")
        except:
            print("erroneous input")
        
    def list_finished_tasks(self):
        if self._order_book.finished_orders():
            for order in self._order_book.finished_orders():
                print(order)
        else:
            print("no finished tasks")

    def list_unfinished_tasks(self):
        if self._order_book.unfinished_orders():
            for order in self._order_book.unfinished_orders():
                print(order)
        else:
            print("no unfinished tasks")

    def mark_finished(self):
        id = input("id: ")
        try:
            self._order_book.mark_finished(int(id))
            print("marked as finished")
        except:
            print("erroneous input")
    
    def programmers(self):
        for programmer in self._order_book.programmers():
            print(programmer)


    def status_of_programmer(self):
        programmer = input("programmer: ")
        try:
            status = self._order_book.status_of_programmer(programmer)
            print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")
        except ValueError:
            print("erroneous input")

    def execute(self):
        self.help()        
        while True:
            command = input("command: ")            
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.status_of_programmer()


program = OrderBookApplication()
program.execute()





