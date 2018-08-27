# Library-management-system
It is a simple library management system(Using Python) that can perform tasks like - ( Issuing book, Entering new book, showing list of all available books, &amp; Return book).

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
  
  6. In issue book page, Enter only Reader id and book id. All the other information will be fetched automatically (See Screenshots below).

Home page

![screenshot 498](https://user-images.githubusercontent.com/22103635/44652806-860a0a80-aa0a-11e8-8cdf-c8211ca4de57.png)
.
.
.
.
Available books

![screenshot 499](https://user-images.githubusercontent.com/22103635/44652821-991cda80-aa0a-11e8-867a-87e37dcdf10d.png)
.
.
.
.
Enter new book

![screenshot 502](https://user-images.githubusercontent.com/22103635/44652916-dbdeb280-aa0a-11e8-8460-78cc89ede129.png)
.
.
.
.
Issue book

![screenshot 500](https://user-images.githubusercontent.com/22103635/44652951-f7e25400-aa0a-11e8-92e5-18c84fe18793.png)
.
.
.
.
Return book without entry

![screenshot 503](https://user-images.githubusercontent.com/22103635/44653276-e8afd600-aa0b-11e8-9cd1-3add89d95d08.png)
.
.
.
.
Entering reader id and book id on issue book page.

![screenshot 505](https://user-images.githubusercontent.com/22103635/44653326-0aa95880-aa0c-11e8-9a48-658944dd81e3.png)
.
.
.
.
Clicking on submit button

![screenshot 504](https://user-images.githubusercontent.com/22103635/44653343-1dbc2880-aa0c-11e8-810d-30648d925b8a.png)
