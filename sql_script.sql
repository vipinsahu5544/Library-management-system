drop database if exists lms;
create database lms;
use lms;

create table available_books
(book_id int(3) primary key AUTO_INCREMENT,
book_name varchar(30) NOT NULL,
Author varchar(20),
Rack_num int(3),
Total_copies int(3) default 5
);


insert into available_books (book_name,Author) values ("A doll's house",'Henrik Ibsen'),
('Word power','Norman Lewis'),('Think and grow rich','Napolian Hill'),('Data structues','Schaum'),
('data analysis','v.k. tripathi'),('Acting course','Rajesh Singh'),('Spirit','Michael Phelps'),
('Gravity','Ashish Upadhyay'),('Coding','Zuckerburg'),('Innovation','Elon Musk'),
('Book11','Author11'),('Book12','Author12'),('Book13','Author13'),('Book14','Author14'),('Book15','Author15'),
('Book16','Author16'),('Book17','Author17'),('Book18','Author18'),('Book19','Author19'),('Book20','Author20'),
('Book21','Author21'),('Book22','Author22'),('Book23','Author23'),('Book24','Author24'),('Book25','Author25'),
('Book26','Author26'),('Book27','Author27'),('Book28','Author28'),('Book29','Author29'),('Book30','Author30'),
('Book31','Author31'),('Book32','Author32'),('Book33','Author33'),('Book34','Author34'),('Book35','Author35'),
('Book36','Author36'),('Book37','Author37'),('Book38','Author38'),('Book39','Author39'),('Book40','Author40'),
('Book41','Author41'),('Book42','Author42'),('Book43','Author43'),('Book44','Author44'),('Book45','Author45'),
('Book46','Author46'),('Book47','Author47'),('Book48','Author48'),('Book49','Author49'),('Book50','Author50');

create table reader
(reader_id int(3) primary key AUTO_INCREMENT,
reader_name varchar(30) NOT NULL,
phone int(10)
);


insert into reader (reader_name,phone) values ("rajesh",7982),
('ram','7985'),
('shyam','7775'),
('sonali','7975'),
('sarthak','5775'),
('sumer','7875'),
('sarad','6775'),
('farhan','4775'),
('raju','8975'),
('rencho','9975');

create table issued_books
(issue_id int(3) primary key AUTO_INCREMENT,
book_id int(3) NOT NULL,
reader_id int(3) NOT NULL,
issue_date datetime,
return_date datetime,
foreign key (reader_id) REFERENCES reader(reader_id),
foreign key (book_id) REFERENCES available_books(book_id)
);


insert into issued_books (book_id,reader_id,issue_date,return_date) values (2,5,'2018-2-13','2018-2-28'),
(3,7,'2018-3-15','2018-2-30');