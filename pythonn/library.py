members= { 'A':3, 'B':0, 'C':5, 'D':8, 'E':9 }
books = { 'Python':10, 'DS':5, 'OOPCG': 7, 'DEL':3 }

total_borrowed= sum(members.values())
num_members= len(members)
average= total_borrowed / num_members
print(f"Average books borrowed: {average} ")
print(f"Total biiks borrowed: {total_borrowed}")

max_book = min_book = list(books.keys())[0]
for book in books:
    if books[book] > books[max_book]:
        max_book = book
    elif books[book] < books[min_book]:
        min_book = book

print(f"Most borrowed book: {max_book}")
print(f"Least borrowed book: {min_book}")

zero_count = 0
for borrow in members.keys():
    if borrow ==0:
        zero_count += 1
print(f"Member who borowed 0 books: {zero_count}")

count_freq= {}
for borrow_count in books.values():
    if borrow_count in count_freq:
        count_freq[borrow_count] += 1
    else:
        count_freq[borrow_count] = 1

most_common_count = max(count_freq, key=count_freq.get)
frequent_books = []
for biik, count in books.items():
    if count == most_common_count:
        frequent_books.append(book)

print(f"Most frequently borrowed book: {frequent_books}")
