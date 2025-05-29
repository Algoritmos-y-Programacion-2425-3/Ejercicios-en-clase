from articles import Article

class Employee:
    def __init__(self, name, dni):
        self.name = name
        self.dni = dni

class WriterManager(Employee):
    def __init__(self, name, dni, writers):
        super().__init__(name, dni)
        self.writers = writers

    def supervise(self):
        print("Supervising...")

    def choose_article(self, articles):
        print("The selected article is...")

class Writer(Employee):
    def __init__(self, name, dni):
        super().__init__(name, dni)
        
    def write_article(self):
        print("Writing...")
        return Article(
            input("Please enter a title: "),
            input("Please enter a sum up: "),
            input("Please enter a body: "),
            [],
            input("Please enter a date: "),
            self
        )