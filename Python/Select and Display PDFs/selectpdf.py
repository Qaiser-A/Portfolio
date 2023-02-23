# Import Tkinter to create and use GUI for selecting PDFs
import tkinter
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# Importing ntpath will allow me to display the filename (tail of the path) without the whole directory path 
import ntpath

# Invoke an instance of a window/GUI
window = tkinter.Tk()
window.title('PDF File Selector')
window.geometry('800x500')

# Creating a label to display a message to the user
Label(window, text="Select any PDF file(s)", font='Calibri 14').pack(pady=15)


# Function to select multiple files using askopenfilenames()
def select_files():
	try:
		filetypes = [ ('PDF File', '*.pdf') ] # Type of file to be found and selected within the directory
	
		# File dialog is represented as fd
		filenames = fd.askopenfilenames(title='Open Files', initialdir='/', filetypes=filetypes) 

		# Loop to print all filenames selected within the specified text area
		for filename in filenames:
			names_of_files = ntpath.basename(filename) # Puts the files selected without the path in names_of_files
			print ('Selected files:', names_of_files) # Prints the filenames to console/terminal
			#filelabel['text'] = names_of_files # Displays the filename stored in names_of_files to the filelabel
			textArea.insert(END, names_of_files + '\n') # Displays every filename selected on a new line in the text area
			showinfo(title='Selected Files', message='Files selected successfully') # Show message in a message box
			
	except IOError:
		showinfo(title='Error', message='Could not open one or more files') # Error message if exception caught


filelabel = Label(text='Selected files seen below will be merged and converted to Excel', font='12', fg='green')
filelabel.pack(padx=2, pady=2)

textArea = Text(window, height='12', width='70', wrap=WORD)
textArea.pack()

# Button to select files
select_button = Button(window, text='Open Files', command=select_files, font='12', bg='blue', fg='white', height='2', width='10')

select_button.pack(expand=True)

# Keeping the window open until it is closed by the user
window.mainloop()
