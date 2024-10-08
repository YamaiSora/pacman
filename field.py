from item import Item
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
        pass