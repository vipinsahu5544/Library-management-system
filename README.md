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

![screenshot 498](https://user-images.githubusercontent.com/22103635/44654034-0120f000-aa0e-11e8-818d-30513dae6c10.png)


.
.
.
.
Available books

![screenshot 506](https://user-images.githubusercontent.com/22103635/44654051-0aaa5800-aa0e-11e8-8ac9-d7efa5b461f6.png)

.
.
.
.
Enter new book

![screenshot 502](https://user-images.githubusercontent.com/22103635/44654096-36c5d900-aa0e-11e8-825a-3909dcca3843.png)

.
.
.
.
Return book

![screenshot 501](https://user-images.githubusercontent.com/22103635/44654187-7a204780-aa0e-11e8-9a5b-ba5ab5f0725e.png)

.
.
.
.
Issue book page without entry

![screenshot 500](https://user-images.githubusercontent.com/22103635/44654083-2a418080-aa0e-11e8-8a4f-4a430e646cba.png)
.
.
.
.
Entering reader id and book id on issue book page.

![screenshot 505](https://user-images.githubusercontent.com/22103635/44654143-58bf5b80-aa0e-11e8-8e14-6aff9a9578d0.png)

.
.
.
.
Clicking on submit button

![screenshot 504](https://user-images.githubusercontent.com/22103635/44654156-61b02d00-aa0e-11e8-89cd-7bafcbd8fe7d.png)

