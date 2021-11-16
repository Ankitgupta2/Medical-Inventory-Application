from sqlalchemy import create_engine, Column,Integer,String,Float, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import VARCHAR, DateTime
Base= declarative_base()
class Drug(Base):

    __tablename__ = "Drug"

    drugID= Column(Integer, primary_key=True)
    drugName=Column(String)
    drugCategory = Column(String)
    manufacturer=Column(String)
    unitPrice=Column(Float)
    no_of_units_in_package=Column(Integer)
    # emailAddress = Column(VARCHAR,unique=True)
    # Address = Column(VARCHAR)
    # City=Column(String)
    # supplier=ForeignKey('Supplier')


class Storedrug(Base):

    __tablename__ = "StoredDrug"

    drugId= Column(Integer, primary_key=True)
    batchNo=Column(VARCHAR)
    manufactureDate=Column(DateTime)
    quantity=Column(Integer)
    expiryDate=Column(DateTime)

class Customer(Base):

    __tablename__ = "Customer"

    customerId= Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    mobilePhone = Column(Integer)
    emailAddress = Column(VARCHAR)
    pharmacyName=Column(String)#,unique=True
    address = Column(VARCHAR)
    city=Column(String)#,unique=True

class Sale_Invoice(Base):

    __tablename__ = "Sale_Invoice"

    saleInvoiceId= Column(Integer, primary_key=True)
    date = Column(DateTime)
    paymentType = Column(String)
    totalAmount = Column(Float)
    discount = Column(Float)
    newPrice = Column(Float)
    # drug=ForeignKey('Drug')
    # customer=ForeignKey('Customer')
class Purchase_Invoice(Base):

    __tablename__ = "Purchase_Invoice"

    purchaseInvoiceId= Column(Integer, primary_key=True)
    date = Column(DateTime)
    paymentType = Column(String)
    totalAmount = Column(Float)
    empId= Column(Integer, primary_key=True)
    supplierId= Column(Integer, primary_key=True)
    discount = Column(Float)
    newPrice = Column(Float)
    payedAmount = Column(Float)
    remainingAmount = Column(Float)
    # drug=ForeignKey('Drug')
    # customer=ForeignKey('Customer')
class Supplier(Base):
    __tablename__ = "Supplier"
    supplierId= Column(Integer, primary_key=True)
    companyName = Column(String)
    mobilePhone = Column(Integer)
    emailAddress = Column(VARCHAR)
    address = Column(VARCHAR)
    city=Column(String)#,unique=True
class Employee(Base):

    __tablename__ = "Employee"

    empId= Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    dateofbirth=Column(DateTime)
    dateofwork=Column(DateTime)
    mobilePhone = Column(Integer)
    emailAddress = Column(VARCHAR)
    residenceAddress=Column(VARCHAR)
    salary=Column(Float)
    role=Column(String)

if __name__ == "__main__":
    engine= create_engine('sqlite:///med.sqlite3')
    Base.metadata.create_all(engine)