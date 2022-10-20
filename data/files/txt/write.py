def search(file_path):
    sections = ""
    books = "Books:\n"

    with open(file_path) as file:
        for line in file:
            if "Section" in line:
                # Add to section string
                sections += line
                pass
            else:
                # Add to books string
                books += line
                pass

    print(sections)
    print(books)


search("books.txt")
