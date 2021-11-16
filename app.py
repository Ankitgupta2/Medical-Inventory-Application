# import sqlalchemy
from google.protobuf.symbol_database import Default
# from sqlalchemy.sql.elements import Label
from sqlalchemy import create_engine, Column,Integer,String,Float, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import VARCHAR, DateTime
import streamlit as st
from newdb import Base, Customer, Drug, Employee, Purchase_Invoice, Sale_Invoice,Storedrug, Supplier
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, engine
def open_db():
    '''function connects to database'''
    engine = create_engine('sqlite:///med.sqlite3')
    Session = sessionmaker(bind=engine)
    return Session()
st.title("Medical Inventory Application")
choices = ['Drug','show Drug details','Stored Drug','show stored Drug','Sales Invoice','sale invoice data','Purchase Invoice','purchase invoice data','Customer','Show Customer Data','supplier','show supplier data','Employee','show employee data','update details','Delete details']
selected_choice = st.selectbox("select an option",options=choices)
if selected_choice == choices[0]:
    with st.form('addform'):
        drugID= st.number_input(label="Enter Drug ID")
        drugName=st.text_input(label="Enter drug Name")
        drugCategory = st.text_input(label="Enter drug Category Name")
        manufacturer=st.text_input(label="Enter Manufacturer Name")
        unitPrice=st.number_input(label="Enter Unit Price")
        no_of_units_in_package=st.number_input(label="Enter no of units in package")
        btn=st.form_submit_button(label="submit")
    if drugID  and btn:
        try:
            newdb = open_db()
            entry = Drug(drugID=drugID,drugName=drugName, drugCategory= drugCategory,manufacturer=manufacturer,unitPrice=unitPrice,no_of_units_in_package=no_of_units_in_package) 
            newdb.add(entry)
            newdb.commit()
            newdb.close()
            st.success("Information successfully saved")
        except Exception as e:

            st.error(f"Could not save the details. {e}")
elif selected_choice == choices[1]:
    st.header("Showing Drug details")
    newdb = open_db()
    medicine_list= newdb.query(Drug)
    newdb.close()
    for item in medicine_list:
        st.markdown(f'''
        #### {item.drugID}
        - ### {item.drugName}
        - ### {item.drugCategory}
        - ### {item.manufacturer}
        - ### {item.unitPrice}
        - ### {item.no_of_units_in_package}
        ''')

elif selected_choice == choices[2]:
    st.header("Stored Drug")
    with st.form('addform'):
        drugID= st.number_input(label="Enter Drug ID")
        batchNo=st.number_input(label="Enter Batch No.")
        manufactureDate=st.date_input(label="Enter Manufacture Date")
        quantity=st.number_input(label="Enter Quantity")
        expiryDate=st.date_input(label="Enter Expiry Date")
        btn=st.form_submit_button(label="submit")
    if batchNo  and btn:
        try:
            newdb = open_db()
            entry = Storedrug(drugId=drugID,batchNo=batchNo, manufactureDate=manufactureDate,quantity=quantity,expiryDate=expiryDate) 
            newdb.add(entry)
            newdb.commit()
            newdb.close()
            st.success("Information successfully saved")
        except Exception as e:

            st.error(f"Could not save the details. {e}")
elif selected_choice == choices[3]:
    st.header("Showing storeDrug details")
    newdb = open_db()
    medicine_list= newdb.query(Storedrug)
    newdb.close()
    for item in medicine_list:
        st.markdown(f'''
        #### {item.drugId}
        - ### {item.batchNo}
        - ### {item.manufactureDate}
        - ### {item.quantity}
        - ### {item.expiryDate}
        ''')
