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
        pdf = fpdf.FPDF(format=self.file.orientation)
        pdf.add_page()
        pdf.set_font("Arial", size=self.file.font_size)
        pdf.write(self.file.line_height,"Invoice Number #")
        pdf.write(self.file.line_height,self.invoice_num)
        pdf.ln()
        pdf.write(self.file.line_height,"Date Invoiced #")
        pdf.write(self.file.line_height,str(date))
        pdf.ln()
        pdf.write(self.file.line_height, "Billed By #")
        pdf.write(self.file.line_height,"{}{}".format(self.creator.first_name,self.creator.last_name))
        pdf.ln()
        pdf.write(self.file.line_height,"Address #")
        pdf.write(self.file.line_height,self.creator.address)
        pdf.ln()
        pdf.write(self.file.line_height, "City #")
        pdf.write(self.file.line_height, self.creator.city)
        pdf.ln()
        pdf.write(self.file.line_height,"Country #")
        pdf.write(self.file.line_height,self.creator.country)
        pdf.ln()
        pdf.write(self.file.line_height, "Email #")
        pdf.write(self.file.line_height, self.creator.email)
        pdf.ln()
        pdf.write(self.file.line_height, "Phone Number #")
        pdf.write(self.file.line_height, self.creator.phone_num)
        pdf.ln()
        pdf.write(self.file.line_height,"Billed To #")
        pdf.ln()
        pdf.write(self.file.line_height,"Organization Name #")
        pdf.write(self.file.line_height,self.organization.name)
        pdf.ln()
        pdf.write(self.file.line_height, "Organization Address #")
        pdf.write(self.file.line_height, self.organization.address)
        pdf.ln()
        pdf.write(self.file.line_height, "Organization City #")
        pdf.write(self.file.line_height, self.organization.city)
        pdf.ln()
        pdf.write(self.file.line_height, "Organization Country #")
        pdf.write(self.file.line_height, self.organization.country)
        pdf.ln()
        pdf.write(self.file.line_height, "Comments #")
        pdf.write(self.file.line_height, self.project.description)
        pdf.ln()
        pdf.write(self.file.line_height, "Amount #")
        pdf.write(self.file.line_height,str(self.project.amount))
        pdf.ln()
        pdf.write(self.file.line_height,'Account details ')
        pdf.ln()
        pdf.write('Account Name #')
        pdf.write(self.file.line_height,self.bankaccountdetail.account_name)
        pdf.ln()
        pdf.write('Account Number #')
        pdf.write(self.file.line_height,self.bankaccountdetail.account_num)
        pdf.ln()
        pdf.write('Account Currency #')
        pdf.write(self.file.line_height, self.bankaccountdetail.currency)
        pdf.ln()
        pdf.write('Bank Name #')
        pdf.write(self.file.line_height, self.bankaccountdetail.bank_name)
        pdf.ln()
        pdf.write('Branch Address #')
        pdf.write(self.file.line_height, self.bankaccountdetail.branch_addr)
        pdf.ln()
        pdf.output(self.file.filename)

creator = Creator('Test','User','test@gmail.com',
         '099006789','Joans Apartment, 123 Test road','Nairobi','Kenya')

organization = Organization('Test Org','Ndemi Road Kilimani', 'Nairobi','Kenya')

bank_detail = BankAccountDetail('Test User','999999678','KES',
                                  'Test Bank','Kenya','BRANCH  Way, ABC Place')

file = File("Invoice.pdf",12,5,"letter")

project = Project('Ecommerce site','Worked on the ecommerce site',10.900)

pdf_inv = PdfInvoice('1393939',creator,organization,project,bank_detail,file)
pdf_inv.generate_pdf()
