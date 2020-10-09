from tkinter import *
import tkinter.messagebox as tmsgbox
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilenames, asksaveasfilename
from PyPDF2 import PdfFileMerger


class MergePdf:
    def __init__(self):
        self.window = Tk()  # user input window
        self.window.title('Merge PDF\'s')
        self.window.iconbitmap(r'F:\Projects\Merge_PDFs_with_GUI\favicon (1).ico' ) 
        self.window.geometry('600x380')
        self.file_selected = []
        self.fontStyle = tkFont.Font(family="Lucida Grande", size=18)
        self.merge_file_name = ''

    def reset(self):
        self.window.destroy()
        a = MergePdf()
        a.start_point()

    def merge_pdf(self):
        if len(self.file_selected) > 1:
            loc = asksaveasfilename(parent=self.window, defaultextension='.pdf', filetypes=[('PDF', '*.pdf')])
            if loc != '':
                pdfs = self.file_selected
                main_file = PdfFileMerger(strict=False)
                for pdf in pdfs:
                    main_file.append(open(pdf, 'rb'))
                with open(loc, "wb") as fout:
                    main_file.write(fout)
                main_file.close()
                tmsgbox.showinfo('Done', 'File has been Merged')
                self.reset()
        else:
            tmsgbox.showerror('Error', 'Select more than one file.')

    def show(self, file_sel):
        temp = ''
        if file_sel != '':
            for i in file_sel:
                if file_sel not in self.file_selected:
                    temp += i + '\n'
            Label(self.window, text="Files Selected:", font=self.fontStyle).place(x=10, y=140)
            t = Text(self.window, wrap=None, font=tkFont.Font(family="Lucida Grande", size=14), height=6, width=37)
            t.insert(INSERT, temp)
            t.insert(END, ' ')
            t.place(x=175, y=140)
            t.config(state=DISABLED)
            Button(self.window, text='Merge', font=self.fontStyle, command=lambda: self.merge_pdf()).place(x=200, y=290)
            Button(self.window, text='Reselect', font=self.fontStyle, command=lambda: self.reset()).place(x=300, y=290)

    def display_dir(self):
        file = askopenfilenames(parent=self.window, filetypes=[('PDF', '*.pdf')])
        if file != '':
            for i in file:
                self.file_selected.append(i)
            self.show(self.file_selected)

    def start_point(self):
        Label(self.window, text="Merge PDF'S", font=tkFont.Font(family="Lucida Grande", size=30), anchor="center").pack(
            ipady=10)
        Label(self.window, text="Developed By: Mayur V, mmvaidya130@rediffmail.com ",font=tkFont.Font(size=8)).place(x=170, y=350)
        Button(self.window, text='Browse Files', font=self.fontStyle, command=lambda: self.display_dir()).place(x=175,
                                                                                                                y=80)
        Button(self.window, text='Close', font=self.fontStyle, command=self.window.destroy).place(x=340, y=80)

        # Gets the requested values of the height and width.
        window_width = self.window.winfo_reqwidth()
        window_height = self.window.winfo_reqheight()
        # Gets both half the screen width/height and window width/height
        position_right = int(self.window.winfo_screenwidth() / 3 - window_width / 3)
        position_down = int(self.window.winfo_screenheight() / 3 - window_height / 3)
        # Positions the window in the center of the page.
        self.window.geometry("+{}+{}".format(position_right, position_down))
        self.window.resizable(0, 0)
        mainloop()


if __name__ == '__main__':
    start = MergePdf()
    start.start_point()
