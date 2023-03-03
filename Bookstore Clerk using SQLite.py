#Ebookstore Database using SQLite

import sqlite3

db = sqlite3.connect("ebookstore_db")


cursor = db.cursor()

#create book table in database

cursor.execute('''
    CREATE TABLE books(id INTEGER PRIMARY KEY,
                                    Title TEXT,
                                    Author TEXT,
                                    Qty INTEGER)
                ''')
db.commit()


#insert the task data into book table
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
VALUES (3001, 'A Tale of Two Cities','Charles Dickens', 30),
(3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
(3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
(3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
(3005, 'Alice in Wonderland', 'Lewis Carroll', 12)''')

db.commit()

#present task menu to user
while True:
    user_choice = input("Please enter one of the following options (e.g. 1)\n"
                        "1. add new books to the database\n"
                        "2. update book information\n"
                        "3. delete books from the database\n"
                        "4. search the database to find a specific book\n"
                        "0. exit:  ")

    #allow user to add a new book to database by inputting relevant data
    if user_choice == '1':
        try:
            new_id = int(input("Please enter the id number of the new book (e.g. 3001): "))
            new_title = input("Please enter the title of the new book: ")
            new_author = input("Please enter the author of the new book: ")
            new_qty = int(input("Please enter the quantity of the new book: "))


            cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
            VALUES (?,?,?,?)''', (new_id, new_title, new_author, new_qty))

            db.commit()

            print(f"You have now added the book {new_title} to the ebookstore!")

        # tryexcept block catches crash incase user inputs incorrect value e.g. book id already exists or quantity is not a number
        except:
            print("One of the values you have entered is invalid, please try again!")

    #allow user to update an existing book record in database - within while loop so they can return to this submenu after choosing an option
    #allow user to choose what field of the book they want to update(id, title, author, or stock)
    elif user_choice == '2':

        while True:
            update_choice = input("Please enter one of the following options: \n"
                                     "'id' - update book id\n"
                                     "'title' - update book title\n"
                                     "'author' - update book author\n"
                                     "'qty' - update book stock\n "
                                     "'m' - return to main menu: ")

            if update_choice == 'id':

                original_id = int(input("Please enter the id of the book you would like to update: "))
                updated_id = int(input("Please enter the updated id of selected book: "))

                cursor.execute('''UPDATE books SET id = ? WHERE id = ?''', (updated_id, original_id))

                print("You have updated the id!")

                db.commit()

            elif update_choice == 'title':

                id = int(input("Please enter the id number of the book you would like to update (e.g. 3001): "))
                new_title = input("Please enter the updated title of the book: ")

                cursor.execute('''UPDATE books SET Title = ? WHERE id = ?''', (new_title, id))

                print(f"You have updated the title of book id {id}!")

                db.commit()


            elif update_choice == 'author':
                id = int(input("Please enter the id number of the book you would like to update (e.g. 3001): "))
                new_author = input("Please enter the updated author of the book: ")

                cursor.execute('''UPDATE books SET Author = ? WHERE id = ?''', (new_author, id))

                print(f"You have updated the author of book id {id}!")

                db.commit()


            elif update_choice == 'qty':
                id = int(input("Please enter the id number of the book you would like to update (e.g. 3001): "))
                new_qty = input("Please enter the updated quantity of the book: ")
                cursor.execute('''UPDATE books SET Qty = ? WHERE id = ? ''', (new_qty, id))

                print(f"You have updated the stock of book id {id}!")

                db.commit()

            elif update_choice == 'm':
                break

            # if user does not enter a valid input then this else statement catches it
            else:
                print("You have not entered a valid selection")

    # allow user to delete a book record from database - we use id as it is the primary key
    elif user_choice == '3':
        id = int(input("Please enter the id number of the book you would like to delete (e.g. 3001): "))
        cursor.execute('''DELETE FROM books WHERE id = ? ''', (id,))
        print(f"You have deleted the book with book id {id}!")

        db.commit()

    # allow user to search for a book in database either by id number or title of the book - if user selects title there may be multiple records displayed if there are multiple books with the same title in the database
    elif user_choice == '4':
        while True:
            search_choice = input("Please enter of the following options:\n"
                                  "'id' - search database by book id \n"
                                  "'title' - search database by book title\n"
                                  "'m' - return to main menu: ")

            if search_choice == 'id':
                id = int(input("Please enter the book id (e.g. 3001): "))

                cursor.execute('''SELECT Title, Author, Qty FROM books WHERE id = ?''', (id,))
                print(f"The database has the following record for book id {id} (Title, Author, and Quantity in stock): ", cursor.fetchall())


            elif search_choice == 'title':
                book_title = input("Please enter the title of the book: ")
                cursor.execute('''SELECT id, Title, Author, Qty FROM books WHERE Title = ?''', (book_title,))
                print(f"The database has the following records with the requested title(book id, title, author, quantity in stock): ", cursor.fetchall())

            elif search_choice == 'm':
                break

            else:
                print("You have not entered a valid choice")

    elif user_choice == '0':
        break

    #if user does not enter a valid input then this else statement catches it
    else:
        print("You have not entered a valid selection")
