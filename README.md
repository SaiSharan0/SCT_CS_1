# 🔐 Caesar Cipher Encryption & Decryption Tool

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Internship](https://img.shields.io/badge/SkillCraft%20Technology-Task%2001-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

> **SCT_CS_1** | SkillCraft Technology – Cyber Security Internship | Task 01

---

## 📌 Project Overview

This project implements the classic **Caesar Cipher** algorithm in Python — one of the oldest and simplest substitution ciphers in cryptography.

The Caesar Cipher works by shifting each letter in a plaintext message by a fixed number of positions (called the **shift value** or **key**) down the alphabet. For example, with a shift of 3: `A → D`, `B → E`, `H → K`.

This tool provides a **menu-driven command-line interface** for:
- Encrypting messages
- Decrypting messages (with a known key)
- Brute-force decryption (trying all 25 possible shifts)
- Educational content about how the cipher works

---

## 🧠 What is Caesar Cipher?

The **Caesar Cipher** is a *substitution cipher* — the oldest documented cipher technique, reportedly used by Julius Caesar to protect his military communications around **58 BC**.

### Encryption Formula
```
Encrypted_char = (original_position + shift) mod 26
```

### Decryption Formula
```
Decrypted_char = (encrypted_position - shift + 26) mod 26
```

### Example (Shift = 3)
```
Plaintext  :  H  E  L  L  O     W  O  R  L  D
Position   :  7  4  11 11 14    22 14 17 11 3
+Shift 3   : 10  7  14 14 17    25 17 20 14 6
Ciphertext :  K  H  O  O  R     Z  R  U  O  G
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔒 **Encrypt** | Convert plaintext to ciphertext using a custom shift |
| 🔓 **Decrypt** | Recover original message using the same shift |
| 🔨 **Brute-Force** | Try all 25 possible shifts (demonstrates cipher weakness) |
| 📚 **Learn Mode** | In-app educational content about Caesar Cipher |
| 🧪 **Test Cases** | Built-in validation with 8 test scenarios |
| ✅ **Input Validation** | Graceful error handling for all user inputs |
| 🔁 **Loop Menu** | Perform multiple operations without restarting |
| 🔡 **Case Aware** | Handles uppercase and lowercase independently |
| 🔢 **Preserves Non-Letters** | Numbers, spaces, punctuation stay unchanged |

---

## 📁 Project Structure

```
caesar_cipher_tool/
│
├── caesar_cipher.py        ← Main program (all logic + UI)
├── README.md               ← This file
└── internship_report.md    ← Full internship report
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- No third-party libraries required

### Running the Program
```bash
# Clone the repository
git clone https://github.com/SaiSharan0/SCT_CS_1.git

# Navigate to the project folder
cd SCT_CS_1

# Run the program
python caesar_cipher.py
```

---

## 🖥️ Sample Usage

### Encrypting a Message
```
Enter plaintext (message to encrypt): Hello, World!
Enter shift value (1–25): 3

  Original Message  : Hello, World!
  Shift Value       : 3
  Encrypted Message : Khoor, Zruog!
```

### Decrypting a Message
```
Enter ciphertext (message to decrypt): Khoor, Zruog!
Enter shift value (1–25): 3

  Encrypted Message : Khoor, Zruog!
  Shift Value       : 3
  Decrypted Message : Hello, World!
```

### Brute-Force (All 25 shifts shown)
```
  Shift 01 → Jgnnq, Vqtnf!
  Shift 02 → Ifmmp, Umpme!
  Shift 03 → Hello, World!   ← Original message revealed!
  Shift 04 → Gdkkn, Vnqkc!
  ...
```

---

## 🧪 Test Cases

| # | Input                   | Shift | Expected Output         | Status   |
|---|-------------------------|-------|-------------------------|---------|
| 1 | `hello world`           | 3     | `khoor zruog`           | ✅ PASS |
| 2 | `HELLO WORLD`           | 3     | `KHOOR ZRUOG`           | ✅ PASS |
| 3 | `Hello, World!`         | 3     | `Khoor, Zruog!`         | ✅ PASS |
| 4 | `Attack at 0600 hours!` | 7     | `Haahjr ha 0600 ovbyz!` | ✅ PASS |
| 5 | `XYZ`                   | 3     | `ABC`                   | ✅ PASS |
| 6 | `A`                     | 1     | `B`                     | ✅ PASS |
| 7 | `ABCDE...Z`             | 25    | `ZABCD...Y`             | ✅ PASS |
| 8 | `Secure the network`    | 13    | `Frpher gur argjbex`    | ✅ PASS |

---

## ⚙️ Algorithm Analysis

| Metric               | Value            |
|----------------------|------------------|
| **Time Complexity**  | O(n) — linear    |
| **Space Complexity** | O(n) — linear    |
| **Key Space**        | 25 possible keys |
| **Brute-Force Time** | < 1 second       |

---

## ⚠️ Limitations (Why Caesar Cipher Is Insecure)

1. **Tiny key space** — only 25 possible shifts; brute-force takes milliseconds
2. **Frequency analysis** — in English, 'E' is most common; patterns are visible
3. **No diffusion** — same input letter always maps to same output letter
4. **No confusion** — relationship between key and ciphertext is trivial
5. **Modern standard** — AES-256 requires 2²⁵⁶ attempts to brute-force; Caesar Cipher requires just 25

---

## 🌍 Real-World Cryptography

| Algorithm     | Type          | Use Case                         |
|---------------|---------------|----------------------------------|
| Caesar Cipher | Substitution  | Education only                   |
| AES-256       | Symmetric     | Banking, VPNs, file encryption   |
| RSA           | Asymmetric    | Key exchange, digital signatures |
| SHA-256       | Hash function | Password storage, blockchain     |
| ChaCha20      | Stream cipher | TLS, mobile encryption           |

---

## 🧩 Skills Demonstrated

- Python fundamentals (loops, functions, conditionals)
- Modular arithmetic and ASCII character manipulation
- Input validation and error handling
- Menu-driven CLI application design
- Cryptographic concepts: plaintext, ciphertext, keys, shift ciphers
- Understanding of brute-force attacks and cipher weaknesses

---

## 📸 Screenshots to Take

1. **Main menu** — showing all 6 options
2. **Encryption result** — plaintext → ciphertext
3. **Decryption result** — ciphertext → plaintext
4. **Brute-force output** — all 25 shifts listed
5. **Test cases output** — all ✓ PASS
6. **Learn mode** — educational text displayed

---

## 👤 Author

**Talari Sai Sharan**  
B.Tech CSE(Cyber Security)  
Koneru Lakshmaiah Education Foundation, Hyderabad
SkillCraft Technology – Cyber Security Internship  
GitHub: [@SaiSharan0](https://github.com/SaiSharan0)

---

## 📜 License

This project is open source under the [MIT License](LICENSE).

---

*Task 01 of 4 | SkillCraft Technology Cyber Security Track*
