
drop  table foreign_priority;

create  table foreign_priority (
 application_number string,
 foreign_parent_id string,
 foreign_parent_date decimal,
 parent_country_code string,
 parent_country  string
)
row format delimited
fields terminated by ','
stored as textfile;

LOAD DATA INPATH '/user/root/w210/foreign_priority/'
OVERWRITE INTO TABLE foreign_priority;

drop table application_data;

create table application_data (

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
invention_title string
small_entity_indicator char(1)
aia_first_to_file char(1)
)
row format delimited
fields terminated by ','
stored as textfile;

LOAD DATA INPATH '/user/root/w210/application_data/'
INTO TABLE application_data;

drop table transactions;
create table transactions(

application_number string,
event_code  string
recorded_date date,
sequence_number decimal,
status_code int
)

row format delimited
fields terminated by ','
stored as textfile;
LOAD DATA INPATH '/user/root/w210/transactions/'
INTO TABLE foreign_priority;

drop table event_codes;
create table event_codes(

event_code string,
event_description string
)
row format delimited
fields terminated by ','
stored as textfile;

LOAD DATA INPATH '/user/root/w210/event_codes/'
INTO TABLE event_codes;

drop table status_codes;
create table status_codes(

appl_status_code  int,
status_description string
)
row format delimited
fields terminated by ','
stored as textfile;

LOAD DATA INPATH '/user/root/w210/status_codes/'
INTO TABLE status_codes;

create table patent_text(
appl_id string,
claim_no string,
claim_txt  string,
dependencies string,
ind_flg char(1),
pat_no  string
)

row format delimited
fields terminated by ','
stored as textfile;

LOAD DATA INPATH '/user/root/w210/full_text/'INTO TABLE patent_text;














