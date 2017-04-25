from __future__ import unicode_literals

def setup(app):
    app.connect('builder-inited', init)
    
def init(app):
    pass

