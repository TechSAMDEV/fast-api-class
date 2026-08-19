from fastapi import FastAPI

# DATABASE book libary
books_db = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "Rich dad, Poor dad", "author": " Robert Kiyosak"},
]

app = FastAPI()

# HTTP get endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Digital Library API!"}

@app.get("/books")
def libary():
    return books_db

@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = next((b for b in books_db if b["id"] == book_id), None)
    return book
        