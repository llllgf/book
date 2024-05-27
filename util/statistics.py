from books.models import Grade


class Grade_Statistics:
    def __init__(self, grade, semester="0"):
        self.grade = Grade.objects.get(id=grade)
        self.students = self.grade.student_set.all()
        self.semester = semester
    def get_students(self):
        return self.students

    def get_students_count(self):
        return len(self.students)

    def get_semester_order(self):
        return self.grade.semesterorder_set.all()

    def get_books(self):
        books = []
        if self.semester == "0":
            for semester in self.get_semester_order():
                orders = semester.order_set.all()
                for order in orders:
                    books.append(order.book)
        else:
            semester = self.grade.semesterorder_set.get(id=self.semester)
            orders = semester.order_set.all()
            for order in orders:
                books.append(order.book)
        return books

    def get_books_count(self):
        books = self.get_books()
        return len(books)

    def get_books_price(self):
        books = self.get_books()
        price = 0
        for book in books:
            price += book.price
        return price * self.get_students_count() / 100

    def csv(self):
        import csv
        import os
        books = self.get_books()
        with open(f"{os.getcwd()}/books.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["书名", "价格", "出版社", "作者", "ISBN"])
            for book in books:
                writer.writerow([book.name, book.price, book.publish, book.author, book.ISBN])
        return f"{os.getcwd()}/books.csv"
