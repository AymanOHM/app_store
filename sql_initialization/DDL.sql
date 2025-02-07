create database appstore;

GO
use appstore;

GO
create table users (
	user_id	int	not null primary key identity(1,1),
	name	varchar(50) not null UNIQUE,
	email	varchar(100) not null UNIQUE,
	password	varchar(25) not null,
	pay_info varchar(25),
	balance decimal(10,2) default 0 CHECK (balance >= 0),
);

GO
create table transactions (
	trans_id	int	not null primary key identity,
	user_id	int not null,
	creation_date date DEFAULT getdate(),
	num_of_apps int default 0 NOT NULL check (num_of_apps >= 0),
	done		bit	default 0,
	Foreign key (user_id) references users (user_id) ON DELETE NO ACTION,
);


create table developers (
	dev_id		int	not null primary key identity(1,1),
	email		varchar(50) not null UNIQUE,
	name		varchar(25) not null UNIQUE,
	password		varchar(25) not null,
	contact_info	varchar(50),
	website	varchar(50),
);


create table categories (
	cat_name	varchar(25)	not null primary key,
	cat_description	varchar(40),
);


GO
create table apps (
	app_id		int	NOT NULL PRIMARY KEY IDENTITY,
	name		varchar(25) UNIQUE,
	cat_name    varchar(25),
	app_version	decimal(5,3),
	rating int default 0 check (rating >= 0),
	release_date	date DEFAULT GETDATE(),
	downloads	int default 0 check (downloads >= 0),
	price		  decimal(10,2) DEFAULT 0,
	app_description	varchar(300),
	dev_id		int,
	app_path	varchar(40) not null UNIQUE,
	icon_path	varchar(40) not null UNIQUE,
FOREIGN KEY (dev_id) REFERENCES developers (dev_id) ON DELETE CASCADE,
FOREIGN KEY (cat_name) REFERENCES categories(cat_name) ON DELETE SET NULL ON UPDATE CASCADE,
);


GO
create table reviews (
	user_id	  int not null,
	app_id		int not null,
	rating		int not null check (rating between 1 and 5),
	review_text	varchar(300),
	review_date	date default getdate(),
	primary key (user_id,app_id),
	foreign key (user_id) references users (user_id) ON DELETE CASCADE,
	foreign key (app_id) references apps (app_id) ON DELETE CASCADE,
);


GO
create table apps_trans (
	trans_id	int not null,
	app_id	int not null,
	primary key (trans_id, app_id),
	foreign key (trans_id) references transactions (trans_id) ON DELETE CASCADE,
	foreign key (app_id) references apps (app_id) ON DELETE CASCADE,
);      