#import haystack
#haystack.autodiscover()

#from whoosh import fields
#from whoosh.fields import SchemaClass, TEXT, KEYWORD, ID, STORED
#
#from whoosh import index
#
##class MySchema(SchemaClass):
##	path = ID(stored=True)
##	title = TEXT(stored=True)
##	content = TEXT
##	tags = KEYWORD
#
##ix = index.create_in("merenbachdotcom_index", MySchema)
#
#ix = index.open_dir("/home/merenbach/webapps/django/whoosh/merenbachdotcom_index")
#
#writer = ix.writer()
#writer.add_field("title", fields.TEXT(stored=True))
###writer.remove_field("content")
#writer.commit()

#from whoosh import store, fields, index
#
#WHOOSH_SCHEMA = fields.Schema(title=fields.TEXT(stored=True),
#		content=fields.TEXT,
#		url=fields.ID(stored=True, unique=True))
#
#import datetime
#from haystack.indexes import *
#from haystack import site
#from cmsplugin_blog.models import Entry, EntryTitle
#
#class EntryIndex(SearchIndex):
#	text = CharField(document=True, use_template=True)
#	#title = CharField(model_attr='title')
#	#author = CharField(model_attr='user')
#	pub_date = DateTimeField(model_attr='pub_date')
#	
#	def index_queryset(self):
#		"""Used when the entire index for model is updated."""
#		return Entry.objects.filter(pub_date__lte=datetime.datetime.now())
#
#
#site.register(Entry, EntryIndex)