elif selected_choice == choices[4]:
    st.header("Sales Invoice")
    with st.form('addform'):
        saleInvoiceId= st.number_input(label="Enter sale Invoice ID")
        date =st.date_input(label="Enter Date")
        paymentType = st.radio("Select Payment Type",('Online Payment','Cash'))
        totalAmount = st.number_input(label="Enter Total amount")
        discount = st.number_input(label="Enter Discount")
        newPrice=st.number_input(label="Enter New price")
        btn=st.form_submit_button(label="submit")
    if saleInvoiceId  and btn:
        try:
            newdb = open_db()
            entry = Sale_Invoice(saleInvoiceId=saleInvoiceId,date=date, paymentType=paymentType,totalAmount=totalAmount,discount=discount,newPrice=newPrice) 
            newdb.add(entry)
            newdb.commit()
            newdb.close()
            st.success("Information successfully saved")
        except Exception as e:

            st.error(f"Could not save the details. {e}")
elif selected_choice == choices[5]:
    st.header("Showing sale Invoice details")
    newdb = open_db()
    medicine_list= newdb.query(Sale_Invoice)
    newdb.close()
    for item in medicine_list:
        st.markdown(f'''
        #### {item.saleInvoiceId}
        - ### {item.date}
        - ### {item.paymentType}
        - ### {item.totalAmount}
        - ### {item.discount}
        - ### {item.newPrice}
        ''')
elif selected_choice == choices[6]:
    st.header("Purchase Invoice")
    with st.form('addform'):

        purchaseInvoiceId= st.number_input(label="Enter Purchase Invoice ID")
        date = st.date_input(label="Enter Date")
        paymentType = st.radio("Select Payment Type",('Online Payment','Cash'))
        totalAmount = st.number_input(label="Enter total Amount")
        empId= st.number_input(label="Enter Employee ID")
        supplierId= st.number_input(label="Enter Supplier ID")
        discount = st.number_input(label="Enter Discount")
        newPrice = st.number_input(label="Enter new Price")
        payedAmount = st.number_input(label="Enter payed Amount")
        remainingAmount=st.number_input(label="Enter Remaining Amount")
        btn=st.form_submit_button(label="submit")
    if purchaseInvoiceId  and btn:
        try:
            newdb = open_db()
            entry = Purchase_Invoice(purchaseInvoiceId=purchaseInvoiceId,date=date, paymentType=paymentType,totalAmount=totalAmount,empId=empId,supplierId=supplierId,discount=discount,newPrice=newPrice,payedAmount=payedAmount,remainingAmount=remainingAmount) 
            newdb.add(entry)
            newdb.commit()
            newdb.close()
            st.success("Information successfully saved")
        except Exception as e:

            st.error(f"Could not save the details. {e}")
elif selected_choice == choices[7]:
    st.header("Showing purchase Invoice details")
    newdb = open_db()
    medicine_list= newdb.query(Purchase_Invoice)
    newdb.close()
    for item in medicine_list:
        st.markdown(f'''
        #### {item.purchaseInvoiceId}
        - ### {item.date}
        - ### {item.paymentType}
        - ### {item.totalAmount}
        - ### {item.empId}
        - ### {item.supplierId}
        - ### {item.discount}
        - ### {item.newPrice}
        - ### {item.payedAmount}
        - ### {item.remainingAmount}
        ''')
if selected_choice == choices[8]:
    with st.form('addform'):
        customerId= st.number_input(label="Enter Customer ID")
        firstName = st.text_input(label="Enter First Name")
        lastName = st.text_input(label="Enter Last Name")
        mobilePhone = st.number_input(label="Enter Phone No")
        emailAddress = st.text_input(label="Enter email aAddress")
        pharmacyName=st.text_input(label="Enter pharmacy Name")
        address = st.text_input(label="Enter Address")
        city=st.text_input(label="Enter city Name")
        btn=st.form_submit_button(label="submit")
    if customerId  and btn:
        try:
            newdb = open_db()
            entry = Customer(customerId=customerId,firstName=firstName, lastName=lastName,mobilePhone=mobilePhone,emailAddress=emailAddress,pharmacyName=pharmacyName,address=address,city=city) 
            newdb.add(entry)
            newdb.commit()
            newdb.close()
            st.success("Information successfully saved")
        except Exception as e:

            st.error(f"Could not save the details. {e}")
