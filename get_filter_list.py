# get the list of filters from FogBugz

from fogbugz import FogBugz
import fbSettings

# login
fb = FogBugz(fbSettings.URL, fbSettings.TOKEN)

# Get list of all filters
resp = fb.listFilters()

print "Raw response:"
print resp

print "\nPrettified response:"
print resp.prettify()
    