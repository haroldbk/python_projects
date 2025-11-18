#https://www.youtube.com/watch?v=M7UdAX77kpY
import sys 
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtPrintSupport as qtps

class InvoiceForm(qtw.QWidget):
    submitted = qtc.pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QFormLayout())
        self.inputs = {}
        self.inputs['Customer Name']=qtw.QLineEdit()
        self.inputs['Customer Address']=qtw.QPlainTextEdit()
        self.inputs['Invoice Date']=qtw.QDateEdit(
            date=qtc.QDate.currentDate(), calendarPopup=True)
        self.inputs['Days until Due']=qtw.QSpinBox(
            minimum=0, maximum=60, value=30)
        for label, widget in self.inputs.items():
            self.layout().addRow(label, widget)
        self.line_items = qtw.QTableWidget(
            rowCount=10, columnCount=3)    
        self.line_items.setHorizontalHeaderLabels(
            ['Job','Rate','Hours'])    
        self.line_items.horizontalHeader().setSectionResizeMode(
            qtw.QHeaderView.Stretch)
        self.layout().addRow(self.line_items)
        for row in range(self.line_items.rowCount()):
            for col in range(self.line_items.columnCount()):
                if col >0:
                    w=qtw.QSpinBox(
                        minimum=0,maximum=300)
                    self.line_items.setCellWidget(row,col,w)
        submit = qtw.QPushButton("Create Invoice", clicked = self.on_submit)
        self.layout().addRow(submit)


        #functions
    def on_submit(self):
            data= {
                'c_name':self.inputs['Customer Name'].text(),
                'c_addr':self.inputs['Customer Address'].toPlainText(),
                'i_date':self.inputs['Invoice Date'].date().toString(),
                'i_due':self.inputs['Invoice Date'].date().addDays(
                    self.inputs['Days until Due'].value()).toString(),
                'i_terms':'{} days'.format(
                    self.inputs['Days until Due'].value())
                  }
            data['line_items'] = []
            for row in range(self.line_items.rowCount()):
                if not self.line_items.item(row,0):
                    continue
                job = self.line_items.item(row,0).text()
                rate = self.line_items.cellWidget(row,1).value()
                hours = self.line_items.cellWidget(row,2).value()
                total = rate * hours
                row_data = [job,rate,hours, total]
                if any(row_data):
                    data['line_items'].append(row_data)
                data['total_due'] = sum(x[3] for x in data['line_items'])
                self.submitted.emit(data)    