elif selected_choice == choices[9]:
    st.header("Showing Customer details")
    newdb = open_db()
    medicine_list= newdb.query(Customer)
    newdb.close()
    for item in medicine_list:
        st.markdown(f'''
        #### {item.customerId}
        - ### {item.firstName}
        - ### {item.lastName}
        - ### {item.mobilePhone}
        - ### {item.emailAddress}
        - ### {item.pharmacyName}
        - ### {item.address}
        - ### {item.city}
        ''')
elif selected_choice == choices[10]:
    st.header("Supplier")
    with st.form('addform'):
        supplierId= st.number_input(label="Enter Supplier ID")
        companyName = st.text_input(label="Enter Company Name")
        mobilePhone = st.number_input(label="Enter Phone No")
        emailAddress = st.text_input(label="Enter email address")
        address = st.text_input(label="Enter Address")
        city=st.text_input(label="Enter city Name")
        btn=st.form_submit_button(label="submit")
    if supplierId  and btn:
        try:
            newdb = open_db()
            entry = Supplier(supplierId=supplierId,companyName=companyName,mobilePhone=mobilePhone,emailAddress=emailAddress,address=address,city=city) 
            newdb.add(entry)
            newdb.commit()
            newdb.close()
            st.success("Information successfully saved")
        except Exception as e:

            st.error(f"Could not save the details. {e}")
elif selected_choice == choices[11]:
    st.header("Showing Supplier details")
    newdb = open_db()
    medicine_list= newdb.query(Supplier)
    newdb.close()
    for item in medicine_list:
        st.markdown(f'''
        #### {item.supplierId}
        - ### {item.companyName}
        - ### {item.mobilePhone}
        - ### {item.emailAddress}
        - ### {item.address}
        - ### {item.city}
        ''')
elif selected_choice == choices[12]:
    st.header("Employee")
    with st.form('addform'):
        empId= st.number_input(label="Enter Employee ID")
        firstName = st.text_input(label="Enter first Name")
        lastName = st.text_input(label="Enter last Name")
        dateofbirth=st.date_input(label="Enter Date of Birth")
        dateofwork=st.date_input(label="Enter Date of work")
        mobilePhone = st.number_input(label="Enter phone no")
        emailAddress = st.text_input(label="Enter Email Address")
        residenceAddress=st.text_input(label="Enter Residence Address")
        salary=st.number_input(label="Enter Salary")
        role=st.text_input(label="Enter Role")
        btn=st.form_submit_button(label="submit")
    if empId  and btn:
        try:
            newdb = open_db()
            entry = Employee(empId=empId,firstName=firstName,lastName=lastName,dateofbirth=dateofbirth,dateofwork=dateofwork,mobilePhone=mobilePhone,emailAddress=emailAddress,residenceAddress=residenceAddress,salary=salary,role=role) 
            newdb.add(entry)
            newdb.commit()
            newdb.close()
            st.success("Information successfully saved")
        except Exception as e:

            st.error(f"Could not save the details. {e}")
elif selected_choice == choices[13]:
    st.header("Showing Employee details")
    newdb = open_db()
    medicine_list= newdb.query(Employee)
    newdb.close()
    for item in medicine_list:
        st.markdown(f'''
        #### {item.empId}
        - ### {item.firstName}
        - ### {item.lastName}
        - ### {item.dateofbirth}
        - ### {item.dateofwork}
        - ### {item.mobilePhone}
        - ### {item.emailAddress}
        - ### {item.residenceAddress}
        - ### {item.salary}
        - ### {item.role}
        ''')
