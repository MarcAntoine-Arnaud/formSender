import os
import cherrypy
import smtplib
import sendgrid

current_dir = os.path.dirname( os.path.abspath( __file__ ) )

class Form(object):
	def __init__( self ):
		self.mail = "test-mailing-appfog@googlegroups.com"

	@cherrypy.expose
	def index( self ):
		template    = open( os.path.join( current_dir, "html", "template.html" ),    "r" ).read()
		menu        = open( os.path.join( current_dir, "html", "menu.html" ),        "r" ).read()
		formContact = open( os.path.join( current_dir, "html", "index.html" ), "r" ).read()

		template = template.replace( '{%MENU%}', menu )
		template = template.replace( '{%CONTENT%}', formContact )
		return template

	@cherrypy.expose
	def dcp( self ):
		template    = open( os.path.join( current_dir, "html", "template.html" ),    "r" ).read()
		menu        = open( os.path.join( current_dir, "html", "menu.html" ),        "r" ).read()
		formContact = open( os.path.join( current_dir, "html", "formDCP.html" ), "r" ).read()

		template = template.replace( '{%MENU%}', menu )
		template = template.replace( '{%CONTENT%}', formContact )
		return template

	@cherrypy.expose
	def compression( self ):
		template    = open( os.path.join( current_dir, "html", "template.html" ),    "r" ).read()
		menu        = open( os.path.join( current_dir, "html", "menu.html" ),        "r" ).read()
		formContact = open( os.path.join( current_dir, "html", "formCompression.html" ), "r" ).read()

		template = template.replace( '{%MENU%}', menu )
		template = template.replace( '{%CONTENT%}', formContact )
		return template

	@cherrypy.expose
	def contact( self ):
		template    = open( os.path.join( current_dir, "html", "template.html" ),    "r" ).read()
		menu        = open( os.path.join( current_dir, "html", "menu.html" ),        "r" ).read()
		formContact = open( os.path.join( current_dir, "html", "formContact.html" ), "r" ).read()

		template = template.replace( '{%MENU%}', menu )
		template = template.replace( '{%CONTENT%}', formContact )
		return template

	@cherrypy.expose
	def send( self, firstname, pays, age, civility, fromMail, lastname, cv ):
		print "send"

		s = sendgrid.Sendgrid( os.environ.get('SENDGRID_USERNAME'), os.environ.get('SENDGRID_PASSWORD'), secure=True )

		body = '<html><head></head><body>'
		body += 'My name is ' + firstname + ' ' + lastname + '.<br/>'
		body += "I'm comming from " + pays + ' to ask you this DCP.<br/><br/>'
		body += 'Bye bye amigo.'
		body += '</body></html>'

		message = sendgrid.Message( fromMail, "DCP job", '', body )
		message.add_to( self.mail, "Compression Team")

		s.web.send( message )

