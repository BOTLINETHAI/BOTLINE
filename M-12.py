# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from io import StringIO
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,sys
import re,string,os
import os.path,sys,urllib,shutil,subprocess,pickle

cl = LINETCR.LINE()
cl.login(token="ใส่โทเค็น")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="ใส่โทเค็น")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="ใส่โทเค็น")
kk.loginResult()

ks = LINETCR.LINE()
ks.login(token="ใส่โทเค็น")
ks.loginResult()

kc = LINETCR.LINE()
kc.login(token="ใส่โทเค็น")
kc.loginResult()

ka = LINETCR.LINE()
ka.login(token="ใส่โทเค็น")
ka.loginResult()

km = LINETCR.LINE()
km.login(token="ใส่โทเค็น")
km.loginResult()

kn = LINETCR.LINE()
kn.login(token="ใส่โทเค็น")
kn.loginResult()

ko = LINETCR.LINE()
ko.login(token="ใส่โทเค็น")
ko.loginResult()

kp = LINETCR.LINE()
kp.login(token="ใส่โทเค็น")
kp.loginResult()

kq = LINETCR.LINE()
kq.login(token="ใส่โทเค็น")
kq.loginResult()

kr = LINETCR.LINE()
kr.login(token="ใส่โทเค็น")
kr.loginResult()

kj = LINETCR.LINE()
kj.login(token="ใส่โทเค็น")
kj.loginResult()

cl

with open('profileSave.pkl') as f:
    save1 = pickle.load(f)

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage =""" Mr. Bots…⛿
╔══╦═╦═╗
║║║║║║║║
║║║║╦║║║
╚╩╩╩╩╩╩╝ ᵀᴴᴬᴵᴸᴬᴺᴰ Creator
📧http://line.me/R/ti/p/%40uvh1233u
╔════════════════════
║  [C̶̲̅ᴏ̶̲̅ᴍ̶̲̅ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅ᴅ̶̲̅] ☛ Iɴ ᴛʜᴇ ɢʀᴏᴜᴘ
╠════════════════════
╠❂➣[ID]   Selfbot-MAN
╠❂➣[Ginfo]:  •ใอดี:กลุ่ม:ผุ้สร้าง
╠❂➣[Mid]  •MID ผู้ควบคุมบอท
╠❂➣[Me]  •Send contact Me
╠❂➣[Contact @] •Send contact @tag
╠❂➣[Man @tag]   •แท๊กรายชื่อสมาชิกกลุ่ม
╠❂➣[Message add: ] Set message ADD
╠❂➣[Add confirmasi]  I do notknow
╠❂➣[Comment set: ]Set message LIKE
╠❂➣[Comment check] •Cheak Text Like
╠❂➣[Link on]:  •Open Link group
╠❂➣[Link off]:  •Close Link group
╠❂➣[Link url]:  •Link GROUP.
╠❂➣[เชิญ: 'mid'] •เชิญด้วย (MID)ระบุ
╠❂➣[เตะ: 'mid'] •เตะๆ ด้วย (MID)ระบุ
╠❂➣[Say: ]  •บอทพูดตาม / Say: MAN
╠❂➣[Cancel : Cl]  •ยกเลิก ค้างเชิญ'
╠❂➣[Gn:"Text"   •เปลี่ยนชื่อกลุ่ม
╠❂➣[NK @tag]: เตะ @แท๊กระบุ
╠❂➣[Copy]  •Copy to "Chat" 
╠❂➣[Copy @]  •Copy to Group
╠❂➣[Save]. •บันทึกสำเนา
╠❂➣[Load]. •คืนค่าบัญชีหลัก
╠❂➣[Spam on (Number) (Text)
╠❂➣[Spam off (Number) (Text)
╠❂➣[Gcreator] •เช็คสถานะ ใอดี,ผู้สร้างกลุ่ม
╠❂➣[Covergroup]
╠❂➣[Man @tag] @แท๊กสมาชิก ทั้งกลุ่ม
╠❂➣[Ss],[ใครแอบ] Setpoint
╠❂➣[Vv].[เช็คอ่าน ]Setcheck
╠═════════════════════
║ [C̶̲̅ᴏ̶̲̅ᴍ̶̲̅ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅ᴅ̶̲̅] ☛ S E T T I N G ☚
╠═════════════════════
╠❂➣[Contact:      『on/off』
╠❂➣[Auto join:    『on/off』
╠❂➣[Cancel Invite: 1 on/off
╠❂➣[Auto share:   『on/off』
╠❂➣[Auto leave:   『on/off』
╠❂➣[Comment:      『on/off』
╠❂➣[Auto add:     『on/off』
╠❂➣[Auto like. :  『on/off』
╠════════════════════
║[C̶̲̅ᴏ̶̲̅ᴍ̶̲̅ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅ᴅ̶̲̅] ☛ κɪcκєʀ☠️Bot ᴸᶤᶰᵉ
╠════════════════════
╠❂➣[Mybot] •Send contact BOT
╠❂➣[Sendcontact]•ContactBOT&ME
╠❂➣[Name Bot: ]  •Name the bot
╠❂➣[All mid]  •MID Bot kicker
╠❂➣[Contact @] •Send contact
╠❂➣[Kicker}   • บอทเข้ากลุ่ม…… 
╠❂➣[Bye]   • บอทออก…………… 
╠❂➣[ผีเข้า]+[ผีออก]…………………
╠❂➣[คิกผี]…………………………………………
╠❂➣[ผียกเชิญ]………………………………………
╠❂➣[??¿ @] •บอทผี เข้าเตะ แล้วออก
╠❂➣[K1/K2..K gn: ] •Up name group
╠❂➣[K1/K2..K12 in]  •Bot Join group
╠❂➣[K1/K2..K12 fuck:]   •Bot  KICKER
╠❂➣[K1/K2..K5 gift]  •Bot send a gift
╠❂➣[Gift all,All gift]•bots send gift
╠❂➣[Test][Deag][Nk @][Kick @][Fuck @]
K1-K2-K3-K4-K5-K6-K7-K8-K9-K10-K11-K12
╠════════════════════
║ •✯͜͡✍️$ëlf☠️฿❂T☠️ℳѦれ☆۰۪۫
╠════════════════════
╠line.me/ti/p/~1ove..neverdie
╚════════════════════
Message Protect [Help2]
"""
helpMessage2 ="""Mr. Bots…⛿
 ╔══╦═╦═╗
 ║║║║║║║║
 ║║║║╦║║║
 ╚╩╩╩╩╩╩╝ ᵀᴴᴬᴵᴸᴬᴺᴰ Creator
📧http://line.me/R/ti/p/%40uvh1233u
╔═══════════════════════
╠❂➣[PROTECT: ON/OFF]ระบบป้องกัน
╠❂➣[BLOCK URL: ON/OFF]ล็อกลิงก์
╠❂➣[NAMELOCK: ON/OFF]ล็อกชื่อกลุ่ม
╠❂➣[BLOCKINVITE: ON/OFF]ล็อกเชิญ
╚═══════════════════════ 
""" 
KAC = [cl,ki,kk,ks,kc,ka,km,kn,ko,kp,kq,kr,kj]
KAB1 = ki.getProfile().mid
KAB2 = kk.getProfile().mid
KAB3 = ks.getProfile().mid
KAB4 = kc.getProfile().mid
KAB5 = ka.getProfile().mid
KAB6 = km.getProfile().mid
KAB7 = kn.getProfile().mid
KAB8 = ko.getProfile().mid
KAB9 = kp.getProfile().mid
KAB10 = kq.getProfile().mid
KAB11 = kr.getProfile().mid
KAB12 = kj.getProfile().mid
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
kimid = kk.getProfile().mid
ki2mid = ks.getProfile().mid
Cmid = kc.getProfile().mid
Emid = ka.getProfile().mid
Fmid = km.getProfile().mid
Gmid = kn.getProfile().mid
Hmid = ko.getProfile().mid
Imid = kp.getProfile().mid
Jmid = kq.getProfile().mid
Kmid = kr.getProfile().mid
Lmid = kj.getProfile().mid