elif selected_choice== choices[14]:
    st.subheader("Update details")

    choices = ['Update Supplier details','Update Drug details','Update Invoice details','Update Customer details',]
    selected_choice = st.selectbox("select an option",options=choices)

    if selected_choice== choices[0]:
        
        st.subheader("Update Supplier details")
        id = st.number_input("Supplier ID",value=1)
        db = open_db()
        result = db.query(Supplier).get(id)
        if not result:
            st.error("first fill the details.")
        else:
            with st.form("add supplier"):

                companyName=st.text_input("Enter company name",value=result.companyName)
                col1,col2=st.columns(2)
                with col1:
                    mobilePhone=st.number_input(label="Mobile Number",value=result.mobilePhone)
                with col2:
                    emailAddress = st.text_input(label='E-mail',value=result.emailAddress)
                
                address=st.text_input("enter Address",value=result.address)
                city=st.text_input('enter city',value=result.city)
                
                btn= st.form_submit_button("Update")
            
            if id and btn:
                try:
                    result.companyName=companyName
                    result.mobilePhone=mobilePhone
                    result.emailAddress=emailAddress
                    result.address=address
                    result.city=city
                    db.commit()
                    st.success("Supplier info Update successfully")

                    st.markdown(f'''
                    ##### supplier id - {supplierId}
                    - ###### Company name - {companyName}
                    - ###### Mobile Number - {mobilePhone}
                    - ###### E-mail - {emailAddress}
                    - ###### Address - {address}
                    - ###### city - {city}
                    ''')
                except Exception as e:
                    st.error(f"Could not Update the info of supplier . {e}")
        db.close()
    elif selected_choice== choices[1]:
        
        st.subheader("Update Drug details")
        id = st.number_input("Drug ID",value=1)
        db = open_db()
        result = db.query(Drug).get(id)
        if not result:
            st.error("first fill the details.")
        else:
            with st.form("add Drug"):
                drugID= st.number_input(label="Enter Drug ID",value=result.drugID)
                drugName=st.text_input(label="Enter drug Name",value=result.drugName)
                drugCategory = st.text_input(label="Enter drug Category Name",value=result.drugCategory)
                manufacturer=st.text_input(label="Enter Manufacturer Name",value=result.manufacturer)
                unitPrice=st.number_input(label="Enter Unit Price",value=result.unitPrice)
                no_of_units_in_package=st.number_input(label="Enter no of units in package",value=result.no_of_units_in_package)
                btn= st.form_submit_button("Update")
            
            if id and btn:
                try:
                    result.drugID=drugID
                    result.drugName=drugName
                    result.drugCategory=drugCategory
                    result.manufacturer=manufacturer
                    result.unitPrice=unitPrice
                    result.no_of_units_in_package=no_of_units_in_package
                    db.commit()
                    st.success("Drug info Update successfully")

                    st.markdown(f'''
                    ##### Drug id - {id}
                    - ###### Drug Name - {drugName}
                    - ###### Drug Category - {drugCategory}
                    - ###### Manufacturer - {manufacturer}
                    - ###### Unit Price - {unitPrice}
                    - ###### no of units in Package - {no_of_units_in_package}
                    ''')
                except Exception as e:
                    st.error(f"Could not Update the info of supplier . {e}")
        db.close()
    elif selected_choice== choices[2]:
        
        st.subheader("Update Invoice details")
        saleInvoiceId = st.number_input("Sale Invoice ID",value=1)
        db = open_db()
        result = db.query(Sale_Invoice).get(saleInvoiceId)
        if not result:
            st.error("first fill the details.")
        else:
            with st.form("add sale Invoice"):

                saleInvoiceId= st.number_input(label="Enter sale Invoice ID",value=result.saleInvoiceId)
                date =st.date_input(label="Enter Date",value=result.date)
                paymentType = st.radio("Select Payment Type",('Online Payment','Cash'))
                totalAmount = st.number_input(label="Enter Total amount",value=result.totalAmount)
                discount = st.number_input(label="Enter Discount",value=result.discount)
                newPrice=st.number_input(label="Enter New price",value=result.newPrice)

                btn= st.form_submit_button("Update")
            
            if id and btn:
                try:
                    result.saleInvoiceId=saleInvoiceId
                    result.date=date
                    result.paymentType=paymentType
                    result.totalAmount=totalAmount
                    result.discount=discount
                    result.newprice=newPrice
                    db.commit()
                    st.success("Invoice info Update successfully")

                    st.markdown(f'''
                    ##### supplier id - {saleInvoiceId}
                    - ###### Date- {date}
                    - ###### Payment Type - {paymentType}
                    - ###### Total Amount - {totalAmount}
                    - ###### Discount - {discount}
                    - ###### New Price - {newPrice}

                    ''')
                except Exception as e:
                    st.error(f"Could not Update the info of supplier . {e}")
        db.close()
    elif selected_choice== choices[3]:
        
        st.subheader("Update Customer details")
        customerId = st.number_input("Customer ID",value=1)
        db = open_db()
        result = db.query(Customer).get(customerId)
        if not result:
            st.error("first fill the details.")
        else:
            with st.form("add Customer"):
                customerId= st.number_input(label="Enter Customer ID",value=result.customerId)
                firstName = st.text_input(label="Enter First Name",value=result.firstName)
                lastName = st.text_input(label="Enter Last Name",value=result.lastName)
                mobilePhone = st.number_input(label="Enter Phone No",value=result.mobilePhone)
                emailAddress = st.text_input(label="Enter email aAddress",value=result.emailAddress)
                pharmacyName=st.text_input(label="Enter pharmacy Name",value=result.pharmacyName)
                address = st.text_input(label="Enter Address",value=result.address)
                city=st.text_input(label="Enter city Name",value=result.city)
                btn= st.form_submit_button("Update")
            
            if id and btn:
                try:
                    result.customerId=customerId
                    result.firstName=firstName
                    result.lastName=lastName
                    result.mobilePhone=mobilePhone
                    result.emailAddress=emailAddress
                    result.pharmacyName=pharmacyName
                    result.address=address
                    result.city=city
                    db.commit()
                    st.success("Customer info Update successfully")

                    st.markdown(f'''
                    ##### Customer id - {customerId}
                    - ###### First name - {firstName}
                    - ###### Last Name - {lastName}
                    - ###### Mobile Number - {mobilePhone}
                    - ###### E-mail - {emailAddress}
                    - ###### Pharmacy Name - {pharmacyName}
                    - ###### Address - {address}
                    - ###### city - {city}
                    ''')
                except Exception as e:
                    st.error(f"Could not Update the info of supplier . {e}")
        db.close()
