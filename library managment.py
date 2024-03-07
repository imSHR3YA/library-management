-0import pymysql

# Add your own database name and password here to reflect in the code
mypass = "4902"
mydatabase="library"

# table names in library
issueTable = "books_issued"     #issued table
bookTable = "books"             #Book Table

allBookids = []                 #List To store all Book IDs


con = pymysql.connect(host="localhost",user="root",password=mypass, database=mydatabase)
cur = con.cursor()



def bookRegister():
    
    bookid = input("\n\t\t\tEnter book ID  :  ")
    title =  input("\n\t\t\tEnter book Title  :  ")
    author = input("\n\t\t\tEnter book Author  :  ")
    status = input("\n\t\t\tEnter book Status - avail/issued  :  ")
    
    insertBooks = "insert into "+bookTable+" values('"+bookid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        print('\n\t\t\tSuccess!!!',"Book added successfully")
    except:
        print("\n\t\t\tError","Can't add data into Database")
    
    print('\n\t\t\t', bookid)
    print('\t\t\t', title)
    print('\t\t\t', author)
    print('\t\t\t', status)


def deleteBook():
    
    bookid = input("\n\t\t\tEnter book ID to be Deleted  :  ")
    
    deleteSql = "delete from "+bookTable+" where bookid = '"+bookid+"'"
    deleteIssue = "delete from "+issueTable+" where bookid = '"+bookid+"'"


    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        print('\n\t\t\tSuccess',"Book Has Been Deleted Successfully")
    except:
        print("\n\t\t\tPlease recheck Book ID")
    

    print('\n\t\t\t', bookid)


def returnn():

    bookid = input("\n\t\t\tEnter book ID of the returning book  :  ")

    extractBookid = "select bookid from "+issueTable

    try:
        cur.execute(extractBookid)
        con.commit()

        for i in cur:
            allBookids.append(i[0])
        
        if bookid in allBookids:
            checkAvail = "select status from "+bookTable+" where bookid = '"+bookid+"'"
            cur.execute(checkAvail)
            con.commit()

            for i in cur:
                check = i[0]
                
            if check == 'issued':
                status = True
            else:
                status = False

        else:
            print("\n\t\t\tError","Book ID not present")
    except:
        print("\n\t\t\tError","Can't fetch Book IDs")
    
    
    issueSql = "delete from "+issueTable+" where bookid = '"+bookid+"'"
  
    print('\n\t\t\t', bookid in allBookids)
    print('\t\t\t', status)

    updateStatus = "update "+bookTable+" set status = 'avail' where bookid = '"+bookid+"'"

    try:
        if bookid in allBookids and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            print('\n\t\t\tSuccess',"Book Returned Successfully")
        else:
            allBookids.clear()
            print('\n\t\t\tMessage',"Please check the book ID")
            return
    except:
        print("\n\t\t\tSearch Error","The value entered is wrong, Try again")
    
    allBookids.clear()
    

def View(): 
    
    print("\n\t\t\t%-10s%-35s%-25s%-15s"%('BID','Title','Author','Status'))
    getBooks = "select * from "+bookTable

    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            print("\n\t\t\t%-10s%-35s%-25s%-15s"%(i[0],i[1],i[2],i[3]))

    except:
        print("\n\t\t\tFailed to fetch files from database")



def issue():

    global status
    
    bookid = input("\n\t\t\tEnter book ID of the book being issued  :  ")
    issueto = input("\n\t\t\tEnter Name of the person book is being issued to :  ")

    extractBookid = "select bookid from "+ bookTable

    try:
        cur.execute(extractBookid)
        con.commit()
        for i in cur:
            allBookids.append(i[0])
        
        if bookid in allBookids:
            checkAvail = "select status from "+bookTable+" where bookid = '"+bookid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'avail' or check == 'Avail':
                status = True
            else:
                status = False

        else:
            print("\n\t\t\tError","Book ID not present")
    except:
        print("\n\t\t\tError","Can't fetch Book IDs")
    
    issueSql = "insert into "+issueTable+" values ('"+bookid+"','"+issueto+"')"
    
    
    updateStatus = "update "+bookTable+" set status = 'issued' where bookid = '"+bookid+"'"
    
    try:
        if bookid in allBookids and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            print('\n\t\t\tSuccess',"Book Issued Successfully")

        else:
            allBookids.clear()
            print('\n\t\t\tMessage',"Book Already Issued")
            return
    except:
        print("\n\t\t\tSearch Error","The value entered is wrong, Try again")
    
    print('\n\t\t\t', bookid)
    print('\t\t\t', issueto)
    
    allBookids.clear()


def showIssuedbooks(): 
    
    print("\n\t\t\t%-10s%-55s"%('BookID',"Borrower's Name"))
    show = "select * from "+issueTable
    
    try:
        cur.execute(show)
        con.cursor()
        for i in cur:
            print("\n\t\t\t%-10s%-55s"%(i[0],i[1]))

    except:
        print("\n\t\t\tFailed to fetch files from database")



print("""\n
\t\t\t               ********************************************************************
\t\t\t                                                Welcome To              
\t\t\t                                      ಠ▃ಠ BOOK SHOP  ಠ▃ಠ
\t\t\t**************************************************************************************************
""")

print("\t\t\t                                      HAVE FUN EXPLORING MY SHOP   ")

print("""\n
\t\t\t        -------------------------------------        -------------------------------------
\t\t\t               ENTER 1 TO ADD BOOKS                         ENTER 2 TO DELETE BOOKS
\t\t\t        -------------------------------------        ------------------------------------- """)


print("""
\t\t\t        -------------------------------------        -------------------------------------
\t\t\t               ENTER 3 TO VIEW BOOKS                         ENTER 4 TO ISSUE BOOKS
\t\t\t        -------------------------------------        ------------------------------------- """)


print("""
\t\t\t        -------------------------------------        -------------------------------------
\t\t\t              ENTER 5 TO RETURN BOOKS                  ENTER 6 TO VIEW ISSUED BOOKS
\t\t\t        -------------------------------------        -------------------------------------
""")

print("""
\t\t\t                               -------------------------------------
\t\t\t                                        ENTER 'Q' TO QUIT!!
\t\t\t                               -------------------------------------
""")


while True:

    choice = input("\n\t\t\t Enter your choice ( 1 TO 6 or 'Q/q to Quit' )  : ")

    if choice == '1':
        bookRegister()
        
    elif choice == '2':
        deleteBook()

    elif choice == '3':
        View()

    elif choice == '4':
        issue()
    
    elif choice == '5':
        returnn() 
        
    elif choice == '6':
        showIssuedbooks()

    elif choice == 'Q' or choice == 'q':
        break

    else:
        print("\n\t\t\tPlease Enter a VALID choice!!!!\n")






        
