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
        return f'{self.title}'

    def __repr__(self):
        return f'{self.title}'


class UrTube:

    def __init__(self):
        self.videos = []

    def __contains__(self, item):
        if isinstance(item, Video):
            return item in self.videos

    def add(self, *args):
        for video in args:
            if video.title not in self.videos:
                self.videos.append(video)

    def get_videos(self, title_search):
        dict_get_videos = []
        for vid in self.videos:
            if title_search.lower() in vid.title.lower():
                dict_get_videos.append(vid.title)
        return dict_get_videos

    def watch_video(self, title_watch):
        dict_watch_video = UrTube.get_videos(self, title_watch)
        if isinstance(dict_watch_video, Video):
            for time in range(1, dict_watch_video.duration):
                return print(time)


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    print(ur.watch_video('Для чего девушкам парень программист?'))
