# PyDolphyn	 		             //
# Version 1.0	 		        ('>
# 0110002 			            /rr
# ©2023 by KralicekGamer       *\))_


# import
import os
from apk import lgbt, dolphyn, rusian_roulette, marcus_x
from apk.etc import colors, sys

# main
if __name__ == "__main__":
    sys.welcome()
    while True:
        command = input(colors.green + ">>> " + colors.reset)
        command = command.replace(" ", "")
        command = command.lower()

        if command == "help":
            print("""
CLEAR-clear terminal
DOLPHYN-trust me.. i am dolphyn
EXIT-exit
LGBT-not for epileptics
MARCUS X-6 firem za 3 roky
RUSIAN ROULETTE-idk
            """)

        elif command == "exit":
            exit_rl = input("Exit [y/n] ")
            if exit_rl == "y":
                exit()
            elif exit_rl == "n":
                print("")
                pass
            else:
                print(colors.red + "Invalid character")
                print("")

        elif command == "clear":
            os.system("cls")
            sys.welcome()

        elif command == "lgbt":
            lgbt.cmd()

        elif command == "dolphyn":
            os.system("cls")
            dolphyn.cmd()
            os.system("cls")
            sys.welcome()

        elif command == "rusianroulette":
            rusian_roulette.cmd()
            print("")

        elif command == "markusx":
            marcus_x.cmd()

        else:
            print(colors.red + "Invalid command\n" + colors.reset)
