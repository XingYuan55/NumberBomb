# -*- coding: gbk -*-
import random
import types
from datetime import datetime
from colorama import Fore, Style, init as init_


class NumberBomb:
    def __init__(self):
        self.log_fp = open("log.log", 'a')
        self.log(f"== {str(datetime.now())} ==")
        self.basic_log_map = {9: "L009: �û��˳�", 10: "L010: ���÷�Χʱʹ��Ĭ��ֵ(0, 100)", 11: "L01: ���÷�Χʱʹ���Զ���ֵ",
                              20: "L020: �û�����²���ֵ", 22: "L022: ������Χ���", 23: "L023: �²���ֵ��Ч", 25: "L025: һ����Ϸ��������",
                              26: "L026: һ����Ϸ��ǰ����"}
        init_(wrap=True)

        cmd = ''
        while cmd.lower() != 'quit':
            self.ans = None
            self.edge = [0, 100]

            print("""�٣���ã���ӭ����������ը����
            ����quit�˳������������뿪ʼ��Χ�ͽ�����Χ��
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
                print("��ò��û������һ����Ч��ֵ�ޣ��Ѿ���ΪĬ��ֵ(0, 100)��")

            # TODO  һ����Ϸ
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
                userinput = int(input("������µ������������˴�-1����"))
            except:
                self.log(self.basic_log_map[23], userinput)
                continue

            self.log(self.basic_log_map[20], userinput)

            if userinput == -1:
                self.log(self.basic_log_map[26])
                return

            if (userinput < self.edge[0]) or (userinput > self.edge[1]):
                print(f"��Χ����Ӧ����{self.edge[0]}��{self.edge[1]}֮�����")
                self.log(self.basic_log_map[23], self.edge)
                continue

            if userinput < self.ans:
                self.edge[0] = userinput
                print(f"��С����ǰ��Χ��{self.edge[0]}��{self.edge[1]}")
                self.log(self.basic_log_map[22], self.edge)

            elif userinput > self.ans:
                self.edge[1] = userinput
                print(f"���󡣵�ǰ��Χ��{self.edge[0]}��{self.edge[1]}")
                self.log(self.basic_log_map[22], self.edge)

        print(Style.BRIGHT + Fore.RED+"B"+Fore.YELLOW+"O"+Fore.LIGHTRED_EX+"O"+Fore.LIGHTYELLOW_EX+"M" + Fore.RESET + "ը��")
        self.log(self.basic_log_map[25])
        input("���ո�����һ��" + Style.RESET_ALL)


    def log(self, msg, *other):
        oth = ""
        for o in other:
            try:
                oth += " " + str(o)
            except:
                break
        self.log_fp.write(datetime.now().ctime() + ": " + msg + oth + "\n")

    def close(self):
        self.log(self.basic_log_map[9], "ǿ�ƽ���")
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


