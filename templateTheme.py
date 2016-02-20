from enum import Enum

#Example configuration, copy it to theme.py and edit as you like

#Enum of 'programs' that have files that should be copied. Each 'program' corresponds to
#one copied file
class ThemedPrograms(Enum):
    program1 = 0

#Location where temporary info about the current theme is stored
TMP_FILE_DIR = "/tmp/colors/"
#The name of the file where the current theme will be stored inside tmp directory
#The file will contain a single line with the name of the current theme to make toggeling work
CURRENT_THEME_FILE = TMP_FILE_DIR + "current"

#Helper variables to avoid long repeated filenames.
HOME_DIR = "/home/you/" #For some reason ~ doesn't work

#Locations to move theme files to.
#List the destination config file for each program defined in the ThemedPrograms enum. Be aware
#that these destination files will be overwritten when you run the command
TARGET_PATHS = {
                ThemedPrograms.program1: HOME_DIR + ".config/program1/theme",
            }

#Different color themes that list a set of source files and a place to move them. 
#This should be a dictionary from "theme name" to 'theme files' where 'theme files'
#is a dictionary from ThemedProgram to "config source path"
#Each file in the dictionary will get copied to the corresponding TARGET_PATH
CHANGED_FILES = {
        "dark": {
                ThemedPrograms.program1: HOME_DIR + ".config/program1/darkTheme",
            },

        "light": {
                ThemedPrograms.program1: HOME_DIR + ".config/program1/darkTheme",
            }
        }

#This is used internally, don't change it
AVAILABLE_THEMES = list(CHANGED_FILES.keys())


#Commands to run after changing theme
#These can be used to run programs that apply updates. For example, running a program to set the current wallpaper
#after it has been copied somewhere in the previous steps
UPDATE_CMDS = [
        ]
