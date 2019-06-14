import fpdf
from datetime import datetime

class Creator:
    def __init__(self,first_name,last_name,email,phone_num,address,city,country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_num = phone_num
        self.address = address
        self.city = city
        self.country = country

class Organization:
    def __init__(self,name,address,city,country):
        self.name = name
        self.address = address
        self.city = city
        self.country = country

class BankAccountDetail:
    def __init__(self,account_name,account_num,currency,bank_name,branch,branch_addr):
        self.account_name = account_name
        self.account_num = account_num
        self.currency = currency
        self.bank_name =bank_name
        self.branch = branch
        self.branch_addr = branch_addr

class Project:

    def __init__(self,name,description,amount):
        self.name = name
        self.description = description
        self.amount = amount

class Invoice:
    '''
    Invoice class used to model a invoice object which is a composition of
    1. Creator Object
    2. Organization Object
    3. Project Object
    4. BankDetail Object
    '''

    def __init__(self,invoice_num,creator,organization,project,bankaccountdetail):
        self.invoice_num = invoice_num
        self.creator = creator
        self.organization = organization
        self.project = project
        self.bankaccountdetail = bankaccountdetail

    def error(self, msg):
        "Fatal error"
        raise RuntimeError('FPDF error: '+msg)

class File:
    def __init__(self,filename,font_size,line_height,orientation):
        self.filename = filename
        self.font_size = font_size
        self.line_height = line_height
        self.orientation = orientation
        

class PdfInvoice(Invoice):
    '''
    Inherits from the Parent Invoice class and has an extra feature
    1. File Object : Used to specify some basic details about the file
    '''
    def __init__(self,invoice_num,creator,organization,project,bankaccountdetail,file):
        super().__init__(invoice_num,creator,organization,project,bankaccountdetail)
        self.file = file

    def generate_pdf(self):
        dt = datetime.now()
        date = dt.date()
        try:
            pdf = fpdf.FPDF(format=self.file.orientation)
            pdf.add_page()
            pdf.set_font("Arial", size=self.file.font_size)
            pdf_content ={
                "Invoice Number #":self.invoice_num,
                "Date of Invoice #": str(date),
                "Name #":'{}{}'.format(self.creator.first_name,self.creator.last_name),
                "Address #": self.creator.address,
                "City #":self.creator.city,
                "Country #":self.creator.country,
                "Email #":self.creator.email,
                "Phone Number #": self.creator.phone_num,
                "Bill To #": "",
                "Organization Name #":self.organization.name,
                "Organization Address #":self.organization.address,
                "Organization City #": self.organization.city,
                "Organization Country #":self.organization.country,
                "Amount # ": str(self.project.amount),
                "Comments # ": self.project.description,
                "Bank Details": "",
                "Account Name #":self.bankaccountdetail.account_name,
                "Account Number #": self.bankaccountdetail.account_num,
                "Bank Name #": self.bankaccountdetail.bank_name,
                "Branch  #": self.bankaccountdetail.branch,
                "Branch Address  #": self.bankaccountdetail.branch_addr,
                "Currency #":self.bankaccountdetail.currency
            }
            pdf.write(self.file.line_height, "Billed By #")
            pdf.ln()
            for key,value in pdf_content.items():
                pdf.write(self.file.line_height,key)
                pdf.write(self.file.line_height,value)
                pdf.ln()
            pdf.output(self.file.filename)
        except Exception as ex:
            print ('Exception',ex)


if __name__ == "__main__":
    creator = Creator('Test','User','test@gmail.com',
         '099006789','Joans Apartment, 123 Test road','Nairobi','Kenya')

    organization = Organization('Test Org','Ndemi Road Kilimani', 'Nairobi','Kenya')

    bank_detail = BankAccountDetail('Test User','999999678','KES',
                                  'Test Bank','Kenya','BRANCH  Way, ABC Place')

    _file = File("Invoice.pdf",12,5,"letter")

    project = Project('Ecommerce site','Worked on the ecommerce site',10.900)

    pdf_inv = PdfInvoice('1393939',creator,organization,project,bank_detail,_file)
    pdf_inv.generate_pdf()
