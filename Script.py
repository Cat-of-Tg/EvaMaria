class script(object):
    START_TXT = """
𝙷𝙴𝚈 𝙱𝚁𝙾 𝙸 𝙼 𝚁𝙰𝚂𝙷𝙼𝙸𝙺𝙰 𝙰 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙱𝙾𝚃💸
    🧸𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂 𝙸𝙽 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽 𝙸𝙽 𝚃𝙷𝙴 𝙲𝙷𝙰𝚃 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈✨


<a href='https://t.me/CAT_BOI'>𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 𝙿𝙾𝙸𝚂𝙾𝙽 🎀</a>
"""
    HELP_TXT = """
HERE IS THE HELP FOR MY COMMANDS."""
    ABOUT_TXT = """➤  𝗠𝗬 𝗡𝗔𝗠𝗘 : 𝗥𝗔𝗦𝗛𝗠𝗜𝗞𝗔 𝗠𝗔𝗗𝗔𝗡𝗡𝗔
    
➤  𝗖𝗥𝗘𝗔𝗧𝗢𝗥 : <a href='https://t.me/CAT_OF_TG'>𝗣𝗢𝗜𝗦𝗢𝗡</a>       
    
➤  𝗟𝗜𝗕𝗥𝗔𝗥𝗬 : 𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠             
    
➤  𝗟𝗔𝗡𝗚𝗨𝗔𝗚𝗘 : 𝗣𝗬𝗧𝗛𝗢𝗡 𝟯     
    
➤  𝗦𝗘𝗥𝗩𝗘𝗥 : 𝗛𝗘𝗥𝗢𝗞𝗨     
    
➤  𝗗𝗔𝗧𝗔𝗕𝗔𝗦𝗘 : 𝗠𝗢𝗡𝗚𝗢 𝗗𝗕

• @MOVIE_X_ZONE"""
    
    SOURCE_TXT = """ @CAT_OF_TG """
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and rashmika will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Rashmika should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /add - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Rashmika Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Rashmika supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/mx_filter_bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of tessa

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """➥ ᴛᴏᴛᴀʟ ғɪʟᴇs : <code>{}</code>

➥ ᴛᴏᴛᴀʟ ᴜsᴇʀs : <code>{}</code>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
eeeeeeeeeeee
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
eeeeee
"""
