#!/usr/bin/env python

from sys import stdout

__author__ = "Jason Rebuck"
__copyright__ = "2011-2016"
__version__ = "0.11"


class Colorizer:
        """Output Text With Color And Style"""

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

        #Hold Text
        text = ''
              
	def __init__(self, text='', fg="normal", bg="normal", style="normal", align="left", alignWidth=0):
            self.text = self._colorize(text, fg, bg, style, align, alignWidth)

        def get(self):
            return self.text

        def show(self):
            print self.text

	#Main Function
	def _colorize(self, text, fg="normal", bg="normal", style="normal", align="left", alignWidth=0):
	    """Take Text Input and Return Text with ANSI Color/Style Codes Added"""
            try:
	        width = alignWidth or len(text) #if no width given, use the text length
	        if align == 'center': #format text for different alignment
		    alignedText = "{text:^{width}}".format(text = text, width = width)
	        elif align == 'right': #right align
		    alignedText = "{text:>{width}}".format(text = text, width = width)
	        else: #fallback to left alignment
		    alignedText = "{text:<{width}}".format(text = text, width = width)
	        return "{background}{foreground}{style}{text}{reset}".format(background = self.BGcolors[bg], foreground = self.FGcolors[fg], style = self.STYLEcolors[style], text = alignedText, reset = self.STYLEcolors['reset']) #return throw all values into a string and return
            except KeyError:
                print "\n--> Ooops, wrong color or style name! You might want to fix that."
                print '--> Colors ', [c for c in self.FGcolors]
                print '--> Styles ', [s for s in self.STYLEcolors]
                raise 

# Shortcut Classes
class Bold(Colorizer):
    """Output Text In Bold"""
    def __init__(self, text='', color='normal'):
        self.text = self._colorize(text, color, 'normal', 'bold')

class Italic(Colorizer):
    """Output Text In Italics"""
    def __init__(self, text='', color='normal'):
        self.text = self._colorize(text, color, 'normal', 'italic')

class Strike(Colorizer):
    """Output Text In Strike Out"""
    def __init__(self, text='', color='normal'):
        self.text = self._colorize(text, color, 'normal', 'strike')

class Dim(Colorizer):
    """Output Text In Dim"""
    def __init__(self, text='', color='normal'):
        self.text = self._colorize(text, color, 'normal', 'dim')

class Underline(Colorizer):
    """Output Text Underlined"""
    def __init__(self, text='', color='normal'):
        self.text = self._colorize(text, color, 'normal', 'underline')

class Inverse(Colorizer):
    """Output Text Inversed"""
    def __init__(self, text='', fg='black', bg='normal'):
        width = len(str(text)) + 2
        self.text = self._colorize(text, fg, bg, 'inverse', 'center', width)

# Test Class
class TestColorTable(Colorizer):
    """Output Color and Style Table"""
    def __init__(self):
        self.printColorTable()

	#Test Function
    def printColorTable(self):
	"""Print a Table of All Styles and Colors"""
	#filter out non-colored/styled items
	skippedList = ('normal', 'default', 'reset', 'inverse', )
	goodColors = sorted([f for f in self.FGcolors if not f in skippedList ])
	goodStyles = sorted([f for f in self.STYLEcolors if not f in skippedList ])
	print "\n\t", # start on a new line. add a blank col
	for c in goodColors:
	    print self._colorize(c[:5], c, 'normal', 'normal', 'left', 7), #print row of col headers
	print "" #print new line
	# start printing rows
	for c in goodColors: #loop through colors for use as bg color
	   print self._colorize(c[:6], 'white', c, 'normal', 'left', 6), '\t', #print row header
	   for f in goodColors: #loop through colors for fg
	        for s in goodStyles: #loop through styles
		   stdout.write(self._colorize('x', f, c, s, 'left')) #print out combo of fg, row color as bg and style
	        print "\t", #tab to next col
	   print "" #new row
	print "" # end on a new line
	   

if __name__ == "__main__":

    # Run Some Tests...
    print ''
    print Bold("Test Bold Returned").get()
    Bold("Test Bold Printed", "magenta").show()
    Strike("Test Strike", 'red').show()
    Dim("Test Dim", 'cyan').show()
    Italic("Test Italic", 'magenta').show()
    Underline("Test Underline", 'green').show()
    Inverse("Test Inverse", 'blue', 'red').show()

    #Print Test Table
    TestColorTable()


