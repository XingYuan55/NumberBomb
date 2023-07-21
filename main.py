from datetime import datetime


class NumberBomb:
    def __init__(self):
        self.log_fp = open("log.log", 'a')
        self.log(f"== {str(datetime.now())} ==")
        self.basic_log_map = {9: "L009: 用户退出", 10:"L010: 设置范围时使用默认值(0, 100)"}
        self.edge = [0, 100]

        cmd = ''
        while cmd.lower() != 'quit':
            print("""嘿，你好，欢迎来到【数字炸弹】
            输入quit退出，否则请输入开始范围和结束范围：
            """)
            cmd = input().lower()
            if cmd == 'quit':
                self.log(self.basic_log_map[9])
                break

            try:
                for i in range(2):
                    self.edge[i] = cmd.split(" ")[i]

            except:
                self.log(self.basic_log_map[10])
                print("你貌似没有输入一个有效数值噢，已经设为默认值(0, 100)了")

            # TODO  一轮游戏

        self.log_fp.close()

    def log(self, msg):
        self.log_fp.write(str(datetime.time) + ": " + msg)


game = NumberBomb()
