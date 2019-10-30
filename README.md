# Taste the Typo

This is the repository for the CSE 331 final project. We will be writing this modularly, meaning the web dashboard will execute the typogenerator,
then after the list is generated, it will execute many instances of webbrowse.py (numinstances based upon user Input to dashboard)

**Python Third Party Libraries**

Pyppeteer - Python port of Puppeteer - used for creating headless chrome browsers.

Django - Used to connect the front end to the respective scripts.


**Tentative Responsibilities**

William Braxton - Front End (HTML/CSS)

James Castro - Headless Browser/Django

Joey Spivack - Typo Generator/Django

Nathan Chan - Network Node Connections
Comments & Issues:
    -May just be me: but need to append 'https://' to URL (i.e. google.com -> https://google.com) for webbrowse.py to work.
        However, typogenerator.py does not append to this (instead just creates a list of "www.[urlname].com" typos), so nodeConnection does not work correctly yet
    -Not sure how to implement different network nodes yet, as of now I just want to have typoGenerator.py and webbrowse.py place nice
    
