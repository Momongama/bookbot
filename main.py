def main():
    book_path = "/home/momongama/workspace/github.com/momongama/bookbot/books/frankestein.txt"
    file_contents = get_book_txt(book_path)

    print(f"There are {count_words(file_contents)} words in this book.")
    print(f"The characters distribution is as follows:\n{report(count_letters(file_contents))}\n\n-- End report --")


def get_book_txt(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    ldict = {}
    for char in text:
        if char != " " and char != "\n":
            if ldict.get(char.lower()) is None:
                ldict[char.lower()] = 1
            else:
                ldict[char.lower()] += 1
    return ldict

def report(chars):
    let_list = []
    for key in chars:
        let_list.append(f"The {key} character was found {chars[key]} times")
    return "\n".join(let_list)


main()
