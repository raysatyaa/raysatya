class Book:
    def __init__(self, title, penulis):
        self.title = title
        self.penulis = penulis

class BookStack:
    def __init__(self):
        self.stack = []

    # Menambahkan Buku
    def add_book(self, book):
        self.stack.append(book)
        print(f"Buku '{book.title}' oleh {book.penulis} telah ditambahkan ke dalam tumpukan.")

    # Menghapus Buku
    def remove_book(self):
        if len(self.stack) > 0:
            book = self.stack.pop()
            print(f"Buku '{book.title}' oleh {book.penulis} telah dihapus dari tumpukan.")
        else:
            print("Tumpukan buku kosong.")

    # Menampilkan Buku Teratas
    def top_book(self):
        if len(self.stack) > 0:
            book = self.stack[-1]
            print(f"Buku teratas: '{book.title}' oleh {book.penulis}.")
        else:
            print("Tumpukan buku kosong.")

    # Menampilkan Seluruh Buku
    def display_books(self):
        if len(self.stack) > 0:
            print("Buku yang tersimpan:")
            for book in self.stack:
                print(f"'{book.title}' oleh {book.penulis}")
        else:
            print("Tumpukan buku kosong.")


book_stack = BookStack()

while True:
    print("\nMenu:")
    print("1. Tambahkan Buku")
    print("2. Hapus Buku Terakhir")
    print("3. Tampilkan Buku Teratas")
    print("4. Tampilkan Semua Buku")
    print("5. Keluar")

    choice = input("Pilih tindakan (1/2/3/4/5): ")

    if choice == "1":
        book_title = input("Masukkan nama buku: ")
        book_penulis = input("Masukkan nama pengarang: ")
        book = Book(book_title, book_penulis)
        book_stack.add_book(book)
    elif choice == "2":
        book_stack.remove_book()
    elif choice == "3":
        book_stack.top_book()
    elif choice == "4":
        book_stack.display_books()
    elif choice == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
