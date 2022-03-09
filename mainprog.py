from tkinter import *
import random

root = Tk()
root.title('Rivan subnetting exercise')
number = 0
subnet = 0
octetnI = 0
wildcard = 0 
variation = 0 

def check():
	root2 = Tk()
	root2.title('Generated Answer')
	banner = Label(root2,text = "SUBNETTING ANSWER")
	break1 = Label(root2,text='')

	banner.grid(row = 0 , columnspan = 4)

	slash_label2 = Label(root2, text = "SLASH\n '/number'")
	ipv4_label2 = Label(root2, text = "IPV4\n '(X.X.X.X)'")
	octetnI_label2 = Label(root2, text = "(OCTET,I)\n '(position,i)'")
	wildcard_label2 = Label(root2, text = "WILDCARD\n '(X.X.X.X)'")

	slash_entry2 = Entry(root2, width = 15, borderwidth = 3)
	ipv4_entry2 = Entry(root2, width = 15, borderwidth = 3)
	octetnI_entry2 = Entry(root2, width = 15, borderwidth = 3)
	wildcard_entry2 = Entry(root2, width = 15, borderwidth = 3)

	break1.grid(row=1, columnspan=4)

	slash_label2.grid(row = 1, padx = 5, column= 0)
	ipv4_label2.grid(row = 1 , padx = 5, column = 1)
	octetnI_label2.grid(row = 1, padx = 5, column = 2)
	wildcard_label2.grid(row = 1, padx = 5, column = 3)

	slash_entry2.grid(row = 3, column= 0)
	ipv4_entry2.grid(row = 3, column = 1)
	octetnI_entry2.grid(row = 3, column = 2)
	wildcard_entry2.grid(row = 3, column = 3)

	slash_entry2.insert(0, f'/{number}')
	ipv4_entry2.insert(0, subnet)
	octetnI_entry2.insert(0, f'({octetnI})')
	wildcard_entry2.insert(0,wildcard)


	close_button = Button(root2, text = 'CLOSE', command = root2.destroy)

	close_button.grid(row = 4, columnspan = 4)

	root2.mainloop()

def generate_option():

	global number
	global subnet
	global octetnI
	global wildcard

	number = random.randint(1,32)
	contiguios = [255,128,192,224,240,248,252,254,255]

	i = number % 8
	if number <= 8:
		position = 1
		subnet = f'{contiguios[i]}.0.0.0'
		octetnI = f'(1st,{i}i)'
		wildcard = f'{i-1}.255.255.255'

	elif number > 8 and number <= 16:
		position = 2
		subnet = f'255.{contiguios[i]}.0.0'
		octetnI = f'(2nd,{i}i)'
		wildcard = f'0.{i-1}.255.255'

	elif number > 16 and number <= 24:
		position = 3
		subnet = f'255.255.{contiguios[i]}.0'
		octetnI = f'(3rd,{i}i)'
		wildcard = f'0.0.{i-1}.255'

	elif number > 24 and number <= 32:
		position = 4
		subnet = f'255.255.255.{contiguios[i]}'
		octetnI = f'(4th,{i}i)'
		wildcard = f'0.0.0.{i-1}'

	global variation
	variation = random.randint(1,4)

	if variation == 1:
		#option for only slash
		slash_entry.delete(0,END)
		ipv4_entry.delete(0,END)
		octetnI_entry.delete(0,END)
		wildcard_entry.delete(0,END)

		slash_entry.insert(0,f'/{str(number)}')

	elif variation == 2:
		#option for octetnI
		slash_entry.delete(0,END)
		ipv4_entry.delete(0,END)
		octetnI_entry.delete(0,END)
		wildcard_entry.delete(0,END)

		octetnI_entry.insert(0,octetnI)

	elif variation == 3:
		#option for only ipv4
		slash_entry.delete(0,END)
		ipv4_entry.delete(0,END)
		octetnI_entry.delete(0,END)
		wildcard_entry.delete(0,END)

		ipv4_entry.insert(0,subnet)

	elif variation == 4:
		#option for octetnI and wilcard
		slash_entry.delete(0,END)
		ipv4_entry.delete(0,END)
		octetnI_entry.delete(0,END)
		wildcard_entry.delete(0,END)

		octetnI_entry.insert(0,octetnI)
		wildcard_entry.insert(0,wildcard)

	return number



banner = Label(root,text = "SUBNETTING")
generate_button = Button(root, text = "GENERATE", command = generate_option)
checkANS_button = Button(root, text = "CHECK", command = check)

slash_label = Label(root, text = "SLASH\n '/number'")
ipv4_label = Label(root, text = "IPV4\n '(X.X.X.X)'")
octetnI_label = Label(root, text = "(OCTET,I)\n '(position,i)'")
wildcard_label = Label(root, text = "WILDCARD\n '(X.X.X.X)'")

slash_entry = Entry(root, width = 15, borderwidth = 3)
ipv4_entry = Entry(root, width = 15, borderwidth = 3)
octetnI_entry = Entry(root, width = 15, borderwidth = 3)
wildcard_entry = Entry(root, width = 15, borderwidth = 3)


banner.grid(row = 0 , column = 0 , columnspan = 4)
generate_button.grid(row = 1, column = 0, columnspan = 4)
checkANS_button.grid(row = 4, column = 0, columnspan = 4)


slash_label.grid(row = 2, column= 0)
ipv4_label.grid(row = 2 , column = 1)
octetnI_label.grid(row =2, column = 2)
wildcard_label.grid(row = 2, column = 3)



slash_entry.grid(row = 3, column= 0)
ipv4_entry.grid(row = 3, column = 1)
octetnI_entry.grid(row = 3, column = 2)
wildcard_entry.grid(row = 3, column = 3)

#after the check button








root.mainloop()
