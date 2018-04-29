import tkinter
import pyaramorph
import naftawayh.wordtag
import nltk
n=naftawayh
p=pyaramorph.Analyzer()
class GUI:
    def definArab(self,arab):
        self.arab=arab
    def ui(self):
        self.root=tkinter.Tk()
        self.root.title("Task ")
        self.root.geometry("750x500")
        self.lb1=tkinter.Label(self.root,text="Enter the sentence : ")
        self.lb1.grid(row=0,column=0)
        self.en1=tkinter.Entry(self.root)
        self.en1.grid(row=0,column=1,columnspan=5)

        self.bt1=tkinter.Button(self.root,text="Analyzer",relief='raised')
        self.bt1.grid(row=7,column=0,columnspan=1)
        self.bt1['command']=  lambda: self.Analyiz(self,self.en1.get())

        self.bt2=tkinter.Button(self.root,text="Translate",relief='raised')
        self.bt2.grid(row=7,column=1,columnspan=1)
        self.bt2['command']=  lambda: self.Translate(self,self.en1.get())

        self.bt3=tkinter.Button(self.root,text="POS",relief='raised')
        self.bt3.grid(row=7,column=3,columnspan=1)
        self.bt3['command']=  lambda: self.POS(self,self.en1.get())

        self.lb3=tkinter.Label(self.root,text="result : ")
        self.lb3.grid(row=10,column=0)
        self.root.mainloop()
    def printResult(self,text):
        self.lb3=tkinter.Label(self.root,text=text)
        self.lb3.grid(row=10,column=0)
    def Analyiz(self,text):
       ArabicAnalyzer.analysText(self,text)

    def Translate(self,text):
        ArabicAnalyzer.translate(self,text)

    def POS(self,text):
        sent=text
        ArabicAnalyzer.pos_naftawy(self,sent)
class ArabicAnalyzer:
    gui=GUI
    def __int__(self):
        print("starting .......")
    def analysText(self,text):
        print(text)
        p=pyaramorph.Analyzer()
        text=text.split()
        for w in text:
            self.printResult(self,p.analyze_text(w))
            #print(p.analyze_text(w))


    def root(word):
        st =nltk.ISRIStemmer()
        tokens=nltk.word_tokenize(word)
        result=[st.stem(w) for w in tokens]
        return result

    def translate(self,sent):
        sent=sent.split()
        for w in sent:
            w=ArabicAnalyzer.root(w)[0]
            text=p.analyze_text(w)
        #print(text)
        ##translate
            gloss=dict()
            gloss=text[0][1].split(',')[0]
            sol=gloss.split()[-5:]
            self.printResult(self,sol)
            print(sol)


    def pos_naftawy(self,text):
        word_list=text.split()
        word_list=set(word_list)
        tagger = naftawayh.wordtag.WordTagger()
        list_tags = tagger.word_tagging(word_list)
        for word,tag in zip(word_list,list_tags):
            print(word,tag)
        tagger = naftawayh.wordtag.WordTagger();

        previous_word=""
        sol=''
        for word in word_list:
            tag=tagger.context_analyse(previous_word,word);
            st='.'.join((word,tag))
            sol=sol+st
            print(u"%s from context is %s "%(word,tag))
            previous_word=word;
        self.printResult(self,sol)
arab=ArabicAnalyzer
ui=GUI
ui.definArab(ui,arab)
ui.ui(ui)




