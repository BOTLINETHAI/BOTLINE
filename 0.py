# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile 
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator



cl = LINETCR.LINE()
#cl.login(qr=True)
cl.login(token="") 
cl.loginResult()




ki6 = LINETCR.LINE()

AsulLogged = False

print u"login LINETCR success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""||=====  F O R   U S E R  =====||
||✒️✒ Mention       - Mention All Member Group
||✒️✒ Point       - Set Point Read
||✒️✒ Read        - Reading Point
||✒️✒ Ginfo         - Info Grup
||===== F O R   A D M I N =====||
||✒️✒ Glist         - List Group BOT
||✒️✒ Cancel        - Cancel All Pending Grup
||✒️✒ Mid @         - Get MID 
||✒️✒ Invite        - Invite Via Send Contact
||✒️✒ Invite:       - Via MID
||✒️✒ Whitelist @   - Via Tag
||✒️✒ Whitelist:    - Via Mid
||✒️✒ Whitelist     - Via Send Contact
||✒️✒ Blacklist @   - Via Tag
||✒️✒ Blacklist:    - Via Mid
||✒️✒ Blacklist     - Via Send Contact
||✒️✒ Clear ban     - Delete All Blacklist
||✒️✒ Link on       - Open QR
||✒️✒ Link off      - Close QR
||✒️✒ Gurl          - Open QR And Get Link
||✒️✒ Url           - Get QR Link
||✒️✒ Gname         - Change Name Group
||✒️✒ Banlist       - Cek Tersangka Kriminal
||✒️✒ Details grup  - Via Gid
||✒️✒ Inviteme:     - Via Gid
||✒️✒ Info grup
||✒️✒ Clear grup
||✒️✒️ Reject    - ลบรัน
||✒️✒️ Aslogin   - ขอลิ้งล็อคอินasul
||✒️✒️ .         - เช็คสถานะล็อคอิน asul
||✒️✒️ Reject1   - ลบรัน asul
||===== F O R  K I C K E R =====||
||✒️✒ Nuke
||✒️✒ Ratakan
||✒️✒ Kick @        - Via Tag
||✒️✒ Kick:         - Via MID
||===== F O R  P L A Y E R =====||
||✒️✒ Bc:ct 
||✒️✒ Bc:grup
||✒️✒ Block @
||✒️✒ Blocklist
||✒️✒ Spam on/off
||✒️✒ ไวรัส01
||✒️✒ Bot:ct        - Broadcast to All Contact BOT
||✒️✒ Bot:grup      - Broadcast to All Grup Joined BOT
||✒️✒ Allname:      - Change All Name BOT
||✒️✒ Allbio:       - Change All Bio BOT
||✒️✒ Bot sp        - Tes Speed BOT
||✒️✒ Speed         - Tes Speed
||✒️✒ Mycopy @      - Copy Profile 
||✒️✒ Mybackup @    - Backup Profile
||========================||


||===== S E T T I G S =====||          
|| [Like:on/off]     
|| [Add on/off] 	 
|| [Join on/off] 	   
|| [Contact on/off] 	
|| [Leave on/off]  
|| [Share on/off]           
|| [Add on/off] 		   
|| [Jam on/off]			   
|| [Jam say:]			   
|| [Com on/off]	
|| [Message set:]	
|| [Comment set:]	
|| [Pesan add:]	
||===== P R O T E C T =====||        
|| [Panick:on/off]      
|| [Protect on]			   
|| [Qrprotect on/off]			   
|| [Inviteprotect on/off]			   
|| [Cancelprotect on/off]		   
|| [Staff add/remove @]	   
||======= FOR ADMIN =======||

               ✯==== Creator ====✯
	
  Http://line.me/ti/p/~guarmselfbot

                    
"""

Thaihelp ="""\n
        ||=======================||
         ✒️ 👑sᴇʟғʙᴏᴛ ᴛʜᴀɪʟᴀɴᴅ 👑✒️
        ||=======================||

            🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥

👑✒️👑คท  - ส่งคท.ตัวเอง(Me)
👑✒️👑ไอดี  - ส่งMidตัวเอ
👑✒️👑เชคชื่อ  - เชครายชื่อคิกเกอร์
👑✒️👑คิกเกอร์  - เชคคท.คิกเกอร์ทั้งหมด
👑✒👑คิกมา  - เรียกคิกเกอร์เข้ากลุ่ม
👑✒️👑คิกออก  - สั่งคิกเกอร์ออกกลุ่ม
👑✒️👑1-10 in  - เรียกคิกเกอร์
👑✒👑1-10 bye. - สั่งคิกเกอร์ออก
👑✒️👑แทค  - แทคสมาชิก
👑✒️👑จุด   - ตั้งจุดเชคคนอ่าน
👑✒️👑อ่าน  - เชครายชื่อคนอ่าน
👑✒️👑เชคกลุ่ม  - เชคข้อมูลกลุ่ม
👑✒️👑ลิสกลุ่ม  - เชคกลุ่มที่มีทั้งหมด
👑✒️👑ยกเชิญ,ยก  - ยกเลิกเชิญ
👑✒👑Mid @  - เชคMidรายบุคคล
👑✒️👑ดึง  - เชิญคนเข้ากลุ่มด้วยคท.
👑✒👑ดึง:  - เชิญคนเข้ากลุ่ม้ดวยMid
👑✒️👑ขาว  - แก้ดำ(ส่งคท.)
👑✒️👑Ban @ - ยัดดำ
👑✒️👑เชคดำ  - เชคบัญชีดำ
👑✒️👑เชคดำ2 - จะขึ้น คท คนติดดำ
👑✒️👑ล้างดำ  - ล้างบัญชีดำ
👑✒️👑เปิดลิ้ง 
👑✒️👑ปิดลิ้ง
👑️✒️👑ลิ้ง  - เปิดและขอลิ้งกลุ่ม
👑✒️👑Gname:  - เปลี่ยนชื่อกลุ่ม
👑️✒️👑รัน @  - รันกลุ่ม
👑✒️👑ลบรัน  - ลบรันตัวเอง
👑✒️👑Nuke - ล้างห้อง
👑✒️👑- เชคสถานะลอคอิน
👑✒️👑Sp  - เชคสปีด
👑✒️👑Bot sp  - เชคสปีดคิกเกอร์
👑✒️👑Mycopy @  - กอพปี้โปรไฟล์
👑✒️👑Copy @  - คิกเกอร์1กอพปี้
👑✒️👑Mybackup  - กลับร่างเดิม
👑✒️👑Backup  - คิกเกอร์1กลับร่างเดิม
👑✒️👑Spam on/off  - ส่งข้อความสแปม
👑️✒️👑ยูทูป เว้นหนึ่งครั้งแล้วตามด้วยชื่อเพลง
👑✒️👑เพลง เว้นหนึ่งครั้งแล้วตามด้วยชื่อเพลง
👑✒️👑รีบอท
👑✒👑Tr-en แปรภาษาเป็นอังกฤษ
👑✒️👑Tr-id แปรภาษาเป็นอินโด
👑✒️👑Tr-th แปรภาษาเป็นไทย
👑✒️👑Siri: แล้วตามด้วยข้อความ
👑✒️👑Getcover @ - ขโมยปก
👑✒️👑runtime - เช็คเวลาบอท
👑✒️👑Getmid @ - ขโมยmid
👑✒️👑Getinfo @ - ขโมยข้อมูล
👑✒️👑Getbio @ - ขโมยตัส
👑✒️👑Getname @ - ขโมยชื่อ 
👑✒️👑Getprofile @ - ขโมยข้อมูลครบ
👑✒️👑Getcontact @ - ขโมย คท
👑✒️👑Getpict @ - ขโมยดิสรูปภาพ
👑✒️👑Getvid @ - ขโมยดิสวีดีโอ  
👑✒️👑Picturl @ - ขโมยลิ้งดิส
👑✒👑Coverurl @ - ขโมยลิ้งปก
👑✒👑image (ข้อความ) - หารูปภาพ
👑✒️👑say - สั่งสิริ
👑✒️👑เช็คเพื่อน - เช็คเพื่อน
👑✒️👑Music - ขอเพลง
👑✒️👑เช็คบ๊อค - เช็คคนที่บ๊อค

 ---🏆🌟Self & Kicker Premium🌟🏆---
