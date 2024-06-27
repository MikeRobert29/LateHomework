#coding : utf-8

LIBRARY = {"Pride and Prejudice" : ["Fiction", 200], "1984" : ["Fiction", 100], "To Kill a Mockingbird" : ["Fiction", 125], "The Diary of a Young Girl" : ["Non-fiction", 185], "Steve Jobs" : ["Non-fiction", 250], "Sapiens" : ["Non-fiction", 300], "The Waste Land" : ["Poetry", 100], "Leaves of Grass" : ["Poetry", 125], "Les Fleurs du mal" : ["Poetry", 150], "Romeo and Juliet" : ["Drama", 230], "Harry Potter" : ["Children Literature", 80], "Le Petit Prince" : ["Children Literature", 90], "Les Liaisons dangereuses" : ["Epistolary Literature", 250]}

genres  = ["Fiction", "Non-fiction", "Poetry", "Drama", "Children Literature", "Epistolary Literature"]

def add_book() :

    newBook = input("\n\t\t\tEnter the title, genre, and price of the book separated by a vertical bar | character : ")

    i = newBook.index("|")

    LIBRARY[newBook[0 : i]] = newBook[i + 1 : ].split("|")

    LIBRARY[newBook[0 : i]][1] = int(LIBRARY[newBook[0 : i]][1])

    if LIBRARY[newBook[0 : i]][0] not in genres :
        genres.append(LIBRARY[newBook[0 : i]][0])

def remove_book() :

    book = input("\n\t\t\tWich book you want to remove? ")

    if book in LIBRARY :

        LIBRARY.pop(book)
        print("\n\t\t\tThe has been removed from de library successfully")

    else :
        print("\n\t\t\tUuuuuuuh...we don't have this book actually.")

def get_book_info() :

    book = input("\n\t\t\tFine, wich book you want to know about? ")
    
    if book in LIBRARY :
        print("\n\t\t\tAs you know this book is called {};".format(book))
        print("\n\t\t\tIt's a {} book and the price is {} dollars.".format(LIBRARY[book][0], LIBRARY[book][1]))

def list_books():
    
    if not LIBRARY :
        print("\n\t\t\tThe library is empty, youn can had one if you want.")

    for title in sorted(LIBRARY.keys()):
        print("\n\t\t\t{}".format(title))

def list_books_by_genre() :

    for genre in genres :
        booksInThisGrenre = []

        for book in LIBRARY :

            if genre in LIBRARY[book] :
                booksInThisGrenre.append(book)

        print("\n\t\t\t", genre.upper().center(50, "-"), "\n")

        for livre in booksInThisGrenre :
            print("\t\t\t", livre.title().center(50, " "))


file = open("book.txt", "r")
content = file.read()
print(content)

while True :

    choice = input("\n\t\t\tEnter your choice (1-6) : ")

    if choice == "1":
        add_book_return = add_book()
        if add_book_return:
            list_books()
    elif choice == "2":
        remove_book_return = remove_book()
        if remove_book_return:
            list_books()
    elif choice == "3":
        get_book_info()
    elif choice == "4":
        list_books()
    elif choice == "5":
        list_books_by_genre()
    elif choice == "6":
        break
    else:
        print("\n\t\t\tInvalid choice. Please enter a number between 1 and 6.")

print("\n\n\t\t\t\tGOODBYE, COME BACK ANY TIME :) !\n")