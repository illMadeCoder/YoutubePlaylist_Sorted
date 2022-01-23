from flask import Flask, request, redirect
from ytplsorted import ytplsorted
app = Flask("ytplsorted")

# program(argsservice.playlistIDs, 
#         argsservice.sortby, 
#         argsservice.mixin, 
#         argsservice.c, 
#         argsservice.n)    

@app.route("/ytplsorted", methods=['GET'])
def ytplsortedEndpoint():
    playlistIDs = request.args.get('playlistIDs', None)
    sortby = request.args.get('sortby', 'ratio')
    mixin = request.args.get('mixin', "mixin")
    c = request.args.get("c", "1")
    n = request.args.get("n", "1")
    url = ytplsorted(playlistIDs.split(","), sortby, mixin, int(c), int(n))
    return redirect(url, code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
