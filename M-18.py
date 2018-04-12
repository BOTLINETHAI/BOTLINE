# -*- coding: utf-8 -*-

#=======STAP.1======#
#import LINETCR
#from LINETCR.lib.curve.ttypes import *
#from datetime import datetime
#import time,random,sys,json,codecs,threading,glob,requests,urllib
#=======STAP.2======#
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia,tempfile,glob,shutil,unicodedata,goslate
from gtts import gTTS 
#===================#
cl = LINETCR.LINE()
cl.login(token="MAN")
cl.loginResult()
#===================#
ki = LINETCR.LINE()
ki.login(token="MAN")
ki.loginResult()
#===================#
kk = LINETCR.LINE()
kk.login(token="MAN")
kk.loginResult()
#===================#
kc = LINETCR.LINE()
kc.login(token="MAN")
kc.loginResult()
#===================#
kd = LINETCR.LINE()
kd.login(token="MAN")
kd.loginResult()
#===================#
ke = LINETCR.LINE()
ke.login(token="MAN")
ke.loginResult()
#===================#
kf = LINETCR.LINE()
kf.login(token="MAN")
kf.loginResult()
#===================#
kg = LINETCR.LINE()
kg.login(token="MAN")
kg.loginResult()
#===================#
kh = LINETCR.LINE()
kh.login(token="MAN")
kh.loginResult()
#===================#
kj = LINETCR.LINE()
kj.login(token="MAN")
kj.loginResult()
#===================#
kl = LINETCR.LINE()
kl.login(token="MAN")
kl.loginResult()
#===================#
km = LINETCR.LINE()
km.login(token="MAN")
km.loginResult()
#===================#
kn = LINETCR.LINE()
kn.login(token="MAN")
kn.loginResult()
#===================#
ko = LINETCR.LINE()
ko.login(token="MAN")
ko.loginResult()
#===================#
kp = LINETCR.LINE()
kp.login(token="MAN")
kp.loginResult()
#===================#
kq = LINETCR.LINE()
kq.login(token="MAN")
kq.loginResult()
#===================#
kr = LINETCR.LINE()
kr.login(token="MAN")
kr.loginResult()
#===================#
ks = LINETCR.LINE()
ks.login(token="MAN")
ks.loginResult()
#===================#
kt = LINETCR.LINE()
kt.login(token="MAN")
kt.loginResult()
#===================#
cl

print "login SELFBOT_MAN_PC"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage ="""──────┅═ই۝ई═┅──────
             ✯✯❇Thailand❇✯✯
      ✯❇͜͡C͜͡r͜͡e͜͡a͜͡t͜͡o͜͡r✯͜͡$͜͡ë͜͡I͜͡F͜͡-͜͡฿͜͡o͜͡Ŧ❇✯
http://line.me/ti/p/~1ove..neverdie
──────┅═ই۝ई═┅──────
 ╭═════════╬[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]╬═════════╮ 
 ╠•͜͡☆➣  Man tagall แท๊กสมาชิกทั้งกลุ่ม
 ╠•͜͡☆➣  Man@tag แท๊กทั้งกลุ่ม
 ╠•͜͡☆➣  Mention แท๊กกลุ่ม
 ╠•͜͡☆➣  Gc / ข้อมูลผู้สร้างกลุ่ม
 ╠•͜͡☆➣  Me / Contact ME
 ╠•͜͡☆➣  You @ Contact YOU
 ╠•͜͡☆➣  xXx seed69
 ╠•͜͡☆➣  xXx 18+
 ╠•͜͡☆➣  My bot
 ╠•͜͡☆➣  Bot gift
 ╠•͜͡☆➣  Id / Uid
 ╠•͜͡☆➣  Mid / Mid @
 ╠•͜͡☆➣  Mid all / All mid
 ╠•͜͡☆➣  Gift / Gift all
 ╠•͜͡☆➣  Bot1-18 Gift
 ╠•͜͡☆➣  Gift you @
 ╠•͜͡☆➣  Cn: Display Name
 ╠•͜͡☆➣  Cc: Clock Name
 ╠•͜͡☆➣  Mc: Contact
 ╠•͜͡☆➣  Tl: [text]
 ╠•͜͡☆➣  Hi  ทักทาย
 ╠•͜͡☆➣  Auto join: on-off
 ╠•͜͡☆➣  Auto add: on-off
 ╠•͜͡☆➣  Auto leave: on-off
 ╠•͜͡☆➣  Clock: on-off
 ╠•͜͡☆➣  Share on
 ╠•͜͡☆➣  Add message: text
 ╠•͜͡☆➣  Message set:
 ╠•͜͡☆➣  Add comment: text
 ╠•͜͡☆➣  Comment set:
 ╠•͜͡☆➣  Cbroadcast text
 ╠•͜͡☆➣  Gbroadcast text
 ╠•͜͡☆➣  Reject  • ลบรัน
 ╠•͜͡☆➣  Reject1 • ลบรันบอท1
 ╠•͜͡☆➣  Reject2 • ลบรันบอท2
 ╠•͜͡☆➣  Reject3 • ลบรันบอท3
 ╠•͜͡☆➣  Reject4 • ลบรันบอท4
 ╠•͜͡☆➣  Reject5 • ลบรันบอท5
 ╠•͜͡☆➣  Reject6 • ลบรันบอท6
 ╠•͜͡☆➣  Reject7 • ลบรันบอท7
 ╠•͜͡☆➣  Reject8 • ลบรันบอท8
 ╠•͜͡☆➣  Reject9 • ลบรันบอท9
 ╠•͜͡☆➣  Reject10 • ลบรันบอท10
 ╠•͜͡☆➣  Reject11 • ลบรันบอท11
 ╠•͜͡☆➣  Reject12 • ลบรันบอท12
 ╠•͜͡☆➣  Reject13 • ลบรันบอท13
 ╠•͜͡☆➣  Reject14 • ลบรันบอท14
 ╠•͜͡☆➣  Reject15 • ลบรันบอท15
 ╠•͜͡☆➣  Reject16 • ลบรันบอท16
 ╠•͜͡☆➣  Reject17 • ลบรันบอท17
 ╠•͜͡☆➣  Reject18 • ลบรันบอท18
 ╠•͜͡☆➣  ลบแชท  •••••  ล้างแชท
 ╠•͜͡☆➣  ลบแชทบอท • ล้างแชทบอท
 ╰══════════╬★╬══════════╯
 ╭══════════╬💀╬══════════╮
 ║   [C̶̲̅ᴏ̶̲̅ᴍ̶̲̅ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅ᴅ̶̲̅ ̶̲̅ɪ̶̲̅ɴ̶̲̅ ̶̲̅G̶̲̅ʀ̶̲̅ᴏ̶̲̅ᴜ̶̲̅ᴘ̶̲̅] 
 ╠•͜͡☆➣ Creator / Admin
 ╠•͜͡☆➣ Gn: text name group
 ╠•͜͡☆➣ Invite: mid
 ╠•͜͡☆➣ Ambilin @ Steal dp
 ╠•͜͡☆➣ Man copy @ copy profile
 ╠•͜͡☆➣ Mycopy @ Copy profile
 ╠•͜͡☆➣ Botcopy @ 18บอทก๊อปปี้
 ╠•͜͡☆➣ Copy all @ ทั้งหมด โดนปี้
 ╠•͜͡☆➣ Bot backup บอทกลับร่าง
 ╠•͜͡☆➣ Botbb <- บอทกลับร่างเดิม
 ╠•͜͡☆➣ Mybb <- แอดมินกลับร่าง
 ╠•͜͡☆➣ Banlist / เช็คดำ
 ╠•͜͡☆➣ ข้อมูลบัญชีดำ / คท. ดำ
 ╠•͜͡☆➣ Contact ban / Conban
 ╠•͜͡☆➣ Clear ban / Cb / ล้างดำ
 ╠•͜͡☆➣ Mid ban  เช็คดำ id
 ╠•͜͡☆➣ Hack-mid:
 ╠•͜͡☆➣ Hack All 
 ╠•͜͡☆➣ Hack: @[mid-contact]
 ╠•͜͡☆➣ Hack pic @StealpicS
 ╠•͜͡☆➣ Hack cover @StealcoveR
 ╠•͜͡☆➣ Hack tus @StealstatuS
 ╠•͜͡☆➣ My bot / contactbot
 ╠•͜͡☆➣ All gift / Gift all
 ╠•͜͡☆➣ All mid / Bot mid
 ╠•͜͡☆➣ Cancel / Bcancel
 ╠•͜͡☆➣ !Speed / !Sp สปีดหลอก
 ╠•͜͡☆➣ Speedbot / Sp  ความเร็ว
 ╠•͜͡☆➣ Ginfo / ginfo / กลุ่ม
 ╠•͜͡☆➣ Gurl / Up Qr group
 ╠•͜͡☆➣ Link on-off
 ╠•͜͡☆➣ M1 link on-off
 ╠•͜͡☆➣ Gcancel:499 on
 ╠•͜͡☆➣ Glist เช็คกลุ่ม
 ╠•͜͡☆➣ Ban @แท๊กระบุ
 ╠•͜͡☆➣ Uban @แท๊กระบุ
 ╠•͜͡☆➣ Setting / Set
 ╠•͜͡☆➣ Ban -> ส่ง คท.
 ╠•͜͡☆➣ Unban -> ส่ง คท.
 ╠•͜͡☆➣ Invite:on ส่ง คท.
 ╠•͜͡☆➣ Comment bl/wl
 ╠•͜͡☆➣ Kill 
 ╠•͜͡☆➣ Kill ban 
 ╠•͜͡☆➣ music 
 ╠•͜͡☆➣ .reboot
 ╠•͜͡☆➣ Wikipedia
 ╠•͜͡☆➣ Cleanse
 ╠•͜͡☆➣ Pbot / Bot?
 ╠•͜͡☆➣ Bcancel
 ╠•͜͡☆➣ M1-M2 tl:
 ╠•͜͡☆➣ M1-M2 say
 ╠•͜͡☆➣ M1-M2 tag
 ╠•͜͡☆➣ M1-M2 invite:
 ╠•͜͡☆➣ M1-M3 mid
 ╠•͜͡☆➣ M1-M2 url
 ╠•͜͡☆➣ M1-M5 gift
 ╠•͜͡☆➣ M1-M10 in
 ╠•͜͡☆➣ M1-M18 bye
 ╠•͜͡☆➣ M1 link on-off
 ╠•͜͡☆➣ M1-M18 rgroup
 ╠•͜͡☆➣ M1-M18 rename:
 ╠•͜͡☆➣ All: rename all:
 ╠•͜͡☆➣ Allbio: Isi bio:
 ╠•͜͡☆➣ @bye / #bye / Bye
 ╠•͜͡☆➣ Kicker / มาหำ / •••
 ╠•͜͡☆➣ Kick-Kick1-kick2 @tag
 ╠•͜͡☆➣ M1 - M9 kick @tag
 ╠•͜͡☆➣ Nk /Mk /??¿ /Fuck @tag
 ╠•͜͡☆➣ Error! / Kickall ล้างกลุ่ม
 ╠•͜͡☆➣ Run group  รันกลุ่ม
 ╠•͜͡☆➣ Man1-Man18  ข้อมูลบอท
 ║  [Help] - [Help2] - [Helpbot]
 ║   [Set protect] - [Man set]
 ╰══════════╬★╬══════════╯ 
──────┅═ই۝ई═┅──────
•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•
နับთิஏთั้ଏบਹທV⒑
(รับทำเชลกันรัน-บอทแท๊ก)
สอบถามรายละเอียดเพิ่มเติม..   Link⤵️
http://line.me/ti/p/~1ove..neverdie
──────┅═ই۝ई═┅──────
"""

helpMessage2 ="""Mr. Bots…⛿
╔══╦═╦═╗
║║║║║║║║    ✯✯❇ᵀᴴᴬᴵᴸᴬᴺᴰ❇✯✯
║║║║╦║║║  ❇͜͡C͜͡r͜͡e͜͡a͜͡t͜͡o͜͡r✯͜͡$͜͡ë͜͡I͜͡F͜͡-͜͡฿͜͡o͜͡Ŧ❇
╚╩╩╩╩╩╩╝️ နับთิஏთั้ଏบਹທ SirichanV⒑
http://line.me/ti/p/~1ove..neverdie
╔═════════════════════╗
║•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•
╠═════════════════════╝
║[Massage add: "text"]:
║[Add confirmasi]:
║[Comment set : "Text"]:
║[Comment check]:
║[Clock: on]: "Clock name on"
║[Clock: off]: "Clock name off"
║[Ban]: "Add blacklist"
║[Unban]: "Dalate blacklist"
║[Banlist]: "Check blacklist"
╠═════════════════════╗
║        〚C͓̳͓O͓̳͓M͓̳͓M͓̳͓A͓̳͓N͓̳͓D͓̳͓ ͓S͓̳͓E͓̳͓T͓̳͓〛
╠═════════════════════╝
║[Contact: on/off]
║[Auto join: on/off]
║[Auto join: on/off]
║[Cancel Invite: 1 on/off]
║[Auto share: on/off]
║[Auto leave: on/off]
║[Comment: on/off]
║[Auto add: on/off]
║[Auto like: on/off]
╠═════════════════════╗
║   [C̶̲̅ᴏ̶̲̅ᴍ̶̲̅ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅ᴅ̶̲̅ ̶̲̅ɪ̶̲̅ɴ̶̲̅ ̶̲̅G̶̲̅ʀ̶̲̅ᴏ̶̲̅ᴜ̶̲̅ᴘ̶̲̅] 
╠═════════════════════╝
║[Ban " @Tag]:
║[Unban " @Tag]:
║[Urlon]: "Open urL"
║[Urloff]: "Closed urL"
║[Url]: " Check urL room"
║[Ginfo]: "~÷~ data room"
║[Invite: "mid"]:
║[Say: "Text"]: "Kicker talk"
║[Cancel]: "Cancel invite"
║[Gns: "name"]:"Change Gname"
║[NKs: "Name"]:
║[Dead]: "Kick Blacklist"
║[Protect: on/off]:
║[Block url: on/off]:
║[Namelock: on/off]:
║[Blockinvite: on/off]:
╚═════════════════════╝
"""

