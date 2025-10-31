# Base Class
class Publication:
    def __init__(self, name:str):
        self.name = name

    def print_info(self):
        print(f'\n"{self.name}"')


# Subclasses
class Book(Publication):
    def __init__(self, name: str, author:str, page_count:int):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        super().print_info()
        print(f'    By: {self.author}\n    Page count: {self.page_count}')


class Magazine(Publication):
    def __init__(self, name: str, chief_editor: str):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_info(self):
        super().print_info()
        print(f'    Chief Editor: {self.chief_editor}')

# Main Program

book = Book("Big Rules", "Jimmy Bob", 648)
magazine = Magazine("Pedicure Digest", "Mr. Nails")

book1 = Book("Small Rules", "Jumbo Bob", 2)
magazine1 = Magazine("Empire Today", "Not Palpatine")

magazine.print_info()
book.print_info()
magazine1.print_info()
book1.print_info()