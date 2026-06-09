"""
================================================================================
PROJECT    : Caesar Cipher Encryption & Decryption Tool
AUTHOR     : Talari Sai Sharan
INTERNSHIP : SkillCraft Technology – Cyber Security Track
TASK       : Task 01 – Implement a Caesar Cipher Algorithm
DATE       : June 2026
GITHUB     : https://github.com/SaiSharan0/SCT_CS_1
================================================================================

  DESCRIPTION:
  ------------
  This program implements the classic Caesar Cipher – one of the oldest and
  simplest substitution cipher techniques in cryptography.

  The Caesar Cipher works by shifting each letter in the plaintext by a fixed
  number of positions (called the "shift value" or "key") down the alphabet.

  EXAMPLE:
    Plaintext  : H E L L O
    Shift      : 3
    Ciphertext : K H O O R

  The reverse process (subtracting the shift) gives back the original message.

  HOW ENCRYPTION WORKS:
  ---------------------
  For each character in the message:
    1. Check if it is an uppercase letter (A–Z).
    2. Check if it is a lowercase letter (a–z).
    3. If neither, leave it unchanged (numbers, spaces, punctuation stay as-is).
    4. Find the position of the letter in the alphabet (0–25 using ASCII math).
    5. Add the shift value to that position.
    6. Use modulo 26 (%) to "wrap around" past Z back to A.
    7. Convert the new position back to a character.

  HOW DECRYPTION WORKS:
  ---------------------
  Decryption is just encryption with a negative shift:
    → Instead of shifting +3, we shift -3 (or equivalently shift by 26-3 = 23)
    → The same encrypt function handles both when we pass a negative shift.

  TIME COMPLEXITY:
  ----------------
  O(n) — where n is the length of the message.
  Each character is processed exactly once, so the algorithm scales linearly.

  SPACE COMPLEXITY:
  -----------------
  O(n) — we build a new string of the same length as the input.

  LIMITATIONS OF CAESAR CIPHER IN REAL WORLD:
  --------------------------------------------
  1. Only 25 possible keys (shift 1–25) — easy to brute-force.
  2. Frequency analysis can crack it without knowing the key.
  3. No diffusion or confusion — the same letter always maps to the same cipher letter.
  4. Completely insecure for modern use — used only for educational purposes.
  5. Replaced by modern ciphers like AES-256 which are computationally infeasible to break.

================================================================================
"""

# ─────────────────────────────────────────────────────────────────────────────
#  IMPORTS
#  We only need the built-in 'os' module for clearing the terminal screen.
#  No third-party libraries required — this project is self-contained.
# ─────────────────────────────────────────────────────────────────────────────
import os