Bots=[mid,Amid,kimid,ki2mid,Cmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Kmid,Lmid]
admin = ["ud24af63fd62d14c3bf8f719df80c3745"]
me = cl.getProfile().mid
bot1 = cl.getProfile().mid
main = cl.getProfile().mid
kicker1 = ki.getProfile().mid
kicker2 = kk.getProfile().mid
kicker3 = ks.getProfile().mid
kicker4 = kc.getProfile().mid
kicker5 = ka.getProfile().mid
kicker6 = km.getProfile().mid
kicker7 = kn.getProfile().mid
kicker8 = ko.getProfile().mid
kicker9 = kp.getProfile().mid
kicker10 = kq.getProfile().mid
kicker11 = kr.getProfile().mid
kicker12 = kj.getProfile().mid
bots = me + kicker1
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = [] 

admins = ["ud24af63fd62d14c3bf8f719df80c3745"]
Rx12 = ["ud55447120723d599b2bce2d67b14eb08"]
Rx11 = ["u69e29260fae1bae30db65dc8c24c0f16"]
Rx10 = ["ub2d390fda0c7ec03373009a97debe6f9"]
Rx9 = ["ua6153d8c9daa16d799a19716ed0e50f8"]
Rx8 = ["uaffb56a754f810d1ca7c49658503744b"]
Rx7 = ["u81e8c0945d7c86244b31e8f70e45d6e2"]
Rx6 = ["u1642bb26466ae4c647d723692030b418"]
Rx5 = ["u4be0d0fa6d209732889a5c86df184b0a"]
Rx4 = ["u2b8cc0e7eb9e1acdd76ac52cbd304de3"]
Rx3 = ["ub5511376daa821f14e7097bc2d7e90aa"]
Rx2 = ["ud186e0db54125e86130c8219a739e8a1"]
Rx1 = ["u84eaf58cd49bff840407abe3fc4db59c"]
Administrator = admins + Rx12 + Rx11 + Rx10 + Rx9 + Rx8 + Rx7 + Rx6 + Rx5 + Rx4 + Rx3 + Rx2 + Rx1
AS = Rx2 + Rx1 + Rx3 + Rx4 + Rx5 + Rx6 + Rx7 + Rx8 + Rx9 + Rx10 + Rx11 + Rx12
adminsA = admins + Rx3 + Rx5
Administrator = admins + Rx5 + Rx4 + Rx3 + Rx2 + Rx1

omikuzi = ["大吉","中吉","小吉","末吉","大凶","凄1�7"]

wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":False,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':""" \n
「Message AutoAdd」
Thank for add  Man..✍️

⛿เปิดสอนเขียนบอท Selfbot กันรัน
ยกเลิกเชิญออโต้ รันให้ตายก็ไม่เข้า
⛿และสอนเขียนบอทป้องกัน ชุด Bot-Protect

✰มีครบทุกฟังชั่น✰
☛ชุดบอทป้องกัน ☚
☛ จ่ายเพียงรอบเดียว ☚
☛ ไม่ต้องเสียรายเดือน ☚
✰เป็นวิชา รู้หลัก จะไปเปิดสอนต่อได้ด้วย✰

╔══════════•✰•══════════☆۰۪۫
║『ติดตั้งบอท Sirichan v10』 วันนี้..✍️
║มีโปรฯดีๆ 【ติดตั้งบอทพร้อมประกัน】
║〖2ชุด〗☞แถมให้ฟรีอีก 1 กลุ่มบอท☜
╠══════════•✰•══════════☆۰۪۫
║  💡คุณสมบัติพิเศษของบอท v10💡
╠☛🔒ป้องกันสมาชิกเปิดลิงก์ห้อง
╠☛🔒ป้องกันสมาชิกเปลี่ยนรูปกลุ่ม
╠☛🔒ป้องกันสมาชิกเปลี่ยนชื่อกลุ่ม
╠☛🔒ป้องกันสมาชิกเชิญคนนอกเข้ากลุ่ม
╠☛🔒ป้องกันคนนอกเข้ามาลบคนในกลุ่ม
╠☛🔒ห้ามลบสมาชิกในกลุ่ม นอกจากแอด
╠☛🔒ถ้าลบเกิน3คน บอทจะเตะออกทันที
╚📝สามารถเช็คคนที่อ่านในกลุ่มได้ด้วยตนเอง

✫☆✰สนใจทักมาสอบถามได้✰☆✫
http://line.me/ti/p/~1ove..neverdie
🆔 sirichan999 🆔 1ove..neverdie

