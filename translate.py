from nltk.stem import WordNetLemmatizer


class MainTranslation:
    """
    Класс для Лемметизации английских слов
    """
    def __init__(self):
        self.word=''
        self.list_txt=[]
        self.new_correct_list=[]
        self.__lemmatizer = WordNetLemmatizer()
        
    def get_text(self):
        return self.new_correct_list

    def set_text(self, text):
        self.word = text 

    def splitting_text(self):
        return self.word.split()

    def check_correct(self): #TODO исправить то, что склеивает строки при словах в скобках
        buf=''
        self.list_txt=self.word.split()
        for i in self.list_txt:
            buf=''
            if i.isalpha() == False:
                for p in i:
                    if (ord(p)>64 and ord(p)<91) or (ord(p)>96 and ord(p)<123):
                        buf+=p
                self.new_correct_list.append(self.__lemmatizer.lemmatize(buf))
            else: 
                self.new_correct_list.append(i)

    def second_version_correct(self,word):
        """
        Второй варинт для передачи слова уже из другого места 
        """
        buf=''
        if word.isalpha() == False:
            for p in word:
                if (ord(p)>64 and ord(p)<91) or (ord(p)>96 and ord(p)<123):
                    buf+=p
            return self.__lemmatizer.lemmatize(buf)
        else:
            return self.__lemmatizer.lemmatize(word)


            #word.translate(None, ''.join(chars_to_remove))   будет использоваться с удалением символов
        

# TODO if word be clear 
#class Translation(MainTranslation):
    #def splitting_text(self):
        #print(self.lemmatizer.lemmatize())