KAC=[cl,ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,km,kn,ko,kp,kq,kr,ks,kt]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid
Fmid = kf.getProfile().mid
Gmid = kg.getProfile().mid
Hmid = kh.getProfile().mid
Jmid = kj.getProfile().mid
Lmid = kl.getProfile().mid
Mmid = km.getProfile().mid
Nmid = kn.getProfile().mid
Omid = ko.getProfile().mid
Pmid = kp.getProfile().mid
Qmid = kq.getProfile().mid
Rmid = kr.getProfile().mid
Smid = ks.getProfile().mid
Tmid = kt.getProfile().mid
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
Bots = ["ud24af63fd62d14c3bf8f719df80c3745",mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Jmid,Lmid,Mmid,Nmid,Omid,Pmid,Qmid,Rmid,Smid,Tmid]
self = ["ud24af63fd62d14c3bf8f719df80c3745",mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Jmid,Lmid,Mmid,Nmid,Omid,Pmid,Qmid,Rmid,Smid,Tmid]
admin = "ud24af63fd62d14c3bf8f719df80c3745"
owner = "ud24af63fd62d14c3bf8f719df80c3745"
admsa = "ud24af63fd62d14c3bf8f719df80c3745"
adminMID = "ud24af63fd62d14c3bf8f719df80c3745"
wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":True, "members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"""「Auto ADD」 Man..✍️
 ╔══╦═╦═╗
 ║║║║║║║║🌟🌟🌟🌟🌟
 ║║║║╦║║║ Mr. Bots…⛿
 ╚╩╩╩╩╩╩╝ ᵀᴴᴬᴵᴸᴬᴺᴰ  creator 
နับთิஏთั้ଏบਹທ Sirichan V⒑
คำสั่งบอท มีเยอะ คุณสมบัติเน้นๆ ผมยกตัวอย่างให้ทราบคร่าวๆ
คำนี้เป็นการล็อกห้องสั่งแล้วทุกคนจะทำอะไรไม่ได้นอกจากเจ้าของห้องทำได้คนเดียวเช่น
•เปิดลิงค์•เชิญเพื่อน•เปลี่ยนรูปกลุ่ม•เปลี่ยนชื่อกลุ่ม•

มีตั้งเเต่ชุดบอท 12-37 บอท
➖➖➖➖➖➖➖➖➖➖➖➖➖

ล๊อกกันรันสติ๊กเกอร์ก่อกวน
Set:StampLimitation:on

ล๊อกชื่อกลุ่ม(กันสมาชิกเปลี่ยนชื่อ)
Set:changenamelock:on

ล๊อกรูปกลุ่ม(กันสมาชิกเปลี่ยนรูป)
Set:iconlock:on

ล๊อกการเชิญ (ป้องกันสมาชิกเชิญคนมั่ว)
Set:blockinvite:on

ล๊อกแอทมิน (ป้องกันสมาชิกลบแอดมิน)
Set:ownerlock:on
 
คำสั่งปิด Url หากสมาชิกเปิด บอทจะลบออกทันที
Siri:DenyURLInvite

(บอทจะไม่ลบเเอดมินทุกกรณี)
➖➖➖➖➖➖➖➖➖➖➖➖➖
set:changeowner
เปลี่ยนเจ้าของห้อง, ลงสั่งแล้วส่งข้อมูลคนที่จะเป็นเจ้าของห้องคนต่อไปลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖
set:addblacklist
บัญชีดำแบ็คลิสคนไม่ให้เข้ากลุ่มลงสั่งแล้วส่งข้อมูลคนที่เราจะแบ็คลิสลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖
set:addwhitelist
บัญชีขาวแก้ดำสั่งแล้วส่งข้อมูลคนที่เราจะแก้แบ๊คลิสลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖
Set:blockinvite:off  ปลดล็อกการเชิญ
➖➖➖➖➖➖➖➖➖➖➖➖➖
Set:blockinvite:on  ล็อกการเชิญ
➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:inviteurl        เปิดลิงค์
➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:DenyURLInvite    ปิดลิงค์
➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:cancelinvite  ยกเลิกค้างเชิญสั่ง2ครั้ง
➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:groupcreator เช็คแอดมินหลัก
➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:extracreator  เช็คแอดมินสำรอง
➖➖➖➖➖➖➖➖➖➖➖➖➖
set:changeextraowner เพิ่มแอดมินสำรอง
ลงคำสั่งแล้วส่งข้อมูลคนที่จะเป็นคนสำรองลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖
Set:turncreator ใช้สลับแอดมินได้
เมื่อแอดมินหลักไม่ว่าง ให้แอดมินสำรองทำหน้าที่แทนได้
➖➖➖➖➖➖➖➖➖➖➖➖➖
ดูคนอ่าน ใช้ 2คำสั่ง
สั่งเซ็ตเวลาตั้งค่าก่อน
แล้วค่อยสั่งเช็คอ่านคน

Setlastpoint     ตั้งค่า

Viewlastseen    เช็คอ่าน
➖➖➖➖➖➖➖➖➖➖➖➖➖

 ╔•═•-⊰❉⊱•═•⊰❉⊱•═•⊰❉⊱-•═•╗ 
 ║🌐 ✍️$ëcürîty❄️฿❂T✔Ľîη℮ 🌐║ 
 ╚•═•-⊰❉⊱•═•⊰❉⊱•═•⊰❉⊱-•═•╝

   ✍️รับติดตั้ง ฿❂Ŧ✔Sirichan v⒑
 Install Line Group Security Bots.
ระบบรักษาความปลอดภัยของกลุ่มไลน์
  🔘ลงบอทกลุ่มที่มีสมาชิก 200 บาท
  🔘กลุ่มบอท ชุด12ตัว  120 บาท
  🔘เพิ่มบอทเสริม ชุดล่ะ 100 บาท
    🔘ประกันกลุ่ม 50.- ช่วยดูแลแก้ไข
เปลี่ยนฟรีให้ลูกค้าเมื่อบอทขัดข้อง
  🔘ประกันกลุ่ม 100.- ✰✰✰✰✰
เมื่อกลุ่มโดนลบ  [เคลมให้ฟรี 1กลุ่ม]
เมื่อบอทขัดข้อง แก้ไขเปลี่ยนบอทฟรี
แถมบอทคำสั่ง ผู้ช่วยแอดมินเพิ่ม 1ตัว

          ✍️Pro.. ✰โปรโมชั่น✰✰
   🌐ติดตั้งบอทพร้อมประกัน 2 ชุด🌐
        (ฟรี)รับฟรีอีก 1 กลุ่มบอท(ฟรี)

   💡คุณสมบัติพิเศษของบอท v10💡
🔒ป้องกันสมาชิกเปิดลิงก์ห้อง
🔒ป้องกันสมาชิกเปลี่ยนรูปกลุ่ม
🔒ป้องกันสมาชิกเปลี่ยนชื่อกลุ่ม
🔒ป้องกันสมาชิกเชิญคนนอกเข้ากลุ่ม
🔒ป้องกันคนนอกเข้ามาลบคนในกลุ่ม 
🔒ห้ามลบสมาชิกในกลุ่ม นอกจากแอด
🔒ถ้าลบเกิน3คน บอทจะเตะออกทันที
📇สามารถเช็คคนที่แอบอ่านในกลุ่มได้

    ✫☆✰สนใจทักมาสอบถาม✰☆✫
🔽🔻🔽🔻🔽🔻🔽🔻🔽🔻🔽🔻🔽
──────┅═ই۝ई═┅──────
รับทำเชลบอทกันรัน (บอทส่วนตัว) แท๊กได้ทั้งกลุ่ม
สนใจติดต่อที่  ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ
🆔http://line.me/ti/p/~1ove..neverdie
နับთิஏთั้ଏบਹທ  Sirichan V⒑
http://line.me/ti/p/~security_botline
──────┅═ই۝ई═┅──────
""",
    "lang":"JP",
    "comment":"",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "likeOn":False,
    "pname":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "qr":False,
    "Backup":False,
    "protectionOn":False,
    "winvite":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    "posts":False,
	}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

wait3 = {
    "copy":False,
    "copy2":"target",
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']

blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kk.getProfile()
backup = kk.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kc.getProfile()
backup = kc.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kd.getProfile()
backup = kd.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ke.getProfile()
backup = ke.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kf.getProfile()
backup = kf.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kg.getProfile()
backup = kg.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kh.getProfile()
backup = kh.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kj.getProfile()
backup = kj.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kl.getProfile()
backup = kl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = km.getProfile()
backup = km.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kn.getProfile()
backup = kn.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ko.getProfile()
backup = ko.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kp.getProfile()
backup = kp.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kq.getProfile()
backup = kq.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kr.getProfile()
backup = kr.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ks.getProfile()
backup = ks.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kt.getProfile()
backup = kt.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

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

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to, nama):
	aa = ""
	bb = ""
	strt = int(0)
	akh = int(0)
	nm = nama
	print nm
	for mm in nm:
		akh = akh + 3
		aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M","""+json.dumps(mm)+"),"""
		strt = strt + 4
		akh = akh + 1
		bb += "@x \n"
	aa = (aa[:int(len(aa)-1)])
	msg = Message()
	msg.to = to
	msg.from_ = admin
	msg.text = bb
	msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
	print msg
	try:
		cl.sendMessage(msg)
	except Exception as error:
		print error

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

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
                                    G = kc.getGroup(op.param1)
                                except:
                                    try:
                                        G = kd.getGroup(op.param1)
				    except:
					try:
                                            G = ke.getGroup(op.param1)
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
                                    kc.updateGroup(G)
                                except:
                                    try:
                                        kd.updateGroup(G)
                                    except:
                                        try:
                                            ke.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Group Name Lock")
                                        ki.sendText(op.param1,"Haddeuh dikunci Pe'a")
                                        kk.sendText(op.param1,"Wekawekaweka (Har Har)")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)

        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = kd.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = ke.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        X = kf.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                if op.param3 in Fmid:
                    if op.param2 in Gmid:
                        X = kg.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                if op.param3 in Gmid:
                    if op.param2 in Hmid:
                        X = kh.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kh.updateGroup(X)
                        Ti = kh.reissueGroupTicket(op.param1)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kh.updateGroup(X)
                        Ti = kh.reissueGroupTicket(op.param1)
                if op.param3 in Hmid:
                    if op.param2 in Jmid:
                        X = kj.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kj.updateGroup(X)
                        Ti = kj.reissueGroupTicket(op.param1)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kj.updateGroup(X)
                        Ti = kj.reissueGroupTicket(op.param1)
                if op.param3 in Jmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Nmid:
                        G = kn.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kn.updateGroup(G)
                        Ticket = kn.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kn.updateGroup(G)
                        Ticket = kn.reissueGroupTicket(op.param1)

                if op.param3 in Nmid:
                    if op.param2 in Omid:
                        X = ko.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)

                if op.param3 in Omid:
                    if op.param2 in Pmid:
                        X = kp.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kp.updateGroup(X)
                        Ti = kp.reissueGroupTicket(op.param1)
                        ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kp.updateGroup(X)
                        Ti = kp.reissueGroupTicket(op.param1)
                if op.param3 in Pmid:
                    if op.param2 in Qmid:
                        X = kq.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kq.updateGroup(X)
                        Ti = kq.reissueGroupTicket(op.param1)
                        kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kq.updateGroup(X)
                        Ti = kq.reissueGroupTicket(op.param1)
                if op.param3 in Qmid:
                    if op.param2 in Rmid:
                        X = kr.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kr.updateGroup(X)
                        Ti = kr.reissueGroupTicket(op.param1)
                        kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kr.updateGroup(X)
                        Ti = kr.reissueGroupTicket(op.param1)
                if op.param3 in Rmid:
                    if op.param2 in Smid:
                        X = ks.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                        kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                if op.param3 in Smid:
                    if op.param2 in Tmid:
                        X = kt.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kt.updateGroup(X)
                        Ti = kt.reissueGroupTicket(op.param1)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kt.updateGroup(X)
                        Ti = kt.reissueGroupTicket(op.param1)
                if op.param3 in Tmid:
                    if op.param2 in Rmid:
                        X = kr.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kr.updateGroup(X)
                        Ti = kr.reissueGroupTicket(op.param1)
                        kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kr.updateGroup(X)
                        Ti = kr.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid:
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Dmid:
                        X = kd.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Emid:
                        X = ke.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Fmid:
                        X = kf.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Gmid:
                        X = kg.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Hmid:
                        X = kh.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kh.updateGroup(X)
                        Ti = kh.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kh.updateGroup(X)
                        Ti = kh.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Jmid:
                        X = kj.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kj.updateGroup(X)
                        Ti = kj.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kj.updateGroup(X)
                        Ti = kj.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Lmid:
                        X = kl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kL.updateGroup(X)
                        Ti = kl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kl.updateGroup(X)
                        Ti = kl.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Mmid:
                        X = km.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        km.updateGroup(X)
                        Ti = km.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        km.updateGroup(X)
                        Ti = km.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Nmid:
                        X = kn.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kn.updateGroup(X)
                        Ti = kn.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kn.updateGroup(X)
                        Ti = kn.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Omid:
                        X = ko.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Pmid:
                        X = kp.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kp.updateGroup(X)
                        Ti = kp.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kp.updateGroup(X)
                        Ti = kp.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Qmid:
                        X = kq.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kq.updateGroup(X)
                        Ti = kq.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kq.updateGroup(X)
                        Ti = kq.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Rmid:
                        X = kr.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kr.updateGroup(X)
                        Ti = kr.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kr.updateGroup(X)
                        Ti = kr.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Smid:
                        X = ks.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Tmid:
                        X = kt.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kt.updateGroup(X)
                        Ti = kt.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kt.updateGroup(X)
                        Ti = kt.reissueGroupTicket(op.param1)
#===========================================
        if op.type == 32:
            if not op.param2 in Bots:
                if wait["protectionOn"] == True: 
                    try:
                        klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,km,kn,ko,kp,kq,kr,ks,kt]
                        kicker = random.choice(klist) 
                        G = kicker.getGroup(op.param1)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        kicker.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                       print e
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
            if Amid in op.param3:
                G = cl.getGroup(op.param1)
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
            if Bmid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kk.rejectGroupInvitation(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        kk.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kk.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["qr"] == True:  
                try:
                    klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,km,kn,ko,kp,kq,kr,ks,kt]
                    kicker = random.choice(klist) 
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                except Exception, e:
                    print e
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["protectionOn"] == True:
                 try:                    
                    klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,km,kn,ko,kp,kq,kr,ks,kt]
                    kicker = random.choice(klist) 
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                    kicker.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                 except Exception, e:
                           print e
        if op.type == 13:
            G = cl.getGroup(op.param1)
            I = G.creator
            if not op.param2 in Bots:
                if wait["protectionOn"] == True:  
                    klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,km,kn,ko,kp,kq,kr,ks,kt]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    if G is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(op.param1, gInviMids)
        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["protectionOn"] == True:  
                   try:
                       klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,km,kn,ko,kp,kq,kr,ks,kt]
                       kicker = random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                       time.sleep(0.2)
                       X = kicker.getGroup(op.param1)             
                       X.preventJoinByTicket = True
                       kl.kickoutFromGroup(op.param1,[op.param2])
                       kicker.kickoutFromGroup(op.param1,[op.param2])
                       kl.leaveGroup(op.param1)
                       kicker.updateGroup(X)
                   except Exception, e:
                            print e
                if not op.param2 in Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
        if op.type == 19:              
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                   
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ticket = ki.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ticket = kk.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kd.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kd.updateGroup(X)
                    Ti = kd.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ticket = kc.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kd.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kd.updateGroup(X)
                    Ticket = kd.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kf.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kf.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ticket = ke.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kg.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kg.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kg.updateGroup(X)
                    Ti = kg.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kf.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kf.updateGroup(X)
                    Ticket = kf.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kh.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kh.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kh.updateGroup(X)
                    Ti = kh.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kg.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kg.updateGroup(X)
                    Ticket = kg.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kj.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kj.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kj.updateGroup(X)
                    Ti = kj.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kh.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kh.updateGroup(X)
                    Ticket = kh.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Jmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kj.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kj.updateGroup(X)
                    Ticket = kj.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Nmid in op.param3:
                    if op.param2 in Bots:
                        pass                   
                    try:
                        ko.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ko.updateGroup(G)
                    Ti = ko.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kn.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kn.updateGroup(X)
                    Ti = kn.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Omid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kp.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kp.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kp.updateGroup(X)
                    Ti = kp.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ko.updateGroup(X)
                    Ticket = ko.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Pmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kq.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kq.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kq.updateGroup(X)
                    Ti = kq.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kp.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kp.updateGroup(X)
                    Ticket = kp.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Qmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kr.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kr.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kr.updateGroup(X)
                    Ti = kr.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kq.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kq.updateGroup(X)
                    Ticket = kq.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Rmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ks.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr.updateGroup(X)
                    Ticket = kr.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Smid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kt.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kt.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kt.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ticket = ks.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Tmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kt.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kt.updateGroup(X)
                    Ticket = kt.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kf.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kf.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kn.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kn.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kn.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kn.updateGroup(X)
                    Ti = kn.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ko.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kp.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kp.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kp.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

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
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "ud24af63fd62d14c3bf8f719df80c3745":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
		
        """if op.type == 26:
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
     
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
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
                                  break

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy",cName + ""]
                     ret_ = "[Auto] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  msg.contentType = 7
                                  msg.text = ''
                                  msg.contentMetadata = {
                                                            'STKPKGID': '608',
                                                            'STKTXT': '[]',
                                                            'STKVER': '16',
                                                            'STKID':'5507'
                                                        }
                                  cl.sendMessage(msg)
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

            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
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
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                                cl.sendImageWithUrl(msg.to,image)
                                cl.sendText(msg.to,"Cover " + contact.displayName)
                                cl.sendImageWithUrl(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass
	    
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)                                             
                else:
                    cl.sendChatChecked(msg.to,msg.id)"""
