#Credit to: Shaurya Uppal from GeeksForGeeks Website
#https://www.geeksforgeeks.org/cyclic-redundancy-check-python/

import time
import sys
import tkinter as tk

class SetupWindow():
	def __init__(self):
		self.root = tk.Tk()
		frame = tk.Frame(self.root)
		tk.Label(frame, text="Data").grid(row=0)
		tk.Label(frame, text="Divisor").grid(row=1)
	
		self.data_enter = tk.Entry(frame)
		self.div_enter = tk.Entry(frame)
		self.data_enter.grid(row=0, column=1, columnspan=2)
		self.div_enter.grid(row=1, column=1, columnspan=2)	
		self.button = tk.Button(frame,
						   text="Submit",
						   command=self.call_mod2_div)
		self.button.grid(row=2, column=1)
		frame.pack()
		
	def call_mod2_div(self):		
		encodeData(self.data_enter.get(), self.div_enter.get())
	
	
class TextWindow():
	def __init__(self, divident, divisor):
		self.root = tk.Tk()
		top_frame = tk.Frame(self.root)
		bottom_frame = tk.Frame(self.root)
		
		self.divident = divident
		self.divisor = divisor
		
		self.start_btn = tk.Button(top_frame,
								   text="Start",
								   command=self.start)
		#self.start_btn.grid(row=0, column=0)
		self.start_btn.pack()
		self.finish_btn = tk.Button(top_frame,
								    text="Finish",
									command=lambda: self.update_sleep(0))
		#self.finish_btn.grid(row=0, column=1)
		self.finish_btn.pack()
		
		self.text = tk.Text(bottom_frame, height=20, width=80)
		#self.text.grid(row=1, column=0, columnspan=3)
		self.text.pack(side=tk.LEFT)
		
		scroll = tk.Scrollbar(bottom_frame)
		scroll.pack(side=tk.RIGHT, fill=tk.Y)
		scroll.config(command=self.text.yview)
		self.text.config(yscrollcommand=scroll.set)
		
		self.sleep_val = 1
		
		top_frame.pack(side=tk.TOP, fill=tk.X)
		bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
		
	def start(self):
		self.mod2div(self.divident, self.divisor)
		
	def update_text(self, text):
		self.text.insert(tk.END, text)					
		self.root.update()
		self.text.see(tk.END)
		
	def update_sleep(self, val):
		self.sleep_val = val
		
		# Performs Modulo-2 division
	def mod2div(self, divident, divisor):

		spaces = ""
		underscores = "----------------------"
		abz = ""
		afz = "0"
		arrows = ""
		shift = ""
		iter_back = 0
		
		# Number of bits to be XORed at a time.
		pick = len(divisor)
		len_div = len(divisor)
	  
		for i in range(pick):
			arrows += "|"
		
		underscores = '-'*(len(divident)+7)
		# Slicing the divident to appropriate
		# length for particular step
		tmp = divident[0 : pick]

		while pick < len(divident):
			
			spaces += " "
			
			if tmp[0] == '1':
	 
				if pick == len(divisor):
					self.update_text(" " + tmp + divident[pick : len(divident)] +"\n")
					self.root.update()
				else:
					self.update_text(shift[iter_back:] + afz + tmp[:-1])
					#input()
					self.update_text(tmp[-1:] + divident[pick : len(divident)]+"\n")
					
				iter_back = 0
				time.sleep(self.sleep_val)
				self.update_text(spaces+divisor+"\n")
				self.update_text(underscores+"\n")
				
				time.sleep(self.sleep_val)
				
				self.update_text(spaces+arrows+" XORED\n")
				afz = "0"
				time.sleep(self.sleep_val)
				# replace the divident by the result
				# of XOR and pull 1 bit down
				tmp = xor(divisor, tmp) + divident[pick]
	  
			else:   # If leftmost bit is '0'
	 
				# If the leftmost bit of the dividend (or the
				# part used in each step) is 0, the step cannot
				# use the regular divisor; we need to use an
				# all-0s divisor.
				afz += "0"
				iter_back += 1
				tmp = xor('0'*pick, tmp) + divident[pick]
	  
			# increment pick to move further
			pick += 1
			shift += " "

	  
		# For the last n bits, we have to carry it out
		# normally as increased value of pick will cause
		# Index Out of Bounds.
		
		spaces += " "
		underscores = underscores + "-"
		
		if tmp[0] == '1':
			self.update_text(shift[iter_back:] + afz + tmp + divident[pick : len(divident)]+"\n")
			iter_back = 0
			time.sleep(self.sleep_val)
			self.update_text(spaces+divisor+"\n")
			self.update_text(underscores+"\n")
			
			time.sleep(self.sleep_val)
			
			self.update_text(spaces+arrows+" XORED\n")
			time.sleep(self.sleep_val)
			afz = "0"
			tmp = xor(divisor, tmp)
		else:
			iter_back += 1
			afz += "0"
			tmp = xor('0'*pick, tmp)
	  
		checkword = tmp
		shift += " "
		
		self.update_text(shift[iter_back:] + afz + tmp + divident[pick : len(divident)] + " (remainder)\n\n")
		
		codeword = divident + checkword
		self.update_text("Data Word: " + divident+"\n")
		self.update_text("Remainder: " + str(' '*(len(divident)) + checkword)+"\n")
		self.update_text("Code Word: " + codeword+"\n")
		
		return checkword
	
# Function used at the sender side to encode
# data by appending remainder of modular divison
# at the end of data.
def encodeData(data, key):	
	stringdata = data
	binarydata = (''.join(format(ord(x), 'b') for x in stringdata))
	
	l_key = len(key)

	# Appends n-1 zeroes at end of data
	appended_data = binarydata + '0'*(l_key-1)
	
	text = TextWindow(appended_data, key)
	
	text.text.insert(tk.END, "Input data (string): " + stringdata+"\n")
	text.text.insert(tk.END, "Input Data (in binary): " + binarydata+"\n")
	text.text.insert(tk.END, "\nLength of Divisor = " + str(l_key))
	text.text.insert(tk.END, "\n*Data Word will add " + str(l_key-1) + " 0's at the end\n")
	text.text.insert(tk.END, "\nAlter Data: " + binarydata + "|" + '0'*(l_key-1))
	text.text.insert(tk.END, "\nDivisor:    " + key + "\n\n")
	text.root.mainloop()
	
	return    
	
def xor(a, b):
  
    # initialize result
    result = []
  
    # Traverse all bits, if bits are
    # same, then XOR is 0, else 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
  
    return ''.join(result)


def main():
	setup = SetupWindow()	
	setup.root.mainloop()

if __name__=="__main__":
	main()

