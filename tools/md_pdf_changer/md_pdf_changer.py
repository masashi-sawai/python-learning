import markdown
import pdfkit
import glob
import winreg

path = "./"  # ここに変換対象ディレクトリを指定
files = glob.glob(path + "input.md")
for f in files:
    # Markdownのテキストを読む
    with open(f, "rt", encoding="utf-8") as fp:
        text = fp.read()
        # HTMLに変換
        md = markdown.Markdown()
        body = md.convert(text)
        html = '<html lang="ja"><meta charset="utf-8"><body>'
        html += '<style> body { font-size: 3em; } </style>'
        html += body + '</body></html>'
    # PDFで出力
    outfile = f + ".pdf"
    print(outfile)

    try:
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\wkhtmltopdf',
                              access=winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as k:
            data, regtype = winreg.QueryValueEx(k, "PdfPath")
            configure = pdfkit.configuration(wkhtmltopdf=data)
            regtype = regtype

            pdfkit.from_string(html, outfile)
    except FileNotFoundError:
        pass
print("ok")
