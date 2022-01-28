from flask import Flask, request, jsonify
from ytplsorted import ytplsorted
from youtubeservice import playlistIDToPlaylist
from config import PORT
app = Flask("ytplsorted")

@app.route("/ytplsorted", methods=['GET'])
def ytplsortedEndpoint():
    playlistIDs = request.args.get('playlistIDs', None)
    sortby = request.args.get('sortby', 'ratio')
    mixin = request.args.get('mixin', "mixin")
    c = request.args.get("c", "1")
    n = request.args.get("n", "1")
    url = ytplsorted(playlistIDs.split(","), sortby, mixin, int(c), int(n))
    return url

@app.route("/playlistInfo", methods=['GET'])
def playlistsEndpoint():
    playlistID = request.args.get('playlistID', None)
    return jsonify(playlistIDToPlaylist(playlistID))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
