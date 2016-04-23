#!/bin/python
import os
import subprocess

import theme


if not os.path.exists(theme.TMP_FILE_DIR):
    os.makedirs(theme.TMP_FILE_DIR)

cTheme = theme.AVAILABLE_THEMES[0]
#If there is no current theme
if not os.path.isfile(theme.CURRENT_THEME_FILE):
    f = open(theme.CURRENT_THEME_FILE, 'w')
    f.write(theme.AVAILABLE_THEMES[0])
    f.close()
else:
    f = open(theme.CURRENT_THEME_FILE, "r")
    cTheme = f.readline().replace("\n", "")
    f.close()

#Files exist and a theme has been selected, start changing theme
#selecting the next theme
nextTheme = theme.AVAILABLE_THEMES[(theme.AVAILABLE_THEMES.index(cTheme) + 1) % len(theme.AVAILABLE_THEMES)]

print(nextTheme)

for program in theme.ThemedPrograms:
    cmd = "cp {} {}"
    subprocess.run(["cp", theme.CHANGED_FILES[nextTheme][program], theme.TARGET_PATHS[program]])

for cmd in theme.UPDATE_CMDS:
    subprocessCmd = cmd.split(" ")

    subprocess.run(subprocessCmd)

#Write the new theme
f = open(theme.CURRENT_THEME_FILE, "w")
f.write(nextTheme)

