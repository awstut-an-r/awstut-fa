from bottle import route, run

@route('/')
def hello():
  return 'Hello CodePipeline. Updated.'
  
    
if __name__ == '__main__':
  run(host='0.0.0.0', port=8080)
