# Taste the Typo

This is the repository for the CSE 331 final project. We will be writing this modularly, meaning the web dashboard will execute the typogenerator,
then after the list is generated, it will execute many instances of webbrowse.py (numinstances based upon user Input to dashboard)

**How to Run**

Ensure your directory is typosquatted. Type python3 manage.py runserver. Now open your browser and go to http://127.0.0.1:8000/home/

This is the homepage. When you type in a URL (https://facebook.com , for instance), a request is made. Spin up worker nodes by going outside the typosquatted directory and typing python3 workernodelocal.py. The file workernode.py is for worker nodes spun up in a VM, which is what we use in the "production version". It will then start going to the typosquatted sites and taking screenshots.

**Python Third Party Libraries**

Pyppeteer - Python port of Puppeteer - used for creating headless chrome browsers.

Django - Backend used to connect the front end to the respective scripts.

**JavaScript Third Party Resources**

typewriter-effect - Simple script available on npm for typewriter effect


**Tentative Responsibilities**

William Braxton - Django/Backend

James Castro - Pyppeteer Scripts & Frontend

Joey Spivack - Typo Generator & Network Node Connections

Nathan Chan - Network Node Connections & Pyppeteer Scripts

    
