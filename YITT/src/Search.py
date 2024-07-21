from youtubesearchpython import VideosSearch
import os
class Search:
    def __init__(self):
        self.search = None
    def searchTitle(self, title: str, limit: int) -> dict:
        self.search = VideosSearch(title, limit = limit).result()
        return self.search
    def list_all_res(self) -> list:
        res = []
        for i in self.search['result']:
            res.append(i['title'])
        return res
    def getlink(self, index: int) -> str:
        return self.search['result'][index]['link']
    def play_video(self, index: int):
        os.system(f"mpv {self.getlink(index)}")
    def play_audio(self, index: int):
        os.system(f"mpv --no-video {self.getlink(index)}")
