import os
import sys
import cherrypy
import formular

current_dir = os.path.dirname( os.path.abspath( __file__ ) )

config = {
	'/html': {
		'tools.staticdir.on': True,
		'tools.staticdir.dir': os.path.join( current_dir, 'html' )
	},
	'/css': {
		'tools.staticdir.on': True,
		'tools.staticdir.dir': os.path.join( current_dir, 'css' )
	},
	'/img': {
		'tools.staticdir.on':  True,
		'tools.staticdir.dir': os.path.join( current_dir, 'img' )
	},
	'/js': {
		'tools.staticdir.on':  True,
		'tools.staticdir.dir': os.path.join( current_dir, 'js' )
	},
}

def application( environ, start_response ):
	cherrypy.config.update( {} )
	cherrypy.tree.mount( formular.Form(), script_name="/", config=config )
	return cherrypy.tree( environ, start_response )
