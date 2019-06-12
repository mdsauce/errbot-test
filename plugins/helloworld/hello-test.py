from errbot import BotPlugin, botcmd

memory = "nothing"


class HelloWorld(BotPlugin):
    """Example 'Hello, world!' plugin for Errbot"""

    @botcmd
    def hello(self, msg, args):
        """Say hello to the world"""
        return "Hello, world!"
    @botcmd
    def getter(self, msg, args):
        """Remember something and then tell me about it"""
        return "I remember %s" % memory
    @botcmd
    def setter(self, msg, args):
        global memory
        memory = args
        """Store something for later"""
        return "I remember:\n %s" % memory