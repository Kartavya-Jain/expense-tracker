-- Show Databases
show databases;
create database if not exists expense_tracker;
use expense_tracker;
create table if not exists Transactions(
	id int auto_increment primary key,
    amount decimal(10,2) not null,
    category text,
    type varchar(20) not null,
    date date,
    description text
);
show tables;
describe transactions;
insert into Transactions
(amount, category, type, date, description)
values
(299.99, 'food', 'expense','2026-06-07','Ate sandwich at Namo-Sandwich'),
(150, 'pocket-money', 'income','2026-06-07','Got my monthly pocket-money'),
(465, 'stationary','expense','2026-06-03','Bought some drawing material');
select * from Transactions;
delete from Transactions where
id=1;
drop table Transactions;
ALTER USER 'root'@'localhost'
IDENTIFIED WITH mysql_native_password BY 'root';
FLUSH PRIVILEGES;