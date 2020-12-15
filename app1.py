def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello APP1"]

#def application(environ, start_response):
#    start_response('200 OK', [('Content-Type', 'text/html')])
#    return ["<h1 style='color:blue'>Hello APP1!</h1>"]