📧ติดต่อเพิ่มเติม↲  📲 0639375811
http://line.me/ti/p/%40uvh1233u
""",
    "lang":"JP",
    "comment":"☛ Auto Like ☚ ᵀᴴᴬᴵᴸᴬᴺᴰ⛿️Protect-BOT\n📧http://line.me/R/ti/p/%40uvh1233u ", 
    "likeOn":True,
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{}, 
    "wblacklist":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},    
    "dblacklist":False
}

wait2 = {
	'readMember':{},
	'readPoint':{},
	'ROM':{},
	'setTime':{}
    }
	
setTime = {}
setTime = wait2["setTime"]

res = {
    'num':{},
    'us':{},
    'au':{},
}

save1 = {
    "Saved":False,
    "displayName":"",
    "statusMessage":"",
    "pictureStatus":""
}

def Cmd(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = [""]
    for texX in tex:
        for command in commands:
            if string ==texX + command:
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
         
def bot(op):
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
                    kk.cancelGroupInvitation(op.param1, matched_list)
                    ks.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 15:
            if op.param2 in bot1:
                return
            cl.sendText(op.param1,"Ɓy℮ Bye ☛" + cl.getContact(op.param2).displayName + "☚ 〆(・∀・＠)")
            print ("MEMBER HAS LEFT THE GROUP")

        if op.type == 19:
            if op.param2 in bot1:
                return
            cl.sendText(op.param1,cl.getContact(op.param2).displayName + " ☚ ซัดเต็มข้อเลยครับ ท่านผู้ชม")
            print "MEMBER KICK OUT FORM GROUP"

        if op.type == 17:
            if mid in op.param3:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist user flushing is complete")

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
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = ks.getGroup(op.param1)
                                except:
                                    try:
                                        G = ki.getGroup(op.param1)
				    except:
					try:
                                            G = kc.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    ks.updateGroup(G)
                                except:
                                    try:
                                        kc.updateGroup(G)
                                    except:
                                        try:
                                            ka.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            koutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ka.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ks.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Group name lock")
                                        ki.sendText(op.param1,"Haddeuh dikunci Pe'a")
                                        kk.sendText(op.param1,"Wekawekaweka 􀜁􀅔Har Har􏿿")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
		if op.type == 17:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2]) 
                                        kc.kickoutFromGroup(op.param1,[op.param2])
					ka.kickoutFromGroup(op.param1,[op.param2])
					km.kickoutFromGroup(op.param1,[op.param2])
					kn.kickoutFromGroup(op.param1,[op.param2])
                                        ko.kickoutFromGroup(op.param1,[op.param2])
					kp.kickoutFromGroup(op.param1,[op.param2])
					kq.kickoutFromGroup(op.param1,[op.param2])
					kr.kickoutFromGroup(op.param1,[op.param2])
                                        kj.kickoutFromGroup(op.param1,[op.param2])
                if op.type == 32:
			if mid in op.param3:
				wait["blacklist"][op.param2] == True
		if op.type == 32:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
                                        kc.kickoutFromGroup(op.param1,[op.param2])
					ka.kickoutFromGroup(op.param1,[op.param2])
					km.kickoutFromGroup(op.param1,[op.param2])
					kn.kickoutFromGroup(op.param1,[op.param2])
                                        ko.kickoutFromGroup(op.param1,[op.param2])
					kp.kickoutFromGroup(op.param1,[op.param2])
					kq.kickoutFromGroup(op.param1,[op.param2])
					kr.kickoutFromGroup(op.param1,[op.param2])
                                        kj.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 25:
			if mid in op.param3:
				wait["blacklist"][op.param2] == True
		if op.type == 25:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
                                        kc.kickoutFromGroup(op.param1,[op.param2])
					ka.kickoutFromGroup(op.param1,[op.param2])
					km.kickoutFromGroup(op.param1,[op.param2])
					kn.kickoutFromGroup(op.param1,[op.param2])
                                        ko.kickoutFromGroup(op.param1,[op.param2])
					kp.kickoutFromGroup(op.param1,[op.param2])
					kq.kickoutFromGroup(op.param1,[op.param2])
					kr.kickoutFromGroup(op.param1,[op.param2])
                                        kj.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.param3 == "4":
            if op.param1 in protecturl:
				group = cl.getGroup(op.param1)
				if group.preventJoinByTicket == False:
					group.preventJoinByTicket = True
					cl.updateGroup(group)
					cl.sendText(op.param1,"URL can not be changed")
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
                                        kc.kickoutFromGroup(op.param1,[op.param2])
					ka.kickoutFromGroup(op.param1,[op.param2])
					km.kickoutFromGroup(op.param1,[op.param2])
					kn.kickoutFromGroup(op.param1,[op.param2])
                                        ko.kickoutFromGroup(op.param1,[op.param2])
					kp.kickoutFromGroup(op.param1,[op.param2])
					kq.kickoutFromGroup(op.param1,[op.param2])
					kr.kickoutFromGroup(op.param1,[op.param2])
                                        kj.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
				else:
					pass                
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "ud24af63fd62d14c3bf8f719df80c3745":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ki.acceptGroupInvitationByTicket(list_[1],list_[2])
                            kk.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ks.acceptGroupInvitationByTicket(list_[1],list_[2])
                            kc.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ka.acceptGroupInvitationByTicket(list_[1],list_[2])
                            km.acceptGroupInvitationByTicket(list_[1],list_[2])
                            kn.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ko.acceptGroupInvitationByTicket(list_[1],list_[2])
                            kp.acceptGroupInvitationByTicket(list_[1],list_[2])
                            cq.acceptGroupInvitationByTicket(list_[1],list_[2])
                            kr.acceptGroupInvitationByTicket(list_[1],list_[2])
                            kj.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X = ki.getGroup(list_[1])
                            X = kk.getGroup(list_[1])
                            X = ks.getGroup(list_[1])
                            X = kc.getGroup(list_[1])
                            X = ka.getGroup(list_[1])
                            X = km.getGroup(list_[1])
                            X = kn.getGroup(list_[1])
                            X = ko.getGroup(list_[1])
                            X = kp.getGroup(list_[1])
                            X = kq.getGroup(list_[1])
                            X = kr.getGroup(list_[1])
                            X = kj.getGroup(list_[1])							
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                            ki.updateGroup(X)
                            kk.updateGroup(X)
                            ks.updateGroup(X)
                            kc.updateGroup(X)
                            ka.updateGroup(X)
                            km.updateGroup(X)
                            kn.updateGroup(X)
                            ko.updateGroup(X)
                            kp.updateGroup(X)
                            kq.updateGroup(X)
                            kr.updateGroup(X)
                            kj.updateGroup(X)
			except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1002)                    
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"It's included in a blacklist already〄1�7")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"I decided not to make a comment〄1�7")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"It was eliminated from a blacklist〄1�7")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It isn't included in a blacklist〄1�7")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"It's included in a blacklist already.〄1�7")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"It was added to the blacklist.〄1�7")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"It was eliminated from a blacklist〄1�7")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It isn't included in a blacklist〄1�7")
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
                        msg.text = "" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["help","Help","HELP"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Help2","Key","help2"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage2)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn:"in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn:","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("ki1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("ki1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("ki2 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("ki2 gn ","")
                    ki2.updateGroup(X)
                else:
                    ki2.sendText(msg.to,"It can't be used besides the group.")
            elif "เตะ:" in msg.text:
                midd = msg.text.replace("kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "เชิญ:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "ผีเชิญ:" in msg.text:
                midd = msg.text.replace("K1 invite:","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif "คิกผี" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif "K2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                kk.sendMessage(msg)
            elif "K3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ks.sendMessage(msg)    
            elif "K4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
            elif "K5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ka.sendMessage(msg)
            elif "K6" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                ka.sendMessage(msg)
            elif "K7" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                ka.sendMessage(msg)
            elif "K8" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                ka.sendMessage(msg)
            elif "K9" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                ka.sendMessage(msg)
            elif "K10" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}
                ka.sendMessage(msg)
            elif "K11" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Kmid}
                ka.sendMessage(msg)
            elif "K12" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Lmid}
                ka.sendMessage(msg)
            elif "Mybot" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Cmid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Emid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Fmid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Gmid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Hmid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Imid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Jmid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Kmid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Lmid}
                cl.sendMessage(msg)
            elif "Sendcontact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': KAB1}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': KAB2}
                kk.sendMessage(msg)
                msg.contentMetadata = {'mid': KAB3}
                ks.sendMessage(msg)
                msg.contentMetadata = {'mid': KAB4}
                kc.sendMessage(msg)
                msg.contentMetadata = {'mid': KAB5}
                ka.sendMessage(msg)
                msg.contentMetadata = {'mid': KAB6}
                km.sendMessage(msg)
                msg.contentMetadata = {'mid': KAB7}
                kn.sendMessage(msg)
                msg.contentMetadata = {'mid': KAB8}
                ko.sendMessage(msg)
                msg.contentMetadata = {'mid': KAB9}
                kp.sendMessage(msg)
                msg.contentMetadata = {'mid': KAB10}
                kq.sendMessage(msg)
                msg.contentMetadata = {'mid': KAB11}
                kr.sendMessage(msg)
                msg.contentMetadata = {'mid': KAB12}
                kj.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["愛のプレゼンツ1�7","K1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["愛のプレゼンツ1�7","K2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["愛のプレゼンツ1�7","K3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ks.sendMessage(msg)
            elif msg.text in ["愛のプレゼンツ1�7","K4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["愛のプレゼンツ1�7","K5 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ka.sendMessage(msg)
            elif msg.text in ["All gift","Gift all"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                ks.sendMessage(msg)
                kc.sendMessage(msg)
                ka.sendMessage(msg)
                km.sendMessage(msg)
                kn.sendMessage(msg)
                ko.sendMessage(msg)
                kp.sendMessage(msg)
                kq.sendMessage(msg)
                kr.sendMessage(msg)
                kj.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                ks.sendMessage(msg)
                kc.sendMessage(msg)
                ka.sendMessage(msg)
                km.sendMessage(msg)
                kn.sendMessage(msg)
                ko.sendMessage(msg)
                kp.sendMessage(msg)
                kq.sendMessage(msg)
                kr.sendMessage(msg)
                kj.sendMessage(msg)
            elif msg.text in ["Cl","Cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"There isn't an invited person〄1�7")
                        else:
                            cl.sendText(msg.to,"you Sato face-like person absence〄1�7")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group〄1�7")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")

            elif msg.text in ["ผียกเชิญ"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"There isn't an invited person〄1�7")
                        else:
                            ki.sendText(msg.to,"you Sato face-like person absence〄1�7")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group〄1�7")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
                        
            elif "Comment set:" in msg.text:
                c = msg.text.replace("Comment set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Error")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"It was changed。\n\n" + c)
            elif msg.text in ["Comment check"]:
                cl.sendText(msg.to,"An automatic comment is established as follows at present。\n\n" + str(wait["comment"]))
            elif msg.text in ["コメント:オン","Comment:on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done〄1�7")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already〄1�7")
            elif msg.text in ["コメント:オフ","Comment:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done〄1�7")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already〄1�7")          
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Block url:on"]:
                protecturl.append(msg.to)
                cl.sendText(msg.to,"ƊƠƝЄ")
            elif msg.text in ["Block url:off"]:
                if msg.from_ in Administrator:
                    protecturl.remove(msg.to)
                    cl.sendText(msg.to,"ƛԼԼƠƜЄƊ")
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ")
            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƲƦԼ ƠƝ ƛԼƦЄƛƊƳ〄1�7")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƲƦԼ。")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group。")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƲƦԼ ƇԼƠƧЄƊ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƲƦԼ。")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group。")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
            elif msg.text in ["Info","Ginfo"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "ปิดอยู่"
                        else:
                            u = "เปิดอยู่"
                        cl.sendText(msg.to,"[กลุ่ม]\n" + str(ginfo.name) + "\n\n[ไอดีกลุ่ม]\n" + msg.to + "\n\n[ผู้สร้างกลุ่ม]\n" + gCreator + "\n\n[รูปโปรไฟล์กลุ่ม]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nสมาชิก:" + str(len(ginfo.members)) + " ท่าน\nเชิญ:" + sinvitee + " ท่าน\nURL:" + u + "")
                    else:
                        cl.sendText(msg.to,"[名字]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[小组的作成者]\n" + gCreator + "\n[小组图标]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group。")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "Mid" == msg. text:
                cl.sendText(msg.to,mid)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,kimid)
                ks.sendText(msg.to,ki2mid)
                kc.sendText(msg.to,Cmid)
                ka.sendText(msg.to,Emid)
                km.sendText(msg.to,Fmid)
                kn.sendText(msg.to,Gmid)
                ko.sendText(msg.to,Hmid)
                kp.sendText(msg.to,Imid)
                kq.sendText(msg.to,Jmid)
                kr.sendText(msg.to,Kmid)
                kj.sendText(msg.to,Lmid)
            elif "ฮ่าๆ" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ks.sendMessage(msg)
            elif "โกรธ" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "105",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ks.sendMessage(msg)
            elif "ยินดีต้อนรับ" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ks.sendMessage(msg)
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Name:" in msg.text:
                string = msg.text.replace("Name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + " I did NI change。")
            elif "Namebot:" in msg.text:
                string = msg.text.replace("Namebot:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    kk.updateProfile(profile)
                    ks.updateProfile(profile)
                    kc.updateProfile(profile)
                    ka.updateProfile(profile)
                    km.updateProfile(profile)
                    kn.updateProfile(profile)
                    ko.updateProfile(profile)
                    kp.updateProfile(profile)
                    kq.updateProfile(profile)
                    kr.updateProfile(profile)
                    kj.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + " I did NI change。")
#---------------------------------------------------------
            elif "K1 upname:" in msg.text:
                string = msg.text.replace("K1 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"The name " + string + " I did NI change。")
#--------------------------------------------------------
            elif "K2 upname:" in msg.text:
                string = msg.text.replace("K2 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"The name " + string + " I did NI change。")
#--------------------------------------------------------
            elif "K3 upname:" in msg.text:
                string = msg.text.replace("K3 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                    ks.sendText(msg.to,"The name " + string + " I did NI change。")
#--------------------------------------------------------
            elif "K1 upstatus: " in msg.text:
                string = msg.text.replace("K1 upstatus: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile_B = ki.getProfile()
                    profile_B.statusMessage = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"display message " + string + " done")
            elif "K2 upstatus: " in msg.text:
                string = msg.text.replace("K2 upstatus: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile_C = kk.getProfile()
                    profile_C.statusMessage = string
                    kk.updateProfile(profile_C)
                    kk.sendText(msg.to,"display message " + string + " done")
            elif "K3 upstatus: " in msg.text:
                string = msg.text.replace("K3 upstatus: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile_C = ks.getProfile()
                    profile_C.statusMessage = string
                    ks.updateProfile(profile_C)
                    ks.sendText(msg.to,"display message " + string + " done")
            elif "Mic:" in msg.text:
                mmid = msg.text.replace("Mic:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Contact:on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƇƠƝƬƛƇƬ ƠƝ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ。")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƝ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ。")
            elif msg.text in ["Contact:off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƇƠƝƬƛƇƬ ƠƑƑ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ。")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƑƑ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƑƑ。")
            elif msg.text in ["Auto join:on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ʆƠƖƝ ƠƝ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ。")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƝ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ。")
            elif msg.text in ["Auto join:off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ʆƠƖƝ ƠƑƑ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ。")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƑƑ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƑƑ。")
            elif "Cancel invite:" in msg.text:
                try:
                    strnum = msg.text.replace("Cancel invite:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refusal was turned off。\non, please designate and send the number of people.")
                        else:
                            cl.sendText(msg.to,"number of people")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "A group below the person made sure that I'll refuse invitation automatically。")
                        else:
                            cl.sendText(msg.to,strnum + "Self- you for below shinin-like small.")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"The price is wrong。")
                    else:
                        cl.sendText(msg.to,"key is wrong。")
            elif msg.text in ["Auto leave:on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ԼЄƛƔЄ ƠƝ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ。")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƝ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ。")
            elif msg.text in ["Auto leave:off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ԼЄƛƔЄ ƠƑƑ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ。")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƑƑ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƑƑ。")
            elif msg.text in ["共有:オン","共有：オン","Auto share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["共有:オフ","共有：オフ","Auto share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Already。")                        
            elif "Set" == msg.text:
                md = ""
                if wait["contact"] == True: md+="✔ Contact → on \n"
                else: md+="❎ Contact → off \n"
                if wait["autoJoin"] == True: md+="✔  Auto join → on \n"
                else: md +="❎ Auto join → off \n"
                if wait["autoCancel"]["on"] == True:md+="✔ Cancel Invite → " + str(wait["autoCancel"]["members"]) + " \n"     
                else: md+= "❎ Cancel Invite → off \n"
                if wait["leaveRoom"] == True: md+="✔ Auto leave → on \n"
                else: md+="❎ Auto leave → off \n"
                if wait["timeline"] == True: md+="✔ Auto Share → on \n"
                else:md+="❎ Auto Share → off \n"
                if wait["commentOn"] == True: md+="✔ Comment → on \n"
                else:md+="❎ Comment → off \n"
                if wait["autoAdd"] == True: md+="✔ Auto add → on \n"
                else:md+="❎ Auto add → off \n"
                if wait["likeOn"] == True: md+="✔ Auto like → on \n"
                else:md+="❎ Auto like → off \n"
                cl.sendText(msg.to,"Selfbot-MAN ⛿ ᵀᴴᴬᴵᴸᴬᴺᴰ️ \n [C̶̲̅ᴏ̶̲̅ᴍ̶̲̅ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅ᴅ̶̲̅] ☛ S E T T I N G ☚\n "+md)
            elif msg.text in ["Group id","group id"]:
                gid = cl.getGroupIdsJoined()
                g = ""
                for i in gid:
                    g += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,g)
            elif msg.text in ["Rejectall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Completion。")
                else:
                    cl.sendText(msg.to,"key is wrong。")
            elif msg.text in ["Auto like:on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["いいね:オフ","Auto like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")

            elif msg.text in ["Auto add:on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It's on already。")
                    else:
                        cl.sendText(msg.to,"on already。")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It was turned on。")
                    else:
                        cl.sendText(msg.to,"Turned on。")
            elif msg.text in ["Auto add:off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It's off already。")
                    else:
                        cl.sendText(msg.to,"off already。")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It was turned off。")
                    else:
                        cl.sendText(msg.to,"Turned off。")
            elif "Massage add:" in msg.text:
                wait["message"] = msg.text.replace("Massage add:","")
                cl.sendText(msg.to,"The message was changed。")
            elif "Auto addition→" in msg.text:
                wait["message"] = msg.text.replace("Auto addition→","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"The message was changed。")
                else:
                    cl.sendText(msg.to,"was change already。")
            elif msg.text in ["Add confirmasi","自動追加問候語確認"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,".automatic message is established as follows。\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"One  of weeds on the surface below the self- additional breath image。\n\n" + wait["message"])
            elif msg.text in ["CHANGE","言語變更"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"ƇƠƲƝƬƦƳ ԼƛƝƓƲƛƓЄ ƊƲƦƖƝƓ ƛ ƇHƛƝƓЄ。")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,". The language was made English。")
            elif msg.text in ["Url"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƇƛƝ'Ƭ ƁЄ ƲƧЄƊ ƁЄƧƖƊЄƧ ƬHЄ ƓƦƠƲƤ.。")
                    else:
                        cl.sendText(msg.to,"ƖMƤƠƧƧƖƁԼЄ ƲƧЄ ƁЄƧƖƊЄƧ ƬHЄ ƓƦƠƲƤ. ")
            elif "gurl:" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl:","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"ƖƬ ƇƛƝ'Ƭ ƁЄ ƲƧЄƊ ƁЄƧƖƊЄƧ ƬHЄ ƓƦƠƲƤ。")
            elif msg.text in ["Link url"]:
                if msg.toType == 2:
                    x = ki.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƇƛƝ ƝƠƬ ƁЄ ƲƧЄƊ ƠƲƬƧƖƊЄ ƬHЄ ƓƦƠƲƤ")
                    else:
                        cl.sendText(msg.to,"ƝƠƬ ƑƠƦ ƲƧЄ ԼЄƧƧ ƬHƛƝ ƓƦƠƲƤ")
            elif msg.text in ["cb"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send the phone number of the person who adds it to the blacklist.")
            elif msg.text in ["cbd"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send the phone number of the person who adds it to the blacklist.")
            elif msg.text in ["cbc"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"There isn't a person made a blacklist。")
                else:
                    cl.sendText(msg.to,"Below is a blacklist。")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Clock:on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"It's on already。")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"It was turned on")
            elif msg.text in ["Clock:off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"It's off already.。")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"It was tuned off。")
            elif "Clock:" in msg.text:
                n = msg.text.replace("Clock:","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"Last name clock。")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"It was renewed\n\n" + n)
            elif msg.text in ["Up clock"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"It was renewed。")
                else:
                    cl.sendText(msg.to,"Please turn on a name clock.。")
            elif "Man @tag" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 
            elif "Kicker" in msg.text:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  ka.acceptGroupInvitationByTicket(msg.to,Ti)
                  km.acceptGroupInvitationByTicket(msg.to,Ti)
                  kn.acceptGroupInvitationByTicket(msg.to,Ti)
                  ko.acceptGroupInvitationByTicket(msg.to,Ti)
                  kp.acceptGroupInvitationByTicket(msg.to,Ti)
                  kq.acceptGroupInvitationByTicket(msg.to,Ti)
                  kr.acceptGroupInvitationByTicket(msg.to,Ti)
                  kj.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
            elif msg.text in ["ผีเข้า$]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)                  
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["K2 in"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)           
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
				  
            elif msg.text in ["K3 in"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)           
                  G = ks.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ks.updateGroup(G)
                  Ticket = ks.reissueGroupTicket(msg.to)                           

            elif msg.text in ["Bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
					ki.leaveGroup(msg.to)
					kk.leaveGroup(msg.to)
					ks.leaveGroup(msg.to)
					kc.leaveGroup(msg.to)
					ka.leaveGroup(msg.to)
                                        km.leaveGroup(msg.to)
					kn.leaveGroup(msg.to)
					ko.leaveGroup(msg.to)
					kp.leaveGroup(msg.to)
					kq.leaveGroup(msg.to)
                                        kr.leaveGroup(msg.to)
					kj.leaveGroup(msg.to)
                except:
                     pass            
            elif "??¿ " in msg.text:
                       nk0 = msg.text.replace("??¿ ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                                    gs.preventJoinByTicket = True
                                    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                                    cl.updateGroup(gs)
#-----------------------------------------------------------                          
            elif "Kick" in msg.text:
                if msg.contentMetadata is not None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                           cl.kickoutFromGroup(msg.to,[target])
                    else:
                        pass
            elif "K1 fuck" in msg.text:
				OWN = "u84eaf58cd49bff840407abe3fc4db59c"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("K1 fuck","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"ƲƧЄƦ ƊƠЄƧ ƝƠƬ ЄҲƖƧƬ")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									ki.kickoutFromGroup(msg.to, [target])							   
							except:
									ki.kickoutFromGroup(msg.to, [target])							   
									pass
            elif "K2 fuck" in msg.text:
				OWN = "ud186e0db54125e86130c8219a739e8a1"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("K2 fuck","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"ƲƧЄƦ ƊƠЄƧ ƝƠƬ ЄҲƖƧƬ")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									kk.kickoutFromGroup(msg.to, [target])							   
							except:
									kk.kickoutFromGroup(msg.to, [target])							   
									pass

            elif "K3 fuck" in msg.text:
				OWN = "ub5511376daa821f14e7097bc2d7e90aa"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("K3 fuck","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"ƲƧЄƦ ƊƠЄƧ ƝƠƬ ЄҲƖƧƬ")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									ks.kickoutFromGroup(msg.to, [target])							   
							except:
									ks.kickoutFromGroup(msg.to, [target])							   
									pass									
            elif "Ban " in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:                                        
                       ban0 = msg.text.replace("Ban ","")
                       ban1 = ban0.lstrip()
                       ban2 = ban1.replace("@","")
                       ban3 = ban2.rstrip()
                       _name = ban3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"ƲƧЄƦ ƊƠЄƧ ƝƠƬ ЄҲƖƧƬ")
                           pass
                       else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ ƧƲƇƇЄƧƧ")
                                except:
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ ƧƲƇƇЄƧƧ")
#-----------------------------------------------------------
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#-----------------------------------------------------------
            elif "Unban " in msg.text:
               if msg.toType == 2:
                  if msg.from_ in admin:                                        
                       unb0 = msg.text.replace("Unban ","")
                       unb1 = unb0.lstrip()
                       unb2 = unb1.replace("@","")
                       unb3 = unb2.rstrip()
                       x_name = unb3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if x_name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"ƲƧЄƦ ƊƠЄƧ ƝƠƬ ЄҲƖƧƬ")
                           pass
                       else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ ƧƲƇƇЄƧƧ")
                                except:
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ ƧƲƇƇЄƧƧ")
#-----------------------------------------------------------
            elif "Protect:on" == msg.text:
				if msg.to in protection:
					cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
				else:
					wait["pnharfbot"][msg.to] = cl.getGroup(msg.to).name
					f=codecs.open('pnharfbot.json','w','utf-8')
					json.dump(wait["pnharfbot"], f, sort_keys=True, indent=4,ensure_ascii=False)
					protection.append(msg.to)
					cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ")
            elif "Protect:off" == msg.text:
				try:
					if msg.from_ in Administrator:
						protection.remove(msg.to)
						cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƑƑ")
					else:
						cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
				except:
					pass
            elif "Namelock:on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.")
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝ ƠƑƑ.")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
					
            elif "Blockinvite:on" == msg.text:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƝ")
            elif "Blockinvite:off" == msg.text:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƑƑ")
				except:
					pass                                 
#-----------------------------------------------------------
            elif msg.text in ["Delete chat"]:
                cl.removeAllMessages(op.param2)
                ki.removeAllMessages(op.param2)
                kk.removeAllMessages(op.param2)
                ks.removeAllMessages(op.param2)
                kc.removeAllMessages(op.param2)
                ka.removeAllMessages(op.param2)
                cl.sendText(msg.to,"Delete Chat")
                cl.sendText(msg.to,"Success...")
#-----------------------------------------------------------
            elif "Spam @" in msg.text:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Spam Start")
                       ki.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       kk.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ks.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       kc.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ka.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       cl.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ki.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       kk.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ks.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       kc.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ka.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       cl.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ki.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       kk.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ks.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       kc.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ka.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       cl.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ki.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       kk.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ks.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       kc.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ka.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       cl.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ki.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       kk.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ks.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       kc.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ka.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       cl.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ki.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       kk.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ks.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       kc.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ka.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       ks.sendText(g.mid,"•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•")
                       cl.sendText(msg.to, "Ok success")
                       print "Done spam" 
#----------------------------------------------------------
            elif msg.text in ["Conban","ข้อมูลบัญชีดำ","Contact ban"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)
#----------------------------------------------------------
            elif msg.text in ["Test"]:
                ki.sendText(msg.to,"●")
                ki.sendText(msg.to,"●●")
                ki.sendText(msg.to,"●●●")
                ki.sendText(msg.to,"●●●●")
                ki.sendText(msg.to,"●●●●●")
                ki.sendText(msg.to,"●●●●●●")
                kk.sendText(msg.to,"●●●●●●●")
                kk.sendText(msg.to,"●●●●●●●●")
                kk.sendText(msg.to,"●●●●●●●●●")
                kk.sendText(msg.to,"●●●●●●●●●●")
                kk.sendText(msg.to,"●●●●●●●●●●●")
                kk.sendText(msg.to,"●●●●●●●●●●●●")
                ks.sendText(msg.to,"●●●●●●●●●●●●●")
                ks.sendText(msg.to,"●●●●●●●●●●●●●●")
                ks.sendText(msg.to,"●●●●●●●●●●●●●●●")
                ks.sendText(msg.to,"●●●●●●●●●●●●●●●●")
                ks.sendText(msg.to,"●●●●●●●●●●●●●●●●●")
                ks.sendText(msg.to,"●●●●●●●●●●●●●●●●●●")
                kc.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●")
                kc.sendText(msg.to,"●●●●●●●●●●●●●●●●●●")
                kc.sendText(msg.to,"●●●●●●●●●●●●●●●●●")
                kc.sendText(msg.to,"●●●●●●●●●●●●●●●●●")
                kc.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●●●●")
                kc.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●●●●●")
                ka.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●●●●●●")
                ka.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●●●●●●●")
                ka.sendText(msg.to,"●Bot Working●")
                cl.sendText(msg.to,"●( ^^)人(^^ )●")
#----------------------------------------------------------
            elif msg.text == "แอบ":
              if msg.from_ in admin:
                cl.sendText(msg.to, "sᴇᴛ ᴛʜᴇ ʟᴀsᴛsᴇᴇɴs' ᴘᴏɪɴᴛ(｀・ω・´)")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
	            pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,'%d-%m-%Y📅 ↔ ⏰%H:%M:%S') 
                wait2['ROM'][msg.to] = {}
                print wait2
            elif msg.text == "อ่าน":
              if msg.from_ in admin:
		  if msg.to in wait2['readPoint']:
	            if wait2["ROM"][msg.to].items() == []:
	              chiya = ""
	            else:
	              chiya = ""
	              for rom in wait2["ROM"][msg.to].items():
	                print rom
	                chiya += rom[1] + "\n"

	            cl.sendText(msg.to, " %s\n\n\nPeople who have ignored reads\n(｀・ω・´)\n%s\n\nThese anu anu uesrs have seen at the lastseen point(｀・ω・´)\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
	          else:
	            cl.sendText(msg.to, "Sider ga bisa di read cek setpoint dulu bego tinggal ketik\nSetlastpoint\nkalo mau liat sider ketik\nViewlastseen")
#-----------------------------------------------------------speed
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"ƤԼЄƛƧЄ ƧЄƝƊ ƬHЄ ƛƇƇƠƲƝƬ ƦЄƓƖƧƬЄƦЄƊ ƜƖƬH ƛ ƁԼƛƇƘԼƖƧƬ。")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"ƤԼЄƛƧЄ ƧЄƝƊ ƬHЄ ƛƇƇƠƲƝƬ ƦЄƓƖƧƬЄƦЄƊ ƜƖƬH ƛ ƁԼƛƇƘԼƖƧƬ。")
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"ƬHЄƦЄ ƖƧƝ'Ƭ ƛ ƤЄƦƧƠƝ MƛƊЄ ƛ ƁԼƛƇƘԼƖƧƬ.。")
                else:
                    cl.sendText(msg.to,"ƁЄԼƠƜ ƖƧ ƛ ƁԼƛƇƘԼƖƧƬ。")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Blist"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "・" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "But it's a blacklist.。")
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"There wasn't a blacklist user。")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,ks,kc,ka,km,kn,ko,kp,kq,kr,kj]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass							
            elif msg.text in ["Single"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I have feigned and have canceled it。")
            elif "random:" in msg.text:
                if msg.toType == 2:
                    strnum = msg.text.replace("random:","")
                    source_str = '•✯͜͡✍️$ëlf☠️฿❂T☠️ℳѦれ☆۰۪۫'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"ЄƦƦƠƦ")
            elif "Album making" in msg.text:
                try:
                    albumtags = msg.text.replace("Album making","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "An album was made。")
                except:
                    cl.sendText(msg.to,"ЄƦƦƠƦ")
            elif "FAK" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakec→","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass                
#-----------------------------------------------
            elif msg.text in ["Cb","Clearban"]:
                                wait["blacklist"] = {}
                                cl.sendText(msg.to,"clear")
#-----------------------------------------------
            elif "Contact @" in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("Contact @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                         pass
#-----------------------------------------------
            elif "Say " in msg.text:
                string = msg.text.replace("Say ","")
                if len(string.decode('utf-8')) <= 50:
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    ks.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    ka.sendText(msg.to," " + string + " ")
                    km.sendText(msg.to," " + string + " ")
                    kn.sendText(msg.to," " + string + " ")
                    ko.sendText(msg.to," " + string + " ")
                    kp.sendText(msg.to," " + string + " ")
                    kq.sendText(msg.to," " + string + " ")
                    kr.sendText(msg.to," " + string + " ")
                    kj.sendText(msg.to," " + string + " ")
#-----------------------------------------------
            elif msg.text in ["Group creator","Gc","Gcreator","gcreator"]:
                ginfo = cl.getGroup(msg.to)
                gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"""╔══════════════
