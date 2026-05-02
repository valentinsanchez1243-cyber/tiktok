import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    'onclick="cp(${JSON.stringify(desc)},\'${did}\')"',
    'onclick=\\\'cp(${JSON.stringify(desc).replace(/\\\'/g, "&#39;")}, "${did}")\\\''
)

text = text.replace(
    'onclick="cp(${JSON.stringify(s)},\'${iSlide}\')"',
    'onclick=\\\'cp(${JSON.stringify(s).replace(/\\\'/g, "&#39;")}, "${iSlide}")\\\''
)

text = text.replace(
    'onclick="cp(${JSON.stringify(p.ti)},\'${iPort}\')"',
    'onclick=\\\'cp(${JSON.stringify(p.ti).replace(/\\\'/g, "&#39;")}, "${iPort}")\\\''
)

text = text.replace(
    'onclick="cp(${JSON.stringify(desc)},\'${iDesc}\')"',
    'onclick=\\\'cp(${JSON.stringify(desc).replace(/\\\'/g, "&#39;")}, "${iDesc}")\\\''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Fixed onClick quotes')
