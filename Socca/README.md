<snippet>
  <content>

Socca is a tkinter GUI application written in python that collects live soccer(football for some!) results from the competitions you choose(This version only supports the English Premier League) and displays them in real time.
## Socca

Changelog :
+ Completed the ViewMatches function and let it display the full EPL matches.
+ Added several tweaks to the ViewMatches function
such as real match times.
+ Added a time function that grabs the UTC time and displays it into the textbox.
+ Added some visual effects to the textbox and a logo.
+ Some general code tweaks.


## To do on the next version
+ Add a refresh button or probably make the application refreshes it self automatically at a given rate.
+ Some future visual GUI improvements.
+ Will expand to other Leagues and Championships.

## Requirments
+ Python 2.7
+ pip install -r requirements.txt

## Installation
To get socca to work follow the following steps :
+ Clone this application
+ Register a http://football-api.com/ account
+ Replace the current API key with yours (in the api variable inside the functions, in the run.py file.)
+ Add your IP address into your football-api account to get the application to connect to the API and you'll be ready to go!

## Usage
![alt tag](http://i.imgur.com/x98O1mh.png)

The UI is pretty straight forward, the code will grab the json response from the API and will behave accordantly.

## Notes
If you run into problems getting this code running in Linux, try updating both your requests and PIL modules
(pip install requests -U) and (pip install PIL)