║ผู้สร้างกลุ่ม Creator Group
╚══════════════""")
#-----------------------------------------------
            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kc.kickuotFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    kc.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                                    gs.preventJoinByTicket = True
                                    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                                    cl.updateGroup(gs)
#-----------------------------------------------
            elif "Covergroup" in msg.text:
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                cl.createGroup("•✯͜͡✍️$ëlf☠️฿❂T☠️ℳѦれ☆۰۪۫", mi_d)
                cl.sendText(msg.to,"Cover Group")
#-----------------------------------------------
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                text = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (text+"\n")
                if txt[1] == "on":
                    if jmlh <= 1000:
                        for x in range(jmlh):
                            cl.sendText(msg.to, text)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
                elif txt[1] == "off":
                    if jmlh <= 1000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
#-----------------------------------------------
            elif "Steal dp @" in msg.text:
                nama = msg.text.replace("Steal dp @","")
                target = nama.rstrip(' ')
                van = cl.getGroup(msg.to)
                for linedev in van.members:
                    if target == linedev.displayName:
                        midddd = cl.getContact(linedev.mid)
                        PATH = "http://dl.profile.line-cdn.net/" + midddd.pictureStatus
                    cl.sendImageWithURL(msg.to,PATH)
#-----------------------------------------------
            elif "Steal home @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:                                                                   ki.sendText(msg.to,"Contact not found")
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
#-----------------------------------------------
            elif "Mc " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
            elif "Mc: " in msg.text:
                mmid = msg.text.replace("Mc: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                ks.sendMessage(msg)
                kc.sendMessage(msg)
                ka.sendMessage(msg)
                km.sendMessage(msg)
                kn.sendMessage(msg)
                ko.sendMessage(msg)
                kp.sendMessage(msg)
                kq.sendMessage(msg)
                kr.sendMessage(msg)
                kj.sendMessage(msg)                        
#-----------------------------------------------
            elif "Speed" in msg.text:
                start = time.time()
                cl.sendText(msg.to, "ᴘʀᴏɢʀᴇss...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                kk.sendText(msg.to, "%sseconds" % (elapsed_time))
                ks.sendText(msg.to, "%sseconds" % (elapsed_time))
                kc.sendText(msg.to, "%sseconds" % (elapsed_time))
                ka.sendText(msg.to, "%sseconds" % (elapsed_time))
                km.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kn.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ko.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kp.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kq.sendText(msg.to, "%sseconds" % (elapsed_time))
                kr.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kj.sendText(msg.to, "%sseconds" % (elapsed_time))
#-----------------------------------------------
            elif "Sp" in msg.text:
                start = time.time()
                cl.sendText(msg.to, "ᴘʀᴏɢʀᴇss...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
#-----------------------------------------------             
            elif msg.text == "Save":
                me = cl.getProfile()
                save1["displayName"] = me.displayName
                save1["statusMessage"] = me.statusMessage
                save1["pictureStatus"] = me.pictureStatus
                save1["Saved"] = True
                cl.sendText(msg.to,"บันทึกสถานะบัญชีเรียบร้อยแล้ว")
            elif msg.text == "Load":
                if save1["Saved"]:
                    me = cl.getProfile()
                    me.displayName = save1["displayName"]
                    me.statusMessage = save1["statusMessage"]
                    me.pictureStatus = save1["pictureStatus"]
                    cl.updateDisplayPicture(me.pictureStatus)
                    cl.updateProfile(me)
                    cl.sendText(msg.to,"โหลดสถานะบัญชีเรียบร้อยแล้ว")
                else:
                    cl.sendText(msg.to,"ก่อนหน้านี้ยังไม่ได้มีการบันทึกสถานะบัญชี")
            elif msg.text == "Copy":
                if msg.toType == 0:
                    targ = cl.getContact(msg.to)
                    me = cl.getProfile()
                    me.displayName = targ.displayName
                    me.statusMessage = targ.statusMessage
                    me.pictureStatus = targ.pictureStatus
                    cl.updateDisplayPicture(me.pictureStatus)
                    cl.updateProfile(me)
                    cl.sendText(msg.to,"สำเร็จแล้ว")
                else:
                    cl.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในแชทส่วนตัวเท่านั้น")
            elif "Copy " in msg.text:
                if msg.toType == 2:
                    red = re.compile(re.escape('Copy '),re.IGNORECASE)
                    tname = red.sub('',msg.text)
                    tname = tname.lstrip()
                    tname = tname.replace(" @","$spliter$")
                    tname = tname.rstrip()
                    tname = tname.split("$spliter$")
                    tname = tname[0]
                    tname = tname[1:]
                    clist = {
                        "Founded":False,
                        "displayName":"",
                        "statusMessage":"",
                        "pictureStatus":""
                    }
                    mems = cl.getGroup(msg.to).members
                    for targ in mems:
                        if targ.displayName == tname:
                            clist["displayName"] = targ.displayName
                            clist["statusMessage"] = targ.statusMessage
                            clist["pictureStatus"] = targ.pictureStatus
                            clist["Founded"] = True
                    if clist["Founded"]:
                        me = cl.getProfile()
                        me.displayName = clist["displayName"]
                        me.statusMessage = clist["statusMessage"]
                        me.pictureStatus = clist["pictureStatus"]
                        cl.updateDisplayPicture(me.pictureStatus)
                        cl.updateProfile(me)
                        cl.sendText(msg.to,"สำเร็จแล้ว")
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)                        
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = False

                elif op.param3 in op.param3:
                    if op.param1 in protection:
                        OWN = "ud24af63fd62d14c3bf8f719df80c3745","u84eaf58cd49bff840407abe3fc4db59c","ud186e0db54125e86130c8219a739e8a1","ub5511376daa821f14e7097bc2d7e90aa","u2b8cc0e7eb9e1acdd76ac52cbd304de3","u4be0d0fa6d209732889a5c86df184b0a","u1642bb26466ae4c647d723692030b418","u81e8c0945d7c86244b31e8f70e45d6e2","uaffb56a754f810d1ca7c49658503744b","ua6153d8c9daa16d799a19716ed0e50f8","ub2d390fda0c7ec03373009a97debe6f9","u69e29260fae1bae30db65dc8c24c0f16","ud55447120723d599b2bce2d67b14eb08"
                    if op.param2 in OWN:
                        kicker1 = [cl,ki,kk,ks,kc,ka,km,kn,ko,kp,kq,kr,kj]
                        G = random.choice(kicker1).getGroup(op.param1)
                        G.preventJoinByTicket = False
                        random.choice(kicker1).updateGroup(G)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(kicker1).updateGroup(G)
                    else:
                        G = random.choice(kicker1).getGroup(op.param1)

                        random.choice(kicker1).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        random.choice(kicker1).updateGroup(G)
                        Ticket = random.choice(kicker1).reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(kicker1).updateGroup(G)

                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        
                elif op.param3 in Amid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass

        if op.type == 19:
            try:
                if op.param3 in Amid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)


                elif op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
                
        if op.type == 19:
            try:
                if op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ks.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                    else:
                        G = ks.getGroup(op.param1)

                        
                        ks.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)

                        
                elif op.param3 in Amid:
                    if op.param2 in kimid:
                        G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
                
        if op.type == 19:
            try:
                if op.param3 in ki2mid:
                    if op.param2 in kimid:
                        if op.param4 in Cmid:
                            if op.param5 in Emid:
                                G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        
                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)


                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ks.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                    else:
                        G = ks.getGroup(op.param1)

                        
                        ks.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
                
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in ki2mid:
                        G = ks.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                    else:
                        G = ks.getGroup(op.param1)

                        
                        ks.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)

                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
             
        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
                                        cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass
                    
        if op.type == 32:
                        OWN = "ud24af63fd62d14c3bf8f719df80c3745","u84eaf58cd49bff840407abe3fc4db59c","ud186e0db54125e86130c8219a739e8a1","ub5511376daa821f14e7097bc2d7e90aa","u2b8cc0e7eb9e1acdd76ac52cbd304de3","u4be0d0fa6d209732889a5c86df184b0a","u1642bb26466ae4c647d723692030b418","u81e8c0945d7c86244b31e8f70e45d6e2","uaffb56a754f810d1ca7c49658503744b","ua6153d8c9daa16d799a19716ed0e50f8","ub2d390fda0c7ec03373009a97debe6f9","u69e29260fae1bae30db65dc8c24c0f16","ud55447120723d599b2bce2d67b14eb08" 
			if op.param2 in OWN:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                ks.kickoutFromGroup(op.param1,[op.param2])
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                ka.kickoutFromGroup(op.param1,[op.param2])
                                km.kickoutFromGroup(op.param1,[op.param2])
                                kn.kickoutFromGroup(op.param1,[op.param2])
                                ko.kickoutFromGroup(op.param1,[op.param2])
                                kp.kickoutFromGroup(op.param1,[op.param2])
                                kq.kickoutFromGroup(op.param1,[op.param2])
                                kr.kickoutFromGroup(op.param1,[op.param2])
                                kj.kickoutFromGroup(op.param1,[op.param2])
			        wait["blacklist"][op.param2] = True
				f=codecs.open('st2__b.json','w','utf-8')
				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#------------------------------------------------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n☑" + Name
                        wait2['ROM'][op.param1][op.param2] = "☑" + Name
                else:
                    cl.sendText
            except:
                  pass
                  
#-----------------------------------------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
#----------------------------------------

#-------------------------------
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

try:
    while True:
        try:
            Ops = cl.fetchOps(cl.Poll.rev, 5)
        except EOFError:
            raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

        for Op in Ops:
            if (Op.type != OpType.END_OF_OPERATION):
                cl.Poll.rev = max(cl.Poll.rev, Op.revision)
                bot(Op)
except Exception as e:
    print e
    with open('profileSave.pkl', 'w') as f:
        pickle.dump([save1], f)

