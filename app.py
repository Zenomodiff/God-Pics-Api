from math import ceil
from random import randint, choice
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return '''
	            <!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
      <h1 class="project-name">Welcome to God Image API 🕉️✡️🙏📿</h1>
      <h2 class="project-tagline">An API which returns random God Images</h2
<h2 id="usage">Usage:</h2>
<ul>
<p>The Endpoint Of The API</p>
  <li><code class="language-plaintext highlighter-rouge">/ayappa</c ode> will return Random Images Of Lord Ayappa</li>
    <li><code class="language-plaintext highlighter-rouge">/siva</code> will return Random Images Of Lord Siva</li>
      <li><code class="language-plaintext highlighter-rouge">/krishna</code> will return Random Images Of Lord Krishna</li>
        <li><code class="language-plaintext highlighter-rouge">/hanuman</code> will return Random Images Of Lord Hanuman</li>
          <li><code class="language-plaintext highlighter-rouge">/ganapathy</code> will return Random Images Of Lord Ganapathy</li>
            <li><code class="language-plaintext highlighter-rouge">/vishnu</code> will return Random Images Of Lord Vishnu</li>
</ul>
    </main>
  </body>
</html>
 '''

@app.route('/ayappa', methods=['GET'])
def ayappa_pic():
	im_index = randint(1,45)
	file = f'lords/ayyappa/image{im_index}.jpg'
	return send_file(file, mimetype='image/jpg')

@app.route('/ganapathy', methods=['GET'])
def ganapathy_pic():
	im_index = randint(1,46)
	file = f'lords/ganapathy/image{im_index}.jpg'
	return send_file(file, mimetype='image/jpg')

@app.route('/krishna', methods=['GET'])
def krishna_pic():
	im_index = randint(1,46)
	file = f'lords/krishna/image{im_index}.jpg'
	return send_file(file, mimetype='image/jpg')

@app.route('/hanuman', methods=['GET'])
def hanuman_pic():
	im_index = randint(1,42)
	file = f'lords/hanuman/image{im_index}.jpg'
	return send_file(file, mimetype='image/jpg')

@app.route('/siva', methods=['GET'])
def siva_pic():
	im_index = randint(1,45)
	file = f'lords/siva/image{im_index}.jpg'
	return send_file(file, mimetype='image/jpg')

@app.route('/vishnu', methods=['GET'])
def vishnu_pic():
	im_index = randint(1,50)
	file = f'lords/vishnu/image{im_index}.jpg'
	return send_file(file, mimetype='image/jpg')

if __name__ == '__main__':
	app.run(threaded=True, port=5000)
