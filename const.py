# Do not edit this file, copy this file & rename it to const.py. Any format error will result in not getting start or help message.

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


'''START_KB = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🆘 Help", callback_data="help_cb"),            
        ]
    ]
)'''
START_KB = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('🔗 ᴏᴜʀ ᴄʜᴀɴᴇʟꜱ ʟɪɴᴋꜱ 🔗', url='https://t.me/CINEMAHUB_LINK')
            ],[
            InlineKeyboardButton('📌 ᴍʏ ɢʀᴏᴜᴘ', url='https://t.me/+sZr3rX7Al48yZTI1'),
            InlineKeyboardButton('🛠 ᴍʏ ᴏᴡɴᴇʀ', url='https://t.me/BATMAN_CINEMAHUB')
            ],[
            InlineKeyboardButton('⚠️ ʜᴇʟᴘ', callback_data='help_cb'),
            InlineKeyboardButton('⚙️ ᴀʙᴏᴜᴛ', callback_data='about_cb')
            ],[
            InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ', url='https://t.me/JERRYCINEMAHUB_BOT?startgroup=true')           
        ]
    ]
)
HELP_KB = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔙 Back", callback_data="back_m"),
        ],
    ]
)


#START_MSG = "Hi **[{}](tg://user?id={})**, I am a an autofilter bot which finds & shares media from my database."
START_MSG = """Hi <b><a href='tg://user?id={user_id}'>{name}</a></b>,  
ഞാൻ ഒരു <b>AUTO FILTER BOT</b> ആണ്, എന്റെ ഉടമസ്ഥർ <a href='https://t.me/+sZr3rX7Al48yZTI1'>CINEMA-HUB</a> ആണ്, നിങ്ങൾക്കും നിങ്ങളുടെ ഗ്രൂപ്പുകളിൽ ഇപ്പോൾ എന്നെ ഉപയോഗിക്കാവുന്നതാണ്"""


ST_HELP_MSG = """
**You can find the bot commands here.**
**Group Commands:-**
‣/help - __Show this help message__
‣/settings - __Toggle settings of Precise Mode and Button Mode__
`Precise Mode:` 
- __If Enabled, bot will match the word & return results with only the exact match__
- __If Disabled, bot will match the word & return all the results containing the word__ 
`Result Mode:` 
- __If Button, bot will return results in button format__
- __If List, bot will return results in list format__
- __If HyperLink, bot will return results in hyperlink format__"""

ABOUT_MSG = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: <a href='https://t.me/tomcinemahubbot'>TOM BOT</a>
✯ Cʀᴇᴀᴛᴏʀ: <a href='https://t.me/BATMAN_CINEMAHUB'>Tʜɪs ᴘᴇʀsᴏɴ</a>
✯ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a>
✯ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 3</a>
✯ DᴀᴛᴀBᴀsᴇ: <a href='https://www.mongodb.com/'>MᴏɴɢᴏDB</a>
✯ Bᴏᴛ Sᴇʀᴠᴇʀ: <a href='https://t.me/MYFASTSERVERR'>Qᴜɪᴄᴋ Fᴀsᴛ</a>
✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: v2.0.3 [ Sᴛᴀʙʟᴇ ]</b>"""

HELP_MSG = """
**You can find the bot commands here.**
**Group Commands:-**
‣/help - __Show this help message__
‣/settings - __Toggle settings of Precise Mode and Button Mode__
`Precise Mode:` 
- __If Enabled, bot will match the word & return results with only the exact match__
- __If Disabled, bot will match the word & return all the results containing the word__ 
`Result Mode:` 
- __If Button, bot will return results in button format__
- __If List, bot will return results in list format__
- __If HyperLink, bot will return results in hyperlink format__

