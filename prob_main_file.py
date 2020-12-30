import os
from multiprocessing import Pool

#import slova_eng
#from Py_Docx import File
from PyQt5 import QtWidgets
#from pathlib import Path
import sys # sys нужен для передачи argv в QApplication
#для документов
import first_mainwindow
import works_file
import translate

class ExampleApp(QtWidgets.QMainWindow, first_mainwindow.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле first_mainwindow
        super().__init__()
        self.setupUi(self) # нужно для инициализации дизайна
        self.choose_file.clicked.connect(self.coose_file_function)
        self.batton_save.clicked.connect(self.save_function)
        self.btn_delete_all.clicked.connect(self.delete_all)
        self.button_translate.clicked.connect(self.translation)
        self.buf_text=" "
        self.all_dict=[]
        #self.impl=[]
        
    #Выбор файла для открытия
    def coose_file_function(self):
        #self.listWidget.clear()  # На случай, если в списке уже есть элементы
        """
        Сохранение файла в директорию QtWidgets.QFileDialog.getSaveFileName(self, "Выберите папку")
        Выбор директории getOpenFineNames
        """

        file_path = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите папку", "", "*.docx *.txt")[0]
        print(file_path)

        if not file_path:
            return
        ext = os.path.splitext(file_path)[1]
        
        try:
            source = works_file.SOURCES[ext](file_path)
        except KeyError:
            return

        if not source.parse():
            return
        self.buf_text= source.text
        self.textEdit.setText(source.text)

    #Сохранение в документы 
    def save_function(self):
        save_file=QtWidgets.QFileDialog.getSaveFileName(self, "Выберите папку", "", "*.docx *.txt")[0]
        if not save_file:
            return
        abc=os.path.splitext(os.path.basename(save_file)) #кортеж с именем и типом файла 
        # TODO do open file 
        #переделать вот этот под запись 
        saving = works_file.SOURCES[abc[1]](abc)
        if not saving.save_path(self.buf_text):
            return

    #Получение словаря
    def get_csv_dict(self):
        kran=works_file.CSVSource('red_medical_dictionary.csv')
        self.all_dict=self.all_dict+kran.get_dict()

    #Передача счетчику значения 
    def see_my_counter(self, number):
        self.words_counter.display(number)

    #Очистка всех полей
    def delete_all(self):
        self.textEdit.setText("")
        self.textEdit_2.setText("")

    #Получение текста с поля ввода
    def get_text_from_edittext(self):
        return self.textEdit.toPlainText().split()

    #Перевод слов
    def translation(self):  #функция для сборки перевода
        slova=''
        perevod=translate.MainTranslation()
        kran=works_file.CSVSource('red_medical_dictionary.csv')
        #kran.get_dict_in_this_class()
        kran.get_dict_terms()

        with Pool(4) as p:
            res=p.map(perevod.second_version_correct,self.get_text_from_edittext())
            res=list(filter(self.filtration,res))
            res.append('***01010***')
            print('finish translate==========',res)
        tic=list(map(kran.check_dict_for_word,res))
        print('finish check==============')
        tic=list(filter(self.filtration,tic))
        self.see_my_counter(len(tic))
            #tic=list(set(tic))
            #list(set(tic))
            #self.textEdit_2.setText(tic)
        
        for i in tic:
            for j in i:
                slova=slova + j +'\n'
        print(slova)
        self.textEdit_2.setText(slova)

#ANTEPOSITION, ANTICARIOGENIC ACTIVITY, (hello world), ANTI-IMPLANTATION ACTIVITY
    def filtration(self,x):
        if x==' ' or x==None or x=="" or x==[]:
            return 0
        else:
            return 1


"""
    class Check_dict(object):
        def __init__(self):
            self.lol_word=[]
        
        def check(self):
            pass
"""

def main():
    app = QtWidgets.QApplication(sys.argv) # Новый экземпляр QApplication
    window = ExampleApp() #создадим объект нового класса интерфейса
    window.show()# показываем окно 
    sys.exit(app.exec_()) # запускаем приложениe
    # #transfer=File_transfer()
    #window.get_csv_dict()

if __name__ == "__main__": #если запускаем файл напрямую, а не импортируем 
    main()# то запускаем функцию main() ['ANTICARIOGENIC ACTIVITY']


#cx_freez
#pyinstaller