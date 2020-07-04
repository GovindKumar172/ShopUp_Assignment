-- create table web_scaping.book_details

CREATE TABLE IF NOT EXISTS web_scaping.book_details
(
	Id identity(1,1) INTEGER   ENCODE az64
	,book_name CHAR(125)   ENCODE lzo
	,image_link CHAR(225)   ENCODE lzo
	,rating CHAR(10)   ENCODE lzo
	,price decimal(10,5)   ENCODE az64
	,in_stock CHAR(50)   ENCODE lzo

)
DISTSTYLE KEY
 DISTKEY (book_name)
 SORTKEY (book_name) 
;

-- create table Web_Scaping.category_details

CREATE TABLE IF NOT EXISTS web_scaping.category_details
(
	Id identity(1,1) INTEGER   ENCODE az64
	,category_name CHAR(125)   ENCODE lzo
	,link CHAR(225)   ENCODE lzo
)
DISTSTYLE KEY
 DISTKEY (category_name)
 SORTKEY (category_name) 
;

-- Data loading for web_scaping.book_details 

copy web_Scaping.book_details 
from 's3://data-engineer/assignment_data/bookScrap.csv'
credentials 'aws_access_key_id=XXXXX;aws_secret_access_key=YYYYYYYYYY' 
delimiter ','  IGNOREHEADER 1;

-- Data loading for web_scaping.category_details 

copy web_Scaping.category_details 
from 's3://data-engineer/assignment_data/category.csv'
credentials 'aws_access_key_id=XXXXX;aws_secret_access_key=YYYYYYYYYY' 
delimiter ','  IGNOREHEADER 1;

