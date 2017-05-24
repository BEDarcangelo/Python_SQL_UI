import pymysql

username = raw_input("Please enter your username: ")
password = raw_input("Please enter your password: ")
database = raw_input("Please indicate which database you'd like to access: (BTC_Accounting or SJCK_Accounting) ")

db = pymysql.connect('localhost', username, password, database)
cursor = db.cursor()

#functions go here
def insertData(data):
    cursor.execute(data)
    db.commit()

    
table = raw_input("Which table would you like to access? ")
action = raw_input("Would you like to input data or run a query? (Input or Query) ")
print ("Accessing %s from %s") %(table, database)

addMore = True

while addMore == True:
    
    if action == "Input":
        if database == "BTC_Accounting":
            date = raw_input("DATE: ")
            btc_in = float(raw_input("BTC IN: "))
            btc_out = float(raw_input("BTC OUT: "))
            balance = float(raw_input("BALANCE: "))
            fees_paid = float(raw_input("FEES PAID: "))
            cash_value = float(raw_input("CASH VALUE: "))
            trans_type = raw_input("TYPE: ")
            reason = raw_input("REASON: ")

            sql = "INSERT INTO %s (date, btc_in, btc_out, balance, fees_paid, cash_value, trans_type, reason) VALUES ('%s', '%f', '%f', '%f', '%f', '%f', '%s', '%s');" % (table, date, btc_in, btc_out, balance, fees_paid, cash_value, trans_type, reason)
            
            insertData(sql)

        elif database == "SJCX_Accounting":
            date = raw_input("DATE: ")
            sjcx_in = float(raw_input("SJCX IN: "))
            sjcx_out = float(raw_input("SJCX OUT: "))
            balance = float(raw_input("BALANCE: "))
            dollar_value = float(raw_input("DOLLAR VALUE: "))
            trans_type = raw_input("TYPE: ")
            trans_who = raw_input("WHO: ")
            reason = raw_input("REASON: ")
            trans_category = raw_input("CATEGORY: ")
            
            sql = "INSERT INTO %s (date, sjcx_in, sjcx_out, balance, dollar_value, trans_type, trans_who, reason, trans_category) VALUES ('%s', '%f', '%f', '%f', '%f', '%s', '%s', '%s', '%s');" % (table, date, sjcx_in, sjcx_out, balance, dollar_value, trans_type, trans_who, reason, trans_category)
   
            insertData(sql)   
    
    moreData = raw_input("Would you like to add more data? (Y/N)")
    
    if moreData == "N":
        addMore = False
        db.close()