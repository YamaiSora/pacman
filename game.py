import time
from player import Player
from field import Field
from controller import UserInput
from config import Parameters
import logging
import os
import random



logger = logging.getLogger(__name__)


class Game:
    """ゲームクラス
    ゲームの初期設定とメインループを実行してゲームを実施するクラス．

    Attributes:
        players (list[Player]): プレイヤーのリスト
        enemies (list[Enemy]): 敵のリスト
        foods (list[Food]): 食べ物のリスト
        blocks (list[Block]): ブロックのリスト
        field (Field): フィールドのインスタンス
    """

    def __init__(self, params: Parameters) -> None:
        """ゲームクラスの初期化

        Args:
            params (Parameters): configのパラメータのインスタンス
        """

        # self.players: list = []
        # self.field = None
        self.setup(params)  # ゲームの初期設定
        self.start()  # ゲームのメインループ

    def setup(self, params: Parameters) -> None:
        """ゲームの初期設定
        ゲームの初期設定を行うメソッド．

        Args:
            params (Parameters): configのパラメータのインスタンス
        """

        # フィールドの初期化
        self.players = [Player(1, 1)]

        self.field = Field(self.players)

    def start(self) -> str:
        """ゲームのメインループ
        ゲームのメインループを実行するメソッド．
        キー入力を受け取り，プレイヤーと敵の移動を行い，フィールドを更新する．
        ゲーム終了条件を満たした場合は終了する．

        Returns:
            str: ゲーム終了時のメッセージ (例: "Game Over!", "Game Clear!")
        """
        # ゲームのメインループ
        user_input = UserInput()
        while True:
            #  フィールドを表示
            os.system("cls" if os.name == "nt" else "clear")  # ターミナルをクリア
            self.field.display_field()

            # プレイヤーの移動を決定
            for player in self.players:
                # self.field.display_field()
                # キー入力を受け取る
                key = user_input.get_user_input()
                player.get_next_pos(key)
                player.update_position()
            self.field.update_count(user_input.key_press_count)
            # fieldを更新
            self.field.update_field()
            # self.field.display_field()
            # 一定の間隔で処理を繰り返す
            random_number = random.randint(0, 100)
            print(user_input.key_press_count, random_number)
            if user_input.key_press_count > random_number*2:
                exit()

            # 0.3秒待つ
            time.sleep(0.3)

            # 終了条件のチェック
            # 例えば、全ての食べ物が消えたり、敵とプレイヤーが衝突したりしたら終了する処理を追加する


if __name__ == "__main__":
    import doctest
    doctest.testmod()
