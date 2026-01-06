def detect_crypto_type(text: str) -> str:
    text = text.strip()

    if text.startswith(("$2a$", "$2b$", "$2y$")):
        return "bcrypt"

    if text.startswith("gAAAAA"):
        return "fernet"

    return "unknown"
