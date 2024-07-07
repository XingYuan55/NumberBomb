# -*- coding: gbk -*-
import random
import types
from datetime import datetime
from colorama import Fore, Style, init as init_


class NumberBomb:
    def __init__(self):
        self.log_fp = open("log.log", 'a')
        self.log(f"== {str(datetime.now())} ==")
        self.basic_log_map = {9: "L009: 用户退出", 10: "L010: 设置范围时使用默认值(0, 100)", 11: "L01: 设置范围时使用自定义值",
                              20: "L020: 用户输入猜测数值", 22: "L022: 猜数范围变更", 23: "L023: 猜测数值无效", 25: "L025: 一轮游戏正常结束",
                              26: "L026: 一轮游戏提前结束"}
        init_(wrap=True)

        cmd = ''
        while cmd.lower() != 'quit':
            self.ans = None
            self.edge = [0, 100]

            print("""嘿，你好，欢迎来到【数字炸弹】
            输入quit退出，否则请输入开始范围和结束范围：
            """)

            cmd = input().lower()

            if cmd == 'quit':
                self.log(self.basic_log_map[9])
                break

            try:
                for i in range(2):
                    self.edge[i] = int(cmd.split(" ")[i])
                    self.log(self.basic_log_map[11], str(self.edge))

            except:
                self.log(self.basic_log_map[10])
                print("你貌似没有输入一个有效数值噢，已经设为默认值(0, 100)了")

            # TODO  一轮游戏
            try:
                self.guess_game()
            except KeyboardInterrupt:
                self.close()

        self.log_fp.close()

    def guess_game(self):
        self.ans = random.randint(*self.edge)
        userinput = None
        while userinput != self.ans:
            try:
                userinput = int(input("请输入猜的数（不想玩了打-1）："))
            except:
                self.log(self.basic_log_map[23], userinput)
                continue

            self.log(self.basic_log_map[20], userinput)

            if userinput == -1:
                self.log(self.basic_log_map[26])
                return

            if (userinput < self.edge[0]) or (userinput > self.edge[1]):
                print(f"范围有误，应输入{self.edge[0]}至{self.edge[1]}之间的数")
                self.log(self.basic_log_map[23], self.edge)
                continue

            if userinput < self.ans:
                self.edge[0] = userinput
                print(f"过小。当前范围：{self.edge[0]}至{self.edge[1]}")
                self.log(self.basic_log_map[22], self.edge)

            elif userinput > self.ans:
                self.edge[1] = userinput
                print(f"过大。当前范围：{self.edge[0]}至{self.edge[1]}")
                self.log(self.basic_log_map[22], self.edge)

        print(Style.BRIGHT + Fore.RED+"B"+Fore.YELLOW+"O"+Fore.LIGHTRED_EX+"O"+Fore.LIGHTYELLOW_EX+"M" + Fore.RESET + "炸了")
        self.log(self.basic_log_map[25])
        input("按空格开启下一局" + Style.RESET_ALL)


    def log(self, msg, *other):
        oth = ""
        for o in other:
            try:
                oth += " " + str(o)
            except:
                break
        self.log_fp.write(datetime.now().ctime() + ": " + msg + oth + "\n")

    def close(self):
        self.log(self.basic_log_map[9], "强制结束")
        self.log_fp.close()
        exit(-3)


try:
    game = NumberBomb()
except KeyboardInterrupt:
    try:
        game.close()
        exit(-3)
    except NameError:
        exit(-2)


