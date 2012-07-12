# Change the specified case's milestone ("Fixfor" in fogbugz API parlance)
# This will change a case's milestone even if the case is closed
# This is a fast way to change case milestones, especially for 
# closed cases that the UI forces you to reopen before editing

from fogbugz import FogBugz
from datetime import datetime, timedelta
import fbSettings

# user input
sCase = raw_input('Case #: ')
sMilestone = raw_input('New milestone: ')

# open session with FogBugz using our API token
fb = FogBugz(fbSettings.URL, fbSettings.TOKEN)

# update the case
try:
	resp = fb.edit(ixBug=sCase, sFixFor=sMilestone)
except:
    print "Update not performed - Error from FogBugz"

print "Done"