#=================================================
        if op.type == 25:
            msg = op.message
            if msg.text.lower() in ["mention"]:
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
                cnt.text = "[Member List TAG number : " + str(jml) +  " Members]\n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•"
                cnt.to = msg.to
                cl.sendMessage(cnt)

        if op.type == 25:
            msg = op.message
            if msg.text.lower() in ["man tagall"]:
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
                cnt.text = "[Member List TAG number : " + str(jml) +  " Members]\n\n──────┅═ই۝ई═┅──────\nနับთิஏთั้ଏบਹທ.. Sirichan V⒑\nรับเขียนบอทกันรัน - แท๊กได้ทั้งกลุ่ม\nทักมาสอบถามรายละเอียดได้ครับ  คลิ้กลิงก์↲\n📧https://line.me/R/ti/p/%40uvh1233u\n──────┅═ই۝ई═┅──────"
                cnt.to = msg.to
                cl.sendMessage(cnt)

        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")
                        
               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Deleted")
                        wait["dblack"] = False
                        
                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        
               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Deleted")
                        
                        wait["dblacklist"] = False
                        
                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"⎈ Profile Name :\n" + msg.contentMetadata["displayName"] + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Message :\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu) + "\n\n [☸]➦Powered By: メTamii々•┅─────")
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"⎈ Profile Name :\n" + contact.displayName + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Mesage:\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu) + "\n\n [☸]➦Powered By: メTamii々•┅─────")
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL→\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Hp","Help","help","คำสั่ง"]:
                print "\nHelp pick up..."
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage + "")
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Hp2","Help2","help2"]:
                print "\nHelp pick up..."
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage2 + "")
                else:
                    cl.sendText(msg.to,helpt)

            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn:","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:"," ")
                klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,km,kn,ko,kp,kq,kr,ks,kt,cl]
                kicker = random.choice(klist)
                kicker.kickoutFromGroup(msg.to,[midd])

        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["winvite"] == True:
                     if msg.from_ == admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
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
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         cl.findAndAddContactsByMid(invite)
                                         cl.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:"," ")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "M1 invite:" in msg.text:
                midd = msg.text.replace("M1 invite:"," ")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "M2 invite:" in msg.text:
                midd = msg.text.replace("M2 invite:"," ")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'my bot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Lmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Mmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Nmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Omid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Pmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Qmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Rmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Smid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Tmid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact bot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                kd.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ke.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                kf.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                kg.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                kh.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}
                kj.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Lmid}
                kl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Mmid}
                km.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Nmid}
                kn.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Omid}
                ko.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Pmid}
                kp.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Qmid}
                kq.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Rmid}
                kr.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Smid}
                ks.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Tmid}
                kt.sendMessage(msg)
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif "Man1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif "Man2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
            elif "Man3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
            elif "Man4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                kd.sendMessage(msg)
            elif "Man5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ke.sendMessage(msg)
            elif "Man6" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                kf.sendMessage(msg)
            elif "Man7" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                kg.sendMessage(msg)
            elif "Man8" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                kh.sendMessage(msg)
            elif "Man9" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}
                kj.sendMessage(msg)
            elif "Man10" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Lmid}
                kl.sendMessage(msg)
            elif "Man11" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Mmid}
                km.sendMessage(msg)
            elif "Man12" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Nmid}
                kn.sendMessage(msg)
            elif "Man13" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Omid}
                ko.sendMessage(msg)
            elif "Man14" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Pmid}
                kp.sendMessage(msg)
            elif "Man15" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Qmid}
                kq.sendMessage(msg)
            elif "Man16" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Rmid}
                kr.sendMessage(msg)
            elif "Man17" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Smid}
                ks.sendMessage(msg)
            elif "Man18" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Tmid}
                kt.sendMessage(msg)
 
            elif "youtt " in msg.text.lower():
                if msg.toType == 2:
                   query = msg.text.split(":")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
            elif "youtt:" in msg.text.lower():
                if msg.toType == 2:
                   query = msg.text.split(":")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
            elif 'testyt ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('testyt ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
#-----------------------------------------------------------
            elif msg.text in ["ลบแชท","ล้างแชท"]:
                cl.removeAllMessages(op.param2)
                cl.sendText(msg.to,"❇️Delete Chat Bot❇️")
#-----------------------------------------------------------
            elif msg.text in ["ลบแชทบอท","ล้างแชทบอท"]:
                ki.removeAllMessages(op.param2)
                kk.removeAllMessages(op.param2)                  
                kc.removeAllMessages(op.param2)
                kd.removeAllMessages(op.param2)
                ke.removeAllMessages(op.param2)
                kf.removeAllMessages(op.param2)
                kg.removeAllMessages(op.param2)
                kh.removeAllMessages(op.param2)
                kj.removeAllMessages(op.param2)
		kl.removeAllMessages(op.param2)
                km.removeAllMessages(op.param2)
		kn.removeAllMessages(op.param2)
                ko.removeAllMessages(op.param2)
                kp.removeAllMessages(op.param2)
                kq.removeAllMessages(op.param2)
		kr.removeAllMessages(op.param2)
                ks.removeAllMessages(op.param2)
                kt.removeAllMessages(op.param2)
                cl.sendText(msg.to,"❇️Delete Chat Bot❇️")
                cl.sendText(msg.to,"──────┅═ই۝ई═┅──────\n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nได้เคลียร์แชทบอท 18Kicker เรียบร้อย\n──────┅═ই۝ई═┅──────")
#-----------------------------------------------------------
            elif "Spam @" in msg.text:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       kk.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")  
                       ki.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")  
                       kc.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       kd.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       ke.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       kf.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       kg.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       kh.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       kj.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       kl.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       km.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       kn.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       ko.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       kp.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       kq.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       kr.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       ks.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       kt.sendText(g.mid,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                       cl.sendText(msg.to, "Done...S.P.A.M \n •─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─• ")
                       print "Berhasil Spam Kontak"

            elif "spm " in msg.text:
                if msg.from_ in admin:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[1])
                    teks = msg.text.replace("spm " + str(jmlh) + " ","")
                    if jmlh <= 20:
                        for x in range(jmlh):
                            cl.sendText(msg.to,teks)
                            kk.sendText(msg.to,teks)
                            ki.sendText(msg.to,teks)
                            kc.sendText(msg.to,teks)
                            kd.sendText(msg.to,teks)
                            ke.sendText(msg.to,teks)
                            kf.sendText(msg.to,teks)
                            kg.sendText(msg.to,teks)
                            kh.sendText(msg.to,teks)
                            kj.sendText(msg.to,teks)
                            kl.sendText(msg.to,teks)
                            km.sendText(msg.to,teks)
                            kn.sendText(msg.to,teks)
                            ko.sendText(msg.to,teks)
                            kp.sendText(msg.to,teks)
                            kq.sendText(msg.to,teks)
                            kr.sendText(msg.to,teks)
                            ks.sendText(msg.to,teks)
                            kt.sendText(msg.to,teks)
