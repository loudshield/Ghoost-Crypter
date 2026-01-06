from rich.console import Console
from rich.text import Text

console = Console()


def show_help():
    console.print("\n[bold white]Available commands:\n")

    commands = [
        ("help",    "Show this hmenu with all available commands"),
        ("hash",    "Securely hash a password using bcrypt (no-reversible)"),
        ("encrypt", "Encrypt a password using AES (reversible)"),
        ("decrypt", "Decrypt a previously encrypted text"),
        ("history", "Display the local history of encrypted and hashed entries"),
        ("version", "Display current version of GHOOST CRYPTER"),
        ("update",  "Check for updates from the official GitHub repository"),
        ("clear",   "Clear the terminal screen"),
        ("exit",    "Exit the tool"),
    ]

    for name, description in commands:
        line = Text()
        line.append("[CMD] ", style="bold red")
        line.append(f"{name:<10}", style="bold white")
        line.append(description, style="white")
        console.print(line)

    console.print()
