#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 17:10:08 2021

@author: elturayev
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
class Oyna(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.start()
    def start(self):
        self.yozuv=QtWidgets.QLineEdit(self)
        self.yozuv.setGeometry(50,50,463,45)
        self.yozuv1=QtWidgets.QTextEdit(self)
        self.yozuv1.setGeometry(50,100,463,45)
        self.button1=QtWidgets.QPushButton(self)
        self.button1.setGeometry(50,200,60,40)
        self.button1.setText("1")
        self.button1.setFont(QFont("Times",18))
        self.button2=QtWidgets.QPushButton(self)
        self.button2.setGeometry(150,200,60,40)
        self.button2.setText("2")
        self.button2.setFont(QFont("Times",18))
        self.button3=QtWidgets.QPushButton(self)
        self.button3.setGeometry(250,200,60,40)
        self.button3.setText("3")
        self.button3.setFont(QFont("Times",18))
        self.bolish=QtWidgets.QPushButton(self)
        self.bolish.setGeometry(350,200,60,40)
        self.bolish.setText("/")
        self.qavs2=QtWidgets.QPushButton(self)
        self.qavs2.setGeometry(450,200,60,40)
        self.qavs2.setText("(")
        self.bolish.setFont(QFont("Times",18))
        self.button4=QtWidgets.QPushButton(self)
        self.button4.setGeometry(50,250,60,40)
        self.button4.setText("4")
        self.button4.setFont(QFont("Times",18))
        self.button5=QtWidgets.QPushButton(self)
        self.button5.setGeometry(150,250,60,40)
        self.button5.setText("5")
        self.button5.setFont(QFont("Times",18))
        self.button6=QtWidgets.QPushButton(self)
        self.button6.setGeometry(250,250,60,40)
        self.button6.setText("6")
        self.button6.setFont(QFont("Times",18))
        self.kopaytma=QtWidgets.QPushButton(self)
        self.kopaytma.setGeometry(350,250,60,40)
        self.kopaytma.setText("*")
        self.qavs1=QtWidgets.QPushButton(self)
        self.qavs1.setGeometry(450,250,60,40)
        self.qavs1.setText(")")
        self.kopaytma.setFont(QFont("Times",18))
        self.button7=QtWidgets.QPushButton(self)
        self.button7.setGeometry(50,300,60,40)
        self.button7.setText("7")
        self.button7.setFont(QFont("Times",18))
        self.button8=QtWidgets.QPushButton(self)
        self.button8.setGeometry(150,300,60,40)
        self.button8.setText("8")
        self.button8.setFont(QFont("Times",18))
        self.button9=QtWidgets.QPushButton(self)
        self.button9.setGeometry(250,300,60,40)
        self.button9.setText("9")
        self.button9.setFont(QFont("Times",18))
        self.ayirish=QtWidgets.QPushButton(self)
        self.ayirish.setGeometry(350,300,60,40)
        self.ayirish.setText("-")
        self.clir=QtWidgets.QPushButton(self)
        self.clir.setGeometry(450,300,60,40)
        self.clir.setText("<=")
        self.clir.setFont(QFont("Times",15))
        self.ayirish.setFont(QFont("Times",18))
        self.button0=QtWidgets.QPushButton(self)
        self.button0.setGeometry(50,350,60,40)
        self.button0.setText("0")
        self.button0.setFont(QFont("Times",18))
        self.nuqta=QtWidgets.QPushButton(self)
        self.nuqta.setGeometry(150,350,60,40)
        self.nuqta.setText(".")
        self.nuqta.setFont(QFont("Times",18))
        self.teng=QtWidgets.QPushButton(self)
        self.teng.setGeometry(250,350,60,40)
        self.teng.setText("=")
        self.teng.setFont(QFont("Times",18))
        self.qoshish=QtWidgets.QPushButton(self)
        self.qoshish.setGeometry(350,350,60,40)
        self.qoshish.setText("+")
        self.qoshish.setFont(QFont("Times",18))
        self.uchirish=QtWidgets.QPushButton(self)
        self.uchirish.setGeometry(450,350,60,40)
        self.uchirish.setText("CL")
        self.uchirish.setFont(QFont("Times",15))
        self.button1.clicked.connect(self.bir)
        self.button2.clicked.connect(self.ikki)
        self.button3.clicked.connect(self.uch)
        self.button4.clicked.connect(self.tort)
        self.button5.clicked.connect(self.besh)
        self.button6.clicked.connect(self.olti)
        self.button7.clicked.connect(self.yetti)
        self.button8.clicked.connect(self.sakkiz)
        self.button9.clicked.connect(self.toqqiz)
        self.button0.clicked.connect(self.nol)
        self.bolish.clicked.connect(self.bol)
        self.kopaytma.clicked.connect(self.kopayt)
        self.ayirish.clicked.connect(self.ayir)
        self.qoshish.clicked.connect(self.qosh)
        self.nuqta.clicked.connect(self.nuq)
        self.teng.clicked.connect(self.hisob)
        self.uchirish.clicked.connect(self.tozalash)
        self.clir.clicked.connect(self.push)
        self.a=str()
        self.i=0
    def bir(self):
        
        self.a=self.a+self.button1.text()
        self.yozuv.setText(self.a)
        self.yozuv.setFont(QFont("Times",16))
        if self.yozuv1.setText(" "):
            self.yozuv1.clear()
    def ikki(self):
        
        self.a=self.a+self.button2.text()
        self.yozuv.setText(self.a)
        self.yozuv.setFont(QFont("Times",16))
        if self.yozuv1.setText(" "):
            self.yozuv1.clear()
    def uch(self):
        self.a=self.a+self.button3.text()
        self.yozuv.setText(self.a)
        self.yozuv.setFont(QFont("Times",16))
        if self.yozuv1.setText(" "):
            self.yozuv1.clear()
    def tort(self):
        self.a=self.a+self.button4.text()
        self.yozuv.setText(self.a)
        self.yozuv.setFont(QFont("Times",16))
        if self.yozuv1.setText(" "):
            self.yozuv1.clear()
    def besh(self):
        self.a=self.a+self.button5.text()
        self.yozuv.setText(self.a)
        self.yozuv.setFont(QFont("Times",16))
        if self.yozuv1.setText(" "):
            self.yozuv1.clear()
    def olti(self):
        self.a=self.a+self.button6.text()
        self.yozuv.setText(self.a)
        self.yozuv.setFont(QFont("Times",16))
        if self.yozuv1.setText(" "):
            self.yozuv1.clear()
    def yetti(self):
        self.a=self.a+self.button7.text()
        self.yozuv.setText(self.a)
        self.yozuv.setFont(QFont("Times",16))
        if self.yozuv1.setText(" "):
            self.yozuv1.clear()
    def sakkiz(self):
        self.a=self.a+self.button8.text()
        self.yozuv.setText(self.a)
        self.yozuv.setFont(QFont("Times",16))
        if self.yozuv1.setText(" "):
            self.yozuv1.clear()
    def toqqiz(self):
        self.a=self.a+self.button9.text()
        self.yozuv.setText(self.a)
        self.yozuv.setFont(QFont("Times",16))
        if self.yozuv1.setText(" "):
            self.yozuv1.clear()
    def nol(self):
        self.a=self.a+self.button0.text()
        if self.a[0]==self.button0.text():
            self.yozuv.setText(self.a[0])
            self.a=''
        else:
            self.yozuv.setText(self.a)
        self.yozuv.setFont(QFont("Times",16))
        if self.yozuv1.setText(" "):
            self.yozuv1.clear()
    def kopayt(self):
        self.a=self.a+self.kopaytma.text()
        self.yozuv.setText(self.a)
        self.yozuv.setFont(QFont("Times",16))
    def bol(self):
        self.a=self.a+self.bolish.text()
        self.yozuv.setText(self.a)
        self.yozuv.setFont(QFont("Times",16))
    def ayir(self):
        self.a=self.a+self.ayirish.text()
        self.yozuv.setText(self.a)
        self.yozuv.setFont(QFont("Times",16))
    def qosh(self):

        self.a=self.a+self.qoshish.text()
        self.yozuv.setText(self.a)
        self.yozuv.setFont(QFont("Times",16))
        
    def nuq(self):
        self.a=self.a+self.nuqta.text()
        self.yozuv.setText(self.a)
        self.yozuv.setFont(QFont("Times",16))
    def push(self):
        self.yozuv.setText(self.a[:-(self.i+1)])
        self.a=self.a[:-(self.i+1)]
        self.i=0
    def tozalash(self):
        self.yozuv.clear()
        self.yozuv1.clear()
        self.a=''
        
    def hisob(self):
        n=self.yozuv.text()
        r='0123456789'
        l=[]
        n=n+'*'
        s=str()
        for i in n:
            if i in r or i=='.':
                s+=i
            else:
                l.append(float(s))
                l.append(i)
                s=''
        l.pop()
        c=0;c1=0
        for i in l:
            if i=='*' or i=='/':
                c+=1
            elif i=='-' or i=='+':
                c1+=1
        i=0;q=0
        while 1:
            if l[i]=='*' or l[i]=='/':
                if l[i]=='*':
                    d=l[i-1]*l[i+1]
                    l.pop(i-1)
                    l.pop(i-1)
                    l.pop(i-1)
                    l.insert(i-1,d)
                    q+=1
                    i=0
                elif l[i]=='/':
                    d=l[i-1]/l[i+1]
                    l.pop(i-1)
                    l.pop(i-1)
                    l.pop(i-1)
                    l.insert(i-1,d)
                    i=0
                    q+=1
            if q==c:
                break
            i+=1
            
        i=0;q1=0
        while 1:
            if l[i]=='-' or l[i]=='+':
                if l[i]=='-':
                    d=l[i-1]-l[i+1]
                    l.pop(i-1)
                    l.pop(i-1)
                    l.pop(i-1)
                    l.insert(i-1,d)
                    i=0
                    q1+=1
                else:
                    d=l[i-1]+l[i+1]
                    l.pop(i-1)
                    l.pop(i-1)
                    l.pop(i-1)
                    l.insert(i-1,d)
                    i=0
                    q1+=1
            if q1==c1:
                break
            i+=1
        s1=str(l)
        satr=str()
        satr+=s1[1:-1]
        s3=str()
        for i in s1:
            if i!='.':
                s3+=i
            else:
                break
        s2=str()
        for i in range(len(satr)):
            if satr[i]=='.':
                s2+=satr[i+1:]
        if s2=='0':
            self.yozuv1.setText(s3[1:])
            self.yozuv1.setFont(QFont("Times",18))
        else:
            self.yozuv1.setText(s1[1:-1])
            self.yozuv1.setFont(QFont("Times",18)) 
        self.ketmaket()
    def ketmaket(self):
        self.a=''
        
app=QtWidgets.QApplication(sys.argv)
ob=Oyna()
ob.setGeometry(350,250,600,400)
ob.setWindowTitle("Calculator")
ob.show()
sys.exit(app.exec_())
