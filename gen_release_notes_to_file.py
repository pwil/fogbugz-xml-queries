# Output a list of closed cases ordered by Area and case
# Write to a file to enable easy cut/paste to your release notes document
# This script adds qualifying cases to a list as a tuple containing each 
# of the fields that will be output to the file

from fogbugz import FogBugz
from datetime import datetime, timedelta
import fbSettings

def compare(a, b):
# standard custom compare-two-value routine for use by built-in sort function
  return cmp(int(a), int(b)) # compare as integers
        
# user input
sProject = raw_input('Project to get: ')
sMilestone = raw_input('Milestone to get: ')
sFilename = "releasenotes_" + sProject + "_" + sMilestone + ".txt"

# FogBugz search string
sSearch = "project:\"" + sProject + "\" milestone:\"" + sMilestone + "\""

# open session with FogBugz using our API token
fb = FogBugz(fbSettings.URL, fbSettings.TOKEN)

# run the search
resp = fb.search(q=sSearch,cols='ixBug,sArea,sTitle,sReleaseNotes')

# list that we will read cases into
L = list()

# iterate over the returned list of cases and add those with release notes to the list
for case in resp.cases.childGenerator():
  myReleaseNote = case.sreleasenotes.string
  
  # just capture cases with release notes attached ('None' is the null result)
  if myReleaseNote != None:
    # add the case to the list
    L.append((case.sarea.string, case.ixbug.string, case.stitle.string.encode('UTF-8'), case.sreleasenotes.string.encode('UTF-8'))) #tuple

L.sort()

# get ready to write release notes output
item=L[0]  # first element in list
currentArea = item[0] # zeroeth element in tuple is the Area

# open and write the release notes file and automatically close when done
with open(sFilename, 'w') as f: 

  f.write('Release notes for ' + sProject + ' ' + sMilestone + '\n\n')

  # header for first FogBugz Area
  f.write('--- ' + currentArea + ' ---\n')

  for item in L:
    recordArea = item[0] # get area (zero element of tuple) from the current list item
    if recordArea != currentArea:  # header for next FogBugz Area
      f.write('\n--- ' + recordArea + ' ---\n')
      currentArea = recordArea
    f.write(item[1] + " - " + item[2] + '\n')
    f.write(item[3] + '\n')
    f.write('\n')