─┅═हই ᵀᴱᴬᴹᴃᴏᴛ ᴌᵻᴎᴇ™ᵀᴴᴬᴵᴸᴬᴺᴰ ইह═┅─

🔥🔥🔥 คำสั่งตั้งค่า  🔥🔥🔥         

👑✒️[เปิดแทค/ปิดแทค]                   
👑✒️[เปิดแทค2/ปิดแทค2]
👑✒️[เปิดไลค์/ปิดไลค์]     
👑✒️[เปิดแอด/ปิดแอด]   
👑✒️[เปิดเข้า/ปิดเข้า]     
👑✒️[เปิดคท./ปิดคท.]  
👑✒️[เปิดออก/ปิดออก]  
👑✒️[เปิดแชร์/ปิดแชร์]          
👑✒️[เปิดแอด/ปิดแอด]
👑✒️[เปิดข้อความคนเข้า/เปิดข้อความคนเข้า]-[Wm on/Wm off]
👑✒️[Wm cek/เช็คข้อความคนเข้า]
👑✒️[Wm set: ] เซตข้อความคนเข้าห้อง
👑✒️[Lm set: ] เซตข้อความคนออกห้อง
👑✒️[เปิดข้อความคนออก/เปิดข้อความคนออก]-[Lm on/Lm off]
👑✒️[Lm cek/เช็คเข้าความคนออก]
👑✒️[Respon set: ] เซตข้อความคนแทค 
👑✒️["Respon cek/เช็คข้อความคนแทค]
👑✒️[Jam on/off]      
👑✒️[Jam say:]      
👑✒️[Com on/off] 
👑✒️[Message set:] 
👑✒️[Comment set:] 
👑✒️[Pesan add:] 

🔥🔥🔥คำสั่งป้องกัน🔥🔥🔥

🔒🔥️[เปิดหมด/ปิดหมด]      
🔒🔥️[เปิดกัน/ปิดกัน]      
🔒🔥[เปิดกันลิ้ง/ปิดกันลิ้ง]      
🔒🔥[เปิดเชิญ/ปิดเชิญ]     
🔒🔥[เปิดกันยก/ปิดกันยก]     
🔒🔥[Staff add/remove @]    

🔥🔥🔥สำหรับแอดมิน 🔥🔥🔥

╔•═•-⊰✯⊱•═•⊰✯⊱•═•⊰✯⊱ •═•╗ 
✫   👑ŤỂÄΜ ж βǾŦ👑฿Ǿ¥👑    ✫   
╚•═•-⊰✯⊱•═•⊰✯⊱•═•⊰✯⊱ •═•╝


        •   S҉̉̈́͐͋҉̉̈́͐͋K҉̉̈́͐͋҉̉̈́͐͋Y҉ͩ͂҉̉̈́͐͋҉̉̈́͐͋⚒B҉̉̈́͐͋Ω҉̉̈́͐͋T҉̉̈́͐͋S҉̉̈́͐͋   •

 
ŤỂÄΜ Bot :👑ŤỂÄΜ ж βǾŦ👑฿Ǿ¥👑
 

"""
selfMessage="""\n
Respon on/off 
Respon set:
Wm on/off 
Wm set:
Wm1 on/off
Wm1 set:
Wm2 on/off 
Wm2 set: 
Lm on/off 
Lm set: 
Respon cek
Wm cek
Lm cek
"""

helo=""

KAC=[cl]
mid = cl.getProfile().mid
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
Bots = [mid,""]
bot1 = cl.getProfile().mid
owner = [""]
admsa = ""
admin = ""
adminMID = ""
Creator= ""

wait = {
    "alwayRead":False,
   # "detectMention":False,  
    'potoMention':False,
    "kickMention":False,
    "steal":False,
    'pap':{},
    'invite':{},
    "spam":{},
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":True, "members":1},
    #"Members":1,
    "AutoCancel":False,
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'message':"ᴛʜᴀɴκ ᶠᴼᴿ ᴀᴅᴅ ᴹᴱ \n\n─┅═✥ sᴀᴛᴀɴ ᴛᴇs̵ᴛ - ʙᴏᴛ✥═┅─\n		line://ti/p/~0625199257",
    "lang":"JP",
    "comment":"ᴛʜιs ιs ᴀυтᴏ ʟικᴇ вч\n\n─┅═✥ sᴀᴛᴀɴ ᴛᴇs̵ᴛ - ʙᴏᴛ✥═┅─\n			line://ti/p/~esci_",
    "commentOn":False,
    "welkam":"ข้อความคนเข้า",
    "welkam1": "Selamat Bergabung",
    "welkam2": "Selamat Bergabung",
    "bye":"เข้าความคนออก",
    "tag":"ข้อความแทค",
    "read":"Masuk chat sini.. !!",
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "likeOn":False,
    "pname":False,
    #"WC":False,
    #"Gbye":False,
    "blacklist":{},
    #"blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "qr":False,
    "Backup":False,
    "protectionOn":False,
    "winvite":False,
    "ainvite":False,
    "binvite":False,
    "cinvite":False,
    "dinvite":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "Notifed":False,
    "Notifedbot":False,
    "atjointicket":True,
    "pnharfbot":{},
    "Welcome":False,
    "Welcome1": False,
    "Welcome2": False,
    "Leave": False,
    "Mention": False,
    "sticker":False,
    "pname":{},
    "pro_name":{},
    "posts":False,
	}

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

settings = {
    "simiSimi":{}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
  
res = {
    'num':{},
    'us':{},
    'au':{},
    }

tikel = {
     'STKID': '17866',
     'STKPKGID': '1070',
     'STKVER': '2'
     }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

blacklistFile='blacklist.txt'
BpendinglistFile='pendinglist.txt'
lgncall = ""

def logincall(this):
    cl.sendText(lgncall,"Asul login url: "+this)

setTime = {}
setTime = wait2['setTime']
blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus




user1 = mid
user2 = ""

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'CHROMEOS\t7.18.0\tChrome_OS\t1'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    image = client.upload_from_path(image_path, config=config, anon=False)
    print()
	
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    day, hours = divmod(hours,24)
    return '\n🕛 %02d วัน 🕛\n🕛 %02d ชั่วโมง 🕛\n🕛 %02d นาที 🕛\n🕛 %02d วินาที 🕛' % (day, hours, mins, secs)
	
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    print nm
    for mm in nama:
      akh = akh + 3
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 4
      akh = akh + 1
      bb += "@x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = bb
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       cl.sendMessage(msg)
    except Exception as error:
        print error
        
def sendAudio(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentType = 3).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': objectId,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True
        
def sendAudio(self, to_, path):
        M = Message(to=to_,contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        return True
        
def sendAudioWithURL(self, to_, url):
        path = 'pythonLiness.data'
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download Audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e       
            
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items
    
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()            
    
def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)

 
def removeAllMessages(self, lastMessageId):
     return self._cl.removeAllMessages(0, lastMessageId)
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："] 
    for tex in tex:
      for command in commands:
        if string ==command:
          return True
     
def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text
        
def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n • " + Name
                wait2['ROM'][op.param1][op.param2] = " • " + Name
        else:
            pass
    except:
        pass
      
def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
	       sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return
      
            

#def kedapkedip(self, tomid, text):
#        M = Message()
#        M.to = tomid
#        t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
#        t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
#        rst = t1 + text + t2
#        M.text = rst.replace("\n", " ")
#        return self.Talk.client.sendMessage(0) 
    
def bot(op):
    global AsulLogged
    global ki6
    global user2
    global readAlert
    global lgncall
    global save1
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
            if mid in op.param3:
                if wait["AutoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                else:
		    cl.rejectGroupInvitation(op.param1)
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in admin:
                        pass
		    else:
                        cl.cancelGroupInvitation(op.param1, [op.param3])
                else:
		    if op.param3 in wait["blacklist"]:
                        cl.cancelGroupInvitation(op.param1, [op.param3])
                        cl.sendText(op.param1, "Itu kicker jgn di invite!")
		    else:
                        pass
                
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = ki2.getGroup(op.param1)
                            except:
                                try:
                                    G = ki3.getGroup(op.param1)
                                except:
                                    try:
                                        G = ki4.getGroup(op.param1)
                                    except:
                                        try:
                                            G = ki5.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pname'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                ki2.updateGroup(G)
                            except:
                                try:
                                    ki3.updateGroup(G)
                                except:
                                    try:
                                        ki4.updateGroup(G)
                                    except:
                                        try:
                                            ki5.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in DEF:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        ki5.sendText(op.param1,"please do not change group name-_-")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)
                    
#-----------------------------------------------
            if kimid in op.param3:
                G = ki.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki.cancelGroupInvitation(op.param1, matched_list)
            if ki2mid in op.param3:
                G = ki2.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki2.rejectGroupInvitation(op.param1)
                        else:
                            ki2.acceptGroupInvitation(op.param1)
                    else:
                        ki2.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki2.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki2.cancelGroupInvitation(op.param1, matched_list)                  
#      
#          
            if ki3mid in op.param3:
                G = ki3.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki3.rejectGroupInvitation(op.param1)
                        else:
                            ki3.acceptGroupInvitation(op.param1)
                    else:
                        ki3.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki3.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki3.cancelGroupInvitation(op.param1, matched_list)                  
#      
            if ki4mid in op.param3:
                G = ki4.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki4.rejectGroupInvitation(op.param1)
                        else:
                            ki4.acceptGroupInvitation(op.param1)
                    else:
                        ki4.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki4.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki4.cancelGroupInvitation(op.param1, matched_list)                  
#      
            if ki5mid in op.param3:
                G = ki5.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki5.rejectGroupInvitation(op.param1)
                        else:
                            ki5.acceptGroupInvitation(op.param1)
                    else:
                        ki5.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki5.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki5.cancelGroupInvitation(op.param1, matched_list)                  
#      
#            if k1mid in op.param3:
#                G = cl.getGroup(op.param1)
#
#if wait["autoJoin"] == True:
#                    if wait["autoCancel"]["on"] == True:
#                        if len(G.members) <= wait["autoCancel"]["members"]:
#                            k1.rejectGroupInvitation(op.param1)
#                        else:
#                            k1.acceptGroupInvitation(op.param1)
#                    else:
#                        k1.acceptGroupInvitation(op.param1)
#                elif wait["autoCancel"]["on"] == True:
#                    if len(G.members) <= wait["autoCancel"]["members"]:
#                        k1.rejectGroupInvitation(op.param1)
#            else:
#                Inviter = op.param3.replace("",',')
#                InviterX = Inviter.split(",")
#                matched_list = []
#                for tag in wait["blacklist"]:
#                    matched_list+=filter(lambda str: str == tag, InviterX)
#                if matched_list == []:
#                    pass
#                else:
#                    k1.cancelGroupInvitation(op.param1, matched_list)                  
      
# 
#if k2mid in op.param3:
#                G = cl.getGroup(op.param1)
#                if wait["autoJoin"] == True:
#                    if wait["autoCancel"]["on"] == True:
#                        if len(G.members) <= wait["autoCancel"]["members"]:
#                            k2.rejectGroupInvitation(op.param1)
#                        else:
#                            k2.acceptGroupInvitation(op.param1)
#                    else:
#                        k2.acceptGroupInvitation(op.param1)
#                elif wait["autoCancel"]["on"] == True:
#                    if len(G.members) <= wait["autoCancel"]["members"]:
#                        k2.rejectGroupInvitation(op.param1)
#            else:
#                Inviter = op.param3.replace("",',')
#                InviterX = Inviter.split(",")
#                matched_list = []
#                for tag in wait["blacklist"]:
#                    matched_list+=filter(lambda str: str == tag, InviterX)
#                if matched_list == []:
#                    pass
#                else:
#                    k2.cancelGroupInvitation(op.param1, matched_list)                  
       
#            if k3mid in op.param3:
#                G = cl.getGroup(op.param1)
#                if wait["autoJoin"] == True:
#                    if wait["autoCancel"]["on"] == True:
#                        if len(G.members) <= wait["autoCancel"]["members"]:
##                            k3.rejectGroupInvitation(op.param1)
#                        else:
#                            k3.acceptGroupInvitation(op.param1)
#                    else:
#                        k3.acceptGroupInvitation(op.param1)
#                elif wait["autoCancel"]["on"] == True:
#                    if len(G.members) <= wait["autoCancel"]["members"]:
#                        k3.rejectGroupInvitation(op.param1)
 #           else:
#                Inviter = op.param3.replace("",',')
#                InviterX = Inviter.split(",")
#                matched_list = []
#  
 # for tag in wait["blacklist"]:
#                    matched_list+=filter(lambda str: str == tag, InviterX)
#                if matched_list == []:
#                    pass
#                else:
#                    k3.cancelGroupInvitation(op.param1, matched_list)                  
      
#            if k4mid in op.param3:
#                G = cl.getGroup(op.param1)
#                if wait["autoJoin"] == True:
#                    if wait["autoCancel"]["on"] == True:
#                        if len(G.members) <= wait["autoCancel"]["members"]:
#                            k4.rejectGroupInvitation(op.param1)
#                        else:
#                            k4.acceptGroupInvitation(op.param1)
#                    else:
#                        k4.acceptGroupInvitation(op.param1)
#                elif wait["autoCancel"]["on"] == True:
#                    if len(G.members) <= wait["autoCancel"]["members"]:
#                        k4.rejectGroupInvitation(op.param1)
##            else:

#Inviter = op.param3.replace("",',')
#                InviterX = Inviter.split(",")
#                matched_list = []
#                for tag in wait["blacklist"]:
#                    matched_list+=filter(lambda str: str == tag, InviterX)
#                if matched_list == []:
#                    pass
#                else:
#                    k4.cancelGroupInvitation(op.param1, matched_list)                  
      
#            if k5mid in op.param3:
#                G = cl.getGroup(op.param1)
#                if wait["autoJoin"] == True:
#                    if wait["autoCancel"]["on"] == True:
#                        if len(G.members) <= wait["autoCancel"]["members"]:
#                            k5.rejectGroupInvitation(op.param1)
#                        else:
#                            k5.acceptGroupInvitation(op.param1)
#                    else:
#                        k5.acceptGroupInvitation(op.param1)
#                elif wait["autoCancel"]["on"] == True:
#                    if len(G.members) <= wait["autoCancel"]["members"]:
#                        k5.rejectGroupInvitation(op.param1)
#            else:
#                Inviter = op.param3.replace("",',')
#                InviterX = Inviter.split(",")
#                matched_list = []
#                for tag in wait["blacklist"]:
#                    matched_list+=filter(lambda str: str == tag, InviterX)
#                if matched_list == []:
#                    pass
#                else:
#                    k5.cancelGroupInvitation(op.param1, matched_list)                  
      
        #if op.type == 15:
            #if wait["Gbye"] == True:
                #if op.param2 in Bots:
                    #return
                #cl.sendText(op.param1,cl.getContact(op.param2).displayName + " 😭เอ้า..ไปซะละ😭\n👋👋👋\n👼แร้วกลับมาเจอกันใหม่น๊าาา👼")
               # print "MEMBER OUT GROUP"

      #  if op.type == 17:
            #if wait["WC"] == True:
                #if op.param2 in Bots:
                    return
                #ginfo = cl.getGroup(op.param1)
                #cl.sendText(op.param1, "🙏สวัสดี🙏" + cl.getContact(op.param2).displayName + " 👏ยินต้อนรับสมาชิกใหม่ " + "👉" + str(ginfo.name) + "👈" + " 💌ชื่ออะไรเอ่ย?💌 " + " 😘แนะนำตัวหน่อยจ้า😘 ")
                #cl.sendText(op.param1, "Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
                #print "MEMBER HAS JOIN THE GROUP"
                
      #  if op.type == 17:
           # if wait["WC"] == True:
              #  if op.param2 in Bots:
                  #  return
               # G = cl.getGroup(op.param1)
                #h = cl.getContact(op.param2)
                #cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
                #print "MEMBER HAS JOIN THE GROUP"
                
        if op.type == 17:
            if wait["Welcome1"] == True:
                ginfo = ki.getGroup(op.param1)
                ki.sendText(op.param1,"Selamat Bergabung di  " + str(ginfo.name)+"\n"+str(wait["welkam1"]))
                
        if op.type == 17:
            if wait["Welcome2"] == True:
                ginfo = ki2.getGroup(op.param1)
                ki2.sendText(op.param1,"Selamat Bergabung di  " + str(ginfo.name)+"\n"+str(wait["welkam2"]))
       
        if op.type == 17:
            if wait["Welcome"] == True:
                if op.param2 in Bots:
                    return
                cl.getGroup(op.param1)
                contact = cl.getContact(op.param2)
                #path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                if (wait["welkam"] in [""," ","\n",None]):
                    pass
                else:
                    #cl.sendImageWithURL(op.param1)
                    cl.sendText(op.param1,str(wait["welkam"]))
                    #cl.sendText(op.param1,"ข้อความอัตโนมัติ" + str(ginfo.name)+"\n"+str(wait["welkam"]))
                    
        if op.type == 17:
            if wait["Welcome"] == True:
                if op.param2 in Bots:
                    return
                G = cl.getGroup(op.param1)
                h = cl.getContact(op.param2)
                cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
                print "MEMBER HAS JOIN THE GROUP"
                    
        if op.type == 15:
            if wait["Leave"] == True:
                if op.param2 in Bots:
                    return
                cl.getGroup(op.param1)
                contact = cl.getContact(op.param2)
                #path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                if (wait["bye"] in [""," ","\n",None]):
                    pass
                else:
                    #cl.sendImageWithURL(op.param1, path)
                    cl.sendText(op.param1,str(wait["bye"]))
                    #cl.sendText(op.param1,"ข้อความอัตโนมัติ" + str(ginfo.name)+"\n"+str(wait["bye"]))
                    
                    
        if op.type == 15:
            if wait["Leave"] == True:
                if op.param2 in Bots:
                    return
                G = cl.getGroup(op.param1)
                h = cl.getContact(op.param2)
                cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
                print "MEMBER HAS JOIN THE GROUP"
                    
                    
      
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "[ChatBOT] " + data['result']['response'].encode('utf-8'))


            #if 'MENTION' in msg.contentMetadata.keys() != None:
                 #if wait["detectMention"] == True:
                     #contact = cl.getContact(msg.from_)
                     #cName = contact.displayName
                     #balas = ["เรียกมีไรค้า \n 🌈🤘สต.มานะ🤘🌈 \n 💌🌈⏳...เดะมาตอบน๊าาาา⏳🌈💌  \n 💕💕💕💕💕💕💕💕💕💝💕💕💕 "]       
                     #ret_ = "[Auto Respond] " + random.choice(balas)
                     #name = re.findall(r'@(\w+)', msg.text)
                     #mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     #mentionees = mention['MENTIONEES']
                     #for mention in mentionees:
                           #if mention['M'] in Bots:
                                  #cl.sendText(msg.to,ret_ + cName)
                                  #break
                            
        #if op.type == 26:
            #msg = op.message
            #if 'MENTION' in msg.contentMetadata.keys() != None:
                 #if wait["Mention"] == True:
                     #contact = cl.getContact(msg.from_)
                     #cName = contact.displayName
                     #ret_ = "Ada apa  " + cName + "  ?\n" + str(wait["tag"])
                     #name = re.findall(r'@(\w+)', msg.text)
                     #mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     #mentionees = mention['MENTIONEES']
                     #for mention in mentionees:
                           #if mention['M'] in mid:
                                   #xname = cl.getContact(msg.from_).displayName
                                   #xlen = str(len(xname)+1)
                                   #msg.contentType = 0
                                   #balas = "@"+xname+ " Jangan Tag Ahhh Jika Kangen PC Sono...\n\n","@"+xname+ " Fan Gue Buangeeeet...\n\n"
                                   #msg.text = random.choice(balas)
                                   #msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(msg.from_)+'}]}','EMTVER':'4'}
                                   #cl.sendMessage(msg)
                                   #msg.contentType = 7   
                                   #msg.text = None
                                   #msg.contentMetadata = tikel
                                           #"STKID": "527",
                                           #"STKPKGID": "2",
                                           #"STKVER": "100" }
                                   #cl.sendMessage(msg)
                                  
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     #balas = + str(wait["tag"])       
                     ret_ = "[Auto Respond] " "\n" + str(wait["tag"])
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_ + cName)
                                  break
                                
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['potoMention'] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.pictureStatus
                     balas = ["http://dl.profile.line-cdn.net/" + cName]
                     ret_ = random.choice(balas)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in Bots:
                                  cl.sendImageWithURL(msg.to,ret_)
                                  break 
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","-_-","Alin lagi off", cName + " Kenapa Tag saya?","SPAM PC aja " + cName, "Jangan Suka Tag gua " + cName, "Kamu siapa " + cName + "?", "Ada Perlu apa " + cName + "?","Tenggelamkan tuh yang suka tag pake BOT","Tersummon -_-"]
                     ret_ = "[Auto Respond] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break
                              
                              
                              
#------------------------------Kicker-----------------------------------------

  
#-------------------------------------------------------------------------------
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[ @ ]    Target Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                balas = ["โสด","ไม่โสด"]
                                ret_ = random.choice(balas)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to,"[ ชื่อ ] :\n" + contact.displayName + "\n\n[ Mid ] :\n" + msg.contentMetadata["mid"] + "\n\n[ ข้อความสถานะ ] :\n" + contact.statusMessage + "\n\n[ สถานะ ] :\n" + res_)
                                cl.sendText(msg.to,"[ รูปโปรไฟล์ ]" + contact.displayName)
                                cl.sendImageWithURL(msg.to,image)
                                cl.sendText(msg.to,"[ ปก ]" + contact.displayName)
                                cl.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass
                                

        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u5d777f646c37180c939be97aa5097096":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
                            
                            
            if msg.text.lower() in ["1123"]: 
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                cnt = Message()
                cnt.text = "PHET TAG DONE : " + str(jml) +  " Members"
                cnt.to = msg.to
                cl.sendMessage(cnt)

            elif msg.text in [".อยู่ไหม"]:
                        cl.sendText(msg.to,"❤อยู่ในใจเธอเสมอ❤")
                            
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
# ----------------- NOTIFED MEMBER OUT GROUP
#        if op.type == 15:
#            if op.param2 in bot1:
#                return
#            cl.sendText(op.param1,"ไปซะละ ลาก่อย\n(*´･ω･*)\nSelfbot by\n┅═ह वतेु১तेั७ழণ১ह═┅")
#            print "MEMBER HAS LEFT THE GROUP"
#------------------ KICK OUT FORM GROUP
#        if op.type == 19:
#            if op.param2 in Bots:
#                return
#            cl.sendText(op.param1,cl.getContact(op.param2).displayName + " ซัดเต็มข้อเลยครับ ท่านผู้ชม")
#            print "MEMBER KICK OUT FORM GROUP"
# ----------------- NOTIFED MEMBER JOIN GROUP
#        if op.type == 17:
#            if op.param2 in bot1:
#                return
#            ginfo = cl.getGroup(op.param1)
#            cl.sendText(op.param1, "ยินดีต้อนรับ 😊" + cl.getContact(op.param2).displayName + " สู่กลุ่ม " + "👉" + str(ginfo.name) + "👈")
#            print "MEMBER HAS JOIN THE GROUP"
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["ricoinvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ki.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     ki.findAndAddContactsByMid(target)
                                     ki.inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"Invited this nigga💋: \n➡" + _name)
                                     wait2["ricoinvite"] = False
                                     break                              
                                 except:             
                                          cl.sendText(msg.to,"Negative, Err0r Detected")
                                          wait2["ricoinvite"] = False
                                          break
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower()  == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
            elif msg.text.lower()  == 'คำสั่ง':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Thaihelp)
                else:
                    cl.sendText(msg.to,Thaihelp)
 
            elif "As5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
            elif "As6" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k1mid}
                k1.sendMessage(msg)
            elif "As7" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k2mid}
                k2.sendMessage(msg)
            elif "As8" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k3mid}
                k3.sendMessage(msg)
            elif "As9" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k4mid}
                k4.sendMessage(msg)
            elif "As10" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k5mid}
                k5.sendMessage(msg)
            elif msg.text in ["Bot1 Gift","1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","แจก"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Bot2 Gift","2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)

            elif msg.text in ["Bot3 Gift","3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["Bot4 Gift","4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki4.sendMessage(msg)

            elif msg.text in ["Cancel","cancel","ยก","ยกเชิญ"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"ไม่มีคำเชิญ👈")
                        else:
                            cl.sendText(msg.to,"ไม่มีสมาชิกค้างเชิญ👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เรียบร้อย👈")
                    else:
                        cl.sendText(msg.to,"ไม่มีคำเชิญแล้ว")
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif msg.text in ["Mybot","เด้กๆ"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg) 
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': k1mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k2mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k3mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k5mid}
                cl.sendMessage(msg)
                msg.contentType = 13
  
                
            elif "Timeline: " in msg.text:
                tl_text = msg.text.replace("Timeline: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Allname: " in msg.text:
                string = msg.text.replace("Allname: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k1.getProfile()
                    profile.displayName = string
                    k1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k2.getProfile()
                    profile.displayName = string
                    k2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k3.getProfile()
                    profile.displayName = string
                    k3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k4.getProfile()
                    profile.displayName = string
                    k4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k5.getProfile()
                    profile.displayName = string
                    k5.updateProfile(profile)
            elif "Allbio: " in msg.text:
                string = msg.text.replace("Allbio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k1.getProfile()
                    profile.statusMessage = string
                    k1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k2.getProfile()
                    profile.statusMessage = string
                    k2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k3.getProfile()
                    profile.statusMessage = string
                    k3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k4.getProfile()
                    profile.statusMessage = string
                    k4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k5.getProfile()
                    profile.statusMessage = string
                    k5.updateProfile(profile)
#--------------------------------
            elif msg.text in ["Flistmid"]:
                if msg.from_ in admin:
                    gruplist = cl.getAllContactIds()
                    kontak = cl.getContacts(gruplist)
                    num=1
                    msgs="═════════ʆίςϯ ƒɾίεηδʍίδ═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n═════════ʆίςϯ ƒɾίεηδʍίδ═════════\n\nTotal Friend : %i" % len(kontak)
                    cl.sendText(msg.to, msgs)
                    
            elif msg.text in ["Flist","เช็คเพื่อน"]:
                if msg.from_ in admin:
                    contactlist = cl.getAllContactIds()
                    kontak = cl.getContacts(contactlist)
                    num=1
                    msgs="═══════เพื่อนทั้งหมด══════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════เพื่อนทั้งหมด════════\n\nจำนวนเพื่อนทั้งหมด : %i" % len(kontak)
                    cl.sendText(msg.to, msgs)
                    
            elif msg.text in ["Memlist"]:
                if msg.from_ in admin:
                    kontak = cl.getGroup(msg.to)
                    group = kontak.members
                    num=1
                    msgs="═════════List Member═════════-"
                    for ids in group:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                    cl.sendText(msg.to, msgs)
                    
#----------------------------
            elif "Image " in msg.text:
                if msg.from_ in admin:
                    search = msg.text.replace("Image ","")
                    url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    print path
                    try:
                        cl.sendImageWithURL(msg.to,path)
                    except:
                        pass

#-------------ขโมย---------------

            elif "/ตั้งเวลา" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Lurking already on\nเปิดการอ่านอัตโนมัตกรุณาพิมพ์ ➠ /อ่าน")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "โปรเเกรมเปิดการอ่านอัตโนมัต\nSet reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "/ปิดการอ่าน" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Lurking already off\nปิดการอ่านอัตโนมัต")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "ปิดการอ่านอัตโนมัต\nDelete reading point:\n" + datetime.now().strftime('%H:%M:%S'))

                    
            elif "/อ่าน" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "SELFBOT PHET HACK BOT\n\nLurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "กรุณาตั้งเวลาการอ่านใหม่อีกครั้งโปรดพิมพ์ ➠ /ตั้งเวลา")
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:
            		cl.sendText(msg.to, "[อัตโนมัติ]: " + text)
                
            elif msg.text in ["เปิดเตะแทค"]:
                wait["kickMention"] = True
                cl.sendText(msg.to,"🇹🇭เปิดแล้ว🇹🇭")
                
            elif msg.text in ["ปิดเตะแทค"]:
                wait["kickMention"] = False
                cl.sendText(msg.to,"🇹🇭ปิดแตะแทคเสดแล้ว🇹🇭")
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")


            elif msg.text in ["Mypict"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                    h = cl.getContact(mid)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
            elif "Getmid @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Getmid @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            cl.sendText(msg.to, g.mid)
                        else:
                            pass
            elif "Getinfo" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    cu = cl.channel.getCover(key1)
                    try:
                        cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                    except:
                        cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
            elif "Getbio" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    cu = cl.channel.getCover(key1)
                    try:
                        cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                    except:
                        cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif "Getname" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    cu = cl.channel.getCover(key1)
                    try:
                        cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                    except:
                        cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif "Getprofile" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    cu = cl.channel.getCover(key1)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                        cl.sendImageWithURL(msg.to,image)
                        cl.sendText(msg.to,"Cover " + contact.displayName)
                        cl.sendImageWithURL(msg.to,path)
                    except:
                        pass
            elif "Getcontact" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]                
                    mmid = cl.getContact(key1)
                    msg.contentType = 13
                    msg.contentMetadata = {"mid": key1}
                    cl.sendMessage(msg)
            elif "Getpict @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Getpict @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendImageWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
            elif "Getvid @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Getvid @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendVideoWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
            elif "Getcover @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]cover executing"
                    _name = msg.text.replace("Getcover @","")    
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)          
                                path = str(cu)
                                cl.sendImageWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]cover executed"
            elif "Picturl @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Picturl @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
            elif "Coverurl @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]cover executing"
                    _name = msg.text.replace("Coverurl @","")    
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)          
                                path = str(cu)
                                cl.sendText(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]cover executed"
            elif "Getgrup image" in msg.text:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    cl.sendImageWithURL(msg.to,path)
            elif "Urlgrup image" in msg.text:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    cl.sendText(msg.to,path)
            elif msg.text.lower() == 'ออน':
                if msg.from_ in admin:
                    eltime = time.time() - mulai
                    van = "ใช้บอทมาเป็นเวลา "+waktu(eltime)
                    cl.sendText(msg.to,van)
            elif msg.text in ["Blocklist","เช็คบ๊อค"]:
                if msg.from_ in admin:
                    blockedlist = cl.getBlockedContactIds()
                    kontak = cl.getContacts(blockedlist)
                    num=1
                    msgs="═════════List Blocked═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                    cl.sendText(msg.to, msgs)
                    
            elif "say " in msg.text.lower():
                if msg.from_ in admin:
                    say = msg.text.lower().replace("say ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")

            elif "Wm set: " in msg.text:
                wait["welkam"] = msg.text.replace("Wm set: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Welcome message changed\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Wm cek","เช็คข้อความคนเข้า"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Welcome message saat ini:\n\n" + wait["welkam"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"Welcome message saat ini:\n\n" + wait["welkam"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))           

            elif "Wm1 set: " in msg.text:
                wait["welkam1"] = msg.text.replace("Wm1 set: ","")
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"Welcome message changed\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    ki.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Wm1 cek","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"Welcome message change to\n\n" + wait["welkam1"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    ki.sendText(msg.to,"Welcome message saat ini:\n\n" + wait["welkam1"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    
            elif "Wm2 set: " in msg.text:
                wait["welkam2"] = msg.text.replace("Wm2 set: ","")
                if wait["lang"] == "JP":
                    ki2.sendText(msg.to,"Welcome message changed\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    ki2.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Wm2 cek","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    ki2.sendText(msg.to,"Welcome message change to\n\n" + wait["welkam2"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    ki2.sendText(msg.to,"Welcome message saat ini:\n\n" + wait["welkam2"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                          
            elif "Lm set: " in msg.text:
                wait["bye"] = msg.text.replace("Lm set: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Leave message changed\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Lm cek","เช็คเข้าความคนออก"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Leave message saat ini:\n\n" + wait["bye"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"Leave message saat ini:\n\n" + wait["bye"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))   
            
            elif "Respon set: " in msg.text:
                wait["tag"] = msg.text.replace("Respon set: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Auto respon changed\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"doneã€‚")  
            elif msg.text in ["Respon cek","เช็คข้อความแทค"]:
                if wait["tag"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["tag"])
                else:
                    cl.sendText(msg.to,"Auto respon saat ini:\n\n" + wait["tag"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    
            elif msg.text in ["Wm on","เปิดข้อความคนเข้า"]:
              if msg.from_ in admin:
                if wait["Welcome"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👑เปิดข้อความคนเข้าร้อยแล้ว👑")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Welcome"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👑เปิดข้อความคนเข้าร้อยแล้ว👑")
                    else:
                        cl.sendText(msg.to,"done")
                        
            elif msg.text in ["Wm off","ปิดข้อความคนเข้า"]:
              if msg.from_ in admin:
                if wait["Welcome"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👑ปิดข้อความคนเข้าร้อยแล้ว👑")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Welcome"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👑ปิดข้อความคนเข้าร้อยแล้ว👑")
                    else:
                        cl.sendText(msg.to,"done")
                        
            elif msg.text in ["Respon on","เปิดแทค"]:
              if msg.from_ in admin:
                if wait["Mention"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto respon On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Mention"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto respon On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
                        
            elif msg.text in ["Respon off","ปิดแทค"]:
              if msg.from_ in admin:
                if wait["Mention"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto respon Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Mention"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to," Auto respon Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
                        
            elif msg.text in ["Lm on","เปิดข้อความคนออก"]:
              if msg.from_ in admin:
                if wait["Leave"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👑เปิดข้อความคนออกร้อยแล้ว👑")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Leave"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👑เปิดข้อความคนออกร้อยแล้ว👑")
                    else:
                        cl.sendText(msg.to,"done")
                        
            elif msg.text in ["Lm off","ปิดข้อความคนออก"]:
              if msg.from_ in admin:
                if wait["Leave"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👑ปิดข้อความคนออกร้อยแล้ว👑")
                    else:
                        cl.sendText(msg.to,"done")
                        
#--------------
            elif "Gbc " in msg.text:
                if msg.from_ in admin:
                    bc = msg.text.replace("Gbc ","")
                    gid = cl.getGroupIdsJoined()
                    for i in gid:
                        cl.sendText(i, bc)
                        
            elif "Cbc " in msg.text:
                if msg.from_ in admin:
                    bc = msg.text.replace("Cbc ","")
                    gid = cl.getAllContactIds()
                    for i in gid:
                        cl.sendText(i, bc)
                        
            elif "/T: " in msg.text:
                if msg.from_ in admin:
                    txt = msg.text.replace("Testext: ", "")
                    cl.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"
                                            
                        
            elif msg.text in ["ตั้งค่า","1150","Help 3"]:
                cl.sendText(msg.to,selfMessage)
      
            elif "Bc:" in msg.text:
                bctxt = msg.text.replace("Bc:", "")
                a = cl.getGroupIdsJoined()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
                    
            elif 'ยูทูป ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ยูทูป ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
                    
            elif 'Youtube > ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube > ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")

            elif 'ขอเพลง ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ขอเพลง ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"ไม่พบสื่งที่คุณต้องการค้นหา (｀・ω・´)")
            elif 'Song ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ขอเพลง ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"ไม่พบสื่งที่คุณต้องการค้นหา (｀・ω・´)")
#---------------------------
            elif "Tx: " in msg.text:
                txt = msg.text.replace("Tx: ", "")
                cl.kedapkedip(msg.to,txt)
                print "[ @ ]	Kedapkedip"
            
            elif "Music " in msg.text:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))

            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-ar" in msg.text:
                isi = msg.text.replace("Tr-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-jp" in msg.text:
                isi = msg.text.replace("Tr-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-th" in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            
            elif "Id-en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id-en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'CHROMEOS\t7.18.0\tChrome_OS\t1'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"╔═══════\n║    From ID    \n╚═══════\n" + "" + kata + "╔═══════\n║    To EN    \n╚═══════\n" + "" + result + "\n·÷±‡±±‡±÷··÷±‡±±‡±÷·")
            elif "Th-id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th-id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'CHROMEOS\t7.18.0\tChrome_OS\t1'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"╔═══════\n║    From En    \n╚═══════\n" + "" + kata + "╔═══════\n║    To ID    \n╚═══════\n" + "" + result + "\n·÷±‡±±‡±÷··÷±‡±±‡±÷·")
            elif "Id-th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id-th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'CHROMEOS\t7.18.0\tChrome_OS\t1'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"╔═══════\n║    From ID    \n╚═══════\n" + "" + kata + "╔═══════\n║    To JP    \n╚═══════\n" + "" + result + "\n·÷±‡±±‡±÷··÷±‡±±‡±÷·")
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-th " in msg.text:
                say = msg.text.replace("Say-th ","")
                lang = 'th'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ar " in msg.text:
                say = msg.text.replace("Say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
            elif "siri:" in msg.text.lower():
                    query = msg.text.lower().replace("siri:","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'CHROMEOS\t7.18.0\tChrome_OS\t1'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            elif "siri-en " in msg.text.lower():
                    query = msg.text.lower().replace("siri-en ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'CHROMEOS\t7.18.0\tChrome_OS\t1'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'en', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            elif "Talk " in msg.text.lower():
                    query = msg.text.lower().replace("Talk ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'CHROMEOS\t7.18.0\tChrome_OS\t1'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            elif "Steal bio" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,contact.statusMessage)
                except:
                    cl.sendText(msg.to,contact.statusMessage)    
	
            elif "Steal cover @" in msg.text:
              if msg.from_ in admin:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal cover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
            elif "Midpict:" in msg.text:
              if msg.from_ in admin:
                umid = msg.text.replace("Midpict:","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithURL(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass
			
            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		
            elif "Steal pict " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Steal pict ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = cl.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")
	
         
            elif "Steal mid" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
            elif "Steal contact" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
            elif "Mc:" in msg.text:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)

#---------------------------------------------------------
            elif "1pro: " in msg.text:
                string = msg.text.replace("1pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "2pro: " in msg.text:
                string = msg.text.replace("2pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "3pro: " in msg.text:
                string = msg.text.replace("3pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "4pro: " in msg.text:
                string = msg.text.replace("4pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "5pro: " in msg.text:
                string = msg.text.replace("5pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "6pro: " in msg.text:
                string = msg.text.replace("10pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k1.getProfile()
                    profile.displayName = string
                    k1.updateProfile(profile)
                    k1.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "7pro: " in msg.text:
                string = msg.text.replace("11pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k2.getProfile()
                    profile.displayName = string
                    k2.updateProfile(profile)
                    k2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "8pro: " in msg.text:
                string = msg.text.replace("12pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k3.getProfile()
                    profile.displayName = string
                    k3.updateProfile(profile)
                    k3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "9pro: " in msg.text:
                string = msg.text.replace("13pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k4.getProfile()
                    profile.displayName = string
                    k4.updateProfile(profile)
                    k4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "10pro: " in msg.text:
                string = msg.text.replace("14pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k5.getProfile()
                    profile.displayName = string
                    k5.updateProfile(profile)
                    k5.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "Mid: " in msg.text:
                mmid = msg.text.replace("Mid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Contact on","เปิดคท."]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"ระบบอ่านคท.เปิดอยู่แล้ว")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอ่านคท. 👈")
                    else:
                        cl.sendText(msg.to,"เปิดระบบอ่านคท.􀜁􀇔􏿿")
            elif msg.text in ["Contact off","ปิดคท."]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดอยู่แล้ว 👈")
                    else:
                        cl.sendText(msg.to,"ระบบอ่านคท.ปิดอยู่แล้ว 👈")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดอ่านคท.")
                    else:
                        cl.sendText(msg.to,"ปิดระบบอ่านคท. 👈")
            elif msg.text in ["protect on","เปิดกัน"]:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอยู่แล้ว 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"บอทป้องกันเปิดอยู่แล้ว 👈")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดบอทป้องกัน􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"เปิดบอทป้องกันเรียบร้อย ")
            elif msg.text in ["qrprotect on","เปิดกันลิ้ง"]:
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอยู่แล้ว 􀜁􀇔👈")
                    else:
                        cl.sendText(msg.to,"ระบบป้องกันลิ้งเปิดอยู่ 👈")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดป้องกันลิ้ง􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"เปิดระบบป้องกันลิ้ง ")
            elif msg.text in ["inviteprotect on","เปิดกันเชิญ"]:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอยู่แล้ว 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"ระบบป้องกันการเชิญเปิดอยู่ 👈")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดป้องกันเชิญ􀜁􀇔􏿿 👈")
                    else:
                        cl.sendText(msg.to,"เปิดระบบป้องกันการเชิญ")
            elif msg.text in ["cancelprotect on","เปิดกันยก"]:
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอยู่แล้ว 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"ระบบป้องกันการยกเลิกคำเชิญเปิดอยู่ 👈")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดกันยกเลิกเชิญ􀜁􀇔􏿿")
                    else:
                        