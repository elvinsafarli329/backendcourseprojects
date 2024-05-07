class Reading():
    attribute = "book"

    def __init__(self, name, genre, language, page_count, author, date):
        self.name = name
        self.genre = genre
        self.language = language
        self.page_count = page_count
        self.author = author
        self.date = date

    def book_color(self, book_color=True):
        if book_color == False:
            return "the pages are not yellow"
        else:
            return "the pages are yellow"
        
    def book_style(self):
        return f"{self.name} has a hard cover"
    
    def book_overview(self):
        return f"{self.name} by {self.author} was published in {self.date}"

first_book = Reading("Inferno", "adventure", "english", 500, "Dan Brown", 2007)
second_book = Reading("Animal Farm", "classic", "russian", 800, "G.Orwell", 2000)       
third_book = Reading("Mavi Melekler", "mystery", "azerbaijani", 300, "C.Abdullayev", 2017)

print(Reading.attribute)

print(f"{first_book.name} and {second_book.name} are interesting books. {first_book.name} is written in {first_book.language} and has {first_book.page_count} pages.")

print(f"The pages of {first_book.name} book are {first_book.book_color(True)}")

print(third_book.book_overview())

print(first_book.book_style())
