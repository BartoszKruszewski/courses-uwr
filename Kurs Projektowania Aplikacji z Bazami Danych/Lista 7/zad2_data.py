from datetime import datetime

books_data = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "copies": [
            {"copy_id": "A101", "status": "available"},
            {"copy_id": "A102", "status": "borrowed"}
        ]
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "copies": [
            {"copy_id": "B201", "status": "available"},
            {"copy_id": "B202", "status": "available"}
        ]
    }
]

readers_data = [
    {
        "id": "R001",
        "name": "Alice Johnson",
        "borrowings": [
            {"copy_id": "A101", "borrow_date": datetime(2023, 2, 15), "return_date": datetime(2023, 3, 1)},
            {"copy_id": "B201", "borrow_date": datetime(2023, 3, 10), "return_date": None}
        ]
    },
    {
        "id": "R002",
        "name": "Bob Smith",
        "borrowings": [
            {"copy_id": "A102", "borrow_date": datetime(2023, 3, 5), "return_date": None},
            {"copy_id": "B202", "borrow_date": datetime(2023, 3, 15), "return_date": None}
        ]
    }
]