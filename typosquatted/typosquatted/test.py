import sys
import signal
from masternode import setupConnections, gatherTypoSquatSites, shutdown

#this sets it up such that when Ctrl+C interupt occurs it cleans up all the reciveing threads and shuts down
signal.signal(signal.SIGINT, shutdown)
#this sets up the daemon thread that accepts new connections from worker nodes. this is called once when the
#server is started up.
setupConnections()
#this begins sending requests to registered worker nodes typos of the given site. this is called to generate
#results for a new request. you may not whant to recall it if the requested results already exists.
#but as it stands now there is no clean up for those results.
gatherTypoSquatSites("www.q.com")

