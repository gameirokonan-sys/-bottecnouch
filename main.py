import os, json, urllib.request, urllib.parse, threading, time
from http.server import BaseHTTPRequestHandler, HTTPServer
TOKEN="8747601947:AAFJcb9jVtFuVek_PjANkcV_EBUVSMFFr_A"
BASE=f"https://api.telegram.org/bot{TOKEN}/"
def send(cid,txt):
 p={"chat_id":cid,"text":txt,"parse_mode":"HTML"}
 try: urllib.request.urlopen(BASE+"sendMessage",urllib.parse.urlencode(p).encode(),timeout=10).read()
 except: pass
def bot():
 o=0
 while True:
  try:
   r=urllib.request.urlopen(BASE+f"getUpdates?offset={o}&timeout=15",timeout=20).read().decode()
   d=json.loads(r)
   for u in d.get("result",[]):
    o=u["update_id"]+1
    m=u.get("message",{});cid=m.get("chat",{}).get("id");txt=m.get("text","")
    if not cid: continue
    if "/start" in txt: send(cid,"🔥 BIENVENUE CHEZ TECNOUCH225 🇨🇮\n\nBot en ligne 24h/24 ! Tape /help")
    else: send(cid,f"Tu as dit: {txt}")
  except: time.sleep(2)
threading.Thread(target=bot,daemon=True).start()
class H(BaseHTTPRequestHandler):
 def do_GET(self):
  self.send_response(200);self.end_headers();self.wfile.write(b"OK TECNOUCH225")
HTTPServer(("0.0.0.0",int(os.environ.get("PORT",10000))),H).serve_forever()
