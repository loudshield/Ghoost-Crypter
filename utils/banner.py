from colorama import Fore, Style

def show_banner():
    print(Fore.RED + r"""
 ██████╗ ██╗  ██╗ ██████╗  ██████╗ ███████╗████████╗
██╔════╝ ██║  ██║██╔═══██╗██╔═══██═██╔════╝╚══██╔══╝
██║  ███╗███████║██║   ██║██║   ██╗███████╗   ██║   
██║   ██║██╔══██║██║   ██║██║   ██║╚════██║   ██║   
╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝███████║   ██║   
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   
    """ + Style.RESET_ALL)
    print(Fore.LIGHTRED_EX + "        GHOOST CRYPTER   \n" + Style.RESET_ALL)

    print(Fore.WHITE + "Welcome to Ghoost Crypter.")
    print(Fore.WHITE + "Type " +
      Fore.GREEN + "help" +
      Fore.WHITE + " to see the list of available commands.")

