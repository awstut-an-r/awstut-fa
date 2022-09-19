#from aws_xray_sdk.core import xray_recorder
#from aws_xray_sdk.ext.bottle.middleware import XRayMiddleware
from bottle import route, run

#app = Bottle()

#xray_recorder.configure(service='fa-074')
#plugins = ('ECSPlugin',)
#xray_recorder.configure(plugins=plugins)
#
#app.install(XRayMiddleware(xray_recorder))

##xray_recorder.configure(service='fa-074')
##patch_all()

#@app.route('/')
@route('/')
def hello():
  ##xray_recorder.begin_segment('fa-074-segment')
  ##xray_recorder.end_segment()
  return 'Hello CodePipeline.'
  
    
if __name__ == '__main__':
  #run(app=app, host='0.0.0.0', port=8080)
  #run(app=app, host='0.0.0.0', port=8080)
  run(host='0.0.0.0', port=8080)