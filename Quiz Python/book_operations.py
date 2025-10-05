import math
from datetime import datetime, timedelta

borrowed_books = []

def borrow_book(isbn, borrower_name, days=14):
    """Borrow a book from inventory"""
    from book_inventory import inventory
    
    for book in inventory:
        if book['isbn'] == isbn and book['quantity'] > 0:
            due_date = datetime.now() + timedelta(days=days)
            borrowed_book = {
                'isbn': isbn,
                'title': book['title'],
                'borrower': borrower_name,
                'borrow_date': datetime.now(),
                'due_date': due_date,
                'returned': False
            }
            borrowed_books.append(borrowed_book)
            book['quantity'] -= 1
            print(f"'{book['title']}' borrowed by {borrower_name}. Due: {due_date.strftime('%Y-%m-%d')}")
            return True
    
    print(f"Book with ISBN {isbn} not available for borrowing")
    return False

def return_book(isbn, borrower_name):
    """Return a borrowed book"""
    for book in borrowed_books:
        if book['isbn'] == isbn and book['borrower'] == borrower_name and not book['returned']:
            book['returned'] = True
            book['return_date'] = datetime.now()
            
            # Update inventory
            from book_inventory import inventory
            for inv_book in inventory:
                if inv_book['isbn'] == isbn:
                    inv_book['quantity'] += 1
                    break
            
            # Calculate fine if overdue
            fine = calculate_fine(book['due_date'], book['return_date'])
            if fine > 0:
                print(f"Book returned. Overdue fine: ${fine:.2f}")
            else:
                print("Book returned on time. Thank you!")
            return True
    
    print(f"No matching borrowed book found")
    return False

def calculate_fine(due_date, return_date):
    """Calculate fine for late return using math module"""
    if return_date > due_date:
        days_late = (return_date - due_date).days
        # Fine formula: $0.50 per day, with $2 minimum
        fine = max(2, 0.5 * days_late)
        return math.ceil(fine * 100) / 100  # Round up to nearest cent
    return 0

def check_availability(isbn):
    """Check if a book is available"""
    from book_inventory import inventory
    
    for book in inventory:
        if book['isbn'] == isbn:
            return book['quantity'] > 0
    return False

# Lambda function to filter overdue books
get_overdue_books = lambda: list(filter(
    lambda book: not book['returned'] and datetime.now() > book['due_date'],
    borrowed_books
))

# List comprehension for borrowed books report
def generate_borrowed_report():
    """Generate report of currently borrowed books"""
    current_borrowed = [book for book in borrowed_books if not book['returned']]
    
    print("\nBorrowed Books Report:")
    print("-" * 60)
    for book in current_borrowed:
        status = "OVERDUE" if datetime.now() > book['due_date'] else "On Time"
        print(f"Title: {book['title']}")
        print(f"Borrower: {book['borrower']}")
        print(f"Due Date: {book['due_date'].strftime('%Y-%m-%d')}")
        print(f"Status: {status}")
        print("-" * 30)