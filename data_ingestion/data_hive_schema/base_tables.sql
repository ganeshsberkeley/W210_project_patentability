-- 
-- Foreign Priority Tables for 2014 and 2015 
--

DROP TABLE IF EXISTS foreign_priority_2014;
CREATE EXTERNAL TABLE foreign_priority_2014
(
	application_number string,
	foreign_parent_id string,
	foreign_parent_date decimal,
	parent_country_code string,
	parent_country  string
)
ROW FORMAT DELIMITED
fields terminated by ','
STORED AS TEXTFILE
LOCATION '/user/root/w210/foreign_priority/2014';

DROP TABLE IF EXISTS foreign_priority_2015;
CREATE EXTERNAL TABLE foreign_priority_2015
(
	application_number string,
	foreign_parent_id string,
	foreign_parent_date decimal,
	parent_country_code string,
	parent_country  string
)
ROW FORMAT DELIMITED
fields terminated by ','
STORED AS TEXTFILE
LOCATION '/user/root/w210/foreign_priority/2015';


-- 
-- Application Priority Tables for 2014 and 2015 
-- 

DROP TABLE IF EXISTS application_data_2014;
CREATE EXTERNAL TABLE application_data_2014 (
	application_number CHAR(14),
	filing_date date,
	invention_subject_matter char(3),
	application_type  char(7),
	examiner_name_last string,
	examiner_name_first string,
	examiner_name_middle string,
	examiner_id string,
	examiner_art_unit string,
	uspc_class string,
	uspc_subclass string,
	confirm_number int,
	customer_number string,
	atty_docket_number string,
	appl_status_code decimal,
	appl_status_date date,
	file_location string,
	file_location_date date,
	earliest_pgpub_number string,
	earliest_pgpub_date date,
	wipo_pub_number decimal,
	patent_number string,
	patent_issue_date date,
	abandon_date date,
	disposal_type string,
	invention_title string,
	small_entity_indicator char(1),
	aia_first_to_file char(1)
)
ROW FORMAT DELIMITED
fields terminated by ','
STORED AS TEXTFILE
LOCATION '/user/root/w210/application_data/2014' ;

DROP TABLE IF EXISTS application_data_2015;
CREATE EXTERNAL TABLE application_data_2015 (
	application_number CHAR(14),
	filing_date date,
	invention_subject_matter char(3),
	application_type  char(7),
	examiner_name_last string,
	examiner_name_first string,
	examiner_name_middle string,
	examiner_id string,
	examiner_art_unit string,
	uspc_class string,
	uspc_subclass string,
	confirm_number int,
	customer_number string,
	atty_docket_number string,
	appl_status_code decimal,
	appl_status_date date,
	file_location string,
	file_location_date date,
	earliest_pgpub_number string,
	earliest_pgpub_date date,
	wipo_pub_number decimal,
	patent_number string,
	patent_issue_date date,
	abandon_date date,
	disposal_type string,
	invention_title string,
	small_entity_indicator char(1),
	aia_first_to_file char(1)
)
ROW FORMAT DELIMITED
fields terminated by ','
STORED AS TEXTFILE
LOCATION '/user/root/w210/application_data/2015' ;

-- 
-- Transactions Tables for 2014 and 2015 
-- 

DROP TABLE IF EXISTS transactions_2014;
CREATE EXTERNAL TABLE transactions_2014(
	application_number string,
	event_code  string,
	recorded_date date,
	sequence_number decimal,
	status_code int
)
row format delimited
fields terminated by ','
stored as textfile
LOCATION '/user/root/w210/transactions/2014' ;

DROP TABLE IF EXISTS transactions_2015;
CREATE EXTERNAL TABLE transactions_2015(
	application_number string,
	event_code  string,
	recorded_date date,
	sequence_number decimal,
	status_code int
)
row format delimited
fields terminated by ','
stored as textfile
LOCATION '/user/root/w210/transactions/2015' ;

-- 
-- Event Codes Tables for 2014 and 2015 
-- 

DROP TABLE IF EXISTS event_codes_2014;
CREATE EXTERNAL TABLE event_codes_2014(
	event_code string,
	event_description string
)
row format delimited
fields terminated by ','
stored as textfile
LOCATION '/user/root/w210/event_codes/2014' ;

DROP TABLE IF EXISTS event_codes_2015;
CREATE EXTERNAL TABLE event_codes_2015(
	event_code string,
	event_description string
)
row format delimited
fields terminated by ','
stored as textfile
LOCATION '/user/root/w210/event_codes/2015' ;

-- 
-- Status Codes Tables for 2014 and 2015 
-- 

DROP TABLE IF EXISTS status_codes_2014;
CREATE EXTERNAL TABLE status_codes_2014(
	appl_status_code  int,
	status_description string
)
row format delimited
fields terminated by ','
stored as textfile
LOCATION '/user/root/w210/status_codes/2014' ;

DROP TABLE IF EXISTS status_codes_2015;
CREATE EXTERNAL TABLE status_codes_2015(
	appl_status_code  int,
	status_description string
)
row format delimited
fields terminated by ','
stored as textfile
LOCATION '/user/root/w210/status_codes/2015' ;

-- 
--   Patents Text Tables for 2014 and 2015 
-- 

DROP TABLE IF EXISTS patent_text_2014 ;
CREATE EXTERNAL TABLE patent_text_2014(
	appl_id string,
	claim_no string,
	claim_txt  string,
	dependencies string,
	ind_flg char(1),
	pat_no  string
)
row format delimited
fields terminated by ','
stored as textfile
LOCATION '/user/root/w210/full_text/2014' ;


DROP TABLE IF EXISTS patent_text_2015 ;
CREATE EXTERNAL TABLE patent_text_2015(
	appl_id string,
	claim_no string,
	claim_txt  string,
	dependencies string,
	ind_flg char(1),
	pat_no  string
)
row format delimited
fields terminated by ','
stored as textfile
LOCATION '/user/root/w210/full_text/2015' ;














