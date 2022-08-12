from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
from bottle import route, run

xray_recorder.configure(service='fa-074')
plugins = ('ECSPlugin',)
xray_recorder.configure(plugins=plugins)
patch_all()

@route('/')
def hello():
  xray_recorder.begin_segment('fa-074-segment')
  xray_recorder.end_segment()
  
  return 'X-Ray Test.'
  
    
if __name__ == '__main__':
  run(host='0.0.0.0', port=8080)