**Admin Commands:-**
‣/server - __Get server stats__
‣/restart - __Restart the bot__
‣/stats - __Get bot user stats__
‣/broadcast - __Reply to a message to send that to all bot users__
‣/index - __Start indexing a database channel (bot must be admin of the channel if that is private channel)__
__You can just forward the message from database channel for starting indexing, no need to use the /index command__
/indexlink - __Start indexing a database channel using link (bot must be admin of the channel if that is private channel)__
__`/indexlink <last message link>` or `/indexlink <start message link> <last message link>`__
‣/ban - __Ban a user from bot__ - `/ban user_id`
‣/unban - __Unban a user from bot__ - `/unban user_id`
‣/addfilter - __Add a text filter__ - `/addfilter filter message` __or__ `/addfilter "filter multiple words" message` __(If a filter is there, bot will send the filter rather than file)__
‣/delfilter - __Delete a text filter__ - `/delfilter filter`
‣/listfilters - __List all filters currently added in the bot__
‣/forcesub - __Set force subscribe channel__ - `/forcesub channel_id/off` __or__ `/forcesub channel_id request`(for request channel) __Bot must be admin of that channel (Bot will create a new invite link for that channel)__
‣/fsubrequest - __Toggle force subscribe join request after adding force subscribe channel__ - `/fsubrequest on/off`
‣/clearfsubusers - __Clear all force subscribe users from db__
‣/checklink - __Check invite link for force subscribe channel__
‣/infomsg - __Set info message before sending file__ - `/infomsg message/off`
‣/infoimg - __Set info image before sending file__ - Reply `/infoimg` to an image to set or  `/infoimg off` to remove
‣/delmsg - __Set delete message after sending file (File auto delete needs to be enabled to work)__ - `/delmsg message/off`
‣/delimg - __Set delete image after sending file (File auto delete needs to be enabled to work)__ - Reply `/delimg` to an image to set or  `/delimg off` to remove
‣/notfoundmsg - __Set message to send when file not found__ - `/notfoundmsg message/off`
‣/notfoundimg - __Set image to send when file not found__ - Reply `/notfoundimg` to an image to set or  `/notfoundimg off` to remove
‣/fsubmsg - __Set force subscribe message__ - `/fsubmsg message/off`
‣/fsubimg - __Set force subscribe image__ - Reply `/fsubimg` to an image to set or  `/fsubimg off` to remove
‣/total - __Get count of total files in DB__
"""

REMOVE_WORDS = [
    "[MCU]", "@WMR", "Dramaost", "@R A R B G", "AMZN", "WEBDL", "WEB DL", "DVDRip", "HDRip", "HDTV", 
    "rarbg", "HSWEBDL", "10Bit", "WEBRip", "AAC", "DD5 1", "6CH", "2CH", "DDP5 1", "Mp3", "ESub", "EAC3", 
    "Uncut", "192Kbps", "HQ", "AVC", "UNTOUCHED", "mp4", "bluray", "@Ava", "384kbps", "192kbps", "WEB-DL", 
    "ZEE5", "10 bit", "10bit", "XVid", "unrated", "avc", "Hswebdl", "@MM LINKZ", "[MZM]", "@IM", "IMAX", 
    "EXTENDED", "viki", "iqiyi", "Seriesland4u", "DSNP", "DVDWO", "@MM OLD", "@CC", "Atmos", "Mubi", "AAC2 0", 
    "Repack", "proper", "Seriesland", "Mallu hub", "Mallumovies", "Mallumv", "Tamilmv", "Tamilrockers", "www", 
    "Directors cut", "FC_HEVC", "CDL", "Cdrama", "Kdrama", "Kdramaforyouall", "Ccineclub", "400MB", "250MB", 
    "500mB", "700MB", "900MB", "1600MB", "950MB", "600MB", "intermedia", "Sample", "CPTN5DW", "JrRip", "SH3LBY", 
    "Telly", "Primefix", "mkvCinemas", "HEvcbay", "Mkvking", "Dramahub", "Dramaday", "NF Webdl", "DDP5.1", 
    "Adrama Lovers", "TBPINDEX", "MZM", "MOVIEZ", "RAREFILMS", "Raremoviez", "backup", "Open matte", "AAC5.1 1", 
    "MCU", "YTS", "FULLHD", "HDSECTOR", "Extended", "vmax", "yessma", "king.com", "Divxtotal", "Tuktukcinema", 
    "Cimaclub.com", "Shahid4U.com", "Aflamfree", "backup", "DA Rips", "HDMovies", "kbps", "IMEDIASHARE", 
    "Rickychannel", "mubimovies", "CC ALL", "Infotainment", "mkvcage", "movie mania", "[Dno]", "zeemarathimovies", 
    "C C Channel", "WMR", "UCParadiso", "imovieshare", "Team HDT", "TeamHDT", "Toonsworld4all", "INTERNAL", "DnO", 
    "Cinemavilla", "Ongoing", "MMAX", "MM OLD", "[MM]", "Cinema naab", "NSSS", "[", "]", "mkv", "@MM", "Adrama", 
    "Toonworld4all", "SONYLIV", "SS DD 5 1", "DD 5 1", "CC Telugu", "Cc Tamil", "cc new", "hindimovies", "bm links", 
    "mm links", "Piro", "DS4K", "DDP5 1", "DDP 5 1", "voot", "Fanszz", "Tv2us", "CC ALL", "AAC2 0", "AAC", "(", ")", 
    "Ddp2 0", "FBM ALL", "FB TAMIL", "FBM HW", "FBM NEW", "FBM x265", "FBM KOREAN", "FBM", "KICKASS", "TORRENTS", 
    "@", "Dubbed", "Tamilblasters", "dubb", "ssrreq", "VGCINEMAS", "SNXT", "TG SKY MOVIES HD"
]

STOP_WORDS = []
