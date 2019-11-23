CREATE DATABASE IMSDATABASE

USE IMSDATABASE;

CREATE TABLE CUSTOMER
	( UserID 		INT			NOT NULL,
	  Email		VARCHAR(100)	NOT NULL,
	  Fname		VARCHAR(20)	NOT NULL,
	  Lname		VARCHAR(20)	NOT NULL,
	  Address		VARCHAR(100)	NOT NULL,	
	  PhoneNum		CHAR(10)
	  PRIMARY KEY (UserID, Email) );

CREATE TABLE SUPPLIER
	( SupplierID		INT			NOT NULL,
	  Supplier_Name	VARCHAR(40)	NOT NULL,
	  Address		VARCHAR(100)	NOT NULL,
	  PRIMARY KEY(SupplierID),
	  UNIQUE(Supplier_Name) );

CREATE TABLE MANAGER
	( ManagerID		INT			NOT NULL,
	  Email		VARCHAR(100)	NOT NULL,
	  Fname		VARCHAR(20)	NOT NULL,
	  Lname		VARCHAR(20)	NOT NULL,
	  PhoneNum		CHAR(10)		NOT NULL,
	  StoreID		INT,
	  PRIMARY KEY(ManagerID, Email),
	  FOREIGN KEY(StoreID) REFERENCES STORE(StoreID) );

CREATE TABLE PURCHASE
	( ItemID		INT			NOT NULL,
	  UserID		INT 			NOT NULL,
	  PurchaseID		INT			NOT NULL,
	  DateTime		DATE			NOT NULL,
	  Quantity		INT			NOT NULL,
	  PRIMARY KEY(ItemID, UserID, PurchaseID),
	  FOREIGN KEY(ItemID) REFERENCES ITEM(ItemID),
  FOREIGN KEY(UserID) REFERENCES CUSTOMER(UserID),
  FOREIGN KEY (PurchaseID) REFERENCES PURCHASE(PurchaseID) );
	
CREATE TABLE STORE
( StoreID		INT			NOT NULL,
  Name		VARCHAR(25)	NOT NULL,
  Address		VARCHAR(30)	NOT NULL,
  PRIMARY KEY (StoreID) );


CREATE TABLE RESTOCKORDER
( OrderID		INT			NOT NULL,
  Price			INT			NOT NULL,
  Date			DATE			NOT NULL,
  Quantity		INT			NOT NULL,
  ItemID		INT			NOT NULL,
  SupplierID		INT			NOT NULL,
  StoreID		INT			NOT NULL,
  PRIMARY KEY (OrderID),
  FOREIGN KEY (StoreID) REFERENCES STORE(StoreID),
  FOREIGN KEY (SupplierID) REFERENCES SUPPLIER(SupplierID),
  FOREIGN KEY (ItemID) REFERENCES ITEM(ItemID) );

CREATE TABLE INVENTORY
( StoreID		INT			NOT NULL,
  Capacity		INT			NOT NULL,
  PRIMARY KEY (StoreID),
  FOREIGN KEY (StoreID) REFERENCES STORE(StoreID) );

CREATE TABLE ITEM
( ItemID		INT			NOT NULL,
  Name		INT			NOT NULL,
  Price			INT			NOT NULL,
  Gender		CHAR(1)		NOT NULL,
  Stock		INT,
  StoreID		INT			NOT NULL,
  SupplierID		INT			NOT NULL,
  PRIMARY KEY (ItemID), 
  FOREIGN KEY (StoreID) REFERENCES STORE(StoreID),
  FOREIGN KEY (SupplierID) REFERENCES SUPPLIER(SupplierID) );


CREATE TABLE TOPS
( ItemID		INT			NOT NULL,
  Chest_Size		INT			NOT NULL,
  Shirt_Length	INT			NOT NULL,
  Type			VARCHAR(8)	NOT NULL,
  PRIMARY KEY (ItemID),
  FOREIGN KEY (ItemID) REFERENCES ITEM(ItemID) );

CREATE TABLE BOTTOMS
( ItemID		INT			NOT NULL,
  Waist_Size		INT			NOT NULL,
  Pant_Length	INT			NOT NULL,
  Type			VARCHAR(15)	NOT NULL,
  PRIMARY KEY (ItemID),
  FOREIGN KEY (ItemID) REFERENCES ITEM(ItemID) );

CREATE TABLE SHOES
( ItemID		INT			NOT NULL,
  ShoeSize		INT			NOT NULL,
  Type			VARCHAR(15)	NOT NULL,
  PRIMARY KEY (ItemID),
  FOREIGN KEY (ItemID) REFERENCES ITEM(ItemID));


CREATE TABLE ACCESSORIES
( ItemID		INT			NOT NULL,
  Type			VARCHAR(15)	NOT NULL,
  PRIMARY KEY (ItemID),
  FOREIGN KEY (ItemID) REFERENCES ITEM(ItemID));