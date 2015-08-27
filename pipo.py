import OSC
import time, random

client = OSC.OSCClient()
client.connect( ('10.0.1.119', 9999) )       # note that the argument is a tupple and not two arguments
msg = OSC.OSCMessage()                      #  we reuse the same variable msg used above overwriting it
msg.setAddress("/print")
msg.append(4321)
client.send(msg)                            # now we dont need to tell the client the address anymore

print "done"
