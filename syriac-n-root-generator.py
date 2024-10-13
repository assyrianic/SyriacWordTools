#!/usr/bin/python3

# Author: Kevin S. Yonan | 2015
# License: MIT License

import sys
import os.path
from itertools import product
from tkinter import *
from multiprocessing import Pool

miltheh = "ܐܒܓܕܗܘܙܚܛܝܟܠܡܢܣܥܦܨܩܪܫܬ"

def repcombinations_with_replacement(r:int, f):
	n = len(miltheh)
	for indices in product(range(n), repeat=r):
		for i in indices:
			f.write(miltheh[i])
		f.write('\n')


class SyriacRootsApplication(Tk):
	def __init__(self):
		Tk.__init__(self)
		
		self.entry = Entry(self)
		self.entry.grid(row=0, column=1)
		self.button_generate = Button(self, text="Generate Root List", command=self.on_button)
		self.button_generate.grid(row=3, column=1, sticky=W, pady=4)
		self.label = Label(self, text="Number of Roots")
		self.label.grid(row=0)
		
		self.button_quit = Button(self, text="Quit", command=self.quit)
		self.button_quit.grid(row=3, column=0, sticky=W, pady=4)
	
	def on_button(self):
		number = int( self.entry.get() )
		number = max(1, min(number, 5))
		output_file = f"syriac-roots-{number}-consonants.txt"
		with open(output_file, "w+") as file:
			file.write("File created by the Syriac N-Root Generator\nAuthor: Kevin Sahda Yonan\n")
			repcombinations_with_replacement(number, file);
	

if __name__ == '__main__':
	app = SyriacRootsApplication()
	app.mainloop()
