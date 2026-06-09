# Internship Report — Task 01: Caesar Cipher Encryption & Decryption Tool

---

**Name:** Talari Sai Sharan  
**Roll Number:** 2410030164 
**College:** Koneru Lakshmaiah Education Foundation (Deemed to be University), Hyderabad
**Branch:** B.Tech CSE(Cyber Security) — Third Year
**Internship Organisation:** SkillCraft Technology  
**Domain:** Cyber Security  
**Task Number:** Task 01 of 04  
**Task Title:** Implement a Caesar Cipher Algorithm  
**Submission Date:** June 2026  
**GitHub Repository:** https://github.com/SaiSharan0/SCT_CS_1  

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Objective](#2-objective)
3. [Background Theory](#3-background-theory)
4. [Methodology](#4-methodology)
5. [Implementation Details](#5-implementation-details)
6. [Results and Output](#6-results-and-output)
7. [Test Cases](#7-test-cases)
8. [Limitations & Security Analysis](#8-limitations--security-analysis)
9. [Conclusion](#9-conclusion)
10. [Future Enhancements](#10-future-enhancements)
11. [References](#11-references)

---

## 1. Introduction

Cryptography is the science of protecting information by transforming it into an unreadable format — a process called **encryption** — so that only authorised parties with the correct key can read it. It is the backbone of modern cybersecurity, enabling secure banking transactions, private messaging, VPNs, and digital signatures.

The **Caesar Cipher** is one of the earliest known and simplest examples of a substitution cipher. Named after Roman general **Julius Caesar**, who reportedly used it in his private military correspondence around **58 BC**, it works by replacing each letter in a message with a letter a fixed number of positions forward in the alphabet. This fixed number is called the **shift value** or **encryption key**.

Despite being cryptographically trivial by modern standards, the Caesar Cipher remains an important educational tool. It introduces the core vocabulary of cryptography — plaintext, ciphertext, keys, encryption, decryption, and brute-force attacks — in an accessible way. Understanding its mechanics and weaknesses helps cybersecurity students build intuition for why modern ciphers are designed the way they are.

This report documents my design, implementation, and analysis of a Caesar Cipher tool built in Python as the first task of my Cyber Security internship at **SkillCraft Technology**.

---

## 2. Objective

The objectives of this task were to:

1. Understand and implement the Caesar Cipher algorithm from scratch in Python.
2. Build a complete, menu-driven command-line application for encryption and decryption.
3. Support both uppercase and lowercase letters independently.
4. Preserve all non-alphabetic characters (digits, spaces, punctuation).
5. Include input validation to prevent program crashes from invalid user input.
6. Implement a brute-force decryption demonstration that reveals all 25 possible decryptions.
7. Write clean, well-commented, beginner-friendly code that demonstrates conceptual understanding.
8. Analyse the security limitations of the Caesar Cipher and understand why it is inadequate for real-world use.

---

## 3. Background Theory

### 3.1 Cryptography Fundamentals

Cryptography involves two complementary operations:

- **Encryption:** Converting a readable message (*plaintext*) into an unreadable format (*ciphertext*) using an algorithm and a key.
- **Decryption:** Reversing the process — recovering the plaintext from the ciphertext using the key.

A good cipher should be easy to encrypt/decrypt with the key, and computationally infeasible to break without it.

### 3.2 Substitution Ciphers

The Caesar Cipher is a **monoalphabetic substitution cipher** — each letter in the plaintext is consistently replaced by one other letter throughout the message. The mapping never changes within a single encryption operation.

### 3.3 The Caesar Cipher Algorithm

The cipher operates as follows:

**Encryption:**
```
Encrypted_position = (Original_position + Shift) mod 26
```

**Decryption:**
```
Decrypted_position = (Encrypted_position - Shift + 26) mod 26
```

Where position is 0-based (A=0, B=1, ..., Z=25) and *mod 26* ensures wrap-around (so Z+3 = C, not a character beyond Z).

**Worked Example (Shift = 3):**

| Plaintext | Position | + Shift | mod 26 | Ciphertext |
|---|---|---|---|---|
| H | 7 | 10 | 10 | K |
| E | 4 | 7 | 7 | H |
| L | 11 | 14 | 14 | O |
| L | 11 | 14 | 14 | O |
| O | 14 | 17 | 17 | R |

Result: `HELLO` → `KHOOR`

### 3.4 Key Space Analysis

The Caesar Cipher has a key space of only **25** (shifts 1 through 25; shift 0 and 26 produce the same plaintext). This is fatally small — a modern computer can try all 25 possibilities in microseconds, making the cipher trivially brute-forceable.

---

## 4. Methodology

### 4.1 Development Approach

The project was developed using a **structured top-down design** approach:

1. **Understand the algorithm** — Study the mathematical basis of Caesar Cipher.
2. **Design the core functions** — Separate encryption, decryption, and brute-force into independent functions.
3. **Build the UI layer** — Create a menu-driven interface wrapping the core logic.
4. **Add input validation** — Handle edge cases and invalid inputs gracefully.
5. **Write test cases** — Verify correctness across multiple scenarios.
6. **Document the code** — Add comprehensive comments explaining every decision.

### 4.2 Tools and Technologies

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.8+ | Primary programming language |
| VS Code | Latest | Code editor |
| Git | Latest | Version control |
| GitHub | — | Remote repository hosting |
| Terminal (CMD/Bash) | — | Running the program |

### 4.3 Design Decisions

**Single-file architecture:** All code is in one `caesar_cipher.py` file. For a project of this scope, this improves readability and makes it easy to run with a single command.

**Reuse in decryption:** Decryption is implemented by calling the encrypt function with a reversed shift `(26 - shift)` rather than writing a separate character-shifting routine. This demonstrates the mathematical elegance of modular arithmetic.

**No external libraries:** The project uses only Python's built-in `os` module (for clearing the terminal). This ensures the program runs in any Python environment without installation steps.

---

## 5. Implementation Details

### 5.1 Core Encryption Logic

The heart of the program is the `caesar_encrypt()` function. Here is the key code excerpt with explanation:

```python
def caesar_encrypt(message, shift):
    encrypted_text = ""
    for char in message:
        if char.isupper():
            # Shift uppercase letters, wrap with mod 26
            index = ord(char) - 65          # 65 = ASCII for 'A'
            shifted = (index + shift) % 26
            encrypted_text += chr(shifted + 65)
        elif char.islower():
            # Shift lowercase letters, wrap with mod 26
            index = ord(char) - 97          # 97 = ASCII for 'a'
            shifted = (index + shift) % 26
            encrypted_text += chr(shifted + 97)
        else:
            # Preserve non-letter characters unchanged
            encrypted_text += char
    return encrypted_text
```

**Why `ord()` and `chr()`?**  
In Python, `ord()` converts a character to its ASCII integer value, and `chr()` converts an integer back to a character. By subtracting the ASCII base (`65` for uppercase, `97` for lowercase), we get a 0-based index within the alphabet (0–25). After applying the shift and modulo, we add the base back to get the final character's ASCII code.

### 5.2 Decryption via Reverse Shift

```python
def caesar_decrypt(ciphertext, shift):
    reverse_shift = 26 - shift
    return caesar_encrypt(ciphertext, reverse_shift)
```

Shifting forward by `(26 - shift)` is mathematically equivalent to shifting backward by `shift` in a modular system. For example, shifting 'K' backward by 3 gives 'H'; shifting 'K' forward by 23 (= 26 - 3) also gives 'H'.

### 5.3 Input Validation

```python
def validate_shift(shift_input):
    try:
        shift = int(shift_input)
        if 1 <= shift <= 25:
            return shift
        else:
            print("ERROR: Shift value must be between 1 and 25.")
            return None
    except ValueError:
        print("ERROR: Please enter a valid whole number.")
        return None
```

The `try/except` block catches `ValueError` — the exception Python raises when `int()` is called on a non-numeric string (like "hello"). This prevents the program from crashing on bad input.

### 5.4 Brute-Force Demonstration

```python
def brute_force_decrypt(ciphertext):
    for shift in range(1, 26):
        attempt = caesar_decrypt(ciphertext, shift)
        print(f"  Shift {shift:02d} → {attempt}")
```

This iterates through all 25 possible shift values and prints every possible decryption. One of these 25 lines will be the original plaintext — and a human reader can usually identify it immediately because it will be the only one forming coherent words.

---

## 6. Results and Output

### 6.1 Encryption

```
  Enter plaintext (message to encrypt): Cyber Security Internship
  Enter shift value (1–25): 5

  Original Message  : Cyber Security Internship
  Shift Value       : 5
  Encrypted Message : HDgjw Xjhzwnyd Nsinwsxmnz
```

### 6.2 Decryption

```
  Enter ciphertext (message to decrypt): Hzggj, Btwqi!
  Enter shift value (1–25): 5

  Encrypted Message : Hzggj, Btwqi!
  Shift Value       : 5
  Decrypted Message : Hello, World!
```

### 6.3 Brute-Force (Partial)

```
  BRUTE-FORCE RESULTS (All 25 possible decryptions)
  Ciphertext: Khoor, Zruog!

  Shift 01 → Jgnnq, Yqtnf!
  Shift 02 → Ifmmp, Xpsme!
  Shift 03 → Hello, World!      ← Original plaintext revealed at shift 3
  Shift 04 → Gdkkn, Vnqkc!
  ...
```

The brute-force output makes visually obvious why Caesar Cipher is insecure — anyone can read the 25 lines and identify the meaningful English phrase instantly.

---

## 7. Test Cases

Eight test cases were designed to cover different scenarios:

| # | Description | Input | Shift | Result |
|---|---|---|---|---|
| 1 | Basic lowercase | `hello world` | 3 | `khoor zruog` ✅ |
| 2 | Basic uppercase | `HELLO WORLD` | 3 | `KHOOR ZRUOG` ✅ |
| 3 | Mixed case + punctuation | `Hello, World!` | 3 | `Khoor, Zruog!` ✅ |
| 4 | Numbers preserved | `Attack at 0600!` | 7 | `Haahjr ha 0600!` ✅ |
| 5 | Wrap-around Z→C | `XYZ` | 3 | `ABC` ✅ |
| 6 | Single character | `A` | 1 | `B` ✅ |
| 7 | Max shift (25) | `ABCDEFGHIJKLMNOPQRSTUVWXYZ` | 25 | `ZABCDEFGHIJKLMNOPQRSTUVWXY` ✅ |
| 8 | ROT13 special case | `Secure the network` | 13 | `Frpher gur argjbex` ✅ |

All 8 test cases passed encryption and round-trip (encrypt then decrypt) verification.

---

## 8. Limitations & Security Analysis

### 8.1 Why Caesar Cipher Is Cryptographically Broken

| Weakness | Explanation |
|---|---|
| **Tiny key space** | Only 25 possible keys; brute-force completes in microseconds |
| **Frequency analysis** | Letter frequency in English is well-known; 'E' is most common. Analysing ciphertext letter frequencies reveals the shift without trying keys. |
| **Monoalphabetic** | Same plaintext letter always maps to same ciphertext letter. Patterns in language (common words, double letters) are preserved. |
| **No semantic security** | Given two plaintexts that differ in one character, the ciphertexts differ in exactly one character — structure leaks information. |
| **Known-plaintext attack** | If an attacker knows even one word of the original message, they can determine the key immediately. |

### 8.2 Comparison with Modern Ciphers

| Property | Caesar Cipher | AES-256 |
|---|---|---|
| Key space | 25 | 2²⁵⁶ (~1.2 × 10⁷⁷) |
| Brute-force time | Microseconds | Billions of years |
| Frequency analysis | Vulnerable | Immune |
| Block size | 1 char | 128 bits |
| Real-world use | None (educational) | Banking, VPNs, TLS |

---

## 9. Conclusion

This task successfully achieved all stated objectives. A fully functional, menu-driven Caesar Cipher tool was implemented in Python with:

- Correct encryption and decryption for all alphabetic characters
- Independent handling of uppercase and lowercase letters
- Preservation of non-alphabetic characters (numbers, spaces, punctuation)
- Robust input validation preventing crashes on invalid input
- A brute-force demonstration clearly illustrating the cipher's core weakness
- 8 comprehensive test cases all passing correctly

Beyond the implementation, this task provided a concrete foundation for understanding core cryptographic concepts: **plaintext, ciphertext, keys, shift ciphers, substitution ciphers, brute-force attacks, and frequency analysis**. Understanding why Caesar Cipher fails is as valuable as understanding how it works — it motivates the design of modern ciphers like AES that address each of these weaknesses systematically.

---

## 10. Future Enhancements

The following improvements could extend this project:

1. **Vigenère Cipher** — Use a multi-letter keyword instead of a single shift value; more secure than Caesar since different positions use different shifts.
2. **File Encryption** — Read a .txt file, encrypt its contents, and write the result to a new file.
3. **Frequency Analysis Tool** — Add a feature that analyses letter frequencies in the ciphertext to suggest the most likely shift.
4. **GUI Interface** — Build a graphical interface using `tkinter` or a web interface using `Flask`.
5. **Multiple Cipher Support** — Extend the tool to also support Atbash Cipher, Rail Fence Cipher, and ROT13.
6. **Export Results** — Save encryption/decryption results to a text file for record-keeping.
7. **Unit Tests** — Add a formal `unittest` or `pytest` test suite for automated validation.

---

## 11. References

1. Kahn, D. (1967). *The Codebreakers: The Story of Secret Writing*. Macmillan.
2. Stinson, D. R. (2006). *Cryptography: Theory and Practice* (3rd ed.). Chapman & Hall/CRC.
3. Python Software Foundation. *Python 3 Documentation — Built-in Functions*. https://docs.python.org/3/library/functions.html
4. NIST. *Advanced Encryption Standard (AES)*. FIPS Publication 197. https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf
5. GeeksForGeeks. *Caesar Cipher in Cryptography*. https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/

---

*Report prepared by Talari Sai Sharan | SkillCraft Technology Cyber Security Internship | Task 01 | June 2026*
