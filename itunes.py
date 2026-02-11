import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
    
response = requests.get('https://itunes.apple.com/search?entity=song&limit=20&term=' + sys.argv[1])

o = response.json() # understand that from the url response.json(), it is a massive string with dictionaries/lists
for result in o['results']: # identifies the dictionary/list name
    print(result['trackName']) # prints the VALUE stored in the KEY 'trackName' in the results dictionary