elif selected_choice== choices[15]:
    st.subheader("delete detalis")

    choices = ['delete Supplier details','delete Drug details','delete Invoice details','delete Customer details',]
    selected_choice = st.selectbox("select an option",options=choices)

    if selected_choice== choices[0]:
        
        st.subheader("delete Supplier details")
        id = st.number_input("Supplier ID",value=1)
        b =st.button("delete supplier")
        if b:
            db = open_db()
            result = db.query(Supplier).get(supplierId)
            if result:
                db.delete(result)
                db.commit()
                st.success("removed")
                db.close()
    if selected_choice== choices[1]:
        
        st.subheader("delete Drug details")
        id = st.number_input("Drug ID",value=1)
        b =st.button("delete drug")
        if b:
            db = open_db()
            result = db.query(Drug).get(drugID)
            if result:
                db.delete(result)
                db.commit()
                st.success("removed")
                db.close()
    if selected_choice== choices[2]:
        
        st.subheader("delete Invoice details")
        saleInvoiceId = st.number_input("Invoice ID",value=1)
        b =st.button("delete Invoice")
        if b:
            db = open_db()
            result = db.query(Sale_Invoice).get(saleInvoiceId)
            if result:
                db.delete(result)
                db.commit()
                st.success("removed")
                db.close()
    if selected_choice== choices[3]:
        
        st.subheader("delete Customer details")
        id = st.number_input("Customer ID",value=1)
        b =st.button("delete Customer")
        if b:
            db = open_db()
            result = db.query(Customer).get(id)
            if result:
                db.delete(result)
                db.commit()
                st.success("removed")
                db.close()
