from tkinter import *
from flask import Flask,redirect, url_for,render_template,request
import os

def d_dtcn():
	root = Tk()
	root.configure(background = "#CD201F")
	root.geometry('500x250+400+250')
	root.resizable(0,0)

	def function1(): 
		os.system("python drowsiness_detection.py --shape_predictor shape_predictor_68_face_landmarks.dat")
		exit()

			
	root.title("DROWSINESS DETECTION SYSTEM")	
	Label(root, text="DROWSINESS DETECTION SYSTEM",font=("times new roman",20),fg="white",bg="#1877F2",height=2).grid(row=2,rowspan=2,columnspan=20,sticky=N+E+W+S,padx=25,pady=10)
	Button(root,text="Start Monitoring Alarm",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=5,columnspan=40,sticky=W+E+N+S,padx=25,pady=5)
	Button(root,text="Exit",font=("times new roman",20),bg="#0D47A1",fg='white',command=root.destroy).grid(row=9,columnspan=40,sticky=W+E+N+S,padx=25,pady=13)

	root.mainloop()
