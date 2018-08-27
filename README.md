# Library-management-system
It is a simple library management system that can perform some common tasks,i.e. ( Issuing book, Entering new book, showing list of all available books, &amp; Return book).

Follow the steps.
  1. Download all the files and store them in the same folder.
  
  2. Make sure there is a user "root" and without password in your local database. Host should be localhost.
     i.e.   pymysql.connect(host="localhost",user='root',password='')
     
     Note- A database named "lms" will be automatically created. All the database activity will take place in this "lms" database.
     
  3.The root file is gui_of_lms so you have to execute it. 
    i.e. using command prompt--
         pyhton gui_of_lms.py
         
  4. End.
  
  
  Some points to remember--
  
  1. Some books in available_books table are already entered.
  
  2. Some books in issued_books table are already entered.
  
  3. Members are already entered in member table.
  
  4. For better understanding of tables in database go to your phpMyAdmin after step 3 which is mentioned above.
  
  4. ExecuteSQLQuery has a execute function that executes all the sql command in any sql script.
  
  5. For better redability use any ide. (I have used PyCharm.)
