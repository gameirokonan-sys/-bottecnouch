import urllib.request, urllib.parse, json, time
TOKEN="8747601947:AAFJcb9jVtFuVek_PjANkcV_EBUVSMFFr_A"
BASE=f"https://api.telegram.org/bot{TOKEN}/"
def send(cid,txt,kb=None):
 p={"chat_id":cid,"text":txt,"parse_mode":"HTML"}
 if kb: p["reply_markup"]=json.dumps(kb)
 try: urllib.request.urlopen(BASE+"sendMessage?"+urllib.parse.urlencode(p),timeout=10).read()
 except: pass
def get(o=0):
 return json.loads(urllib.request.urlopen(BASE+f"getUpdates?offset={o}&timeout=20",timeout=25).read().decode())
KB={"keyboard":[["\u26bd Matchs du Jour","\U0001f525 Coupon"],["\U0001f48e VIP","\U0001f4ca Stats"]],"resize_keyboard":True}
off=0
while True:
 try:
  d=get(off)
  for u in d.get("result",[]):
   off=u["update_id"]+1
   m=u.get("message",{});c=m.get("chat",{}).get("id");t=m.get("text","")
   if not c: continue
   if t=="/start": send(c,"\U0001f525 BIENVENUE CHEZ TECNOUCH225 \U0001f1e8\U0001f1ee\n\nLe meilleur bot de pronos d'Afrique !",KB)
   elif "Matchs" in t: send(c,"\u26bd <b>MATCHS DU JOUR</b>\n\nMan City - Liverpool: <b>1X & +1.5</b>\nReal - Barca: <b>BTTS OUI</b>\nPSG - OM: <b>+2.5</b>",KB)
   elif "Coupon" in t: send(c,"\U0001f525 <b>COUPON Cote 3.45</b>\n\nMan City 1X\nBarca BTTS\nPSG +2.5",KB)
   elif "VIP" in t: send(c,"\U0001f48e <b>VIP 10.000F/mois</b>\nContact: @TecnoUch225",KB)
   elif "Stats" in t: send(c,"\U0001f4ca <b>STATS 80% ce mois</b> \U0001f1e8\U0001f1ee",KB)
   else: send(c,"Tape /start",KB)
 except: time.sleep(2)
