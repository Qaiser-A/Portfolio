# Import Tkinter to create and use GUI for selecting and merging PDFs
import tkinter
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# Importing ntpath will allow me to display the filename (tail of the path) without the whole directory path 
import ntpath

# Importing PDF merger function from the PyPDF2 module
from PyPDF2 import PdfMerger 

# Invoke an instance of a window/GUI
window = tkinter.Tk()
window.title('PDF File Converter')
window.geometry('800x500')

# Creating a label to display a message to the user
Label(window, text="Select the PDF file(s) to convert to Excel", font='Calibri 14').pack(pady=15)

# Merge and convert PDFs in one function
def merge_selected_pdfs(filenames):
	try:
		filetypes = [ ('PDF File', '*.pdf') ] # Type of file to be found and selected within the directory
	
		# File dialog is represented as fd
		filenames = fd.askopenfilenames(title='Open Files', initialdir='/', filetypes=filetypes) 

		# Loop to print all filenames selected within a label
		for filename in filenames:
			names_of_files = ntpath.basename(filename) # Puts the files selected without the path in names_of_files
			print ('Selected files:', names_of_files) # Prints the filenames to console/terminal
			# outputfile = os.path.join(output_directory, pdf) # Save merged file in Downlaods directory
			merger = PdfMerger() # Referencing and storing the merger function from PyPDF2 in merger
			merger.append(filename) # Merging all of the files selected
		# Files merged with a message outside of the loop
		merger.write('Merged.pdf') # Saving it as the new specified filename
		merger.close() # Stopping the function from running once it's done
		showinfo('Success','PDF files successfully merged') # Displaying successful merger message
		

	except FileNotFoundError:
		showinfo('Error', 'File(s) Not Found')


filelabel = Label(text='Selected files will be merged', font='12', fg='green')
filelabel.pack(padx=2, pady=2)


# Button to select files and command calls the function the button is linked to
select_button = Button(window, text='Open Files', command=merge_selected_pdfs, font='12', bg='blue', fg='white', height='2', width='10')

select_button.pack(expand=True)

# Keeping the window open until it is closed by the user
window.mainloop()
