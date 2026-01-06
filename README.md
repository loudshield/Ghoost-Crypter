# 👻 GHOOST CRYPTER

**Ghoost Crypter** is a minimal, terminal-based password cryptography tool written in **Python**.
It allows you to **hash, encrypt, decrypt, and analyze passwords** securely, with a clean CLI interface and local history storage.

Designed to feel like a real hacking / security utility.

---

## ✨ Features

- 🔐 **Password Hashing** (bcrypt – one-way)
- 🔒 **Password Encryption & Decryption** (AES / Fernet)
- 🧠 **Automatic crypto type detection**
- 🕘 **Local history** of hashed & encrypted entries
- 🎨 **Colored CLI interface** (Windows compatible)
- 📦 **Automatic dependency installation**
- 🔄 **Update checker via GitHub**
- 🧹 `clear` command to clean terminal


## 🚀 Installation & Usage (Windows)

### 2️⃣ Start the application

👉 **Double-click**:
```
start.bat
```

or from terminal:
```bat
start.bat
```

---

## ⌨️ Available Commands

```
[CMD] help      Show all available commands
[CMD] hash      Hash a password using bcrypt (non-reversible)
[CMD] encrypt   Encrypt a password using AES (reversible)
[CMD] decrypt   Decrypt an encrypted text (auto-detection)
[CMD] history   Show local encryption/hash history
[CMD] version   Show current version
[CMD] update    Check for updates on GitHub
[CMD] clear     Clear the terminal screen
[CMD] exit      Exit the application
```

---


## 🗂️ Structure

```
ghoost_crypter/
│
├── main.py
├── start.bat
├── requirements.txt
├── README.md
│
├── crypto/
│   ├── hasher.py
│   └── encryptor.py
│
├── utils/
│   ├── banner.py
│   ├── clear.py
│   ├── detector.py
│   ├── update.py
│   └── version.py
│
├── ui/
│   └── menu.py
│
└── storage/
    └── history.py
```

---


## 📦 Requirements

Automatically installed, but listed here for reference:

- `colorama`
- `rich`
- `bcrypt`
- `cryptography`
- `requests`

---

## 👻 Author

Created by **LoudShield**

> *"If you use this script to improve it, please give me credit."*

