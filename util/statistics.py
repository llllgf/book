from xlsxwriter import Workbook

from book.settings import TEMP_PATH
from books.models import Grade,  Order


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


    def excel_sheet(self, workbook:Workbook,name, orders: list[Order]):
        ll=["书名", "单价（元）", "作者","数量","总价（元）"]
        sheet=workbook.add_worksheet(name)
        for i,title in enumerate(ll):
            sheet.write(0,i,title)
        for i,order in enumerate(orders):
            i+=1
            book=order.book
            sheet.write(i,0,book.name)
            sheet.write(i,1,book.price/100)
            sheet.write(i,2,book.author)
            sheet.write(i,3,self.get_students_count())
            sheet.write(i,4,f"=B{i+1}*D{i+1}")
        sheet.write(len(orders)+1,4,f"=SUM(E2:E{len(orders)+1})")



    def excel(self):
        path = f"{TEMP_PATH}/{self.grade.name}.xlsx"
        workbook =Workbook(path)
        orders=[]
        semesters = self.get_semester_order()
        for semester in semesters:
            order=semester.order_set.all()
            orders.extend(order)
            self.excel_sheet(workbook,semester.name,order)
        self.excel_sheet(workbook,"总览",orders)
        workbook.close()
        return path

