'''
A little side project created by meddbeibia@gmail.com
'''

from Tkinter import *
import requests
import ImageTk
import Image
import json
import time

# Create the root window
root= Tk()
# Modify the window
root.title("Socca Interface")
root.geometry("600x600")
root.resizable(width=FALSE, height=FALSE)
# Favicon
root.iconbitmap('./images/favicon.ico')
# Images
img = ImageTk.PhotoImage(Image.open("./images/back.png"))
panel = Label(root, image = img)
panel.pack(side = "top", fill = "both", expand = "yes")

# Labels and widgets
label1 = Label( root, text="")
# Create a text box in tkinter GUI (to display output from the function)
output = Text(root,background="gray",selectbackground="red", height=20, width=50) 
output.pack()

# Time function
def CheckTime():
  js = "http://date.jsontest.com/"
  respobj = requests.get(js)
  adict = respobj.json()
  theresponse = adict['time']
  return theresponse

# Quit function
def quit():
	print 'Bye bye!'
	time.sleep(2)
	root.destroy() 
# Check connection to the API function	
def CheckAuth():
  api = "http://football-api.com/api/?Action=today&APIKey=INSERT-API-KEY-HERE"
  respobj = requests.get(api)
  adict = respobj.json()
  theresponse = adict['ERROR']
  return theresponse
# Check if there is any matches
def CheckMatches():
  api = "http://football-api.com/api/?Action=today&APIKey=INSERT-API-KEY-HERE"
  respobj = requests.get(api)
  adict = respobj.json()
  theresponse = adict['ERROR']
  return theresponse
  
# Display the matches  
def ViewMatches():
  api = "http://football-api.com/api/?Action=today&APIKey=INSERT-API-KEY-HERE"
  respobj = requests.get(api)
  adict = respobj.json()
  output.insert(END, "TIME IS NOW ")
  output.insert(END, CheckTime())
  output.insert(END, " UTC" )
  output.insert(END, "\n")
  output.insert(END, "\n")
  output.insert(END, "Today's Premier League Matches are : ")
  for idx,item in enumerate(adict['matches']): 
   output.insert(END, "\n")
   output.insert(END, "\n")
   output.insert(END, adict['matches'][idx]['match_localteam_name'])
   output.insert(END, " ")
   output.insert(END, adict['matches'][idx]['match_localteam_score'])
   output.insert(END, " - ")
   output.insert(END, adict['matches'][idx]['match_visitorteam_score'])
   output.insert(END, " ")
   output.insert(END, adict['matches'][idx]['match_visitorteam_name'])
   output.insert(END, " ")
   output.insert(END, adict['matches'][idx]['match_status'],adict['matches'][idx]['match_time'] )
# End of Matches display
  
if(CheckMatches()) == "no matches found today":
   output.insert(END, "  There are no premier league matches today")
   # submit button to begin the exit function
   submit = Button(root, text ="EXIT", command = quit)
   submit.pack(side =BOTTOM) 

elif(CheckAuth()) == "This IP is not recognized. Please make sure to enter the allowed IPs in the Account area":
   output.insert(END, "You are not connected to the API(make sure you've added your IP to the football-api.com account.)")
   # submit button to begin the exit function
   submit = Button(root, text ="EXIT", command = quit)
   submit.pack(side =BOTTOM) 
else:
   submit = Button(root, text ="View matches", command = ViewMatches)
   submit.pack(side =BOTTOM)
print 'Socca is functioning!'

# Packing labels
label1.pack()
# Run loop
root.mainloop()