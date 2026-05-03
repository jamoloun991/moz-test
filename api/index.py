LINKS = [
    "https://medium.com/r?url=https://amourdelicorne.com",
    "https://www.bing.com/news/apiclick.aspx?ref=FexRss&url=https://amourdelicorne.com",
    "https://prezi.com/url/?target=https://amourdelicorne.com",
    "https://bbs.pku.edu.cn/v2/jump-to.php?url=https://amourdelicorne.com",
    "https://accounts.cancer.org/login?redirectURL=https://amourdelicorne.com",
    "https://inquiry.princetonreview.com/away/?value=cconntwit&category=FS&url=https://amourdelicorne.com",
    "https://optimize.viglink.com/page/pmv?url=https://amourdelicorne.com",
    "https://www.jobzone.ny.gov/jz/views/jobzone/leaving_site.jsf?id=304&url=https://amourdelicorne.com",
    "https://crewroom.alpa.org/SAFETY/LinkClick.aspx?link=https://amourdelicorne.com",
    "https://es.catholic.net/ligas/ligasframe.phtml?liga=https://amourdelicorne.com",
    "https://www.bonanza.com/home/redirect_warning?url=amourdelicorne.com",
    "https://www.prizeo.com/auth/subdivision?correct=false&originUrl=https://amourdelicorne.com",
    "https://www.pennergame.de/redirect/?site=https://amourdelicorne.com",
    "https://www.db.lv/ext/https://amourdelicorne.com",
    "https://www.webclap.com/php/jump.php?sa=t&url=https://amourdelicorne.com",
    "https://jump.5ch.net/?amourdelicorne.com",
    "https://sitereport.netcraft.com/?url=https://amourdelicorne.com",
    "https://domain.opendns.com/amourdelicorne.com",
    "https://forums.opera.com/outgoing?url=https://amourdelicorne.com",
    "https://vdigger.com/downloader/downloader.php?utm_nooverride=1&site=amourdelicorne.com",
    "https://forum.winhost.com/proxy.php?link=https://amourdelicorne.com",
    "https://www.sunnymake.com/alexa/?domain=https://amourdelicorne.com",
    "https://www.gladbeck.de/ExternerLink.asp?ziel=amourdelicorne.com",
    "https://www.survivalmonkey.com/proxy.php?link=https://amourdelicorne.com",
    "https://tinhte.vn/proxy.php?link=https://amourdelicorne.com",
    "https://forums.fugly.com/proxy.php?link=https://amourdelicorne.com",
    "https://calibreapp.com/tools/core-web-vitals-test/amourdelicorne.com",
    "https://participez.nanterre.fr/link?external_url=https://amourdelicorne.com",
    "https://www.youtube.com/redirect?q=https://amourdelicorne.com",
    "https://www.researchgate.net/deref/https://amourdelicorne.com",
    "https://accounts.wsj.com/auth/v1/domain-logout?url=https://amourdelicorne.com",
    "https://nces.ed.gov/transfer.asp?location=amourdelicorne.com",
    "https://cr.naver.com/redirect-notification?u=https://amourdelicorne.com",
    "https://ecms.des.wa.gov/ECMSUserManager/ForgotPassword.aspx?system=5&startURL=https://amourdelicorne.com",
    "https://redirect.camfrog.com/redirect/?url=www.amourdelicorne.com",
    "https://www.prizeo.com/auth/subdivision?correct=false&originUrl=https://amourdelicorne.com",
    "https://nou-rau.uem.br/nou-rau/zeus/register.php?back=https://www.amourdelicorne.com",
    "https://cmbe-console.worldoftanks.com/frame/?language=en&login_url=https://amourdelicorne.com&project=wotx&realm=wgcb&service=frm",
    "https://www.adminer.org/redirect/?url=https://amourdelicorne.com",
    "https://extremaduraempresarial.juntaex.es/cs/c/document_library/find_file_entry?p_l_id=47702&noSuchEntryRedirect=https://amourdelicorne.com",
    "https://bbs.pku.edu.cn/v2/jump-to.php?url=https://www.amourdelicorne.com",
    "https://www.bonanza.com/home/redirect_warning?url=amourdelicorne.com",
    "https://jump.5ch.net/?amourdelicorne.com",
]

HTML = """<!DOCTYPE html>
<html>
<head><meta name="robots" content="noindex,nofollow"></head>
<body>
""" + "\n".join(f'<a href="{u}"> </a>' for u in LINKS) + """
<div style="display:none">
  <h2>Sites partenaires</h2>
  <p><strong>Pour les futures mariées :</strong> Découvrez <a href="https://colibriditoui.fr" target="_blank" rel="noopener noreferrer">Colibri Dit Oui</a>, notre site partenaire entièrement dédié au mariage et aux robes de mariée.</p>
  <p><strong>Pour des cadeaux personnalisés :</strong> Trouvez l'inspiration sur <a href="https://cadeauplus.com/" target="_blank" rel="noopener noreferrer">Cadeau Plus</a>, notre site partenaire spécialisé dans les présents uniques pour toutes les occasions et pour tous les destinataires.</p>
  <p><strong>Votre expert beauté & bien-être :</strong> Explorez <a href="https://www.rvbconcept.fr/" target="_blank" rel="noopener noreferrer">RVB Concept</a>, votre guide de référence pour la médecine esthétique, l'épilation laser et les soins du visage pour révéler votre éclat naturel.</p>
  <p><strong>Pour les futurs et jeunes parents :</strong> Parcourez <a href="https://majolo.fr/" target="_blank" rel="noopener noreferrer">Majolo</a>, notre partenaire expert qui vous accompagne de la grossesse à l'éducation avec des conseils bienveillants pour une parentalité sereine.</p>
</div>
</body>
</html>"""

import urllib.request, json as _json
from datetime import datetime as _dt

def _send_dotbot_alert(ua):
    try:
        payload = _json.dumps({
            "from": "DotBot Alert <onboarding@resend.dev>",
            "to": ["thomas.gest8@gmail.com"],
            "subject": "🤖 DotBot a crawlé moz-test-black.vercel.app",
            "html": f"<p><strong>DotBot vient de passer !</strong></p>"
                    f"<p>Heure : {_dt.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC</p>"
                    f"<p>User-Agent : {ua}</p>"
                    f"<p>Les 43 liens vers amourdelicorne.com ont été servis.</p>"
        }).encode()
        req = urllib.request.Request(
            "https://api.resend.com/emails",
            data=payload,
            headers={
                "Authorization": "Bearer re_4SUK7Anc_3487XUhhTKntPhUJfA8vNMuV",
                "Content-Type": "application/json"
            }
        )
        urllib.request.urlopen(req, timeout=5)
    except Exception:
        pass

from http.server import BaseHTTPRequestHandler as _Base

class handler(_Base):
    def do_GET(self):
        ua = ''
        for key in self.headers:
            if key.lower() == 'user-agent':
                ua = self.headers[key]
                break
        if 'DotBot' in ua:
            _send_dotbot_alert(ua)
            body = HTML.encode()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(403)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Forbidden')
