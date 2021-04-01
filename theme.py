from enum import Enum

class ThemedPrograms(Enum):
    vim = 0
    term = 1
    wallpaper = 2
    tint2 = 3
    # kitty = 4
    alacritty = 5
    delta = 6

#Location where temporary info about the current theme is stored
TMP_FILE_DIR = "/tmp/colors/"
#The name of the file where the current theme will be stored inside tmp directory
CURRENT_THEME_FILE = TMP_FILE_DIR + "current"

#Because for some reason ~ doesn't work
HOME_DIR = "/home/frans/"
WALLPAPER_DIR = HOME_DIR + "Pictures/wallpapers/"
KITTY_DIR = HOME_DIR + ".config/kitty/"

KITTY_TARGET_PATH = KITTY_DIR + "colors"

#Locations to move theme files to
TARGET_PATHS = {
                ThemedPrograms.vim: TMP_FILE_DIR + "vimtheme",
                ThemedPrograms.term: HOME_DIR + ".config/xfce4/terminal/terminalrc",
                ThemedPrograms.wallpaper: WALLPAPER_DIR + "current.png",
                ThemedPrograms.tint2: HOME_DIR + ".config/tint2/tint2rc",
                ThemedPrograms.alacritty: HOME_DIR + ".config/alacritty/alacritty.yml",
                ThemedPrograms.delta: TMP_FILE_DIR + "deltatheme"
            }

#Different color themes that list a set of source files and a place to move them
CHANGED_FILES = {
        "dark": {
                ThemedPrograms.term: HOME_DIR + ".config/xfce4/terminal/darkrc",
                ThemedPrograms.vim: HOME_DIR + ".vim/darkvim",
                ThemedPrograms.wallpaper: WALLPAPER_DIR + "current_dark.png",
                ThemedPrograms.tint2: HOME_DIR + ".config/tint2/rcdark",
                ThemedPrograms.alacritty: HOME_DIR + ".config/alacritty/dark.yml",
                ThemedPrograms.delta: HOME_DIR + ".dotfiles/delta_dark"
            },

        "blue": {
                ThemedPrograms.term: HOME_DIR + ".config/xfce4/terminal/bluerc",
                ThemedPrograms.vim: HOME_DIR + ".vim/bluevim",
                ThemedPrograms.wallpaper: WALLPAPER_DIR + "current_dark.png",
                ThemedPrograms.tint2: HOME_DIR + ".config/tint2/rcdark",
                ThemedPrograms.alacritty: HOME_DIR + ".config/alacritty/dark.yml",
                ThemedPrograms.delta: HOME_DIR + ".dotfiles/delta_dark"
            },

        "light": {
                ThemedPrograms.term: HOME_DIR + ".config/xfce4/terminal/lightrc",
                ThemedPrograms.vim: HOME_DIR + ".vim/lightvim",
                ThemedPrograms.wallpaper: WALLPAPER_DIR + "current_light.png",
                ThemedPrograms.tint2: HOME_DIR + ".config/tint2/rclight",
                ThemedPrograms.alacritty: HOME_DIR + ".config/alacritty/light.yml",
                ThemedPrograms.delta: HOME_DIR + ".dotfiles/delta_light"
            }
        }

THEME_COMMANDS = {
            "dark": [
                    "bspc config normal_border_color #101010",
                    "bspc config focused_border_color #808080"
                ],
            "blue": [
                    "bspc config normal_border_color #101010",
                    "bspc config focused_border_color #808080"
                ],
            "light": [
                    "bspc config normal_border_color #ffffff",
                    "bspc config focused_border_color #808080"
                ]
        }

THEME_NAME_FILES = [
            TMP_FILE_DIR + "konsole"
        ]

AVAILABLE_THEMES = list(CHANGED_FILES.keys())

# print("kitty @ set-colors --all " + TMP_FILE_DIR + "kittycolors")
#Commands to run after changing theme
UPDATE_CMDS = [
            #Update wallpaper
            #"feh --bg-fill --no-xinerama " + WALLPAPER_DIR + "current.png",
            # "kitty @ --to unix:/tmp/kitty set-colors --all " + TMP_FILE_DIR + "kittycolors",
            #Update tint2 panel
            "killall -SIGUSR1 tint2",
            "feh --bg-fill " + WALLPAPER_DIR + "current.png",
        ]
