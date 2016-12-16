# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from models import Articles, db_connect, create_articles_table

class SpidermanPipeline(object):
    """Spiderman pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates articles table.
        """
        engine = db_connect()
        create_articles_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Save articles in the database.
        This method is called for every item pipeline component.
        """
        session = self.Session()
        article = Articles(**item)

        try:
            if session.query(Articles).filter(Articles.url == article.url).count() == 0:
                session.add(article)
                session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
