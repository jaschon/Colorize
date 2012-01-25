#!/usr/bin/env python

from sys import stdout

__author__ = "Jason Rebuck"
__copyright__ = "2011-2012"
__version__ = "0.07"

#ANSI Codes
FGcolors = {
"black" : "\033[30m",
"red" : "\033[31m",
"green" : "\033[32m",
"yellow" : "\033[33m",
"blue" : "\033[34m",
"magenta" : "\033[35m",
"cyan" : "\033[36m",
"white" : "\033[37m",
"normal" : "\033[39m",
}

BGcolors = {
"black" : "\033[40m",
"red" : "\033[41m",
"green" : "\033[42m",
"yellow" : "\033[43m",
"blue" : "\033[44m",
"magenta" : "\033[45m",
"cyan" : "\033[46m",
"white" : "\033[47m",
"normal" : "\033[49m",
}

STYLEcolors = {
"reset" : "\033[0m",
"bold" : "\033[1m", 
"dim" : "\033[2m", 
"italic" : "\033[3m",
"underline" : "\033[4m",
"inverse" : "\033[7m",
"strike" : "\033[9m",
"normal" : "",
}

#Main Function
def colorize(text, fg="normal", bg="normal", style="normal", align="left", alignWidth=0):
    """Take Text Input and Return Text with ANSI Color/Style Codes Added"""
    width = alignWidth or len(text) #if no width given, use the text length
    if align == 'center': #format text for different alignment
        alignedText = "{text:^{width}}".format(text = text, width = width)
    elif align == 'right': #right align
        alignedText = "{text:>{width}}".format(text = text, width = width)
    else: #fallback to left alignment
        alignedText = "{text:<{width}}".format(text = text, width = width)
    return "{background}{foreground}{style}{text}{reset}".format(background = BGcolors[bg], foreground = FGcolors[fg], style = STYLEcolors[style], text = alignedText, reset = STYLEcolors['reset']) #return throw all values into a string and return

#Shortcuts
def bold(text, color='normal'):
    return colorize(text, color, 'normal', 'bold')

def underline(text, color='normal'):
    return colorize(text, color, 'normal', 'underline')

def inverse(text, color='black'):
    width = len(str(text)) + 2
    return colorize(text, color, 'normal', 'inverse', 'center', width)

#Test Function
def printColorTable():
    """Print a Table of All Styles and Colors"""
    #filter out non-colored/styled items
    skippedList = ('normal', 'default', 'reset', 'inverse', )
    goodColors = sorted([f for f in FGcolors if not f in skippedList ])
    goodStyles = sorted([f for f in STYLEcolors if not f in skippedList ])
    print "\n\t", # start on a new line. add a blank col
    for c in goodColors:
        print colorize(c[:5], c, 'normal', 'normal', 'left', 7), #print row of col headers
    print "" #print new line
    # start printing rows
    for c in goodColors: #loop through colors for use as bg color
       print colorize(c[:6], 'white', c, 'normal', 'left', 6), '\t', #print row header
       for f in goodColors: #loop through colors for fg
           for s in goodStyles: #loop through styles
               stdout.write(colorize('x', f, c, s, 'left')) #print out combo of fg, row color as bg and style
           print "\t", #tab to next col
       print "" #new row
    print "" # end on a new line
           

if __name__ == "__main__":

    print ""
    print bold("Bold Test", 'red')
    print underline("Underline Test", 'blue')
    print inverse("Inverse Test", 'cyan')

    printColorTable()



