# Book inventory management module

inventory = []

def add_book(title, author, isbn, quantity=1):
    """Add a book to the inventory"""
    for book in inventory:
        if book['isbn'] == isbn:
            book['quantity'] += quantity
            print(f"Updated quantity for '{title}' to {book['quantity']}")
            return
    
    new_book = {
        'title': title,
        'author': author,
        'isbn': isbn,
        'quantity': quantity
    }
    inventory.append(new_book)
    print(f"Added '{title}' to inventory")

def remove_book(isbn, quantity=1):
    """Remove a book from inventory"""
    for book in inventory:
        if book['isbn'] == isbn:
            if book['quantity'] > quantity:
                book['quantity'] -= quantity
                print(f"Removed {quantity} copy/copies of '{book['title']}'")
            elif book['quantity'] == quantity:
                inventory.remove(book)
                print(f"Removed all copies of '{book['title']}' from inventory")
            else:
                print(f"Cannot remove {quantity} copies - only {book['quantity']} available")
            return
    
    print(f"Book with ISBN {isbn} not found in inventory")

def display_inventory():
    """Display current inventory"""
    if not inventory:
        print("Inventory is empty")
        return
    
    print("\nCurrent Inventory:")
    print("-" * 50)
    for book in inventory:
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"ISBN: {book['isbn']}")
        print(f"Quantity: {book['quantity']}")
        print("-" * 30)