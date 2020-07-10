# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector

class MyPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = '',
            user = '',
            passwd = '',
            database = '',
            port = ''
        )
        self.curr = self.conn.cursor()
        
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS table_name""")
        self.curr.execute("""CREATE TABLE table_name(
            Name text,
            Phone text,
            Address text,
            Location text,
            Website text
        )""")
        
    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipeline:" + item['Name'])
        return item
    
    def store_db(self, item):
        self.curr.execute("""INSERT INTO table_name VALUES (%s, %s, %s, %s, %s)""", (
            item['Name'],
            item['Phone'],
            item['Address'],
            item['Location'],
            item['Website']
        ))
        self.conn.commit()
