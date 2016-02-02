#### Before coming for the session, do the following : 

1. Install pip
  * If Windows and using Python3(which in any case you should be) pip comes by default. Make sure Python is in your path
  * If Debian/RedHat/Arch install from your package manager. The command for debian based distros using apt-get would be
  `sudo apt-get install python3-pip`. Similarly search for your own OS
  
2. After you have installed pip, type `pip install virtualenv` (or sudo if requires)
3. Create a new project directory, let's say `webbot` and `cd webbot`
4. You should be now in an empty directory `webbot`
5. On the command line type `virtualenv venv`
6. `venv` folder would be created. Type
  * If *Windows : `venv\Scripts\activate.bat`
  * If *nix :`source venv/bin/activate` 
7. You should see something like `(venv)~/webbot >>`. That means your virtual env has been activated
8. Install two modules we will be using for the session
  * pip install tweepy
  * pip install python-forecastio
9. In order to use Twitter API and Weather API you need to have API keys which you get by registering on them
  * [Forecastio](https://developer.forecast.io/)
  * [Twitter](http://apps.twitter.com/)

10. See you at the session 


