# Author: Kevin S. Yonan | 2015
# License: AGPL v3.0

import sys
import os.path
import itertools
from tkinter import *

miltheh = "ܐܒܓܕܗܘܙܚܛܝܟܠܡܢܣܥܦܨܩܪܫܬ"

def generate_roots(N: int, alphabet: str) -> list[str]:
	if N < 2:
		return []
	
	# Start with all two-letter combinations where the first two letters are not the same
	roots = [l1 + l2 for l1, l2 in itertools.product(alphabet, repeat=2) if l1 != l2]
	
	# If N is greater than 2, extend each root to length N
	if N > 2:
		extended_roots = []
		for root in roots:
			for letters in itertools.product(alphabet, repeat=N-2):
				extended_roots.append(root + ''.join(letters))
		roots = extended_roots
	
	return roots



class SyriacRootsApplication(Tk):
	def __init__(self):
		Tk.__init__(self)
		Tk.title = "Syriac Root Generator"
		self.entry = Entry(self)
		self.entry.grid(row=0, column=1)
		self.button_generate = Button(self, text="Generate Root List", command=self.on_button)
		self.button_generate.grid(row=3, column=1, sticky=W, pady=4)
		self.label = Label(self, text="Number of Roots")
		self.label.grid(row=0)
		self.button_quit = Button(self, text="Quit", command=self.quit)
		self.button_quit.grid(row=3, column=0, sticky=W, pady=4)
	
	def on_button(self):
		number = max(2, min(int( self.entry.get() ), 4))
		output_file = f"syriac-roots-{number}-consonants.txt"
		with open(output_file, "w+", encoding="utf-8") as file:
			file.write("File created by the Syriac N-Root Generator\nAuthor: Kevin Sahda Yonan\n")
			root_list = generate_roots(number, miltheh)
			for root in root_list:
				file.write(root)
				file.write('\n')

if __name__ == '__main__':
	app = SyriacRootsApplication()
	app.title = "syriac root generator"
	app.mainloop()
