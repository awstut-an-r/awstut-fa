from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.bottle.middleware import XRayMiddleware
from bottle import Bottle, route, run

app = Bottle()

xray_recorder.configure(service='fa-074')
plugins = ('ECSPlugin',)
xray_recorder.configure(plugins=plugins)

app.install(XRayMiddleware(xray_recorder))

@app.route('/')
def hello():
  return 'Hello X-Ray!'
  
    
if __name__ == '__main__':
  run(app=app, host='0.0.0.0', port=8080)
