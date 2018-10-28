# Scraping comments from regulationsgov

This is an initial attempt to contribute to 
[data for democracy - public charge project](https://github.com/Data4Democracy/immigration-connect/tree/master/public-charge).

The regulations site is rendered using javascript. As such, simple scrapping
tools will fail and thus the use of selenium in this project.

Comments are organized using an ID of the type `USCIS-*`.
To minimize the ammount of request done to the site, we are proposing to get
all USCIS IDs and then use this to get the url for each individual comment.

The url for each comment is of the type `{baseURL}/document?D=USCIS-XXXXXX`.

The current script will print the request uri for the first 50 comments on the
site.
