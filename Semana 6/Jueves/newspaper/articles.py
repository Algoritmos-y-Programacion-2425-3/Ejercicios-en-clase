class Article:
    def __init__(self,title, sum_up, body, images, creation_date, writer):
        self.title = title
        self.sum_up = sum_up
        self.body = body
        self.images = images
        self.publish_date = None
        self.creation_date = creation_date
        self.writer = writer

    def show(self):
        print(f"{self.title} - {self.writer.name}")