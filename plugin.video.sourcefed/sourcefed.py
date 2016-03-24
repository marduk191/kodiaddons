# -*- coding: utf-8 -*-
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.ytcodingvids'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
fanart = local.getAddonInfo('fanart')

def run():
    plugintools.log("sourcefed.run")
    
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

def main_list(params):
    plugintools.log("sourcefed.main_list "+repr(params))

    plugintools.add_item(
        #action="",
        title="[COLOR red]Sourcefed[/COLOR]",
        url="plugin://plugin.video.youtube/channel/UC_gE-kg7JvuwCNlbZ1-shlA/",
        thumbnail="https://yt3.ggpht.com/-yIuOtsVJIL4/AAAAAAAAAAI/AAAAAAAAAAA/tPGZUl1gL2E/s100-c-k-no/photo.jpg",
        fanart="https://yt3.ggpht.com/-pzPllYqp4JI/VqawKqInG8I/AAAAAAAAAm8/HdtGk40Imns/w1060-fcrop64=1,00005a57ffffa5a8-nd/SF%2BYouTube%2BChannel%2BArt%2Bjan%2B2016%2Bv2.jpg",
        folder=True )

    plugintools.add_item(
        #action="",
        title="[COLOR red]Sourcefed[/COLOR] [COLOR blue]NERD[/COLOR]",
        url="plugin://plugin.video.youtube/channel/UCuCLhzmx0AGnsViXF0Q44tg/",
        thumbnail="https://yt3.ggpht.com/-VvGlntHkqNk/AAAAAAAAAAI/AAAAAAAAAAA/fCb0Rjkk55A/s100-c-k-no/photo.jpg",
        fanart="https://yt3.ggpht.com/-kZ8g3PvaEeo/Vfb9hjy18JI/AAAAAAAAAaE/DNCVB_KjQt8/w1060-fcrop64=1,00005a57ffffa5a8-nd/SF%2BNERD%2BYouTube%2BChannel%2BArt%2BTemp.jpg",
        folder=True )

    plugintools.add_item(
        #action="",
        title="Nuclear Family",
        url="plugin://plugin.video.youtube/channel/UCLMLTE5R-LR26VKfnaDQtEA/",
        thumbnail="https://yt3.ggpht.com/-i87vxdnuR9M/AAAAAAAAAAI/AAAAAAAAAAA/sNhiSlRc7q8/s100-c-k-no/photo.jpg",
        fanart="https://yt3.ggpht.com/-kt5wpcW41U4/VkuqDIyjqjI/AAAAAAAAACc/h-gBfzP5w8M/w1060-fcrop64=1,00005a57ffffa5a8-nd/Nuclear%2BFam%2BYouTube%2BChannel%2BArt.jpg",
        folder=True )

    plugintools.add_item(
        #action="",
        title="[COLOR blue]People Be Like[/COLOR]",
        url="plugin://plugin.video.youtube/channel/UCAdt0pw24jpW4nK9Ajc1nWg/",
        thumbnail="https://yt3.ggpht.com/-sHpRAdT6tYs/AAAAAAAAAAI/AAAAAAAAAAA/6LbpBubL3Tc/s100-c-k-no/photo.jpg",
        fanart="http://yt3.ggpht.com/-_5GXd8GXEG4/VdeJ_BjT2kI/AAAAAAAAADM/KhG_bDpuJ7c/w1060-fcrop64=1,00005a57ffffa5a8-nd/YouTube%2Bbanner%2B8.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
    	title="Search for 'Sourcefed' on YouTube",
  	    url='plugin://plugin.video.youtube/search/?q=Sourcefed',
        thumbnail="https://yt3.ggpht.com/-yIuOtsVJIL4/AAAAAAAAAAI/AAAAAAAAAAA/tPGZUl1gL2E/s100-c-k-no/photo.jpg",
        fanart="https://yt3.ggpht.com/-pzPllYqp4JI/VqawKqInG8I/AAAAAAAAAm8/HdtGk40Imns/w1060-fcrop64=1,00005a57ffffa5a8-nd/SF%2BYouTube%2BChannel%2BArt%2Bjan%2B2016%2Bv2.jpg",
    	folder=True )
        
run()
