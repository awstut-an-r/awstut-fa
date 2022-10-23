import urllib.request
from flask import Flask

app = Flask(__name__)
url = 'http://169.254.169.254/latest/meta-data/instance-id'

@app.route('/')
def main():
  request = urllib.request.Request(url)
  with urllib.request.urlopen(request) as response:
    data = response.read().decode('utf-8')
    return data
    
if __name__ == '__main__':
  app.run()