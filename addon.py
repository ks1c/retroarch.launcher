import xbmcgui
import subprocess

if xbmcgui.Dialog().yesno("Retroarch Launcher", "Do you want to launch Retroarch?"):
    xbmc.executebuiltin("Quit")
    subprocess.call([".kodi/addons/retroarch.launcher/launch-retroarch.sh"])
