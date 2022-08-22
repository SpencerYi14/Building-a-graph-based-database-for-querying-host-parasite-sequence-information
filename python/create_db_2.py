#!/usr/bin/env python3
import pymysql as mysql
import os
# This will need to be changed to work on the webserver
# doing it local for now

conn = mysql.connect(host='localhost',
        user='gbfilter_user',
        password='yisizhuo',
        db='gb_filter',
        charset='utf8mb4')

cursor = conn.cursor()

drop_cellular = """
DROP TABLE IF EXISTS `host_lineage`;
"""
cursor.execute(drop_cellular)

create_cellular = """
CREATE TABLE `host_lineage` (
`parent_tax_id` mediumint(11) unsigned NOT NULL default '0',
`child_tax_id` mediumint(11) unsigned NOT NULL default '0',
PRIMARY KEY `pk`(`parent_tax_id`, `child_tax_id`),
KEY `parent_tax_id`(`parent_tax_id`),
KEY `child_tax_id`(`child_tax_id`)
);
"""
cursor.execute(create_cellular)

load_cellular = """
LOAD DATA INFILE '/tmp/cellular_lineage.txt'
INTO TABLE `host_lineage` 
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
(parent_tax_id, child_tax_id);
"""
cursor.execute(load_cellular)

drop_viral = """
DROP TABLE IF EXISTS `virus_lineage`;
"""
cursor.execute(drop_viral)
create_viral = """
CREATE TABLE `virus_lineage` (
`parent_tax_id` mediumint(11) unsigned NOT NULL default '0',
`child_tax_id` mediumint(11) unsigned NOT NULL default '0',
PRIMARY KEY `pk`(`parent_tax_id`, `child_tax_id`),
KEY `parent_tax_id`(`parent_tax_id`),
KEY `child_tax_id`(`child_tax_id`)
);
"""
cursor.execute(create_viral)

load_viral = """
LOAD DATA INFILE '/tmp/viral_lineage.txt'
INTO TABLE `virus_lineage`
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
(parent_tax_id, child_tax_id);
"""
cursor.execute(load_viral)

conn.commit()
conn.close()

