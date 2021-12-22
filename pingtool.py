# imports
import os
os.system("pip install pythonping")
import pythonping
from pythonping import ping
os.system("pip install art")
from art import *




#startup code
Art=text2art("Ping Tool")
print(Art)
print("By DumbDannyLol")
print("    ")


#code code
print("Select and option:")
print("Ping [1]     Connection Test [2]   Beginners Manual [3]")
option1 = int(input(""))
if option1 == 1: 
  print("Ping Local [1]    Ping 8.8.8.8 [2]    Custom Ping [3]")
  option1_1 = int(input(""))
  if option1_1 == 1:
    print("Pinging 127.0.0.1 ...")
    ping('localhost', verbose = True)
  if option1_1 == 2:
    print("Pinging 8.8.8.8 ...")
    ping('8.8.8.8')
  if option1_1 == 3:
    print("What would you like to ping? URL or number format only:")
    custom = input("")
    ping(custom, verbose = True)

elif option1 == 2:
  print("Start connection Test now? [Yes = 1   No = 2]")
  option2 = int(input(""))
  if option2 == 1:
    print("Starting Now!")
    ping('8.8.8.8', verbose = True)
    ping('localhost', verbose = True)
    print("Please note if the handshake from 127.0.0.1 does not go through, you most likely have a driver issue.")
  elif option2 == 2:
    print("Then why did you come here? Script Restart required!")

elif option1 == 3:
  print("BEGINNERS GUILD TO PINGTOOL")
  print("   ")
  print("   ")

  print("Select an option:")
  print("Troubleshooting [1]   Help [2]   Error Report [3]  'Dictionary' [4]  ")

  option4 = int(input(""))

  if option4 == 1:
    print("    ")
    print("    ")
    print("TROUBLESHOOTING")
    print("    ")
    print("Select an option:")
    print("What is a reply? [1]   How do I know if it worked? [2]   Errors [3]   Not Pinging [4]  ")
    option5 = int(input(""))
    if option5 == 1:
      print("   ")
      print("If you get a reply, that usually means that the handshake went through and that everything is alright! No worries for this one.")
      print("   ")
      print("Script Restart reqiured!")

    elif option5 == 2:
      print("To know if your ping or connection test worked you should be getting text stating something along the lines of")
      print("Reply from 127.0.0.1, 9 bytes in 0.02ms")
      print("Please note that the 127.0.0.1, 9 and 0.02ms would most likely be something else.")
      print("    ")
      print("Script Restart required!")

    elif option5 == 3:
      print("To report errors please contact me through GitHub at DumbDannyLol.")
      print("   ")
      print("Script Restart Required!")

    elif option5 == 4:
      print("If you know what you are doing (meaning you probably wouldn't be here...) and you are certain that it is not pinging,")
      print("please contact me through GitHub at DumbDannyLol.")
      print("    ")
      print("If you do not know what you are doing, head to the dictionary to see if you can find the definition for something that is going on")
      print("to see if you can figure it out for yourself.")
      print("   ")
      print("If you don't want to use this PingTool cause it's to complicated go download some other Ping tool.")
      print("   ")
      print("Script Restart required!")


  elif option4 == 2:
    print("   ")
    print(" PINGTOOL HELP")
    print("   ")
    print("Custom Ping Help [1]   localhost ping not working [2] ")
    print("Select an option:")
    help1 = int(input(""))
    if help1 == 1:
      print("   ")
      print("For the custom ping, you can put in a URL, or an IP adress.")
      print("   ")
      print("If that doesn't help you reach out to me on GitHub at DumbDannyLol.")

    if help1 == 2:
      print("   ")
      print("If your localhost ping isn't working that means you probably have driver issues.")
      print("   ")
      print("Script restart required!")

  elif option4 == 4:
    print("   ")
    print("PingTool Dictionary")
    print("   ")
    print("Reply: The word that lets you know if the other side is there. It will usually only display if it worked.")
    print("IP adress: uhhh, look it up. Im not explaining it here.")
    print("URL: basically a short name for finding soemthing on the internet i think.")
    print("   ")
    print("Google will have anything else you need.")
    print("   ")
    print("Script restart required!")
