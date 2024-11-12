from player import Player


class Field:
    """Fieldクラス
    Fieldクラスはゲームのフィールドを担うクラスです。
    フィールドの初期化やディスプレイを行なう。

    Attributes:
        players (list[Player]): プレイヤーのリスト
        field (list[list[str]]): フィールドの情報
    """
    pass

    def __init__(self,
                 players: list[Player]) -> None:
        """
        フィールドの初期化を行なう関数

        Args:
            players (list[Player]): プレイヤーのリスト
        """
        self.field = [["　" for _ in range(3)] for _ in range(3)]
        self.players = players
        # それぞれのアイテムの位置をFieldに反映
        self.update_field()

    def update_field(self) -> list[list[str]]:
        """
        フィールドを更新する関数

        Returns:
            list[list[str]]: 更新されたフィールド

        Examples:
            >>> p = [Player(1, 0)]
            >>> p[0].icon = "p1"
            >>> field = Field(p)
            >>> field.update_field()[0]
            ['\\u3000', 'p1', '\\u3000']
            >>> field.update_field()[1]
            ['\\u3000', '\\u3000', '\\u3000']
            >>> field.update_field()[2]
            ['\\u3000', '\\u3000', '\\u3000']
        """
        # fieldを一旦すべて空白にする
        for i in range(3):
            for j in range(3):
                self.field[i][j] = "　"
        #  Fieldを更新する処理を記述
        for player in self.players:
            if player.status:
                self.field[player.now_y][player.now_x] = player.icon
        return self.field

    def display_field(self) -> None:
        """
        ディスプレイを行なう関数

        Examples:
            >>> p = [Player(1, 0)]
            >>> p[0].icon = "p1"
            >>> field = Field(p)
            >>> field.display_field()
            w: 上に移動
            a: 左に移動
            s: 下に移動
            d: 右に移動
            　p1　
            　　　
            　　　
        """
        # 動きか方を表示
        print("w: 上に移動")
        print("a: 左に移動")
        print("s: 下に移動")
        print("d: 右に移動")
        # print(self.field, type(self.field))
        for row in self.field:
            for sow in row:
                # 各行の文字列を作成し、不足分を空白文字で埋める
                print(sow, end="")
            print()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
