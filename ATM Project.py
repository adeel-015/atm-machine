import mysql.connector as sql
con=sql.connect(host='localhost',user='root',password='toor',database='ATM_MACHINE')
con1=con.cursor()
print("================================================================================")
print("                       WELCOME TO OUR ATM ")
print("================================================================================")
print("1.To create account")
print("2.To login")
print("3.Exit")
print("================================================================================")
o=int(input("Enter your choice : "))
print("================================================================================")
if o==1:
      c="y"
      while c=="y":
            m=int(input("Enter a 4 digit number as account number: "))
            cb="select * from records where ACCOUNT_NO={}".format(m)
            con1.execute(cb)
            d=con1.fetchall()
            data=con1.rowcount
            if data==1:
                  print("================================================================================")
                  print("This account number already exists:")
                  c=input("Do you want to continue? y/n -")
                  print("================================================================================")
                  if c=="y":
                        continue
                  else:
                        print("                    Thank You!")
                        print("           PLEASE CLOSE THIS FILE BEFORE EXITING")
                        print("Visit again")
                        print("================================================================================")
            else:
                  name=input("Enter your name: ")
                  password=int(input("Enter a 4 digit PIN code (numeric only): "))
                  ab="insert into records(ACCOUNT_NO,PASSWORD,NAME) values({},{},'{}')".format(m,password,name)
                  print("================================================================================")
                  con1.execute(ab)
                  con.commit()
                  print("Account sucessfully created")
                  print("The minimum balance is 1000 ")
                  print("================================================================================") 
                  s=int(input("Enter the money to be deposited : "))
                  print("================================================================================")
                  sr="update records set  CURRENT_AMOUNT={} where ACCOUNT_NO={}".format(s,m)
                  con1.execute(sr)
                  con.commit()
                  ef="update records set balance=current_amount-withdrawl where ACCOUNT_NO={}".format(m)
                  con1.execute(ef)
                  con.commit()
                  print("sucessfully deposited")
                  print("                    Thank You!")
                  print("           PLEASE CLOSE THIS FILE BEFORE EXITING")
                  print("Visit again")
                  break
if o==2:
      y="y"
      while y=="y":
            acc=int(input("Enter your account number:"))
            cb="select * from records where ACCOUNT_NO={}".format(acc)
            con1.execute(cb)
            con1.fetchall()
            data=con1.rowcount
            if data==1:
                  password=int(input("Enter your password: "))
                  print("================================================================================")
                  e="select password from records where ACCOUNT_NO={}".format(acc)
                  con1.execute(e)
                  a=con1.fetchone()
                  d=list(a)
                  if password==d[0]:
                        print("correct")
                        print("1.Deposit Money")
                        print("2.Withdraw Money")
                        print("3.Transfer Money")
                        print("4.Check Balance")
                        print("5.Change Account Number")
                        print("================================================================================")
                        r=int(input("Enter your choice:"))
                        print("================================================================================")
                        if r==1:
                              amount=int(input("Enter the money to be deposited: "))
                              print("================================================================================")
                              sr="update records set CURRENT_AMOUNT=CURRENT_AMOUNT + {} where ACCOUNT_NO={}".format(amount,acc)
                              con1.execute(sr)
                              con.commit()
                              ef="update records set balance=current_amount-withdrawl where ACCOUNT_NO={}".format(acc)
                              con1.execute(ef)
                              con.commit()
                              print("sucessfully deposited")
                              t=input("Do you want to continue? y/n -")
                              print("================================================================================")
                              if t=="y":
                                    continue
                              else:
                                    print("                    Thank You!")
                                    print("           PLEASE CLOSE THIS FILE BEFORE EXITING")
                        if r==2:
                              amount=int(input("Enter the money to withdraw: "))
                              print("================================================================================")
                              ah="select  BALANCE from records where account_no={}".format(acc)
                              con1.execute(ah)
                              m=con1.fetchone()
                              if amount>m[0]:
                                    print("You are having less than",amount)
                                    print("Please try again")
                                    print("================================================================================")
                              else:
                                    sr="update records set balance=balance - {}  where ACCOUNT_NO={}".format(amount,acc)
                                    ed="update records set  WITHDRAWL ={}  where ACCOUNT_NO={}".format(amount,acc)
                                    con1.execute(ed)
                                    con1.execute(sr)
                                    con.commit()
                                    print("Successfully Updated")
                              y=input("Do you want to continue? y/n -")
                              if y=="y":
                                    continue
                              else:
                                    print("                    Thank You!")
                                    print("           PLEASE CLOSE THIS FILE BEFORE EXITING")
                        if r==3:
                              account=int(input("Enter the account number to be transferred to: "))
                              print("================================================================================")
                              cb="select * from records where ACCOUNT_NO={}".format(account)
                              con1.execute(cb)
                              con1.fetchall()
                              data=con1.rowcount
                              if data==1:
                                    print(account ,"number exists")
                                    m=int(input("Enter the money to be transferred: "))
                                    print("================================================================================")
                                    ah="select BALANCE from records where account_no={}".format(acc)
                                    con1.execute(ah)
                                    c=con1.fetchone()
                                    if m>c[0]:
                                          print("You are having less than",m)
                                          print("Please try again")
                                          print("================================================================================")
                                    else:
                                          av="update records set balance=balance-{} where ACCOUNT_NO={}".format(m,acc)  
                                          cv="update records set balance=balance+{} where ACCOUNT_NO={}".format(m,account)
                                          w="update records set withdrawl=withdrawl+{} where account_no={}".format(m,acc)
                                          t="update records set  CURRENT_AMOUNT=CURRENT_AMOUNT+{} where account_no={}".format(m,account)
                                          con1.execute(av)
                                          con1.execute(cv)
                                          con1.execute(w)
                                          con1.execute(t)
                                          con.commit()
                                          print("Successfully Transferred!")
                                    y=input("Do you want to continue? y/n -")
                                    if y=="y":
                                          continue
                                    else:
                                          print("                    Thank You!")
                                          print("           PLEASE CLOSE THIS FILE BEFORE EXITING")
                        if r==4:
                              ma="select balance from records where account_no={}".format(acc)
                              con1.execute(ma)
                              k=con1.fetchone
                              print("Balance in your account=",k)
                              print("================================================================================")
                              y=input("Do you want to continue? y/n -")
                              if y=="y":
                                    continue
                              else:
                                    print("                    Thank You!")
                                    print("           PLEASE CLOSE THIS FILE BEFORE EXITING")
                        if r==5:
                              i=int(input("Enter your new account number: "))
                              cb="select * from records where ACCOUNT_NO={}".format(i)
                              con1.execute(cb)
                              con1.fetchall()
                              data=con1.rowcount
                              if data==1:
                                    print("This number already exists")
                                    print("Try again")
                                    y=input("Do you want to continue? y/n -")
                                    if y=="y":
                                          continue
                                    else:
                                          print("                    Thank You!")
                                          print("           PLEASE CLOSE THIS FILE BEFORE EXITING")
                              else:
                                    name=input("Enter your name: ")
                                    ar="Update records set account_no={} where name='{}' and password={}".format(i,name,password)
                                    con1.execute(ar)
                                    con.commit()
                                    print("Your new account number is ",i)
                  else:
                        print("Wrong password")
                        print("================================================================================")
                        y=input("Do you want to continue? y/n -")
            else:
                  print("your Account does not exists")
if o==3:
      print("Exiting")
      print("Please close this file before exiting.")
      con1.close()
