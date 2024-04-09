import pyfiglet
from termcolor2 import colored

validColors = "green" , "blue" , "red" , "yellpw" , "cyan" , "magenta"
message = input ("What would you like to print? : ")
color = input ("what color? : ")

if color not in validColors:
    color = "red"
ascii_art = pyfiglet.figlet_format (message)
ascii_art = colored (ascii_art , color= color)
print (ascii_art)