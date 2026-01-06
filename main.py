from rich.console import Console
from colorama import Fore, Style, init
import getpass
from utils.banner import show_banner
from utils.clear import clear_screen
from utils.version import VERSION
from utils.update import check_for_updates
from utils.detector import detect_crypto_type

from ui.menu import show_help

from crypto.hasher import hash_password
from crypto.encrypter import encrypt, decrypt

from storage.history import save_history, load_history

init(autoreset=True)

console = Console()


def main():
    clear_screen()
    show_banner()

    user = getpass.getuser()

    while True:
        try:
            prompt = (
                Fore.LIGHTRED_EX + "ghoost" + Style.RESET_ALL +
                f"@{user}:-$ "
            )

            command = input(prompt).strip().lower()

            if command == "":
                continue

            if command == "help":
                show_help()

            elif command == "version":
                console.print(
                    f"[bold red]GHOOST CRYPTER[/bold red] [white]{VERSION}[/white]"
                )

            elif command == "update":
                result = check_for_updates()

                if result["status"] == "ok":
                    console.print(
                        f"[green]You are using the latest version ({result['version']})[/green]"
                    )

                elif result["status"] == "update":
                    console.print("[yellow]Update available![/yellow]")
                    console.print(f"Current version: {result['current']}")
                    console.print(f"Latest version:  {result['latest']}")
                    console.print(f"Download: {result['url']}")

                else:
                    console.print("[red]Could not check for updates[/red]")

            elif command == "hash":
                password = input("Password: ")
                hashed = hash_password(password)
                save_history("hash", "bcrypt", hashed)
                console.print("[green]Hash generated successfully:[/green]")
                console.print(hashed)

            elif command == "encrypt":
                password = input("Password: ")
                encrypted = encrypt(password)
                save_history("encrypt", "AES (Fernet)", encrypted)
                console.print("[green]Encrypted text:[/green]")
                console.print(encrypted)

            elif command == "decrypt":
                token = input("Encrypted text: ").strip()
                crypto_type = detect_crypto_type(token)

                if crypto_type == "bcrypt":
                    console.print(
                        "[red]Error:[/red] This is a bcrypt hash and cannot be decrypted."
                    )

                elif crypto_type == "fernet":
                    try:
                        decrypted = decrypt(token)
                        save_history("decrypt", "AES (Fernet)", decrypted)
                        console.print("[green]Decrypted text:[/green]")
                        console.print(decrypted)
                    except Exception:
                        console.print("[red]Error: Invalid encrypted token[/red]")

                else:
                    console.print(
                        "[red]Error:[/red] Unknown or unsupported encrypted format."
                    )

            elif command == "history":
                history = load_history()
                if not history:
                    console.print("[yellow]History is empty[/yellow]")
                else:
                    for entry in history:
                        console.print(entry)

            elif command == "clear":
                clear_screen()
                show_banner()

            elif command == "exit":
                console.print("[bold red]Exiting GHOOST CRYPTER...[/bold red]")
                break

            else:
                console.print(
                    "[red]Unknown command.[/red] "
                    "Type [bold green]'help'[/bold green] to see available commands."
                )

        except KeyboardInterrupt:
            console.print("\n[bold red]Interrupted. Exiting...[/bold red]")
            break


if __name__ == "__main__":
    main()
