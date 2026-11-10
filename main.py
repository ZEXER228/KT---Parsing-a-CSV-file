def get_books(filename):
    with open(filename, encoding="utf-8") as file:
        rows = file.read().splitlines()[1:]
    return list(map(lambda row: [*row.split("|")[:3], int(row.split("|")[3]), float(row.split("|")[4])], rows))


def filtered_books(books, parameter):
    return list(map(
        lambda book: [book[0], f"{book[1]}, {book[2]}", book[3], book[4]],
        filter(lambda book: parameter.lower() in book[1].lower(), books)
    ))


def calculate_prices(books):
    return list(map(lambda book: (book[0], book[2] * book[3]), books))