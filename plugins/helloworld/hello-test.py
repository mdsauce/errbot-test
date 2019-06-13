from errbot import BotPlugin, botcmd


class HelloWorld(BotPlugin):
    """Example 'Hello, world!' plugin for Errbot"""

    @botcmd
    def hello(self, msg, args):
        """Say hello to the world"""
        return "Hello, world!"
    @botcmd
    def get(self, msg, args):
        """Remember something and then tell me about it"""
        return "I remember:\n %s" % self['memory']
    @botcmd
    def set(self, msg, args):
        """Store something for later"""
        self['memory'] = args
        return "I just SET:\n %s" % self['memory']