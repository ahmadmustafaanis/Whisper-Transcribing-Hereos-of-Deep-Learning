import pytube
from tqdm import tqdm

interviews_details = {
    "https://www.youtube.com/watch?v=OT91E6_Qm1A&list=PLkDaE6sCZn6FcbHlDzbVzf3TVgxzxK7lr&index=2&ab_channel=DeepLearningAI": "Ruslan Salakhutdinov",
    "https://www.youtube.com/watch?v=dwFcodBz_2I&list=PLkDaE6sCZn6FcbHlDzbVzf3TVgxzxK7lr&index=3&ab_channel=DeepLearningAI": "Yuanqing Lin",
    "https://www.youtube.com/watch?v=dqwx-F7Eits&list=PLkDaE6sCZn6FcbHlDzbVzf3TVgxzxK7lr&index=4&ab_channel=DeepLearningAI": "Ian GoodFellow",
    "https://www.youtube.com/watch?v=LpAiPYNnxW0&list=PLkDaE6sCZn6FcbHlDzbVzf3TVgxzxK7lr&index=6&ab_channel=DeepLearningAI": "Pieter Abeel",
    "https://www.youtube.com/watch?v=oJFShOfCZiA&list=PLkDaE6sCZn6FcbHlDzbVzf3TVgxzxK7lr&index=5&ab_channel=DeepLearningAI": "Youshua Bengio",
    "https://www.youtube.com/watch?v=xxu4IqwKw0w&list=PLkDaE6sCZn6FcbHlDzbVzf3TVgxzxK7lr&index=7&ab_channel=DeepLearningAI": "Andrej Karpathy",
    "https://www.youtube.com/watch?v=JS12eb1cTLE&list=PLkDaE6sCZn6FcbHlDzbVzf3TVgxzxK7lr&index=8&ab_channel=DeepLearningAI": "Yann Lecunn",
    "https://www.youtube.com/watch?v=eMh5YqKopjE&list=PLkDaE6sCZn6FcbHlDzbVzf3TVgxzxK7lr&index=9&ab_channel=DeepLearningAI": "Dawn Song",
    "https://www.youtube.com/watch?v=-eyhCTvrEtE&list=PLkDaE6sCZn6FcbHlDzbVzf3TVgxzxK7lr&index=11&ab_channel=PreserveKnowledge": "Geoffy Hinton",
}


class DownloadInterviews:
    """
    Helper class to download the interviews from the DeepLearning.AI Youtube Channel
    """

    def __init__(self) -> None:
        self.interviews_details = interviews_details

    def __call__(self):
        """
        Downloads the Heros of the Deep Learning Interviews from the Youtube using Pytube
        """
        print("Downloading Interviews")
        for link, name in tqdm(self.interviews_details.items()):
            yt = pytube.YouTube(link)

            yt.streams.filter(abr="160kbps", progressive=False).first().download(
                filename=f"interviews/{name}.mp3"
            )


if __name__ == "__main__":
    download_interviews = DownloadInterviews()
