from errbot import BotPlugin, botcmd
import datetime

class HelloWorld(BotPlugin):
    """Example 'Hello, world!' plugin for Errbot"""



    @botcmd
    def hello(self, msg, args):
        """Say hello to the world"""
        return "Hello, world!"
    
    # Get and Set examples
    @botcmd
    def get(self, msg, args):
        """Remember something and then tell me about it"""
        return "I remember:\n %s" % self['memory']
    
    @botcmd
    def set(self, msg, args):
        """Store something for later"""
        self['memory'] = args
        return "I just SET:\n %s" % self['memory']
    
    # Incident related methods
    @botcmd
    def start_incident(self, msg, args):
        """Start a new incident"""
        self['is_incident'] = True
        now = datetime.datetime.now()
        self['incident_id'] = now.microsecond
        self['incident_start'] = now
        return "Incident %s started at %s" % (self['incident_id'],now)


    @botcmd
    def end_incident(self, msg, args):
        """Start a new incident"""
        self['is_incident'] = False
        now = datetime.datetime.now()
        self['incident_start'] = "n/a"
        self['incident_end'] = now
        return "Incident %s ended at %s" % (self['incident_id'],now)
    
    @botcmd
    def stop_incident(self, msg, args):
       return "Do you mean 'end incident'?"

    @botcmd
    def show_incidents(self, msg, args):
        """Check the currnent status at Sauce Labs for incidents"""
        status = status_update(self)
        return "%s\n%s" % (status, self['incident_id'])
    
def status_update(self):
    if self['is_incident'] == True:
        update = "There is an active incident"
    else: 
        update = "There is no incident"
    return update
