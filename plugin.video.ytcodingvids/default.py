# -*- coding: utf-8 -*-
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
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
fanart = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.ytcodingvids', 'fanart.jpg'))

#################################################################################
###################### Insert channel ID here ###################################
#################################################################################
################ Types: Channel ID, user ID, list ID ############################
#################################################################################

YOUTUBE_CHANNEL_ID1 = "PLcUid3OP_4OXOUqYTDGjq-iEwtBf-3l2E"
YOUTUBE_CHANNEL_ID2 = "PLcUid3OP_4OW-rwv_mBHzx9MmE5TxvvcQ"
YOUTUBE_CHANNEL_ID3 = "PLcUid3OP_4OX9q80EIEAWsolQV5cr6RQx"
YOUTUBE_CHANNEL_ID4 = "PLcUid3OP_4OUakQfcLmaQADU3nqGXantN"
YOUTUBE_CHANNEL_ID5 = "PLcUid3OP_4OXhaCvxKPE6YGT75UJzrtOl"
YOUTUBE_CHANNEL_ID6 = "PLcUid3OP_4OVMt2os96qImqAoNsXiZRHv"
YOUTUBE_CHANNEL_ID7 = "PL7D2ADFB4C470C6A0"
YOUTUBE_CHANNEL_ID8 = "UCwRXb5dUK4cvsHbx-rGzSgw"

#################################################################################
######################## Insert channel names here ##############################
#################################################################################

CHANNEL_NAME_1 = "Bash basics"
CHANNEL_NAME_2 = "Using SED"
CHANNEL_NAME_3 = "Android"
CHANNEL_NAME_4 = "Python 3 Basics"
CHANNEL_NAME_5 = "HTML5 Canvas Basics"
CHANNEL_NAME_6 = "PHP Tutorials"
CHANNEL_NAME_7 = "JavaScript"
CHANNEL_NAME_8 = "Derek Banas Channel"

#################################################################################

### Entry point
def run():
    plugintools.log("ytcodingvids.run")
    
### Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

### Main menu
def main_list(params):
    plugintools.log("ytcodingvids.main_list "+repr(params))

###################################################################################
##################### Menu code for channels ######################################
###################################################################################

### Channel additions
    plugintools.add_item(
        #action="",
        title=""+CHANNEL_NAME_8+"",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID8+"/",
        thumbnail="https://yt3.ggpht.com/-SN1RQ4kN5bM/AAAAAAAAAAI/AAAAAAAAAAA/T39gSKk4e2g/s100-c-k-no/photo.jpg",
        fanart="https://i.ytimg.com/u/wRXb5dUK4cvsHbx-rGzSgw/channels4_banner.jpg",
        folder=True )

    plugintools.add_item(
        #action="", 
        title=""+CHANNEL_NAME_1+"",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title=""+CHANNEL_NAME_2+"",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID2+"/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title=""+CHANNEL_NAME_3+"",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID3+"/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title=""+CHANNEL_NAME_4+"",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID4+"/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title=""+CHANNEL_NAME_5+"",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID5+"/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )        

    plugintools.add_item( 
        #action="", 
        title=""+CHANNEL_NAME_6+"",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID6+"/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title=""+CHANNEL_NAME_7+"",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID7+"/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )        
        
### Search        
    plugintools.add_item( 
        #action="", 
    	title="Search for 'Coding' on YouTube",
  	url='plugin://plugin.video.youtube/search/?q=Coding',
    	thumbnail=icon,
    	fanart=fanart,
    	folder=True )
        
####################################################################################
run()
