from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", 
    required=True)
video_put_args.add_argument("name", type=int, help="Views of the video", 
    required=True)
video_put_args.add_argument("name", type=int, help="Likes of the video", 
    required=True)

videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[]

api.add_resource(video, "/video/<int: video_id>")

if __name__ == '__main__':
    app.run(debug=True)