# ─────────────────────────────────────────────────────────────────────────────
#  CONSTANTS
#  Defining these at the top makes it easy to spot key values at a glance.
# ─────────────────────────────────────────────────────────────────────────────
ALPHABET_SIZE = 26          # English alphabet has 26 letters
ASCII_UPPERCASE_A = 65      # ord('A') == 65  (ASCII value of 'A')
ASCII_LOWERCASE_A = 97      # ord('a') == 97  (ASCII value of 'a')
APP_VERSION = "1.0.0"


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTION: clear_screen
#  Purpose : Clears the terminal so menus stay clean and readable.
#  Used by : display_banner(), display_menu()
# ─────────────────────────────────────────────────────────────────────────────
def clear_screen():
    """
    Clears the terminal screen.
    - On Windows : runs 'cls'
    - On Mac/Linux: runs 'clear'
    os.name returns 'nt' for Windows and 'posix' for Unix-based systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTION: display_banner
#  Purpose : Prints a styled welcome banner when the program starts.
# ─────────────────────────────────────────────────────────────────────────────
def display_banner():
    """
    Displays the application header/banner.
    This is purely cosmetic — it makes the tool feel professional.
    """
    clear_screen()
    print("=" * 60)
    print("       CAESAR CIPHER ENCRYPTION & DECRYPTION TOOL")
    print("           SkillCraft Technology – Task 01")
    print(f"                     Version {APP_VERSION}")
    print("=" * 60)
    print()


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTION: display_menu
#  Purpose : Prints the main menu options to the user.
#  Returns : Nothing (void function)
# ─────────────────────────────────────────────────────────────────────────────
def display_menu():
    """
    Prints the numbered menu options.
    The user reads this and types a number to choose what they want to do.
    """
    print("\n" + "-" * 60)
    print("                     MAIN MENU")
    print("-" * 60)
    print("  [1]  Encrypt a Message")
    print("  [2]  Decrypt a Message")
    print("  [3]  Brute-Force Decrypt (Try all 25 shifts)")
    print("  [4]  Learn About Caesar Cipher")
    print("  [5]  View Sample Test Cases")
    print("  [6]  Exit")
    print("-" * 60)


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTION: validate_shift
#  Purpose : Makes sure the shift value entered by the user is a valid integer
#            between 1 and 25.
#  Params  : shift_input (str) — the raw string typed by the user
#  Returns : int (valid shift) OR None if input is invalid
#
#  WHY VALIDATE?
#  Without validation, the program crashes if the user types "abc" or leaves
#  it blank. Good software always handles bad input gracefully.
# ─────────────────────────────────────────────────────────────────────────────
def validate_shift(shift_input):
    """
    Validates and converts the user-provided shift value.

    Args:
        shift_input (str): The raw string entered by the user.

    Returns:
        int: A valid shift value between 1 and 25.
        None: If the input is not a valid integer in the allowed range.
    """
    try:
        # Try to convert the string to an integer
        shift = int(shift_input)

        # Shift of 0 means no change — not useful
        # Shift of 26 = full wrap = same as 0 — also not useful
        if 1 <= shift <= 25:
            return shift
        else:
            print("\n  ⚠  ERROR: Shift value must be between 1 and 25.")
            return None

    except ValueError:
        # This block runs if int() fails (e.g., user typed "hello")
        print("\n  ⚠  ERROR: Please enter a valid whole number.")
        return None


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTION: caesar_encrypt
#  Purpose : Core encryption function — shifts each letter by the given value.
#
#  ALGORITHM (step-by-step):
#  ─────────────────────────
#  For each character c in the message:
#    CASE 1: c is uppercase (A–Z)
#      1. ord(c)            → get ASCII code (e.g., 'H' → 72)
#      2. - ASCII_UPPER_A   → shift to 0-based index (72 - 65 = 7, so 'H' is 7th letter)
#      3. + shift           → add the cipher shift (7 + 3 = 10)
#      4. % ALPHABET_SIZE   → wrap around if past Z (10 % 26 = 10, no wrap here)
#      5. + ASCII_UPPER_A   → shift back to ASCII range (10 + 65 = 75)
#      6. chr(...)          → convert ASCII code to character (75 → 'K')
#
#    CASE 2: c is lowercase (a–z)
#      Same steps but use ASCII_LOWER_A (97) as the base.
#
#    CASE 3: c is not a letter
#      Leave it completely unchanged (spaces, digits, punctuation pass through).
#
#  Params  : message (str), shift (int)
#  Returns : encrypted string
# ─────────────────────────────────────────────────────────────────────────────
def caesar_encrypt(message, shift):
    """
    Encrypts a plaintext message using the Caesar Cipher algorithm.

    Args:
        message (str): The original text to be encrypted.
        shift   (int): Number of positions to shift each letter (1–25).

    Returns:
        str: The encrypted ciphertext.

    Example:
        caesar_encrypt("Hello, World!", 3) → "Khoor, Zruog!"
    """
    encrypted_text = ""   # We'll build the result character by character

    # Loop through every character in the message
    for char in message:

        # ── CASE 1: Uppercase letter ──────────────────────────────────────
        if char.isupper():
            # Step 1 & 2: Get 0-based index (0 for A, 1 for B, ..., 25 for Z)
            index = ord(char) - ASCII_UPPERCASE_A

            # Step 3 & 4: Apply shift and wrap around using modulo
            shifted_index = (index + shift) % ALPHABET_SIZE

            # Step 5 & 6: Convert back to uppercase letter
            encrypted_char = chr(shifted_index + ASCII_UPPERCASE_A)
            encrypted_text += encrypted_char

        # ── CASE 2: Lowercase letter ──────────────────────────────────────
        elif char.islower():
            # Same logic, but base is ASCII_LOWERCASE_A (97)
            index = ord(char) - ASCII_LOWERCASE_A
            shifted_index = (index + shift) % ALPHABET_SIZE
            encrypted_char = chr(shifted_index + ASCII_LOWERCASE_A)
            encrypted_text += encrypted_char

        # ── CASE 3: Not a letter (space, digit, punctuation, etc.) ────────
        else:
            # Preserve the character exactly as it is
            encrypted_text += char

    return encrypted_text


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTION: caesar_decrypt
#  Purpose : Decrypts a ciphertext by reversing the shift.
#
#  KEY INSIGHT:
#  Decryption = Encryption with shift going in the opposite direction.
#  Instead of adding the shift, we subtract it.
#  We reuse caesar_encrypt() by passing (ALPHABET_SIZE - shift) as the shift.
#
#  WHY (26 - shift)?
#  Because shifting forward by (26 - shift) is the same as shifting backward
#  by shift, due to the circular/modular nature of the alphabet.
#  Example: shift = 3 → decrypt shift = 23
#           K → (shifted back 3) = H ✓
#           K → (shifted forward 23) = H ✓  (same result!)
#
#  Params  : ciphertext (str), shift (int)
#  Returns : decrypted (original) string
# ─────────────────────────────────────────────────────────────────────────────
def caesar_decrypt(ciphertext, shift):
    """
    Decrypts a Caesar-encrypted message by reversing the shift.

    Args:
        ciphertext (str): The encrypted message to decode.
        shift      (int): The same shift value used during encryption.

    Returns:
        str: The decrypted (original) plaintext.

    Example:
        caesar_decrypt("Khoor, Zruog!", 3) → "Hello, World!"
    """
    # Decryption is encryption with the inverse shift
    # (26 - shift) gives the reverse direction in the alphabet circle
    reverse_shift = ALPHABET_SIZE - shift
    return caesar_encrypt(ciphertext, reverse_shift)


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTION: brute_force_decrypt
#  Purpose : Tries all 25 possible shift values and shows every result.
#            This demonstrates WHY Caesar Cipher is insecure —
#            an attacker can simply try every possibility!
#  Params  : ciphertext (str)
#  Returns : Nothing (prints results directly)
# ─────────────────────────────────────────────────────────────────────────────
def brute_force_decrypt(ciphertext):
    """
    Performs a brute-force attack by decrypting the ciphertext
    with every possible shift value (1 through 25).

    This illustrates the fundamental weakness of Caesar Cipher.

    Args:
        ciphertext (str): The encrypted message to attack.
    """
    print("\n" + "=" * 60)
    print("  BRUTE-FORCE RESULTS (All 25 possible decryptions)")
    print("=" * 60)
    print(f"  Ciphertext: {ciphertext}")
    print("-" * 60)

    for shift in range(1, ALPHABET_SIZE):  # Try shifts 1 through 25
        attempt = caesar_decrypt(ciphertext, shift)
        # Nicely formatted: shift value padded to 2 digits for alignment
        print(f"  Shift {shift:02d} → {attempt}")

    print("=" * 60)
    print("\n  ⚠  Notice: One of these 25 lines is the original message!")
    print("  This is exactly why Caesar Cipher is NOT secure in practice.\n")


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTION: get_message_from_user
#  Purpose : Prompts the user to enter a message and validates it's not empty.
#  Params  : prompt_text (str) — the label shown to the user
#  Returns : str — the non-empty message entered by the user
# ─────────────────────────────────────────────────────────────────────────────
def get_message_from_user(prompt_text):
    """
    Prompts the user to enter a message and ensures it's not blank.

    Args:
        prompt_text (str): Label shown before the input field.

    Returns:
        str: A non-empty message string entered by the user.
    """
    while True:
        message = input(f"\n  {prompt_text}: ").strip()

        if message:  # .strip() removes leading/trailing spaces; if still has content, it's valid
            return message
        else:
            print("\n  ⚠  ERROR: Message cannot be empty. Please try again.")


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTION: get_shift_from_user
#  Purpose : Prompts user for a shift value and keeps asking until valid.
#  Returns : int — a validated shift value between 1 and 25
# ─────────────────────────────────────────────────────────────────────────────
def get_shift_from_user():
    """
    Repeatedly prompts the user for a shift value until a valid one is given.

    Returns:
        int: A validated integer between 1 and 25.
    """
    while True:
        shift_input = input("\n  Enter shift value (1–25): ").strip()
        shift = validate_shift(shift_input)

        if shift is not None:  # validate_shift returns None on invalid input
            return shift
        # If invalid, the while loop runs again and re-prompts the user


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTION: handle_encrypt
#  Purpose : Handles the full encryption flow (user input → output → display).
# ─────────────────────────────────────────────────────────────────────────────
def handle_encrypt():
    """
    Manages the complete encryption workflow:
    1. Get plaintext from user
    2. Get shift value from user
    3. Call caesar_encrypt()
    4. Display the result with formatting
    """
    print("\n" + "─" * 60)
    print("                    ENCRYPT MESSAGE")
    print("─" * 60)

    # Step 1: Get the message the user wants to encrypt
    plaintext = get_message_from_user("Enter plaintext (message to encrypt)")

    # Step 2: Get the secret shift key
    shift = get_shift_from_user()

    # Step 3: Perform encryption
    ciphertext = caesar_encrypt(plaintext, shift)

    # Step 4: Display results in a clean, readable format
    print("\n" + "─" * 60)
    print("                      RESULTS")
    print("─" * 60)
    print(f"  Original Message  : {plaintext}")
    print(f"  Shift Value       : {shift}")
    print(f"  Encrypted Message : {ciphertext}")
    print("─" * 60)
    print("\n  ✓  Encryption complete! Keep your shift value secret.\n")


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTION: handle_decrypt
#  Purpose : Handles the full decryption flow.
# ─────────────────────────────────────────────────────────────────────────────
def handle_decrypt():
    """
    Manages the complete decryption workflow:
    1. Get ciphertext from user
    2. Get the shift key (must be the same one used to encrypt)
    3. Call caesar_decrypt()
    4. Display the result
    """
    print("\n" + "─" * 60)
    print("                    DECRYPT MESSAGE")
    print("─" * 60)

    # Step 1: Get the encrypted message
    ciphertext = get_message_from_user("Enter ciphertext (message to decrypt)")

    # Step 2: Get the shift value (the receiver must know this)
    shift = get_shift_from_user()

    # Step 3: Perform decryption
    plaintext = caesar_decrypt(ciphertext, shift)

    # Step 4: Display results
    print("\n" + "─" * 60)
    print("                      RESULTS")
    print("─" * 60)
    print(f"  Encrypted Message : {ciphertext}")
    print(f"  Shift Value       : {shift}")
    print(f"  Decrypted Message : {plaintext}")
    print("─" * 60)
    print("\n  ✓  Decryption complete!\n")


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTION: handle_brute_force
#  Purpose : Handles the brute-force demo flow.
# ─────────────────────────────────────────────────────────────────────────────
def handle_brute_force():
    """
    Manages the brute-force attack demo:
    1. Get ciphertext from user
    2. Call brute_force_decrypt() to display all 25 possibilities
    """
    print("\n" + "─" * 60)
    print("              BRUTE-FORCE DECRYPT (Demo)")
    print("─" * 60)
    print("  This demonstrates the core weakness of Caesar Cipher.")
    print("  Without knowing the key, an attacker can try all 25 shifts.\n")

    ciphertext = get_message_from_user("Enter ciphertext to brute-force")
    brute_force_decrypt(ciphertext)


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTION: show_about
#  Purpose : Displays educational information about Caesar Cipher.
# ─────────────────────────────────────────────────────────────────────────────
def show_about():
    """
    Prints a structured educational overview of the Caesar Cipher —
    history, mechanism, limitations, and modern alternatives.
    """
    print("\n" + "=" * 60)
    print("            ABOUT THE CAESAR CIPHER")
    print("=" * 60)
    print("""
  WHAT IS CAESAR CIPHER?
  ─────────────────────
  The Caesar Cipher is one of the earliest and simplest
  encryption techniques. Named after Julius Caesar, who used
  it to protect his private military correspondence around
  58 BC (according to Suetonius), it is a substitution cipher
  where each letter is replaced by another letter a fixed
  number of positions down the alphabet.

  HOW ENCRYPTION WORKS:
  ─────────────────────
  Given a shift of 3:
    A → D   B → E   C → F   ...   X → A   Y → B   Z → C
  
  Example:
    Plaintext  : CYBER SECURITY
    Shift      : 4
    Ciphertext : GCFIV Wigyvmxc

  HOW DECRYPTION WORKS:
  ─────────────────────
  Simply shift each letter BACK by the same amount.
    Ciphertext : KHOOR
    Shift back : 3
    Plaintext  : HELLO

  ALGORITHM (Step-by-Step):
  ─────────────────────────
  1. For each character in the message:
  2.   If letter → find its 0-based position in alphabet (0–25)
  3.   Add the shift value to the position
  4.   Apply modulo 26 to wrap around the alphabet
  5.   Convert the new position back to a letter
  6.   If not a letter → keep it unchanged

  TIME COMPLEXITY  : O(n) — linear, proportional to message length
  SPACE COMPLEXITY : O(n) — output string same size as input

  REAL-WORLD LIMITATIONS:
  ───────────────────────
  ✗  Only 25 possible keys — brute-force takes seconds
  ✗  Frequency analysis easily cracks it (E is most common English letter)
  ✗  No diffusion — same letter always encrypts to same cipher letter
  ✗  Completely insecure for any real-world application
  ✓  Great for learning cryptography fundamentals!

  MODERN ALTERNATIVES:
  ────────────────────
  • AES-256   — Advanced Encryption Standard (used in banking, VPNs)
  • RSA       — Asymmetric encryption for key exchange
  • ChaCha20  — High-speed stream cipher used in TLS
  • Bcrypt    — Secure password hashing
