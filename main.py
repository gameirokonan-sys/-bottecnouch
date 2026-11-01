import os, json, urllib.request, urllib.parse, time, threading
from http.server import BaseHTTPRequestHandler, HTTPServer

TOKEN=os.environ.get("BOT_TOKEN","")
if not TOKEN:
    TOKEN="8747601947:AAFJcb9jVtFuVek_PjA3-8vS9kQ2l2r4t5y6u7"
BASE=f"https://api.telegram.org/bot{TOKEN}"

def send(cid,txt,kb=None):
    p={"chat_id":cid,"text":txt,"parse_mode":"HTML"}
    if kb:
        p["reply_markup"]=json.dumps(kb)
    try:
        data=urllib.parse.urlencode(p).encode()
        urllib.request.urlopen(BASE+"/sendMessage",data,timeout=10)
    except Exception as e:
        print(e)

KB={"keyboard":[["🔥 TENDANCE DU JOUR","🎯 PARI DU JOUR"],["💎 DEVENIR VIP","❓ AIDE"]],"resize_keyboard":True}

def bot_loop():
    offset=0
    while True:
        try:
            url=BASE+f"/getUpdates?offset={offset}&timeout=30"
            r=urllib.request.urlopen(url,timeout=35).read()
            d=json.loads(r)
            for u in d.get("result",[]):
                offset=u["update_id"]+1
                m=u.get("message",{})
                cid=m.get("chat",{}).get("id")
                txt=m.get("text","")
                if not cid:
                    continue
                if "/start" in txt:
                    send(cid,"🔥 <b>Bienvenue sur Bot Tecnouch !</b>\n\nJe prédis les matchs pour toi.\nChoisis un bouton :",KB)
                elif "TENDANCE" in txt:
                    send(cid,"🔥 <b>TENDANCE DU JOUR</b>\n\n⚽️ PSG vs Man City\n👉 BTTS OUI @1.80\n\nAnalyse: Les 2 équipes marquent beaucoup.",KB)
                elif "PARI" in txt:
                    send(cid,"🎯 <b>PARI DU JOUR - Prédiction Sûre</b>\n\n✅ Double Chance 1X @1.45\nMise: 10%\n\nPrédiction de l'IA !",KB)
                elif "VIP" in txt:
                    send(cid,"💎 <b>DEVENIR VIP - Prédictions Premium</b>\n\n✅ 3 à 5 pronos / jour\n✅ Cotes combinées 10+\n✅ Score exact\n\n💵 Prix: 5000 FCFA / mois\n📲 Paye via Orange Money / Wave et envoie 'VIP'",KB)
                elif "AIDE" in txt:
                    send(cid,"❓ <b>AIDE</b>\n\n1. Clique sur TENDANCE pour voir la prédiction du jour\n2. Clique sur PARI pour le pari sûr\n3. DEVENIR VIP pour gagner plus\n\nBot 100% automatique 24h/24",KB)
                else:
                    send(cid,f"Tu as dit: {txt}\n\nClique sur un bouton pour voir mes prédictions 👇",KB)
        except Exception as e:
            print(f"Erreur: {e}")
            time.sleep(3)

threading.Thread(target=bot_loop,daemon=True).start()

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is Live!")
    def log_message(self,a,b,c):
        pass

port=int(os.environ.get("PORT",10000))
print(f"Starting server on port {port}")
HTTPServer(("0.0.0.0",port),H).serve_forever()
