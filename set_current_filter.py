# set the current filter to a saved one
# and then retrieve all the cases associated with that filter
#
# the filter is set by number, which has to be looked up by a separate XML query

from fogbugz import FogBugz
import fbSettings

# login
fb = FogBugz(fbSettings.URL, fbSettings.TOKEN)

# Set filter
resp = fb.setCurrentFilter(sFilter='65',)

# Get results
resp = fb.search(cols='ixBug,sTitle,sFixFor,sArea')

print "Raw response:"
print resp

print "\nPrettified response:"
print resp.prettify()
    
print "\nParsed response via Beautiful Soup:"
for case in resp.cases.childGenerator():
  print case.ixbug.string, case.stitle.string.encode('UTF-8'), case.sfixfor.string, case.sarea.string