#----------------------------------------------------------
            elif msg.text in ["Conban","ข้อมูลบัญชีดำ","Contact ban","คท. ดำ"]:
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
            elif msg.text in ["55","555","5555","ฮ่าๆๆ"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }

                cl.sendMessage(msg)
                ki.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
            elif "youname " in msg.text.lower():
                txt = msg.text.replace("youname ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
            elif "Hack all" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Hack all","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "ดำ " in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            wait["blacklist"][target] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Done Banned")
                            print "[Command] Bannad"
                        except:
                            pass
#----------------------------------------------------------------------------
#------------------------------- UNBAN BY TAG -------------------------------
            elif "ขาว " in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del wait["blacklist"][target]
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Done Unbanned")
                            print "[Command] Unbannad"
                        except:
                            pass
#----------------------------------------------------------------------------
            elif msg.text.lower() in ["botkill"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        ki.kickoutFromGroup(msg.to,[jj])
                        pass

            elif msg.text.lower() in ["admin","creator"]:
                msg.contentType = 13
                adm = 'ud24af63fd62d14c3bf8f719df80c3745'
                msg.contentMetadata = {'mid': adm}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"──────┅═ই۝ई═┅──────\nနับთิஏთั้ଏบਹທ  Sirichan V⒑\nสนใจติดต่อที่.. ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ\n http://line.me/ti/p/~1ove..neverdie \n──────┅═ই۝ई═┅──────")

            elif msg.text in ["Man gift","ของขวัญ"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '1'}
                msg.text = None
                cl.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '4'}
                msg.text = None
                cl.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '7'}
                msg.text = None
                cl.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '1'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["Bot1 Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Bot2 Gift","M2gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '3'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["Bot4 Gift","M3gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '4'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["Bot5 Gift","M4gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}
                msg.text = None
                kd.sendMessage(msg)
            elif msg.text in ["Bot6 Gift","M5gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}
                msg.text = None
                ke.sendMessage(msg)
            elif msg.text in ["All gift","Gift all"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                kd.sendMessage(msg)
                ke.sendMessage(msg)
                kf.sendMessage(msg)
                kg.sendMessage(msg)
                kh.sendMessage(msg)
                kj.sendMessage(msg)
                kl.sendMessage(msg)
                km.sendMessage(msg)
                kn.sendMessage(msg)
                ko.sendMessage(msg)
                kp.sendMessage(msg)
                kq.sendMessage(msg)
                kr.sendMessage(msg)
		ks.sendMessage(msg)
                kt.sendMessage(msg)

            #VPS STUFF - VPS NEEDED TO RUN THIS COMMAND :)
            elif msg.text in ["vps","kernel"]:
                 if msg.from_ in admin:
                     botKernel = subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]
                     cl.sendText(msg.to, botKernel)
                     print "[Command]Kernel executed"
                 else:
                     cl.sendText(msg.to,"Command denied.")
                     cl.sendText(msg.to,"Admin permission required.")
                     print "[Error]Command denied - Admin permission required"

            elif "Gc" == msg.text:
                try:
                    group = cl.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    cl.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    cl.sendMessage(M)
                    cl.sendText(msg.to,"old user")

            elif 'Yt ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Yt ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")

            elif "#set" in msg.text:
				cl.sendText(msg.to, "Let's see who lazy to type")
				try:
					del wait2['readPoint'][msg.to]
					del wait2['readMember'][msg.to]
				except:
					pass
				wait2['readPoint'][msg.to] = msg.id
				wait2['readMember'][msg.to] = ""
				wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				wait2['ROM'][msg.to] = {}
				print wait2
            elif "#read" in msg.text:
				if msg.to in wait2['readPoint']:
					if wait2["ROM"][msg.to].items() == []:
						chiya = ""
					else:
						chiya = ""
						for rom in wait2["ROM"][msg.to].items():
							print rom
							chiya += rom[1] + "\n"

					cl.sendText(msg.to, "people who reading%s\n is this\n\n\nDate and time I started it:\n[%s]" % (wait2['readMember'][msg.to],setTime[msg.to]))
				else:
					cl.sendText(msg.to, "read point not set\nReading point setting you send it it will send an esxisting one")

            elif msg.text in ["GinfoID"]:
                gid = cl.getGroupIdsJoined()
                g = ""
                for i in gid:
                    g += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,g)

#==================================================
            elif "ตั้งชื่อบอท:" in msg.text:
                string = msg.text.replace("ตั้งชื่อบอท:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kd.getProfile()
                    profile.displayName = string
                    kd.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ke.getProfile()
                    profile.displayName = string
                    ke.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kf.getProfile()
                    profile.displayName = string
                    kf.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kg.getProfile()
                    profile.displayName = string
                    kg.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kh.getProfile()
                    profile.displayName = string
                    kh.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kj.getProfile()
                    profile.displayName = string
                    kj.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kl.getProfile()
                    profile.displayName = string
                    kl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = km.getProfile()
                    profile.displayName = string
                    km.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kn.getProfile()
                    profile.displayName = string
                    kn.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ko.getProfile()
                    profile.displayName = string
                    ko.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kp.getProfile()
                    profile.displayName = string
                    kp.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kq.getProfile()
                    profile.displayName = string
                    kq.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kr.getProfile()
                    profile.displayName = string
                    kr.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kt.getProfile()
                    profile.displayName = string
                    kt.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name bots : " + string + "")
            elif "ตัสบอท:" in msg.text:
                string = msg.text.replace("ตัสบอท:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kd.getProfile()
                    profile.statusMessage = string
                    kd.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ke.getProfile()
                    profile.statusMessage = string
                    ke.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kf.getProfile()
                    profile.statusMessage = string
                    kf.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kg.getProfile()
                    profile.statusMessage = string
                    kg.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kh.getProfile()
                    profile.statusMessage = string
                    kh.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kj.getProfile()
                    profile.statusMessage = string
                    kj.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kl.getProfile()
                    profile.statusMessage = string
                    kl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = km.getProfile()
                    profile.statusMessage = string
                    km.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kn.getProfile()
                    profile.statusMessage = string
                    kn.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ko.getProfile()
                    profile.statusMessage = string
                    ko.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kp.getProfile()
                    profile.statusMessage = string
                    kp.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kq.getProfile()
                    profile.statusMessage = string
                    kq.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kr.getProfile()
                    profile.statusMessage = string
                    kr.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kt.getProfile()
                    profile.statusMessage = string
                    kt.updateProfile(profile)
            elif "ตั้งชื่อตัวเอง:" in msg.text:
                string = msg.text.replace("ตั้งชื่อตัวเอง:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name : " + string + "")
            elif "BBc:" in msg.text:
                bctxt = msg.text.replace("BBc:", "")
                a = cl.getGroupIdsJoined()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
            elif msg.text.lower() == 'bann':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)

            elif msg.text.lower() == '•••':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        km.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kn.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kp.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kq.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kr.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kt.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki.sendText(msg.to,"Hello " + str(ginfo.name) + "\n\nBy•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─• \n📧https://line.me/R/ti/p/%40uvh1233u")
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
            elif msg.text.lower() == '#bye':
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        ki.leaveGroup(msg.to)
                        kk.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kk.leaveGroup(msg.to)
                        kc.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kc.leaveGroup(msg.to)
                        kd.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kd.leaveGroup(msg.to)
                        ke.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        ke.leaveGroup(msg.to)
                        kf.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kf.leaveGroup(msg.to)
                        kg.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kg.leaveGroup(msg.to)
                        kh.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kh.leaveGroup(msg.to)
                        kj.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kj.leaveGroup(msg.to)
                        kl.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kl.leaveGroup(msg.to)
                        km.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        km.leaveGroup(msg.to)
                        kn.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kn.leaveGroup(msg.to)
                        ko.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        ko.leaveGroup(msg.to)
                        kp.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kp.leaveGroup(msg.to)
                        kq.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kq.leaveGroup(msg.to)
                        kr.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kr.leaveGroup(msg.to)
                        ks.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        ks.leaveGroup(msg.to)
                        kt.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kt.leaveGroup(msg.to)
                    except:
                        pass

            elif "V10" in msg.text:
                cl.sendText(msg.to,"""နับთิஏთั้ଏบਹທ
╔══╦═╦═╗ Sirichan V⒑
║║║║║║║║ 🌟🌟🌟🌟🌟
║║║║╦║║║ Mr. Bots…⛿
╚╩╩╩╩╩╩╝ ᵀᴴᴬᴵᴸᴬᴺᴰ  creator 
 คำสั่งบอท มีเยอะ คุณสมบัติเน้นๆ ผมยกตัวอย่างให้ทราบคร่าวๆ
คำนี้เป็นการล็อกห้องสั่งแล้วทุกคนจะทำอะไรไม่ได้นอกจากเจ้าของห้องทำได้คนเดียวเช่น
•เปิดลิงค์•เชิญเพื่อน•เปลี่ยนรูปกลุ่ม•เปลี่ยนชื่อกลุ่ม•

มีตั้งเเต่ชุดบอท 12-37 บอท
➖➖➖➖➖➖➖➖➖➖➖➖➖

ล๊อกกันรันสติ๊กเกอร์ก่อกวน
Set:StampLimitation:on

ล๊อกชื่อกลุ่ม(กันสมาชิกเปลี่ยนชื่อ)
Set:changenamelock:on

ล๊อกรูปกลุ่ม(กันสมาชิกเปลี่ยนรูป)
Set:iconlock:on

ล๊อกการเชิญ (ป้องกันสมาชิกเชิญคนมั่ว)
Set:blockinvite:on

ล๊อกแอทมิน (ป้องกันสมาชิกลบแอดมิน)
Set:ownerlock:on
 
คำสั่งปิด Url หากสมาชิกเปิด บอทจะลบออกทันที
Siri:DenyURLInvite

(บอทจะไม่ลบเเอดมินทุกกรณี)
➖➖➖➖➖➖➖➖➖➖➖➖➖
set:changeowner
เปลี่ยนเจ้าของห้อง, ลงสั่งแล้วส่งข้อมูลคนที่จะเป็นเจ้าของห้องคนต่อไปลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖
set:addblacklist
บัญชีดำแบ็คลิสคนไม่ให้เข้ากลุ่มลงสั่งแล้วส่งข้อมูลคนที่เราจะแบ็คลิสลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖
set:addwhitelist
บัญชีขาวแก้ดำสั่งแล้วส่งข้อมูลคนที่เราจะแก้แบ๊คลิสลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖
Set:blockinvite:off  ปลดล็อกการเชิญ
➖➖➖➖➖➖➖➖➖➖➖➖➖
Set:blockinvite:on  ล็อกการเชิญ
➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:inviteurl        เปิดลิงค์
➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:DenyURLInvite    ปิดลิงค์
➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:cancelinvite  ยกเลิกค้างเชิญสั่ง2ครั้ง
➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:groupcreator เช็คแอดมินหลัก
➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:extracreator  เช็คแอดมินสำรอง
➖➖➖➖➖➖➖➖➖➖➖➖➖
set:changeextraowner เพิ่มแอดมินสำรอง
ลงคำสั่งแล้วส่งข้อมูลคนที่จะเป็นคนสำรองลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖
Set:turncreator ใช้สลับแอดมินได้
เมื่อแอดมินหลักไม่ว่าง ให้แอดมินสำรองทำหน้าที่แทนได้
➖➖➖➖➖➖➖➖➖➖➖➖➖
ดูคนอ่าน ใช้ 2คำสั่ง
สั่งเซ็ตเวลาตั้งค่าก่อน
แล้วค่อยสั่งเช็คอ่านคน

Setlastpoint     ตั้งค่า

Viewlastseen    เช็คอ่าน
➖➖➖➖➖➖➖➖➖➖➖➖➖

 ╔•═•-⊰❉⊱•═•⊰❉⊱•═•⊰❉⊱-•═•╗ 
 ║🌐 ✍️$ëcürîty❄️฿❂T✔Ľîη℮ 🌐║ 
 ╚•═•-⊰❉⊱•═•⊰❉⊱•═•⊰❉⊱-•═•╝
 
    ✍️รับติดตั้ง ฿❂Ŧ✔Sirichan v⒑
 Install Line Group Security Bots.
ระบบรักษาความปลอดภัยของกลุ่มไลน์
  🔘ลงบอทกลุ่มที่มีสมาชิก 200 บาท
  🔘กลุ่มบอท ชุด12ตัว  100 บาท
  🔘เพิ่มบอทเสริม ชุดล่ะ 100 บาท
  🔘ประกันกลุ่ม 50.- ช่วยดูแลแก้ไข
เปลี่ยนฟรีให้ลูกค้าเมื่อบอทขัดข้อง
  🔘ประกันกลุ่ม 90.- ✰✰✰✰✰
เมื่อกลุ่มโดนลบ  [เคลมให้ฟรี 1กลุ่ม]
เมื่อบอทขัดข้อง แก้ไขเปลี่ยนบอทฟรี
แถมบอทคำสั่ง ผู้ช่วยแอดมินเพิ่ม 1ตัว

          ✍️Pro.. ✰โปรโมชั่น✰✰
   🌐ติดตั้งบอทพร้อมประกัน 2 ชุด🌐
        (ฟรี)รับฟรีอีก 1 กลุ่มบอท(ฟรี)

   💡คุณสมบัติพิเศษของบอท v10💡
🔒ป้องกันสมาชิกเปิดลิงก์ห้อง
🔒ป้องกันสมาชิกเปลี่ยนรูปกลุ่ม
🔒ป้องกันสมาชิกเปลี่ยนชื่อกลุ่ม
🔒ป้องกันสมาชิกเชิญคนนอกเข้ากลุ่ม
🔒ป้องกันคนนอกเข้ามาลบคนในกลุ่ม 
🔒ห้ามลบสมาชิกในกลุ่ม นอกจากแอด
🔒ถ้าลบเกิน3คน บอทจะเตะออกทันที
📇สามารถเช็คคนที่แอบอ่านในกลุ่มได้

    ✫☆✰สนใจทักมาสอบถาม✰☆✫
🔽🔻🔽🔻🔽🔻🔽🔻🔽🔻🔽🔻🔽
http://line.me/ti/p/~security_botline
🔈🔉🔊ท่านที่เพิ่มเพื่อนเด้งแชทด้วยคับ
หากไม่ถูกใจบริการ ไม่ซื้อไม่เป็นไร
ยินดีให้คำแนะนำ พร้อมให้ทดลองบอท
อีกหนึ่งช่องทาง *ติดต่อเพิ่มเติมได้..↲
📲0639375811ติดต่อเรื่องงานเท่านั้น
✅รับเขียนบอทโต้ตอบ ✰Bot API✰
✅รับสร้างไลน์ส่วนตัว LINE ProGram
      แฮ๊กธีมไลน์ฟรีทุกธีม สนใจทัก
     ️📛ย้ำ แอดเพื่อน ควรเด้งแชท📛

──────┅═ই۝ई═┅──────
รับทำเชลบอทกันรัน  (บอทส่วนตัว)
สนใจติดต่อที่  ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ
🆔http://line.me/ti/p/~1ove..neverdie
နับთิஏთั้ଏบਹທ  Sirichan V⒑
📧https://line.me/R/ti/p/%40uvh1233u
──────┅═ই۝ई═┅──────
""")
#-------------------------------------------------
            elif msg.text == "xXx seed69":
                    cl.sendText(msg.to,"╔══╦═╦═╗\n║║║║║║║║\n║║║║╦║║║\n╚╩╩╩╩╩╩╝️  •─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n•┅═ই۝ई═┅•────────────────\nคลิปโป้มาแว๊วว เว็ปเดียว อิ่มจุใจ รวมคลิป จัดให้สายหื่น😍\nหนังเต็มเรื่อง คลิปสั้น คลิปหลุด หนังอาร์ ไทยจีนเกาหลี\nมีหมด ☛ https://www.seed69.com ☚")
#-------------------------------------------------
            elif msg.text == "xXx 18+":
                    cl.sendText(msg.to,"http://nekopoi.host")
                    cl.sendText(msg.to,"http://sexvideobokep.com")
                    cl.sendText(msg.to,"http://memek.com")
                    cl.sendText(msg.to,"http://pornktube.com")
                    cl.sendText(msg.to,"http://faketaxi.com")
                    cl.sendText(msg.to,"http://videojorok.com")
                    cl.sendText(msg.to,"http://watchmygf.mobi")
                    cl.sendText(msg.to,"http://xnxx.com")
                    cl.sendText(msg.to,"http://pornhd.com")
                    cl.sendText(msg.to,"http://xvideos.com")
                    cl.sendText(msg.to,"http://vidz7.com")
                    cl.sendText(msg.to,"http://m.xhamster.com")
                    cl.sendText(msg.to,"http://xxmovies.pro")
                    cl.sendText(msg.to,"http://youporn.com")
                    cl.sendText(msg.to,"http://pornhub.com")
                    cl.sendText(msg.to,"http://anyporn.com")
                    cl.sendText(msg.to,"http://hdsexdino.com")
                    cl.sendText(msg.to,"http://rubyourdick.com")
                    cl.sendText(msg.to,"http://anybunny.mobi")
                    cl.sendText(msg.to,"http://cliphunter.com")
                    cl.sendText(msg.to,"http://sexloving.net")
                    cl.sendText(msg.to,"http://free.goshow.tv")
                    cl.sendText(msg.to,"http://eporner.com")
                    cl.sendText(msg.to,"http://Pornhd.josex.net")
                    cl.sendText(msg.to,"http://m.hqporner.com")
                    cl.sendText(msg.to,"http://m.spankbang.com")
                    cl.sendText(msg.to,"http://m.4tube.com")
                    cl.sendText(msg.to,"http://brazzers.com")
#--------------------------------------------------
#==================================================
            elif msg.text in ["ยกเลิก"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting。")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["บอทยกเลิก"]:
                if msg.toType == 2:
                    klist=[kj,kh,kg,kf,ke,kd,kc,kk,ki,kn,ko,kp,kq,kr,ks,kt]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            kicker.sendText(msg.to,"No one is inviting")
                        else:
                            kicker.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        kicker.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kicker.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["#Link on"]:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"done")
                    else:
                        uye.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["M1 link on"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"done")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["#Link off"]:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"done")
                    else:
                        uye.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["M1 link off"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"done")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text.lower() == 'ginfo':
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
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n[Group Uid]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
            elif msg.text in ["!Glist","Myginfo"]:
                gs = cl.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")

            elif msg.text in ["S1glist"]:
                gs = ki.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki.getGroup(i).name + " | [ " + str(len (ki.getGroup(i).members)) + " ]")
                ki.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S2glist"]:
                gs = kk.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (kk.getGroup(i).name + " | [ " + str(len (kk.getGroup(i).members)) + " ]")
                kk.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S3glist"]:
                gs = kc.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (kc.getGroup(i).name + " | [ " + str(len (kc.getGroup(i).members)) + " ]")
                kc.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")

            elif msg.text in ["Selfbot"]:
				msg.contentType = 13
				msg.contentMetadata = {'mid': mid}
				cl.sendMessage(msg)
				cl.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
            elif "Id" == msg.text:
                key = msg.to
                cl.sendText(msg.to, key)
            elif "Mid bot" == msg.text:
		#	cl.sendText(msg.to,mid)
			ki.sendText(msg.to,Amid)
			kk.sendText(msg.to,Bmid)
			kc.sendText(msg.to,Cmid)
			kd.sendText(msg.to,Dmid)
			ke.sendText(msg.to,Emid)
			kf.sendText(msg.to,Fmid)
			kg.sendText(msg.to,Gmid)
			kh.sendText(msg.to,Hmid)
			kj.sendText(msg.to,Jmid)
			kl.sendText(msg.to,Lmid)
			km.sendText(msg.to,Mmid)
			kn.sendText(msg.to,Nmid)
			ko.sendText(msg.to,Omid)
			kp.sendText(msg.to,Pmid)
			kq.sendText(msg.to,Qmid)
			kr.sendText(msg.to,Rmid)
			ks.sendText(msg.to,Smid)
			kt.sendText(msg.to,Tmid)

            elif ("Hack: " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" + key1)

            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)

            elif "Helpbot" in msg.text:
                cl.sendText(msg.to,"""•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•
            ❇️ Key Only BOT ❇️
[Bot ?]
[My bot]
[Namebot]
[Mid bot]
[Bcancel]
[BotChat]
[Respons]
[Contact bot]
[Man1 - Man18]
[ลบรันบอท1-18]
[1Aditname: ]
[M1-M18]  in
[M1-M18]  bye
[M1-M5]  gift
[M1-M18]  rename: 
[Ban @]+[Kill-Kill ban]
[Conban] + [คท. ดำ]
[Cb] Clear blacklist
[Nk  @] + [Fuck  @]
[M1 kick - M9 kick  @]
 
 www.หรรมใหญ่โว้ย.com （´・ω・｀）
──────┅═ই۝ई═┅──────
နับთิஏთั้ଏบਹທV⒑ (รับทำเชลบอทกันรัน)
สนใจติดต่อที่  ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ
http://line.me/ti/p/~1ove..neverdie
──────┅═ই۝ई═┅──────""")

            elif msg.text in ["Ss"]:
                cl.sendText(msg.to,"既読ポイント設定")
            elif msg.text in ["Vv"]:
                cl.sendText(msg.to,"既読確認")
            elif msg.text in ["1/2"]:
                cl.sendText(msg.to,"設定:作者交換")
            elif msg.text in ["Setbot"]:
                cl.sendText(msg.to,"設定:確認")
            elif msg.text in ["@1"]:
                cl.sendText(msg.to,"Siri:グル作成者")
            elif msg.text in ["@2"]:
                cl.sendText(msg.to,"siri:予備作成者")
            elif msg.text in ["#on"]:
                cl.sendText(msg.to,"Siri:招待URL生成")
            elif msg.text in ["#off"]:
                cl.sendText(msg.to,"Siri:招待URL拒否")
            elif msg.text in ["Bb"]:
                cl.sendText(msg.to,"siri:再招待")
            elif msg.text in ["ตั๋ว"]:
                cl.sendText(msg.to,"Siri:招待回数")
            elif msg.text in ["WL"]:
                cl.sendText(msg.to,"設定:ホワイト追加")
            elif msg.text in ["BL"]:
                cl.sendText(msg.to,"設定:ブラック追加")
            elif msg.text in ["$$"]:
                cl.sendText(msg.to,"Siri:追加アカウント購入")
            elif msg.text in ["#1"]:
                cl.sendText(msg.to,"設定:グル作者変更")
            elif msg.text in ["#2"]:
                cl.sendText(msg.to,"設定:予備作者変更")
            elif msg.text in ["CL"]:
                cl.sendText(msg.to,"Siri:招待キャンセル")
            elif msg.text in ["ล็อกรันติ้ก"]:
                cl.sendText(msg.to,"設定:スタンプ規制:オン")
            elif msg.text in ["ล็อกชื่อกลุ่ม"]:
                cl.sendText(msg.to,"設定:グループ名ロック:オン")
            elif msg.text in ["ล็อกรูปกลุ่ม"]:
                cl.sendText(msg.to,"設定:アイコンロック:オン")
            elif msg.text in ["ล็อกแอด"]:
                cl.sendText(msg.to,"設定:作成者ロック:オン")
            elif msg.text in ["ล็อกการเชิญ"]:
                cl.sendText(msg.to,"設定:招待拒否:オン")
#-------------------------------------------------------------------
            elif msg.text in ["Setsiri","คำสั่งบอท","คำสั่งสิริ"]:
                cl.sendText(msg.to,"✯✯❇Thailand✯Creator❇✯✯\n•─ ͜͡✫ѕєʟғвот﴾ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅﴿κɪcκєʀ ͜͡✫─•\n╭════════╬♥╬════════╮\n║♞ตั้งแอดหลัก พิมพ์➣「#1」\n║♘ตั้งแอดรอง  พิมพ์➢「#2」\n║♜สลับแอด      พิมพ์➣「1/2」\n║♖เพิ่มบอทเสริม พิมพ์➢「$$」\n║♝เช็คตั๋วบอท   พิมพ์➣「ตั๋ว」\n║♗ล้างบัญชีดำ  พิมพ์➢「WL」\n║♚สร้างบัญชีดำ พิมพ์➣「BL」\n║♔เปิดลิงก์กลุ่ม พิมพ์➢「#on」\n║♛ปิดลิงก์กลุ่ม พิมพ์➣「#off」\n║♕เรียกบอทกลับ พิมพ์➢「Bb」\n║♟ตั้งเวลา        พิมพ์➣「Ss」\n║♙เช็คคนอ่าน  พิมพ์➢「Vv」\n║●ตั้งค่ากลุ่ม  พิมพ์➣ Setbot\n║○เช็คแอดหลัก พิมพ์➢「@1」\n║●เช็คแอดรอง  พิมพ์➢「@2」\n║○ยกเลิกค้างเชิญ พิมพ์➢「CL」\n╰════════╬♥╬════════╯\n╭════════╬♥╬════════╮\n║💡Sirichan v10  PROTECT💡\n║🔒 พิมพ์➢「ล็อกรันติ้ก」\n║🔒 พิมพ์➢「ล็อกชื่อกลุ่ม」\n║🔒 พิมพ์➢「ล็อกรูปกลุ่ม」\n║🔒 พิมพ์➢「ล็อกแอด」\n║🔒 พิมพ์➢「ล็อกการเชิญ」\n╰════════╬♥╬════════╯\n╭════════╬♥╬════════╮\nวิธีใช้คำสั่ง ให้พิมพ์อักษรย่อ「...」\n╰════════╬♥╬════════╯") 
#-------------------------------------------------------------------
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"(๑و•̀ω•́)و")
            elif msg.text.lower() == 'bcancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        ki.cancelGroupInvitation(msg.to,[_mid])
                    ki.sendText(msg.to,"I pretended to cancel and canceled\n •─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                    cl.sendText(msg.to,"(๑و•̀ω•́)و")

            elif "You @" in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("You @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                         pass

            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)			
            elif "M1 mid" == msg.text:
                ki.sendText(msg.to,Amid)
            elif "M2 mid" == msg.text:
                kk.sendText(msg.to,Bmid)
            elif "M3 mid" == msg.text:
                kc.sendText(msg.to,Cmid)

            elif msg.text == "กลุ่ม":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "ไม่พบผู้สร้างกลุ่ม"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                          u = "[ปิด]"
                        else:
                            u = "[เปิด]"
                        cl.sendText(msg.to,"[ชื่อของกลุ่ม]:\n" + str(ginfo.name) + "\n[Gid]:\n" + msg.to + "\n[ผู้สร้างกลุ่ม:]\n" + gCreator + "\n[ลิ้งค์รูปกลุ่ม]:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n[จำนวนสมาชิก]:" + str(len(ginfo.members)) + "คน\n[จำนวนค้างเชิญ]:" + sinvitee + "คน\n[สถานะลิ้งค์]:" + u + "URL \nBy : •─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                    else:
                        cl.sendText(msg.to,"Nama Gourp:\n" + str(ginfo.name) + "\nGid:\n" + msg.to + "\nCreator:\n" + gCreator + "\nProfile:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                         cl.sendText(msg.to,"Not for use less than group")
            elif "Bot?" in msg.text:
                ki.sendText(msg.to,"Bot 💀1💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                kk.sendText(msg.to,"Bot 💀2💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                kc.sendText(msg.to,"Bot 💀3💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                kd.sendText(msg.to,"Bot 💀4💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                ke.sendText(msg.to,"Bot 💀5💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                kf.sendText(msg.to,"Bot 💀6💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                kg.sendText(msg.to,"Bot 💀7💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                kh.sendText(msg.to,"Bot 💀8💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                kj.sendText(msg.to,"Bot 💀9💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                kl.sendText(msg.to,"Bot 💀10💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                km.sendText(msg.to,"Bot 💀11💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                kn.sendText(msg.to,"Bot 💀12💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                ko.sendText(msg.to,"Bot 💀13💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                kp.sendText(msg.to,"Bot 💀14💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                kq.sendText(msg.to,"Bot 💀15💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                kr.sendText(msg.to,"Bot 💀16💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                ks.sendText(msg.to,"Bot 💀17💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                kt.sendText(msg.to,"Bot 💀18💀 \n•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
            elif "Man say " in msg.text:
                                bctxt = msg.text.replace("Man say ","")
                                ki.sendText(msg.to,(bctxt))
                                kk.sendText(msg.to,(bctxt))
                                kc.sendText(msg.to,(bctxt))
                                kd.sendText(msg.to,(bctxt))
                                ke.sendText(msg.to,(bctxt))
                                kf.sendText(msg.to,(bctxt))
                                kg.sendText(msg.to,(bctxt))
                                kh.sendText(msg.to,(bctxt))
                                kj.sendText(msg.to,(bctxt))
                                kl.sendText(msg.to,(bctxt))
                                km.sendText(msg.to,(bctxt))
                                kn.sendText(msg.to,(bctxt))
                                ko.sendText(msg.to,(bctxt))
                                kp.sendText(msg.to,(bctxt))
                                kq.sendText(msg.to,(bctxt))
                                kr.sendText(msg.to,(bctxt))
                                ks.sendText(msg.to,(bctxt))
                                kt.sendText(msg.to,(bctxt))

            elif "Tl: " in msg.text:
                tl_text = msg.text.replace("Tl: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "M1 tl: " in msg.text:
                tl_text = msg.text.replace("M1 tl: ","")
                ki.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+ki.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "M2 tl: " in msg.text:
                tl_text = msg.text.replace("M2 tl: ","")
                kk.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+kk.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Protect:on","Protect on"]:
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Qr:off","Qr off"]:
                if wait["qr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Qr:on","Qr on"]:
                if wait["qr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Protect:off","Protect off"]:
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Namelock:on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Done..")
                else:
                    cl.sendText(msg.to,"bone..")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Done..")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"bone..")
#---------------------------------------------
            elif "Blockinvite:on" == msg.text:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"Done..")
            elif "Blockinvite:off" == msg.text:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"Done..")
				except:
					pass
            elif "Cn: " in msg.text:
                string = msg.text.replace("Cn: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif msg.text in ["invite on"]:
                if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif "M1 rename: " in msg.text:
                string = msg.text.replace("M1 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M2 rename: " in msg.text:
                string = msg.text.replace("M2 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M3 rename: " in msg.text:
                string = msg.text.replace("M3 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kc.getProfile()
                    profile_B.displayName = string
                    kc.updateProfile(profile_B)
                    kc.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M4 rename: " in msg.text:
                string = msg.text.replace("M4 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kd.getProfile()
                    profile_B.displayName = string
                    kd.updateProfile(profile_B)
                    kd.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M5 rename: " in msg.text:
                string = msg.text.replace("M5 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ke.getProfile()
                    profile_B.displayName = string
                    ke.updateProfile(profile_B)
                    ke.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M6 rename: " in msg.text:
                string = msg.text.replace("M6 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kf.getProfile()
                    profile_B.displayName = string
                    kf.updateProfile(profile_B)
                    kf.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M7 rename: " in msg.text:
                string = msg.text.replace("M7 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kg.getProfile()
                    profile_B.displayName = string
                    kg.updateProfile(profile_B)
                    kg.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M8 rename: " in msg.text:
                string = msg.text.replace("M8 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kh.getProfile()
                    profile_B.displayName = string
                    kh.updateProfile(profile_B)
                    kh.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M9 rename: " in msg.text:
                string = msg.text.replace("M9 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kj.getProfile()
                    profile_B.displayName = string
                    kj.updateProfile(profile_B)
                    kj.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M10 rename: " in msg.text:
                string = msg.text.replace("M10 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kl.getProfile()
                    profile_B.displayName = string
                    kl.updateProfile(profile_B)
                    kl.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M11 rename: " in msg.text:
                string = msg.text.replace("M11 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = km.getProfile()
                    profile_B.displayName = string
                    km.updateProfile(profile_B)
                    km.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M12 rename: " in msg.text:
                string = msg.text.replace("M12 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kn.getProfile()
                    profile_B.displayName = string
                    kn.updateProfile(profile_B)
                    kn.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M13 rename: " in msg.text:
                string = msg.text.replace("M13 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ko.getProfile()
                    profile_B.displayName = string
                    ko.updateProfile(profile_B)
                    ko.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M14 rename: " in msg.text:
                string = msg.text.replace("M14 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kp.getProfile()
                    profile_B.displayName = string
                    kp.updateProfile(profile_B)
                    kp.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M15 rename: " in msg.text:
                string = msg.text.replace("M15 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kq.getProfile()
                    profile_B.displayName = string
                    kq.updateProfile(profile_B)
                    kq.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M16 rename: " in msg.text:
                string = msg.text.replace("M16 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kr.getProfile()
                    profile_B.displayName = string
                    kr.updateProfile(profile_B)
                    kr.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M17 rename: " in msg.text:
                string = msg.text.replace("M17 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ks.getProfile()
                    profile_B.displayName = string
                    ks.updateProfile(profile_B)
                    ks.sendText(msg.to,"Name " + string + " Updated Name")
            elif "M18 rename: " in msg.text:
                string = msg.text.replace("M18 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kt.getProfile()
                    profile_B.displayName = string
                    kt.updateProfile(profile_B)
                    kt.sendText(msg.to,"Name " + string + " Updated Name")
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
                kc.sendMessage(msg)
                kd.sendMessage(msg)
                ke.sendMessage(msg)
                kf.sendMessage(msg)
                kg.sendMessage(msg)
                kh.sendMessage(msg)
                kj.sendMessage(msg)
                kl.sendMessage(msg)
                km.sendMessage(msg)
                kn.sendMessage(msg)
                ko.sendMessage(msg)
                kp.sendMessage(msg)
                kq.sendMessage(msg)
                kr.sendMessage(msg)
                ks.sendMessage(msg)
                kt.sendMessage(msg)
            elif msg.text in ["K on","Contact:on","Contact on","K:on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Boss")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Boss")
            elif msg.text in ["contact v"]:
                if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif msg.text in ["K:off","Contact:off","Contact off","K off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Boss")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Boss")

            elif msg.text in ["Auto join on","Join on","Join:on","Auto join:on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Boss")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
            elif msg.text in ["Join off","Auto join off","Auto join:off","Join:off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Boss")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Boss")

            elif "Gcancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + " The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")

            elif msg.text in ["Leave:on","Auto leave on","Auto leave:on","Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done👀")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Leave:off","Auto leave off","Auto leave:off","Leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already 👀")

            elif msg.text in ["共有:オン","Share on","Share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["共有:オフ","Share off","Share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done👀")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done👀")
                    else:
                        cl.sendText(msg.to,"要了关断。")
            elif msg.text in ["Auto like:on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。👀")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。👀")
            elif msg.text in ["Like off","Auto like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。👀")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already. 👀")

            elif msg.text in ["Sett","Setting"]:
                print "Setting pick up..."
                md = "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n\n"
                if wait["likeOn"] == True: md+="􀜁􀇔􏿿 Auto like : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Auto like : off 􀜁􀄰􏿿\n"
#                if wait["copy"] == True: md+="�� Mimic : on\n"
#                else:md+=" �� Mimic : off\n"
                if wait["winvite"] == True: md+="􀜁􀇔􏿿 Invite : on  􏿿\n"
                else:md+="􀜁􀇔􏿿 Invite : off 􀜁􀄰􏿿\n"
                if wait["pname"] == True: md+="􀜁􀇔􏿿 Namelock : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Namelock : off 􀜁􀄰􏿿\n"
                if wait["contact"] == True: md+="􀜁􀇔􏿿 Contact : on 􀜁􀄯􏿿\n"
                else: md+="􀜁􀇔􏿿 Contact : off 􀜁􀄰􏿿\n"
                if wait["autoJoin"] == True: md+="􀜁􀇔􏿿 Auto join : on 􀜁􀄯􏿿\n"
                else: md +="􀜁􀇔􏿿 Auto join : off 􀜁􀄰􏿿\n"
                if wait["autoCancel"]["on"] == True:md+="􀜁􀇔􏿿 Group cancel :" + str(wait["autoCancel"]["members"]) + " 􀜁􀄯􏿿\n"
                else: md+= "􀜁􀇔􏿿 Group cancel : off 􀜁􀄰􏿿\n"
                if wait["leaveRoom"] == True: md+="􀜁􀇔􏿿 Auto leave : on 􀜁􀄯􏿿\n"
                else: md+="􀜁􀇔􏿿 Auto leave : off 􀜁􀄰􏿿\n"
                if wait["timeline"] == True: md+="􀜁􀇔􏿿 Share : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Share : off 􀜁􀄰􏿿\n"
                if wait["clock"] == True: md+="􀜁􀇔􏿿 Clock Name : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Clock Name : off 􀜁􀄰􏿿\n"
                if wait["autoAdd"] == True: md+="􀜁􀇔􏿿 Auto add : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Auto add : off 􀜁􀄰􏿿\n"
                if wait["commentOn"] == True: md+="􀜁􀇔􏿿 Comment : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Comment : off 􀜁􀄰􏿿\n"
                if wait["Backup"] == True: md+="􀜁􀇔􏿿 Backup : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Backup : off 􀜁􀄰􏿿\n"
                if wait["qr"] == True: md+="􀜁􀇔􏿿 Protect QR : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Protect QR : off 􀜁􀄰􏿿\n"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
		
            elif msg.text in ["Set","Man set"]:
                print "Setting pick up..."
                md = "✯❇️[C̶̲̅ᴏ̶̲̅ᴍ̶̲̅ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅ᴅ̶̲̅ ̶̲̅S̶̲̅E̶̲̅T̶̲̅T̶̲̅I̶̲̅N̶̲̅G̶̲̅s̶̲̅]❇️✯\n─────┅═ই۝ई═┅─────\n"
                if wait["likeOn"] == True: md+="✔ Auto like : on \n"
                else:md+="❎ Auto like : off \n"
#                if wait["copy"] == True: md+="�� Mimic : on\n"
#                else:md+=" �� Mimic : off\n"
                if wait["winvite"] == True: md+="✔ Invite : on \n"
                else:md+="❎ Invite : off \n"
                if wait["pname"] == True: md+="✔ Namelock : on \n"
                else:md+="❎ Namelock : off \n"
                if wait["contact"] == True: md+="✔ Contact : on \n"
                else: md+="❎ Contact : off \n"
                if wait["autoJoin"] == True: md+="✔ Auto join : on \n"
                else: md+="❎ Auto join : off \n"
                if wait["autoCancel"]["on"] == True:md+="❇️ Group cancel :" + str(wait["autoCancel"]["members"]) + " ⭕\n"
                else: md+="❎ Group cancel : off \n"
                if wait["leaveRoom"] == True: md+="✔ Auto leave : on \n"
                else: md+="❎ Auto leave : off \n"
                if wait["timeline"] == True: md+="✔ Share : on \n"
                else:md+="❎ Share : off \n"
                if wait["clock"] == True: md+="✔ Clock Name : on\n"
                else:md+="❎ Clock Name : off \n"
                if wait["autoAdd"] == True: md+="✔ Auto add : on \n"
                else:md+="❎ Auto add : off \n"
                if wait["commentOn"] == True: md+="✔ Comment : on \n"
                else:md+="❎ Comment : off \n"
                if wait["Backup"] == True: md+="✔ Backup : on \n"
                else:md+="❎ Backup : off \n"
                if wait["qr"] == True: md+="✔ Protect QR : on \n"
                else:md+="❎ Protect QR : off \n"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
#------------------------------------------------
            elif msg.text in ["Gcreator:inv","เชิญเเอทมิน"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
#-----------------------------------------------
            elif msg.text in ["Backup:on","Backup on","เปิดการเชิญกลับ"]:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Sudah on Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Backup:off","Backup off","ปิดการเชิญกลับ"]:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Sudah off Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Reject","ลบรัน"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Semua Spam Undangan Telah Di Tolak")
                else:
                    cl.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject1","ลบรันบอท1"]:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"Bot All invitations is clean")
                else:
                    ki.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject2","ลบรันบอท2"]:
                gid = kk.getGroupIdsInvited()
                for i in gid:
                    kk.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kk.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kk.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject3","ลบรันบอท3"]:
                gid = kc.getGroupIdsInvited()
                for i in gid:
                    kc.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kc.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kc.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject4","ลบรันบอท4"]:
                gid = kd.getGroupIdsInvited()
                for i in gid:
                    kd.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kd.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kd.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject5","ลบรันบอท5"]:
                gid = ke.getGroupIdsInvited()
                for i in gid:
                    ke.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ke.sendText(msg.to,"Bot All invitations is clean")
                else:
                    ke.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject6","ลบรันบอท6"]:
                gid = kf.getGroupIdsInvited()
                for i in gid:
                    kf.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kf.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kf.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject7","ลบรันบอท7"]:
                gid = kg.getGroupIdsInvited()
                for i in gid:
                    kg.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kg.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kg.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject8","ลบรันบอท8"]:
                gid = kh.getGroupIdsInvited()
                for i in gid:
                    kh.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kh.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kh.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject9","ลบรันบอท9"]:
                gid = kj.getGroupIdsInvited()
                for i in gid:
                    kj.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kj.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kj.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject10","ลบรันบอท10"]:
                gid = kl.getGroupIdsInvited()
                for i in gid:
                    kl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kl.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kl.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject11","ลบรันบอท11"]:
                gid = km.getGroupIdsInvited()
                for i in gid:
                    km.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    km.sendText(msg.to,"Bot All invitations is clean")
                else:
                    km.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject12","ลบรันบอท12"]:
                gid = kn.getGroupIdsInvited()
                for i in gid:
                    kn.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kn.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kn.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject13","ลบรันบอท13"]:
                gid = ko.getGroupIdsInvited()
                for i in gid:
                    ko.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ko.sendText(msg.to,"Bot All invitations is clean")
                else:
                    ko.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject14","ลบรันบอท14"]:
                gid = kp.getGroupIdsInvited()
                for i in gid:
                    kp.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kp.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kp.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject15","ลบรันบอท15"]:
                gid = kq.getGroupIdsInvited()
                for i in gid:
                    kq.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kq.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kq.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject16","ลบรันบอท16"]:
                gid = kr.getGroupIdsInvited()
                for i in gid:
                    kr.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kr.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject17","ลบรันบอท17"]:
                gid = ks.getGroupIdsInvited()
                for i in gid:
                    ks.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ks.sendText(msg.to,"Bot All invitations is clean")
                else:
                    ks.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Reject18","ลบรันบอท18"]:
                gid = kt.getGroupIdsInvited()
                for i in gid:
                    kt.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kt.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kt.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Add:on","Auto add on","Auto add:on","Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ok Bosqu")
                    else:
                        cl.sendText(msg.to,"Sudah on Bosqu")
            elif msg.text in ["Add:off","Auto add off","Auto add:off","Add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ok Bosqu")
                    else:
                        cl.sendText(msg.to,"Sudah off Bosqu")
#========================================
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"message changed\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Add message: " in msg.text:
                wait["message"] = msg.text.replace("Add message: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"done。\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Message","Com"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["message"])
            elif "Coms set:" in msg.text:
                c = msg.text.replace("Coms set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment: " in msg.text:
                c = msg.text.replace("Add comment: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)

            elif msg.text in ["Com on","Comment:on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Com off","Comment:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Comment","Coms"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        uye.updateGroup(x)
                    gurl = uye.reissueGroupTicket(msg.to)
                    uye.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
#===========================================
            elif msg.text.lower() == 'namebot':
                profile = ki.getProfile()
                text = profile.displayName + "🇹🇭"
                ki.sendText(msg.to, text)
                profile = kk.getProfile()
                text = profile.displayName + "🇹🇭"
                kk.sendText(msg.to, text)
                profile = kc.getProfile()
                text = profile.displayName + "🇹🇭"
                kc.sendText(msg.to, text)
                profile = kd.getProfile()
                text = profile.displayName + "🇹🇭"
                kd.sendText(msg.to, text)
                profile = ke.getProfile()
                text = profile.displayName + "🇹🇭"
                ke.sendText(msg.to, text)
                profile = kf.getProfile()
                text = profile.displayName + "🇹🇭"
                kf.sendText(msg.to, text)
                profile = kg.getProfile()
                text = profile.displayName + "🇹🇭"
                kg.sendText(msg.to, text)
                profile = kh.getProfile()
                text = profile.displayName + "🇹🇭"
                kh.sendText(msg.to, text)
                profile = kj.getProfile()
                text = profile.displayName + "🇹🇭"
                kj.sendText(msg.to, text)
                profile = kl.getProfile()
                text = profile.displayName + "🇹🇭"
                kl.sendText(msg.to, text)
                profile = km.getProfile()
                text = profile.displayName + "🇹🇭"
                km.sendText(msg.to, text)
                profile = kn.getProfile()
                text = profile.displayName + "🇹🇭"
                kn.sendText(msg.to, text)
                profile = ko.getProfile()
                text = profile.displayName + "🇹🇭"
                ko.sendText(msg.to, text)
                profile = kp.getProfile()
                text = profile.displayName + "🇹🇭"
                kp.sendText(msg.to, text)
                profile = kq.getProfile()
                text = profile.displayName + "🇹🇭"
                kq.sendText(msg.to, text)
                profile = kr.getProfile()
                text = profile.displayName + "🇹🇭"
                kr.sendText(msg.to, text)
                profile = ks.getProfile()
                text = profile.displayName + "🇹🇭"
                ks.sendText(msg.to, text)
                profile = kt.getProfile()
                text = profile.displayName + "🇹🇭"
                kt.sendText(msg.to, text)
            elif "Ambil QR: " in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("Ambil QR: ","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Not for use less than group")
            elif "M1 url" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("M1 url","")
                    x = ki.getGroup(gid)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(gid)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    ki.sendText(msg.to,"Not for use less than group")
            elif "M2 url" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("M2 url","")
                    x = kk.getGroup(gid)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(gid)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    kk.sendText(msg.to,"Not for use less than group")
#========================================
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist s")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)

            elif msg.text in ["Clock:on","Clock on","Jam on","Jam:on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"༺%H:%M༻")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")

            elif msg.text in ["Clock:off","Clock off","Jam off","Jam:off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")

            elif "Cc: " in msg.text:
                n = msg.text.replace("Cc: ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Changed to:\n\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"༺%H:%M༻")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Refresh to update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")
#========================================
            elif "Hack cover @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Hack cover @","")
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
            elif "Hack-mid:" in msg.text:
                umid = msg.text.replace("Hack-mid:","")
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
            elif "Hack pic " in msg.text:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Hack pic ","")
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
                        cl.sendText(msg.to,"Gak da orange")
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
#===============================================
            elif msg.text in ["!sp","sp"]:
                cl.sendText(msg.to, "Progress...")
                start = time.time()
                time.sleep(0.9)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
                print "[Command]Speed palsu executed"
            elif msg.text in ["Speeed"]:
                cl.sendText(msg.to, "Progress...")
                start = time.time()
                time.sleep(0.06)
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kk.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kc.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kd.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ke.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kf.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kg.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kh.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kj.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kl.sendText(msg.to, "%sseconds" % (elapsed_time))    
                km.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kn.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ko.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kp.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kq.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kr.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ks.sendText(msg.to, "%sseconds" % (elapsed_time))    
                kt.sendText(msg.to, "%sseconds" % (elapsed_time))    
                print "[Command]Speed palsu executed"

            elif msg.text in ["Protect help"]:
                cl.sendText(msg.to, "Conmend  [PROTECT] \n❂͜͡☆➣ Protect on/off \n❂͜͡☆➣ Protect:on\off \n❂͜͡☆➣ Qr on/off \n❂͜͡☆➣ Qr:on/off \n❂͜͡☆➣ Blockinvite:on/off \n❂͜͡☆➣ Block url on/off \n❂͜͡☆➣ Block url:on/off \n❂͜͡☆➣ Backup on/off\n\nBy.•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
#========================================
            elif msg.text in ["Botbb"]:
                try:
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    kk.updateDisplayPicture(backup.pictureStatus)
                    kk.updateProfile(backup)
                    kc.updateDisplayPicture(backup.pictureStatus)
                    kc.updateProfile(backup)
                    kd.updateDisplayPicture(backup.pictureStatus)
                    kd.updateProfile(backup)
                    ke.updateDisplayPicture(backup.pictureStatus)
                    ke.updateProfile(backup)
                    kf.updateDisplayPicture(backup.pictureStatus)
                    kf.updateProfile(backup)
                    kg.updateDisplayPicture(backup.pictureStatus)
                    kg.updateProfile(backup)
                    kh.updateDisplayPicture(backup.pictureStatus)
                    kh.updateProfile(backup)
                    kj.updateDisplayPicture(backup.pictureStatus)
                    kj.updateProfile(backup)
                    kl.updateDisplayPicture(backup.pictureStatus)
                    kl.updateProfile(backup)
                    km.updateDisplayPicture(backup.pictureStatus)
                    km.updateProfile(backup)
                    kn.updateDisplayPicture(backup.pictureStatus)
                    kn.updateProfile(backup)
                    ko.updateDisplayPicture(backup.pictureStatus)
                    ko.updateProfile(backup)
                    kp.updateDisplayPicture(backup.pictureStatus)
                    kp.updateProfile(backup)
                    kq.updateDisplayPicture(backup.pictureStatus)
                    kq.updateProfile(backup)
                    kr.updateDisplayPicture(backup.pictureStatus)
                    kr.updateProfile(backup)
                    ks.updateDisplayPicture(backup.pictureStatus)
                    ks.updateProfile(backup)
                    kt.updateDisplayPicture(backup.pictureStatus)
                    kt.updateProfile(backup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
#----------------------------------------------
            elif "Botcopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Botcopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki.cloneContactProfile(target)
                                    kk.cloneContactProfile(target)
                                    kc.cloneContactProfile(target)
                                    kd.cloneContactProfile(target)
                                    ke.cloneContactProfile(target)
                                    kf.cloneContactProfile(target)
                                    kg.cloneContactProfile(target)
                                    kh.cloneContactProfile(target)
                                    kj.cloneContactProfile(target)
                                    kl.cloneContactProfile(target)
                                    km.cloneContactProfile(target)
                                    kn.cloneContactProfile(target)
                                    ko.cloneContactProfile(target)
                                    kp.cloneContactProfile(target)
                                    kq.cloneContactProfile(target)
                                    kr.cloneContactProfile(target)
                                    ks.cloneContactProfile(target)
                                    kt.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Copy Profile")
                                except Exception as e:
                                    print e
#===============================================
            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Copy Profile")
                                except Exception as e:
                                    print e
#=================================================
            elif msg.text in ["Mybb"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#=================================================
            elif "Man copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Man copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Copied.")
                            except Exception as e:
			        print e
            elif "Copy all @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy all @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Copy All Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.CloneContactProfile(target)
                                    ki.CloneContactProfile(target)
                                    kk.CloneContactProfile(target)
                                    kc.CloneContactProfile(target)
                                    kd.CloneContactProfile(target)
                                    ke.CloneContactProfile(target)
                                    kf.CloneContactProfile(target)
                                    kg.CloneContactProfile(target)
                                    kh.CloneContactProfile(target)
                                    kj.CloneContactProfile(target)
                                    kl.CloneContactProfile(target)
                                    km.CloneContactProfile(target)
                                    kn.CloneContactProfile(target)
                                    ko.CloneContactProfile(target)
                                    kp.CloneContactProfile(target)
                                    kq.CloneContactProfile(target)
                                    kr.CloneContactProfile(target)
                                    ks.CloneContactProfile(target)
                                    kt.CloneContactProfile(target)
                                    cl.sendText(msg.to, "Copy ALL Profile BY selfbot-man")
                                except Exception as e:
                                    print e
            elif msg.text in ["Bot backup"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    kk.updateDisplayPicture(backup.pictureStatus)
                    kk.updateProfile(backup)
                    kc.updateDisplayPicture(backup.pictureStatus)
                    kc.updateProfile(backup)
                    kd.updateDisplayPicture(backup.pictureStatus)
                    kd.updateProfile(backup)
                    ke.updateDisplayPicture(backup.pictureStatus)
                    ke.updateProfile(backup)
                    kf.updateDisplayPicture(backup.pictureStatus)
                    kf.updateProfile(backup)
                    kg.updateDisplayPicture(backup.pictureStatus)
                    kg.updateProfile(backup)
                    kh.updateDisplayPicture(backup.pictureStatus)
                    kh.updateProfile(backup)
                    kj.updateDisplayPicture(backup.pictureStatus)
                    kj.updateProfile(backup)
                    kl.updateDisplayPicture(backup.pictureStatus)
                    kl.updateProfile(backup)
                    km.updateDisplayPicture(backup.pictureStatus)
                    km.updateProfile(backup)
                    kn.updateDisplayPicture(backup.pictureStatus)
                    kn.updateProfile(backup)
                    ko.updateDisplayPicture(backup.pictureStatus)
                    ko.updateProfile(backup)
                    kp.updateDisplayPicture(backup.pictureStatus)
                    kp.updateProfile(backup)
                    kq.updateDisplayPicture(backup.pictureStatus)
                    kq.updateProfile(backup)
                    kr.updateDisplayPicture(backup.pictureStatus)
                    kr.updateProfile(backup)
                    ks.updateDisplayPicture(backup.pictureStatus)
                    ks.updateProfile(backup)
                    kt.updateDisplayPicture(backup.pictureStatus)
                    kt.updateProfile(backup)
                    cl.sendText(msg.to, "Backup Profile by Selfbot MAN")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#===============================================
            elif msg.text == "แอบ":
                    cl.sendText(msg.to, "มีใครอยู่ไหม…… !?")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('📅%d-%m-%Y ⏰%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "อ่าน":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "=======『✰$ëlf☠️฿❂T☠️️ℳѦれ✰』\n📇ตรวจสอบรายชื่อ.. [สมาชิกอ่านกลุ่ม]\n %s\n\n\n==============================\n☛Checklist Members Read Chat Groups\n==============================\n%s\n\n☛ Update the latest time♪\n〖%s〗\nby ✍️$ëlf☠️฿❂Ŧ☠️️ℳѦれ☆۰۪۫======="  %(wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "╔═════════════════%s\n╠═════════════════\n%s╠═════════════════\n║Readig point creation:\n║ [%s]\n╚══════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
#========================================
#---------------FUNGSI RATAIN GRUP TANPA KICK SESAMA BOT/Admin/Bots----------#
            elif "Kickall" in msg.text:
              if msg.from_ in Bots:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Kickall","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    ki.sendText(msg.to,"🔸We come to destroy your group🔸")
                    kk.sendText(msg.to,"Relax slow slow no baper...😂😂")
                    kc.sendText(msg.to,"Kenapa diem aja..??")
                    ks.sendText(msg.to,"Tangkis Bego Jangan Gemeter...😂😂")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    ks.sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots:
                            try:
                                klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,km,kn,ko,kp,kq,kr,ks,kt,cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                kl.sendText(msg.to,"H")
                                km.sendText(msg.to,"A")
                                kl.sendText(msg.to,"L")
                                km.sendText(msg.to,"O")
#================================================
            elif msg.text.lower() == 'wc':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
#================================================
            elif msg.text.lower() == 'hi':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Hello, Admin and group members " + str(ginfo.name))
                cl.sendText(msg.to,"สวัสดีกลุ่ม" + str(ginfo.name) + "\nสอบถามเรื่องบอท ทักได้ เพจใหม่! : มีครบทุกฟังชั่น\n•บอทป้องกัน\n•บอทบิน\n•บอทแท๊ก\n•บอทกันรัน และ ล้างรัน\n✯✯❇Thailand✯Creator❇✯✯\n•─ ͜͡✫ѕєʟғвот﴾ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅﴿κɪcκєʀ ͜͡✫─•\nhttps://line.me/R/ti/p/%40uvh1233u "+ ginfo.creator.displayName )
#================================================
#------------------Fungsi spam start--------------------
            elif "Spam change: " in msg.text:
                wait["spam"] = msg.text.replace("Spam change: ","")
                cl.sendText(msg.to,"spam changed")

            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")

            elif "Spam: " in msg.text:
                strnum = msg.text.replace("Spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])

#------------------Fungsi spam finish--------------------

#-----------------------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#===============================================
            elif "Spam " in msg.text:
                if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   #Keke cantik <3
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Out of range! ")
#-------------------------------------------------
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#-------------------------------------------------
            elif "Cbroadcast " in msg.text:
					bctxt = msg.text.replace("Cbroadcast ", "ประกาศแชท")
					t = cl.getAllContactIds()
					for manusia in t:
						cl.sendText(manusia,(bctxt))
            elif "Gbroadcast " in msg.text:
                                        bctxt = msg.text.replace("Gbroadcast ", "ประกาศกลุ่ม")
					n = cl.getGroupIdsJoined()
					for manusia in n:
						cl.sendText(manusia,(bctxt))
#---------------------------------------------------
            elif msg.text in ["บอท","แมน"]:
                msg.contentType = 13
                cl.sendText(msg.to, "สอบถามเรื่องบอท หรือปรึกษาเรื่องเชลบอทกันรัน ทักแชทได้ครับ")
                cl.sendText(msg.to, "✯✯❇Thailand✯Creator❇✯✯")
                msg.contentMetadata = {'mid': 'ud24af63fd62d14c3bf8f719df80c3745'}
                cl.sendMessage(msg)
#---------------------------------------------------
            elif msg.text in ["Man. All","Kicker","มาหำ","บอทเข้า"]:
                                        G = cl.getGroup(msg.to)
                                        info = cl.getGroup(msg.to)
                                        G.preventJoinByTicket = False
                                        cl.updateGroup(G)
                                        invsend = 0 
                                        Ticket = cl.reissueGroupTicket(msg.to)
                                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kk.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kc.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kd.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					ke.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kf.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kg.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kh.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
                                        kj.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kl.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					km.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kn.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					ko.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kp.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kq.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kr.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
                                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kt.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
                                        G = cl.getGroup(msg.to)
					G.preventJoinByTicket = True
					cl.updateGroup(G)
					print "All_Kickers_Ok!"
					G.preventJoinByTicket(G)
					cl.updateGroup(G)
#----------------------------------------------------------
            elif msg.text in ["Y1 join","M1 in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  print "Kicker2_Ok!"
                  Ticket = ki.reissueGroupTicket(msg.to)
	    elif msg.text in ["Y2 join","M2 in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  print "Kicker2_Ok!"
                  Ticket = kk.reissueGroupTicket(msg.to)
	    elif msg.text in ["Y3 join","M3 in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kc.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kc.updateGroup(G)
                  print "Kicker2_Ok!"
                  Ticket = kc.reissueGroupTicket(msg.to)
	    elif msg.text in ["Y4 join","M4 in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kd.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kd.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kd.updateGroup(G)
                  print "Kicker2_Ok!"
                  Ticket = kd.reissueGroupTicket(msg.to)
	    elif msg.text in ["Y5 join","M5 in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ke.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ke.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ke.updateGroup(G)
                  print "Kicker2_Ok!"
                  Ticket = ke.reissueGroupTicket(msg.to)
	    elif msg.text in ["Y6 join","M6 in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kf.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kf.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kf.updateGroup(G)
                  print "Kicker2_Ok!"
                  Ticket = kf.reissueGroupTicket(msg.to)
	    elif msg.text in ["Y7 join","M7 in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kg.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kg.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kg.updateGroup(G)
                  print "Kicker2_Ok!"
                  Ticket = kg.reissueGroupTicket(msg.to)
	    elif msg.text in ["Y8 join","M8 in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kh.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kh.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kh.updateGroup(G)
                  print "Kicker2_Ok!"
                  Ticket = kh.reissueGroupTicket(msg.to)
	    elif msg.text in ["Y9 join","M9 in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kj.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kj.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kj.updateGroup(G)
                  print "Kicker2_Ok!"
                  Ticket = kj.reissueGroupTicket(msg.to)
	    elif msg.text in ["Y10 join","M10 in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kl.updateGroup(G)
                  print "Kicker2_Ok!"
                  Ticket = kl.reissueGroupTicket(msg.to)
#----------------------------------------------------------------
            elif msg.text in ["Go1"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  kd.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  ke.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  G = ke.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ke.updateGroup(G)
                  print "Algojo_Ready!"
                  Ticket = ke.reissueGroupTicket(msg.to)
            elif msg.text in ["Go2"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kf.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  kg.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  kh.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  kj.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  kl.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  G = kl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kl.updateGroup(G)
                  print "Algojo_Ready!"
                  Ticket = kl.reissueGroupTicket(msg.to)
            elif msg.text in ["Go3"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  km.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  kn.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  ko.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  kp.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  kq.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  kr.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  kt.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.00)
                  G = kt.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kt.updateGroup(G)
                  print "Algojo_Ready!"
                  Ticket = kt.reissueGroupTicket(msg.to)
            elif msg.text in ["บอทออกทั้งหมด","บอทออกทุกกลุ่ม"]:
				gid = ki.getGroupIdsJoined()
				gid = kk.getGroupIdsJoined()
				gid = kc.getGroupIdsJoined()
				gid = kd.getGroupIdsJoined()
				gid = ke.getGroupIdsJoined()
				gid = kf.getGroupIdsJoined()
				gid = kg.getGroupIdsJoined()
				gid = kh.getGroupIdsJoined()
				gid = kj.getGroupIdsJoined()
				gid = kl.getGroupIdsJoined()
				gid = km.getGroupIdsJoined()
				gid = kn.getGroupIdsJoined()
				gid = ko.getGroupIdsJoined()
				gid = kp.getGroupIdsJoined()
				gid = kq.getGroupIdsJoined()
				gid = kr.getGroupIdsJoined()
                                gid = ks.getGroupIdsJoined()
				gid = kt.getGroupIdsJoined()
				for i in gid:
					ki.leaveGroup(i)
					kk.leaveGroup(i)
					kc.leaveGroup(i)
					kd.leaveGroup(i)
					ke.leaveGroup(i)
					kf.leaveGroup(i)
					kg.leaveGroup(i)
					kh.leaveGroup(i)
					kj.leaveGroup(i)
					kl.leaveGroup(i)
					km.leaveGroup(i)
					kn.leaveGroup(i)
					ko.leaveGroup(i)
					kp.leaveGroup(i)
					kq.leaveGroup(i)
					kr.leaveGroup(i)
                                        ks.leaveGroup(i)
					kt.leaveGroup(i)
                                if wait["lang"] == "JP":
					ki.sendText(msg.to,"รบกวนค้างเชิญไว้หน่อยน่ะ ขอออกกลุ่มชั่วคราว จะทำการซิงค์ข้อมูลไลน์ ล็อกอินใหม่\n\nTHANK FRO ADMIN GROUP😊")
				else:
					ki.sendText(msg.to,"He declined all invitations")
            elif msg.text in ["Man. Bye","@bye","Bye"]:
                if msg.toType == 2:
                   ginfo = cl.getGroup(msg.to)
                try:
                     ki.sendText(msg.to,"โดนไล่อีกแล้ว..ไปก็ได้😢\n👋😭 Bye~bye.. "  +  str(ginfo.name)  + "")
                     ki.leaveGroup(msg.to)
                     kk.leaveGroup(msg.to)
                     kc.leaveGroup(msg.to)
                     kd.leaveGroup(msg.to)
                     ke.leaveGroup(msg.to)
                     kf.leaveGroup(msg.to)
                     kg.leaveGroup(msg.to)
                     kh.leaveGroup(msg.to)
                     kj.leaveGroup(msg.to)
                     kl.leaveGroup(msg.to)
                     km.leaveGroup(msg.to)
                     kn.leaveGroup(msg.to)
                     ko.leaveGroup(msg.to)
                     kp.leaveGroup(msg.to)
                     kq.leaveGroup(msg.to)
                     kr.leaveGroup(msg.to)
                     ks.leaveGroup(msg.to)
                     kt.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y1 @bye","Y1 pulang","M1 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     ki.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y2 @bye","Y2 pulang","M2 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kk.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y3 @bye","Y3 pulang","M3 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kc.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y4 @bye","Y4 pulang","M4 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kd.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y5 @bye","Y5 pulang","M5 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     ke.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y6 @bye","Y6 pulang","M6 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kf.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y7 @bye","Y7 pulang","M7 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kg.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y8 @bye","Y8 pulang","M8 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kh.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y9 @bye","Y9 pulang","M9 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kj.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y10 @bye","Y10 pulang","M10 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kl.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y11 @bye","Y11 pulang","M11 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     km.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y12 @bye","Y12 pulang","M12 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kn.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y13 @bye","Y13 pulang","M13 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     ko.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y14 @bye","Y14 pulang","M14 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kp.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y15 @bye","Y15 pulang","M15 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kq.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y16 @bye","Y16 pulang","M16 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kr.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y17 @bye","Y17 pulang","M17 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     ks.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y18 @bye","Y18 pulang","M18 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kt.leaveGroup(msg.to)
                except:
                     pass
#-----------------------------------
            elif msg.text in ["Kill"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,km,kn,ko,kp,kq,kr,ks,kt]
                            kicker = random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Error!" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Error!","")
                    klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,km,kn,ko,kp,kq,kr,ks,kt]
                    kicker = random.choice(klist)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = kf.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    gs = kj.getGroup(msg.to)
                    gs = kl.getGroup(msg.to)
                    gs = km.getGroup(msg.to)
                    gs = kn.getGroup(msg.to)
                    gs = ko.getGroup(msg.to)
                    gs = kp.getGroup(msg.to)
                    gs = kq.getGroup(msg.to)
                    gs = kr.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = kt.getGroup(msg.to)
                    kicker.sendText(msg.to,"􂀁􀄃「 Cleanse 」 is Starting")
                    kicker.sendText(msg.to,"Group Anda Pantas Di Bersihkan.")
                    kicker.sendText(msg.to,"Good Bye (*´･ω･*)")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        kk.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                               klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,km,kn,ko,kp,kq,kr,ks,kt]
                               kicker = random.choice(klist)
                               kicker.kickoutFromGroup(msg.to,[target])
                               print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Group cleanse")
                                kk.sendText(msg,to,"Group cleanse")
                            pass
            elif ("Kick " in msg.text):
				if msg.from_ in admin:
					targets = []
					key = eval(msg.contentMetadata["MENTION"])
					key["MENTIONEES"][0]["M"]
					for x in key["MENTIONEES"]:
						targets.append(x["M"])
					for target in targets:
						try:
							cl.kickoutFromGroup(msg.to,[target])
						except:
							cl.sendText(msg.to,"Error")
							
            elif ("Mkick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")

            elif ("Bkick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki.kickoutFromGroup(msg.to,[target])
                           ki.inviteIntoGroup(msg.to,[target])
                           ki.cancelGroupInvitation(msg.to,[target])
                           ki.inviteIntoGroup(msg.to,[target])
                           ki.cancelGroupInvitation(msg.to,[target])
                           ki.inviteIntoGroup(msg.to,[target])
                           ki.cancelGroupInvitation(msg.to,[target])
                           ki.inviteIntoGroup(msg.to,[target])
                           ki.cancelGroupInvitation(msg.to,[target])
                           ki.inviteIntoGroup(msg.to,[target])
                           ki.cancelGroupInvitation(msg.to,[target])
                           ki.inviteIntoGroup(msg.to,[target])
                           ki.cancelGroupInvitation(msg.to,[target])
                           ki.inviteIntoGroup(msg.to,[target])
                           ki.cancelGroupInvitation(msg.to,[target])
                           ki.inviteIntoGroup(msg.to,[target])
                           ki.cancelGroupInvitation(msg.to,[target])
                           ki.inviteIntoGroup(msg.to,[target])
                           ki.cancelGroupInvitation(msg.to,[target])
                           ki.inviteIntoGroup(msg.to,[target])
                           ki.cancelGroupInvitation(msg.to,[target])
                           ki.inviteIntoGroup(msg.to,[target])
                           ki.cancelGroupInvitation(msg.to,[target])
                           ki.inviteIntoGroup(msg.to,[target])
                           ki.cancelGroupInvitation(msg.to,[target])
                           ki.inviteIntoGroup(msg.to,[target])
                           ki.cancelGroupInvitation(msg.to,[target])
                       except:
                           ki.sendText(msg.to,"Error")

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
                       time.sleep(0.01)
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
#-------------------------------------------------------------------
            elif "Fuck " in msg.text:
                       nk0 = msg.text.replace("Fuck ","")
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
                       ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
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
                                    ke.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ke.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-------------------------------------------------------------------
            elif "Fuck1 " in msg.text:
                       nk0 = msg.text.replace("Fuck1 ","")
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
                       kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
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
                                    kl.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    kl.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-------------------------------------------------------------------
            elif "Fuck2 " in msg.text:
                       nk0 = msg.text.replace("Fuck2 ","")
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
                       kp.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
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
                                    kp.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    kp.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-------------------------------------------------------------------
            elif "Fuck3 " in msg.text:
                       nk0 = msg.text.replace("Fuck3 ","")
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
                       kt.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
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
                                    kt.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    kt.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-------------------------------------------------------------------
            elif ("M1 kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki.kickoutFromGroup(msg.to,[target])
                       except:
                           ki.sendText(msg.to,"Error")
            elif ("M2 kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           kk.kickoutFromGroup(msg.to,[target])
                       except:
                           kk.sendText(msg.to,"Error")
            elif ("M3 kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           kc.kickoutFromGroup(msg.to,[target])
                       except:
                           kc.sendText(msg.to,"Error")
            elif ("M4 kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           kd.kickoutFromGroup(msg.to,[target])
                       except:
                           kd.sendText(msg.to,"Error")
            elif ("M5 kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ke.kickoutFromGroup(msg.to,[target])
                       except:
                           ke.sendText(msg.to,"Error")
            elif ("M6 kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           kf.kickoutFromGroup(msg.to,[target])
                       except:
                           kf.sendText(msg.to,"Error")
            elif ("M7 kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           kg.kickoutFromGroup(msg.to,[target])
                       except:
                           kg.sendText(msg.to,"Error")
            elif ("M8 kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           kh.kickoutFromGroup(msg.to,[target])
                       except:
                           kh.sendText(msg.to,"Error")
            elif ("M9 kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           kj.kickoutFromGroup(msg.to,[target])
                       except:
                           kj.sendText(msg.to,"Error")
            elif "Man@tag" in msg.text:
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

            elif ("Mk " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif "Blacklist @" in msg.text:
                _name = msg.text.replace("Blacklist @","")
                _kicktarget = _name.rstrip(' ')
                gs = ki.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    kk.sendText(msg.to,"Success Boss")
                                except:
                                    ki.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "[BL]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Success Masuk daftar orang bejat Boss")
                            except:
                                cl.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[WL]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Sudah di keluarkan dari daftar bejat Boss")
                            except:
                                cl.sendText(msg.to,"There was no blacklist user")
            elif msg.text in ["Clear ban","ล้างดำ","Cb"]:
				wait["blacklist"] = {}
				cl.sendText(msg.to,"[Clear Blacklist]")
				
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
            
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
			
            elif msg.text in ["Banlist","Mcheck"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing 􀨁􀄻double thumbs up􏿿")
                else:
                    cl.sendText(msg.to,"Daftar Banlist􏿿")
                    mc = "[💀] Blacklist [💀]\n"
                    for mi_d in wait["blacklist"]:
                        mc += "[✗] " + cl.getContact(mi_d).displayName + " \n"
                    cl.sendText(msg.to, mc + "")
            elif msg.text in ["M ban","Cekban","Mid ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = "[💀] Mid Blacklist [💀]"
                    for mm in matched_list:
                        cocoa += "\n" + mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
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
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                        kd.kickoutFromGroup(msg.to,[jj])
                        ke.kickoutFromGroup(msg.to,[jj])
                        kf.kickoutFromGroup(msg.to,[jj])
                        kg.kickoutFromGroup(msg.to,[jj])
                        kh.kickoutFromGroup(msg.to,[jj])
                        kj.kickoutFromGroup(msg.to,[jj])
                        kl.kickoutFromGroup(msg.to,[jj])
                        km.kickoutFromGroup(msg.to,[jj])
                        kn.kickoutFromGroup(msg.to,[jj])
                        ko.kickoutFromGroup(msg.to,[jj])
                        kp.kickoutFromGroup(msg.to,[jj])
                        kq.kickoutFromGroup(msg.to,[jj])
                        kr.kickoutFromGroup(msg.to,[jj])
                        ks.kickoutFromGroup(msg.to,[jj])
                        kt.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist user")
#=======================================================================
            elif ("Add mimic " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            mimic["target"][target] = True
                            cl.sendText(msg.to,"Haha")
                            cl.sendMessageWithMention(msg.to,target)
                            break
                        except:
                            cl.sendText(msg.to,"Fail !")
                            break
#=================================Del mimic==============================
            elif ("Del mimic " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del mimic["target"][target]
                            cl.sendText(msg.to,"Ma'afin aku ya kak")
                            cl.sendMessageWithMention(msg.to,target)
                            break
                        except:
                            cl.sendText(msg.to,"Fail !")
                            break
#==============================List mimic status==========================
            elif msg.text in ["Mimic list"]:
                if msg.from_ in admin:
                    if mimic["target"] == {}:
                        cl.sendText(msg.to,"No target")
                    else:
                        lst = "|•{List Mimic}•|"
                        total = len(mimic["target"])
                        for a in mimic["target"]:
                            if mimic["target"][a] == True:
                                stat = "On"
                            else:
                                stat = "Off"
                            lst += "\n=•" + cl.getContact(a).displayName + " | " + stat
                        cl.sendText(msg.to,lst + "\nTotal: {" + total + "}")
#================================Mimic status============================
            elif "Mimic " in msg.text:
                if msg.from_ in admin:
                    cmd = msg.text.replace("Mimic ","")
                    if cmd == "on":
                        if mimic["status"] == False:
                            mimic["status"] = True
                            cl.sendText(msg.to,"Mimic mode on")
                        else:
                            cl.sendText(msg.to,"Sudah on kak")
                    elif cmd == "off":
                        if mimic["status"] == True:
                            mimic["status"] = False
                            cl.sendText(msg.to,"Mimic mode off")
                        else:
                            cl.sendText(msg.to,"Sudah off kak")
#=============================================
            elif "Hack status" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[profilePicture]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[homePicture]\n" + str(cu))
                except:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[homePicture]\n" + str(cu))
#=============================================
            elif msg.text in ["Sp"]:
                start = time.time()
                cl.sendText(msg.to, "•─ ͜͡✯͜͡S͜͡p͜͡e͜͡e͜͡e͜͡d✯͜͡ѕ͜͡є͜͡ʟ͜͡ғ͜͡в͜͡о͜͡т͜͡✯─•")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
            elif msg.text in ["Speed","Speedbot"]:
                start = time.time()
                cl.sendText(msg.to, "•─ ͜͡✯͜͡S͜͡p͜͡e͜͡e͜͡e͜͡d͜͡✯͜͜͡͡в͜͡о͜͡т͜͡✯͜͡κ͜͡ɪ͜͡c͜͡κ͜͡є͜͡ʀ͜͡✯─•")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                ki.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                kk.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                kc.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                kd.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                ke.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                kf.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                kg.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                kh.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                kj.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                kl.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                km.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                kn.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                ko.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                kp.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                kq.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                kr.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                kh.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
                kt.sendText(msg.to, "•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\nความเร็ว﴾ %s ﴿ต่อวินาที" % (elapsed_time))
#----------------- BAN MEMBER BY TAG 2TAG ATAU 10TAG MEMBER
            elif ("ติดดำ " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned Bos")
                   except:
                      pass        
#============================================
            elif "Run group" in msg.text:
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                ki.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                ki.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kk.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kk.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                kc.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kc.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kd.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kd.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                ke.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                ke.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kf.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kf.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                kg.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kg.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kh.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kh.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                kj.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kj.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kl.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kl.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                km.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                km.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kn.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kn.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                ko.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                ko.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kp.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kp.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                kq.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kq.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kr.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kr.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                ks.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                ks.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kt.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kt.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                ki.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                ki.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kk.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kk.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                kc.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kc.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kd.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kd.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                ke.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                ke.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kf.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kf.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                kg.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kg.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kh.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kh.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                kj.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kj.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kl.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kl.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                km.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                km.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kn.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kn.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                ko.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                ko.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kp.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kp.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                kq.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kq.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kr.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kr.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                ks.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                ks.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kt.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kt.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                ki.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                ki.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kk.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kk.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                kc.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kc.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kd.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kd.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                ke.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                ke.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kf.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kf.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                kg.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kg.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kh.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kh.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                kj.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kj.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kl.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kl.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                km.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                km.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kn.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kn.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                ko.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                ko.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kp.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kp.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                kq.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kq.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kr.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kr.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")
                ks.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                ks.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n🏂⛷️[จะออกไปแตะขอบฟ้า]")
                kt.createGroup("🏃​⌒ ก้าว คนล่ะก้าว", mi_d)
                kt.sendText(msg.to,"•─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•\n⛷️🏂[จะออกไปแตะขอบฟ้า]")

            elif "Recover" in msg.text:
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                cl.createGroup("Recover", mi_d)
                cl.sendText(msg.to,"Success recover")

	    elif ("Gift you" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                	   msg.contentType = 9
                           msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                           msg.text = None
                           cl.sendMessage(msg)
                           cl.sendMessage(msg,target)
                       except:
			   cl.sendText(msg.to,"Gift to you 😘")
	    elif ("Bot gift" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                	   msg.contentType = 9
                           msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                           msg.text = None
                           ki.sendMessage(msg)
                           ki.sendMessage(msg,target)
                           kk.sendMessage(msg)
                           kk.sendMessage(msg,target)
                           kc.sendMessage(msg)
                           kc.sendMessage(msg,target)
                           kd.sendMessage(msg)
                           kd.sendMessage(msg,target)
                           ke.sendMessage(msg)
                           ke.sendMessage(msg,target)
                           kf.sendMessage(msg)
                           kf.sendMessage(msg,target)
                           kg.sendMessage(msg)
                           kg.sendMessage(msg,target)
                           kh.sendMessage(msg)
                           kh.sendMessage(msg,target)
                           kj.sendMessage(msg)
                           kj.sendMessage(msg,target)
                           kl.sendMessage(msg)
                           kl.sendMessage(msg,target)
                           km.sendMessage(msg)
                           km.sendMessage(msg,target)
                           kn.sendMessage(msg)
                           kn.sendMessage(msg,target)
                           ko.sendMessage(msg)
                           ko.sendMessage(msg,target)
                           kp.sendMessage(msg)
                           kp.sendMessage(msg,target)
                           kq.sendMessage(msg)
                           kq.sendMessage(msg,target)
                           kr.sendMessage(msg)
                           kr.sendMessage(msg,target)
                           ks.sendMessage(msg)
                           ks.sendMessage(msg,target)
                           kt.sendMessage(msg)
                           kt.sendMessage(msg,target)
                       except:
			   cl.sendText(msg.to,"Gift send to member")
#=================================Add mimic=============================
            elif ("add mimic " in msg.text):
          #      if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            mimic["target"][target] = True
                            cl.sendText(msg.to,"Haha")
                            cl.sendMessageWithMention(msg.to,target)
                            break
                        except:
                            cl.sendText(msg.to,"Fail !")
                            break
#=================================Del mimic==============================
            elif ("del mimic " in msg.text):
           #     if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del mimic["target"][target]
                            cl.sendText(msg.to,"Ma'afin aku ya kak")
                            cl.sendMessageWithMention(msg.to,target)
                            break
                        except:
                            cl.sendText(msg.to,"Fail !")
                            break
#========================NOTIFED MEMBER JOIN GROUP=========================
        if op.type == 17:
          #if wait["sambut"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1," HELLO 😻 " + cl.getContact(op.param2).displayName + "\n✨ยินดีต้อนรับเข้าร่วมกลุ่ม✨\n☛ " + str(ginfo.name) + " ☚" + "\n\nUpdate your Membership Profile to Join The GroupS suggestions  [⏰]  " +datetime.today().strftime('%H:%M:%S'))
            cl.sendImageWithURL(op.param1,image)
            print "ada orang masuk grup"
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
#================================List mimic status=========================
	if op.type == 13:
            if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"グループにメンバーを招待する（´・ω・｀）\n☆時間 🕘 " +datetime.today().strftime('%H:%M:%S'))
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"「Auto Messages」\nแจ้งเตือน📛มีการเชิญสมาชิกเข้าร่วมกลุ่ม\n\n「เวลา」🕘 " +datetime.today().strftime('%H:%M:%S'))
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = cl.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    cl.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"URL/QRが更新されました.☆（´・ω・｀）\n☆時間 🕘 " +datetime.today().strftime('%H:%M:%S'))
#============================================================================
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
#--------------------------------------------------------------------------------
#===========================================
#        if op.type == 55:
#            try:
#				if op.param1 in wait2['readPoint']:
#					Name = cl.getContact(op.param2).displayName
#					if Name in wait2['readMember'][op.param1]:
#						pass
#					else:
#						wait2['readMember'][op.param1] += "\n╠" + Name
#						wait2['ROM'][op.param1][op.param2] = "╠" + Name
#				else:
#					cl.sendText
#            except:
#                pass
#						
#						
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n╠ " + Nama
                        wait2['ROM'][op.param1][op.param2] = "╠ " + Nama
                        wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                else:
                    cl.sendText
            except:
                pass




#------------------------
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
                nowT = datetime.strftime(now2,"༺%H:%M༻")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
    
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev,  5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
