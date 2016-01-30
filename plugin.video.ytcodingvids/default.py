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

#################################################################################
###################### Insert channel ID here ###################################
#################################################################################
################ Types: Channel ID, user ID, list ID ############################
#################################################################################

YOUTUBE_CHANNEL_ID1 = "PLcUid3OP_4OXOUqYTDGjq-iEwtBf-3l2E"
YOUTUBE_CHANNEL_ID2 = "PLcUid3OP_4OW-rwv_mBHzx9MmE5TxvvcQ"

#################################################################################
######################## Insert channel names here ##############################
#################################################################################

CHANNEL_NAME_1 = "Bash basics"
CHANNEL_NAME_2 = "Using SED"

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
        title=""+CHANNEL_NAME_1+"",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail=icon,
        fanart=fan_art,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title=""+CHANNEL_NAME_2+"",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID2+"/",
        thumbnail=icon,
        fanart=fan_art,
        folder=True )

### Search        
    plugintools.add_item( 
        #action="", 
    	title="Search for 'Coding' on YouTube",
  	url='plugin://plugin.video.youtube/search/?q=Coding',
    	thumbnail=icon,
    	fanart=fan_art,
    	folder=True )
        
####################################################################################
run()
