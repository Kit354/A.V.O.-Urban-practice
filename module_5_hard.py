# class User:
#     def __init__(self, nickname, password, age):
#         self.nickname = nickname
#         self.password = password
#         self.age = age


class Video:
    def __init__(self, title, duration=0, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class UrTube:

    def __init__(self):
        self.videos = []

    def __contains__(self, item):
        if isinstance(item, Video):
            return item in self.videos

    def add(self, *args):
        for video in args:
            if isinstance(video, Video) and video.title not in self.videos:
                self.videos.append(video.title)

    def get_videos(self, title):
        dict_videos = []
        for vid in self.videos:
            if title.lower() in vid.lower():
                dict_videos.append(vid)
                return dict_videos


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)
    print(ur.videos)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
