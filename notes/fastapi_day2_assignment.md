# Assignment: Building Your First FastAPI App (Day 2)

## Objective
Practice creating **GET** and **POST** endpoints in FastAPI. You will build a mini-API to manage a small collection of books, work with path parameters, and use Pydantic models to handle request bodies.

---

## Task 1: Setup and GET Endpoints
1. Create a new Python file named `main.py` and import `FastAPI`.
2. Initialize your app instance: `app = FastAPI()`.
3. Create a global Python list to act as your temporary database:
   ```python
   books_db = [
       {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
       {"id": 2, "title": "1984", "author": "George Orwell"}
   ]
   ```
4. **Create a `GET` endpoint** at the root URL (`/`) that returns a welcome message:
   * **Response format:** `{"message": "Welcome to the Digital Library API!"}`
5. **Create a `GET` endpoint** at `/books` that returns the entire `books_db` list.
6. **Create a `GET` endpoint** at `/books/{book_id}`:
   * It must take a path parameter named `book_id` (type: `int`).
   * It should search `books_db` and return only the book matching that ID.

---

## Task 2: POST Endpoint & Pydantic
1. Import `BaseModel` from `pydantic`.
2. Create a Pydantic schema class named `Book` that inherits from `BaseModel`. Define three fields:
   * `id`: integer
   * `title`: string
   * `author`: string
3. **Create a `POST` endpoint** at `/books` that receives a `Book` object from the request body.
4. Inside this endpoint function, convert the Pydantic data to a dictionary and append it to your `books_db` list.
5. Return a confirmation message along with the newly added book.

---

## Task 3: Running and Testing Your API
1. Start your local server using Uvicorn in your terminal:
   ```bash
   uvicorn main:app --reload
   ```
2. Open your browser and navigate to the automatic interactive documentation: `http://127.0.0.1:8000/docs`.
3. Use the Swagger UI to test all your endpoints:
   * Try fetching all books.
   * Try fetching a specific book by ID (e.g., `/books/1`).
   * Send a `POST` request to add a new book and verify it now appears in your `GET /books` list.
