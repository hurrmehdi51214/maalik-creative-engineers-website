import sys, os, subprocess, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SP = r"C:\Users\PC\AppData\Local\Temp\claude\C--Users-PC-Desktop-Claude\993691b8-cb0e-42ba-a274-f177584881f3\scratchpad"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
OVERRIDE = "<style>.hero{min-height:620px!important}.hero.short{min-height:440px!important}.hero.mini{min-height:340px!important}.rv{opacity:1!important;transform:none!important}</style></head>"

def shot(rel_path, out, height=5200):
    src = os.path.join(ROOT, rel_path)
    html = open(src, encoding="utf-8").read().replace("</head>", OVERRIDE, 1)
    tmp = os.path.join(ROOT, "_shot.html")
    # fix relative asset paths since _shot.html sits at root
    depth = rel_path.count("/") if rel_path.endswith("index.html") else 0
    depth = rel_path.count("/")
    if depth:
        html = html.replace('"' + "../" * depth, '"')
        html = re.sub(r'href="(?!http|#|mailto|tel|/)', 'href="' + "/".join([""]) , html) if False else html
    open(tmp, "w", encoding="utf-8").write(html)
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--window-size=1440,%d" % height, "--screenshot=%s" % os.path.join(SP, out + ".png"),
                    "--virtual-time-budget=9000", "http://127.0.0.1:8181/_shot.html"],
                   capture_output=True)
    os.remove(tmp)
    print("shot", out, os.path.getsize(os.path.join(SP, out + ".png")))

if __name__ == "__main__":
    shot(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 5200)
