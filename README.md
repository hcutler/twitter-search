## Experimenting with Twitter's Search API:
Use Twitter's [Search API](https://dev.twitter.com/rest/public/search) to scrape Twitter. Then use [spaCy](https://spacy.io/docs) to do Named Entity Recognition (NER) on results.


### _To use search functionality:_
1. Enter key credentials into config.py (Obtain OAuth credentials [here](https://dev.twitter.com/oauth))
2. Enter a query of choice (i.e. keyword, hashtag, username) into Line __ of api.py
3. Install [Python twitter package](https://pypi.python.org/pypi/twitter) by typing "pip install twitter" or "npm install twitter" on command line.
4. Run api.py to obtain Twitter search results containing query ("python api.py")

### _To use Named Entity functionality:_
1. Paste results of api.py to textfile OR run "python api.py > results.txt" instead of Step 3 above.
2. Replace filename in Line 11 of spacy_NER.py with name of textfile containing results of api.py (if different from resultx.txt)
3. Use spaCy library to extract Named Entities from Twitter data (Run "python spacy_NER.py")
4. Paste results to textfile OR run "python spacy_NER.py > entities.txt" instead of Step 3 above.
