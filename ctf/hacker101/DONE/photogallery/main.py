from flask import Flask, abort, redirect, request, Response 
import base64, json, MySQLdb, os, re, subprocess 

app = Flask(__name__) 
home = '''
    Magical Image Gallery
    $ALBUMS$ 
''' 
viewAlbum = '''
    $TITLE$
    $GALLERY$ 
''' 

def getDb(): 
    return MySQLdb.connect(host="localhost", user="root", password="", db="level5") 
    
def sanitize(data): 
    return data.replace('&', '&').replace('<', '<').replace('>', '>').replace('"', '"') 
    
@app.route('/') 
def index(): 
    cur = getDb().cursor() 
    cur.execute('SELECT id, title FROM albums') 
    albums = list(cur.fetchall()) 
    rep = '' 
    for id, title in albums: 
        rep += '%s\n' % sanitize(title) 
        rep += '' 
        cur.execute('SELECT id, title, filename FROM photos WHERE parent=%s LIMIT 3', (id, )) 
        fns = [] 
        for pid, ptitle, pfn in cur.fetchall(): 
            rep += '%s' % (pid, sanitize(ptitle)) 
            fns.append(pfn) 
        rep += 'Space used: ' + subprocess.check_output('du -ch %s || exit 0' % ' '.join('files/' + fn for fn in fns), shell=True, stderr=subprocess.STDOUT).strip().rsplit('\n', 1)[-1] + '' 
        rep += '\n' 
        return home.replace('$ALBUMS$', rep) 
            
@app.route('/fetch') 
def fetch(): 
    cur = getDb().cursor() 
    if cur.execute('SELECT filename FROM photos WHERE id=%s' % request.args['id']) == 0: 
        abort(404) 

    # It's dangerous to go alone, take this: 
    # ^FLAG^0b4186b3af9832e40e92077fd893046a898ce25463d37cf9fefc192ff3a58e7d$FLAG$ 
    return file('./%s' % cur.fetchone()[0].replace('..', ''), 'rb').read() 
        
if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=80)