""")
    print("=" * 60)


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTION: show_test_cases
#  Purpose : Displays pre-built test cases so the user can verify the program
#            works correctly and understand expected behaviour.
# ─────────────────────────────────────────────────────────────────────────────
def show_test_cases():
    """
    Runs a series of built-in test cases and displays input/output.
    These demonstrate the algorithm working correctly across edge cases.
    """
    print("\n" + "=" * 60)
    print("                 SAMPLE TEST CASES")
    print("=" * 60)

    # Define test cases as a list of dictionaries for clean iteration
    test_cases = [
        {
            "description": "Basic lowercase text",
            "input": "hello world",
            "shift": 3,
            "expected_enc": "khoor zruog"
        },
        {
            "description": "Basic uppercase text",
            "input": "HELLO WORLD",
            "shift": 3,
            "expected_enc": "KHOOR ZRUOG"
        },
        {
            "description": "Mixed case with punctuation",
            "input": "Hello, World!",
            "shift": 3,
            "expected_enc": "Khoor, Zruog!"
        },
        {
            "description": "Numbers and special characters preserved",
            "input": "Attack at 0600 hours!",
            "shift": 7,
            "expected_enc": "Haahjr ha 0600 ovbyz!"
        },
        {
            "description": "Wrap-around test (Z → C)",
            "input": "XYZ",
            "shift": 3,
            "expected_enc": "ABC"
        },
        {
            "description": "Single character",
            "input": "A",
            "shift": 1,
            "expected_enc": "B"
        },
        {
            "description": "Maximum shift (25)",
            "input": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "shift": 25,
            "expected_enc": "ZABCDEFGHIJKLMNOPQRSTUVWXY"
        },
        {
            "description": "Cybersecurity-themed message",
            "input": "Secure the network",
            "shift": 13,  # ROT13 — famous special case of Caesar Cipher
            "expected_enc": "Frpher gur argjbex"
        },
    ]

    for i, tc in enumerate(test_cases, start=1):
        # Run the actual encryption using our function
        actual_enc = caesar_encrypt(tc["input"], tc["shift"])
        # Decrypt the result to verify round-trip works
        round_trip = caesar_decrypt(actual_enc, tc["shift"])

        # Determine pass/fail
        enc_status = "✓ PASS" if actual_enc == tc["expected_enc"] else "✗ FAIL"
        dec_status = "✓ PASS" if round_trip == tc["input"] else "✗ FAIL"

        print(f"\n  Test {i}: {tc['description']}")
        print(f"  {'─' * 50}")
        print(f"  Input      : {tc['input']}")
        print(f"  Shift      : {tc['shift']}")
        print(f"  Encrypted  : {actual_enc}  [{enc_status}]")
        print(f"  Decrypted  : {round_trip}  [{dec_status}]")

    print("\n" + "=" * 60)
    print("  All test cases complete. ✓ = passed, ✗ = failed.")
    print("=" * 60 + "\n")


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTION: pause
#  Purpose : Pauses execution and waits for the user to press Enter.
#            This lets the user read output before the menu redraws.
# ─────────────────────────────────────────────────────────────────────────────
def pause():
    """Pauses execution until the user presses Enter."""
    input("\n  Press Enter to return to the main menu...")


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTION: main
#  Purpose : Entry point — runs the menu-driven application loop.
#
#  PROGRAM FLOW:
#  ─────────────
#  1. Show banner
#  2. Show menu
#  3. Read user's choice
#  4. Execute the chosen function
#  5. Pause for user to read output
#  6. Repeat from step 1 until user chooses "Exit"
# ─────────────────────────────────────────────────────────────────────────────
def main():
    """
    Main function — entry point of the Caesar Cipher tool.
    Runs an infinite loop that shows the menu and handles user choices.
    The loop only exits when the user selects option 6 (Exit).
    """
    # Show the welcome banner once
    display_banner()
    print("  Welcome! This tool lets you encrypt and decrypt messages")
    print("  using the Caesar Cipher — a foundational cryptography concept.")
    print("\n  Built for SkillCraft Technology Cyber Security Internship.")

    # ── MAIN LOOP ───────────────────────────────────────────────────────────
    # This loop runs continuously until the user explicitly exits.
    while True:
        display_banner()   # Redraw banner each iteration for clean UI
        display_menu()     # Show the numbered menu options

        # Read user's menu choice and strip any accidental whitespace
        choice = input("\n  Enter your choice (1–6): ").strip()

        # ── MENU ROUTING ────────────────────────────────────────────────────
        # We use if/elif/else instead of match/case for Python 3.9 compatibility

        if choice == '1':
            # ── ENCRYPT ────────────────────────────────────────────────────
            handle_encrypt()
            pause()

        elif choice == '2':
            # ── DECRYPT ────────────────────────────────────────────────────
            handle_decrypt()
            pause()

        elif choice == '3':
            # ── BRUTE FORCE DEMO ───────────────────────────────────────────
            handle_brute_force()
            pause()

        elif choice == '4':
            # ── EDUCATIONAL INFO ───────────────────────────────────────────
            show_about()
            pause()

        elif choice == '5':
            # ── SAMPLE TEST CASES ──────────────────────────────────────────
            show_test_cases()
            pause()

        elif choice == '6':
            # ── EXIT ───────────────────────────────────────────────────────
            print("\n" + "=" * 60)
            print("  Thank you for using the Caesar Cipher Tool!")
            print("  SkillCraft Technology – Cyber Security Internship")
            print("  GitHub: https://github.com/SaiSharan0/SCT_CS_1")
            print("=" * 60 + "\n")
            break  # Exit the while loop → program ends

        else:
            # ── INVALID INPUT ──────────────────────────────────────────────
            print("\n  ⚠  Invalid choice. Please enter a number from 1 to 6.")
            pause()


# ─────────────────────────────────────────────────────────────────────────────
#  ENTRY POINT
#  In Python, this block ensures main() only runs when this file is executed
#  directly (not when it's imported as a module into another script).
#  This is best practice for every Python program.
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
