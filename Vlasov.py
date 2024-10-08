# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vlasov.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 339)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 30, 565, 211))
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 260, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 260, 141, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 260, 141, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 260, 141, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.tableWidget.setHorizontalHeaderLabels(["ФИО", "Отдел", "Кол-во рабочих дней", "Зарплата"])

        self.tableWidget.setColumnWidth(2, 130)
        self.tableWidget.setColumnWidth(0, 200)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.load_data)
        self.pushButton_2.clicked.connect(self.add_row)  # Добавляем обработчик для кнопки "Добавить данные"
        self.pushButton_3.clicked.connect(self.save_data)  # Добавляем обработчик для кнопки "Сохранить данные"
        self.pushButton_4.clicked.connect(self.delete_row)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Загрузить данные"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить данные"))
        self.pushButton_3.setText(_translate("MainWindow", "Изменить данные"))
        self.pushButton_4.setText(_translate("MainWindow", "Удалить данные"))

    def load_data(self):
        """Загружает данные из файла salary.txt в таблицу."""
        with open("salary.txt", "r", encoding='utf-8') as file:
            data = file.readlines()

        # Очищаем таблицу
        self.tableWidget.setRowCount(0)

        # Добавляем данные в таблицу
        for row, line in enumerate(data):
            # Разделяем строку на элементы
            elements = line.strip().split(",")
            self.tableWidget.insertRow(row)

            # Вставляем элементы в столбцы
            for col, element in enumerate(elements):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(element))

    def add_row(self):
        """Добавляет новую пустую строку в таблицу."""
        row_count = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row_count + 1)  # Увеличиваем количество строк

        # Добавляем пустые ячейки в новой строке
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.setItem(row_count, i, QtWidgets.QTableWidgetItem(""))

    def save_data(self):
        """Сохраняет данные из таблицы в файл salary.txt."""
        with open("salary.txt", "w", encoding='utf-8') as file:
            for row in range(self.tableWidget.rowCount()):
                row_data = []
                for col in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, col)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")
                file.write(",".join(row_data))  # Убираем лишний перенос строки
                if row < self.tableWidget.rowCount() - 1:  # Добавляем перенос строки, если это не последняя строка
                    file.write("\n")

    def delete_row(self):
        """Удаляет выбранную строку из таблицы и файла salary.txt."""
        selected_row = self.tableWidget.currentRow()
        if selected_row != -1:  # Проверяем, выбрана ли строка
            self.tableWidget.removeRow(selected_row)

            # Обновляем файл salary.txt
            with open("salary.txt", "r", encoding='utf-8') as file:
                data = file.readlines()

            with open("salary.txt", "w", encoding='utf-8') as file:
                for i, line in enumerate(data):
                    if i != selected_row:
                        file.write(line)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
