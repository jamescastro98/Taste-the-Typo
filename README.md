# Taste the Typo

This is the repository for the CSE 331 final project. We will be writing this modularly, meaning the web dashboard will execute the typogenerator,
then after the list is generated, it will execute many instances of webbrowse.py (numinstances based upon user Input to dashboard)

**Python Third Party Libraries**

Pyppeteer - Python port of Puppeteer - used for creating headless chrome browsers.

Django - Backend used to connect the front end to the respective scripts.

**JavaScript Third Party Resources**
typewriter-effect - Simple script available on npm for typewriter effect

grapheme-splitter - script used in aiding retyping for typewriter effect

parcel - bundles everything together

**Tentative Responsibilities**

William Braxton - Django/Backend

James Castro - Pyppeteer Scripts & Frontend

Joey Spivack - Typo Generator & Network Node Connections

Nathan Chan - Network Node Connections & Pyppeteer Scripts
Comments & Issues:
    -May just be me: but need to append 'https://' to URL (i.e. google.com -> https://google.com) for webbrowse.py to work.
        However, typogenerator.py does not append to this (instead just creates a list of "www.[urlname].com" typos), so nodeConnection does not work correctly yet
    -Got masternode.py and workernode.py to work and communicate with on another. However have not got around to sending the .png and the .html back to the Master node quite yet.
    