class InvoiceView(qtw.QTextEdit):
    dpi=72
    doc_width=8.5 * dpi
    doc_height=11 * dpi

    def __init__(self):
        super().__init__(readOnly=True)
        # use a helper for widget sizing
        self.setFixedSize(self._int_size())

        #set document page size with float precision
        self.document().setPageSize(self._float_size())
    def _int_size(self):
        # Return QSize with integer dimensions for widgets:
        return qtc.QSize(int(self.doc_width),int(self.doc_height))  
    def _float_size(self):
        return(qtc.QSizeF(self.doc_width,self.doc_height) )
    
    def set_page_size(self,qrect):
        self.doc_width = qrect.width()
        self.doc_height=qrect.height()
        #apply to widget int and to documents floats
        self.setFixedSize(self._int_size())    
        self.document().setPageSize(self._float_size())
    
        
    def build_invoice(self, data):
        document = qtg.QTextDocument()
        self.setDocument(document)    
        document.setPageSize(qtc.QSizeF(self.doc_width, self.doc_height))
        cursor = qtg.QTextCursor(document)
        root = document.rootFrame()
        cursor.setPosition(root.lastPosition())

        # insert top level frames
        logo_frame_fmt = qtg.QTextFrameFormat()
        logo_frame_fmt.setBorder(2)
        logo_frame_fmt.setPadding(10)
        logo_frame=cursor.insertFrame(logo_frame_fmt)

        cursor.setPosition(root.lastPosition())
        cust_addr_frame_fmt = qtg.QTextFrameFormat()
        cust_addr_frame_fmt.setWidth(self.doc_width*.3)
        cust_addr_frame_fmt.setPosition(qtg.QTextFrameFormat.FloatRight)
        cust_addr_frame = cursor.insertFrame(cust_addr_frame_fmt)

        cursor.setPosition(root.lastPosition())
        terms_frame_fmt = qtg.QTextFrameFormat()
        terms_frame_fmt.setWidth(self.doc_width*.5)
        terms_frame_fmt.setPosition(qtg.QTextFrameFormat.FloatLeft)
        term_frame = cursor.insertFrame(terms_frame_fmt)

        cursor.setPosition(root.lastPosition())
        line_items_frame_fmt=qtg.QTextFrameFormat()
        line_items_frame_fmt.setMargin(25)
        line_items_frame = cursor.insertFrame(line_items_frame_fmt)

        # Create the heading
        # create format for the characters
        std_format = qtg.QTextCharFormat()
        logo_format = qtg.QTextCharFormat()
        logo_format.setFont(qtg.QFont('Impact', 24,qtg.QFont.DemiBold))           
        logo_format.setUnderlineStyle(qtg.QTextCharFormat.SingleUnderline)
        logo_format.setVerticalAlignment(qtg.QTextCharFormat.AlignMiddle)

        label_format = qtg.QTextCharFormat()
        label_format.setFont(qtg.QFont('Sans',12,qtg.QFont.Bold))

        # Create a format for the block
        cursor.setPosition(logo_frame.firstPosition())
        #easy way
        #cursor.InsertImage(r'D:\python\pycute\Chapter 11\nc_logo.png')
        # the better way
        logo_img_fmt=qtg.QTextImageFormat()
        logo_img_fmt.setName(r'D:\python\pycute\Chapter 11\nc_logo.png')
        logo_img_fmt.setHeight(48)
        cursor.insertImage(logo_img_fmt,qtg.QTextFrameFormat.FloatLeft)
        cursor.insertText('   ')
        cursor.insertText('Ninja Coders, LLC', logo_format)
        cursor.insertBlock()
        cursor.insertText('123 N. Wizard St, Yonkers,NY 10701',std_format)

        ## customer address
        cursor.setPosition(cust_addr_frame.lastPosition())
        address_format = qtg.QTextBlockFormat()
        address_format.setLineHeight(150,qtg.QTextBlockFormat.ProportionalHeight)
        address_format.setAlignment(qtc.Qt.AlignRight)
        address_format.setRightMargin(25)

        cursor.insertBlock(address_format)
        cursor.insertText('Customer:', label_format)
        cursor.insertBlock(address_format)
        cursor.insertText(data['c_name'], std_format)
        cursor.insertBlock(address_format)
        cursor.insertText(data['c_addr'])

        ## Terms
        cursor.setPosition(term_frame.lastPosition())
        cursor.insertText('Terms', label_format)
        cursor.insertList(qtg.QTextListFormat.ListDisc)
        #Cursor is now at first list item

        term_items = (
            f'<b>Invoice dated:</b> {data["i_date"]}',
            f'<b>Invoice terms:</b> {data["i_terms"]}',
            f'<b>Invoice due:</b> {data["i_due"]}',
        )

        for i, item in enumerate(term_items):
            if i>0:
                cursor.insertBlock()
            # we can insert HTML too but not with a text format
            cursor.insertHtml(item)    
        ## Line items
        table_format = qtg.QTextTableFormat()
        table_format.setHeaderRowCount(1)
        table_format.setWidth(
            qtg.QTextLength(qtg.QTextLength.PercentageLength, 100))
        headings = ('job', 'rate', 'hours', 'cost')
        num_rows = len(data['line_items'])+1
        num_cols = len(headings)

        cursor.setPosition(line_items_frame.lastPosition())
        table = cursor.insertTable(num_rows,num_cols, table_format)

        # now we're in the first row of the table
        # write the headers
        for heading in headings:
            cursor.insertText(heading, label_format)
            cursor.movePosition(qtg.QTextCursor.NextCell)
        # write data
        for row in data['line_items']:
            for col, value in enumerate(row):
                text = f'${value}' if col in (1,3) else f'{value}'
                cursor.insertText(text, std_format)    
                cursor.movePosition(qtg.QTextCursor.NextCell)  

       # append a row
        table.appendRows(1)
        cursor = table.cellAt(num_rows, 0).lastCursorPosition()
        cursor.insertText('total', label_format)
        cursor= table.cellAt(num_rows,3).lastCursorPosition()           
        cursor.insertText(f"${data['total_due']}",label_format)


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
       
        #your code here
        main= qtw.QWidget()
        main.setLayout(qtw.QHBoxLayout())
        self.setCentralWidget(main)

        form = InvoiceForm()
        main.layout().addWidget(form)

        self.preview = InvoiceView()
        main.layout().addWidget(self.preview)

        form.submitted.connect(self.preview.build_invoice)

        #Printing 
        print_tb=self.addToolBar('Printing')
        print_tb.addAction('Configure Printer', self.printer_config)
        print_tb.addAction('Print Preview', self.print_preview)
        print_tb.addAction('Print Dialog', self.print_dialog)
        print_tb.addAction('Export PDF', self.export_pdf)

        self.printer = qtps.QPrinter()
        #configure the defaults
        self.printer.setOrientation(qtps.QPrinter.Portrait)
        self.printer.setPageSize(qtg.QPageSize(qtg.QPageSize.Letter))
        self._update_preview_size()


        #your code ends here
        self.show()     
    def _update_preview_size(self):
        self.preview.set_page_size(
           self.printer.pageRect(qtps.QPrinter.Point))
        
    def printer_config(self):
        dialog = qtps.QPageSetupDialog(self.printer,self)
        dialog.exec()
        self._update_preview_size()
    def _print_document(self):
        # doesn't actually print the document. 
        # just point document to printer object
        self.preview.document().print(self.printer)        

    def print_dialog(self):
       # follow the guidance in the github version rather than the book
       dialog = qtps.QPrintDialog(self.printer,self)
       dialog.accepted.connect(self._print_document)
       dialog.exec()
       self._update_preview_size()
      
    def print_preview(self):
        dialog = qtps.QPrintPreviewDialog(self.printer, self)
        dialog.paintRequested.connect(self._print_document)
        dialog.exec()
        self._update_preview_size()
    def export_pdf(self):
        filename, _ = qtw.QFileDialog.getSaveFileName(
            self, "Save to PDF", qtc.QDir.homePath(), "PDF Files (*.pdf)" ) 
        if filename:
            self.printer.setOutputFileName(filename)
            self.printer.setOutputFormat(qtps.QPrinter.PdfFormat)
            self._print_document()   

if __name__=='__main__':
    app =qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())


