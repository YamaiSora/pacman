from player import Player


class Field:
    """Fieldクラス
    Fieldクラスはゲームのフィールドを担うクラスです。
    フィールドの初期化やディスプレイを行なう。

    Attributes:
        players (list[Player]): プレイヤーのリスト
    """
    pass

    def __init__(self,
                 players: list[Player]) -> None:
        """
        フィールドの初期化を行なう関数

        Args:
            players (list[Player]): プレイヤーのリスト
        """
        pass

    def update_field(self) -> list[list[str]]:
        """
        フィールドを更新する関数

        Returns:
            list[list[str]]: 更新されたフィールド

        Examples:
            >>> p = [Player(1, 0)]
            >>> p[0].icon = "p1"
        """
        pass

    def display_field(self) -> None:
        """
        ディスプレイを行なう関数

        Examples:
            >>> p = [Player(1, 0)]
            >>> p[0].icon = "p1"
            w: 上に移動
            a: 左に移動
            s: 下に移動
            d: 右に移動
             p1
        """
        print("w: 上に移動")
        print("a: 左に移動")
        print("s: 下に移動")
        print("d: 右に移動")
        for y in range(5):
            for x in range(5):
                if Player.x == x and Player.y == y:
                    print("p1")
                else:
                    print(" ")
            print("\n")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
