# Import Tkinter to create and use GUI for selecting and converting PDFs to Excel
import tkinter
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# Importing ntpath will allow me to display the filename (tail of the path) without the whole directory path 
import ntpath

# Importing PDF file merger from the PyPDF2 module
from PyPDF2 import PdfMerger 
# Tabula used to extract data from a PDF
import tabula

# Invoke an instance of a window/GUI
window = tkinter.Tk()
window.title('PDF File Converter')
window.geometry('800x500')

# Creating a label to display a message to the user
Label(window, text="Select the PDF file(s) to convert to Excel", font='Calibri 14').pack(pady=15)


# Function to select multiple files using askopenfilenames()
def select_files():
	try:
		filetypes = [ ('PDF File', '*.pdf') ] # Type of file to be found and selected within the directory
	
		# File dialog is represented as fd
		filenames = fd.askopenfilenames(title='Open Files', initialdir='/', filetypes=filetypes) 

		# Loop to print all filenames selected within a label
		for filename in filenames:
			names_of_files = ntpath.basename(filename) # Puts the files selected without the path in names_of_files
			print ('Selected files:', names_of_files) # Prints the filenames to console/terminal
			#filelabel['text'] = names_of_files # Displays the filename stored in names_of_files to the filelabel
			textArea.insert(END, names_of_files + '\n') # Displays every filename on a new line in a text box
			showinfo(title='Selected Files', message='Files selected successfully') # Show message in a message box
			# outputfile = os.path.join(output_directory, pdf) # Save merged file in Downlaods directory
			# newFileName = input('What do you want to save the merged files as?')
			# Because it's a loop, each file is displayed and merged one at a time instead of one go
			# Merge selected files and output new name of the file chosen by user
			merger = PdfMerger() # Accessing and storing the merger function from PyPDF2 in merger
			merger.append(filename) # Merging all of the files selected
			merger.write('Merged.pdf') # Saving it as the new user specified filename
			merger.close() # Stopping the function from running once it's done
			showinfo('Success','PDF files successfully merged') # Displaying successful merger message
			
	except IOError:
		showinfo(title='Error', message='Could not open one or more files') # Error message if exception caught

# Merge and convert PDFs in one function
#def merge_and_convert(filenames):
	#try:
		

	#except FileNotFoundError:
		#showinfo('Error', 'File(s) Not Found')


filelabel = Label(text='Selected files seen below will be merged and converted to Excel', font='12', fg='green')
filelabel.pack(padx=2, pady=2)

textArea = Text(window, height='12', width='70', wrap=WORD)
textArea.pack()

# Button to select files
select_button = Button(window, text='Open Files', command=select_files, font='12', bg='blue', fg='white', height='2', width='10')

select_button.pack(expand=True)

# Keeping the window open until it is closed by the user
window.mainloop()

# iconbitmap() e.g. window.iconbitmap('./assets/iconpic.ico') icon location inside paramter
# Merge PDF files selected then sort by date and convert to xlsx/csv
# Tabula methods
# read_pdf(), read_pdf_with_template(), convert_into(), convert_into_by_batch()
# Installed tabula-py and pypdf2 using pip in cmd, uninstall them after finishing this
