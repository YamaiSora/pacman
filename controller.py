import sys
import termios


class InputWithoutEnter:
    '''エンターキーを押さずに入力を受け取るクラス'''

    @staticmethod
    def input_without_enter():
        '''エンターキーを押さずに入力を受け取る
        Returns:
            str: 入力された文字
        '''

        # 標準入力のファイルディスクリプタを取得
        fd = sys.stdin.fileno()

        # fdの端末属性をゲットする
        # oldとnewには同じものが入る。
        # newに変更を加えて、適応する
        # oldは、後で元に戻すため
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)

        # new[3]はlflags
        # ICANON(カノニカルモードのフラグ)を外す
        new[3] &= ~termios.ICANON
        # ECHO(入力された文字を表示するか否かのフラグ)を外す
        new[3] &= ~termios.ECHO

        try:
            # 書き換えたnewをfdに適応する
            termios.tcsetattr(fd, termios.TCSANOW, new)
            # キーボードから入力を受ける。
            # lfalgsが書き換えられているので、エンターを押さなくても次に進む。echoもしない
            ch = sys.stdin.read(1)

        finally:
            # fdの属性を元に戻す
            # 具体的にはICANONとECHOが元に戻る
            termios.tcsetattr(fd, termios.TCSANOW, old)

        return ch


class UserInput:
    """ユーザーの入力を受け取るクラス"""

    # クラス変数でキー押下回数をカウント
    key_press_count = 0

    def get_user_input(self) -> tuple[int, int]:
        """ユーザの入力を受けとり、x, y座標の差分とキー押下回数を返す
        Returns:
            tuple[int, int, int]: x, y座標の差分とキー押下回数
        """
        # キー入力を受け取る
        key = InputWithoutEnter.input_without_enter()
        # キーが入力されたのでカウントを増やす
        self.key_press_count += 1
        # 入力されたキーに対応する座標の差分を返す
        if key == "w":
            return (0, -1)
        elif key == "a":
            return (-1, 0)
        elif key == "s":
            return (0, 1)
        elif key == "d":
            return (1, 0)
        else:
            # 無効なキーの場合、座標差分は(0, 0)
            return (0, 0)


if __name__ == "__main__":
    print("キーを押してください (終了するには Ctrl+C):")
    user_input = UserInput()
    try:
        while True:
            x, y = user_input.get_user_input()
            print(f"x: {x}, y: {y}, キー押下回数: {user_input.key_press_count}")
    except KeyboardInterrupt:
        print("\n終了します。")
