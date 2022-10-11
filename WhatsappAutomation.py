
import pywhatkit
 

try:
   
  
  pywhatkit.sendwhatmsg("+916378626112", "Hello Hacktober",22, 28)
  print("Successfully Sent!")
 
except:
   
  # handling exception
  # and printing error message
  print("An Unexpected Error!")
