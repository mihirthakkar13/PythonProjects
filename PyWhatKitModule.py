
# https://www.geeksforgeeks.org/introduction-to-pywhatkit-module/

# above link to refer for pywhatkit module



import pywhatkit
 
#1
try:
   
  # sending message to receiver
  # using pywhatkit
  pywhatkit.sendwhatmsg("+919726366432",
                        "Hello from Mihir",
                        11, 11)
  print("Successfully Sent!")
 
   

  print("An Unexpected Error!")

#2

try:
   
  # it will perform the Google search
  pywhatkit.search("GeeksforGeeks")
  print("Searching...")
 
except:
   
  # Printing Error Message
  print("An unknown error occurred")