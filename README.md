
<div align="center">

# 🔐 Hashnat
### Wordlist-Based Hash Recovery with Python

**Hash • Compare • Learn**

A Python cybersecurity project that compares hashes generated from candidate strings against a given hash to demonstrate how wordlist-based password recovery works.

<br/>

![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Cybersecurity-red?style=for-the-badge)
![Project](https://img.shields.io/badge/Project-Hash%20Recovery-purple?style=for-the-badge)

</div>

---

## 🌍 About the Project

**Hashnat** is an educational Python tool that demonstrates wordlist-based hash recovery.

The program reads candidate strings from a text-based wordlist, calculates their hashes, and compares the results with a supplied hash. When a match is found, the corresponding candidate string is reported.

Hashnat supports six hash formats, making it useful for exploring hashing algorithms and understanding the limitations of password security.

---

## 🚀 Features

- 🔑 **Multiple Hash Formats:** Supports LM, NTLM, MD5, SHA-1, SHA-256, and SHA-512.
- 📚 **Wordlist Processing:** Reads candidate strings from a local text file.
- 🔍 **Hash Comparison:** Compares calculated hashes against a supplied hash.
- 🐍 **Python Implementation:** Provides a practical introduction to hashing and cybersecurity.
- 🧪 **Educational Testing:** Demonstrates why weak passwords can be vulnerable to wordlist attacks.

---

## 🛠️ Technologies

- **Python:** Core programming language.
- **Hashing Libraries:** Used to calculate supported hash digests.
- **Text Wordlists:** Supply candidate strings for comparison.

---

## ▶️ Getting Started

### Prerequisites

- Python installed on your computer.
- A text-based wordlist for authorized testing.
- The dependencies required by the project.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nethen-ui/hashnat
   ```

2. Navigate to the project directory:

   ```bash
   cd hashnat
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   On Linux:

   ```bash
   source venv/bin/activate
   ```

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

4. Install the required libraries using the project's dependency file, if available:

   ```bash
   pip install -r requirements.txt
   ```

5. Place your authorized test wordlist in the project directory and name it `rockyou.txt`, unless you have modified the source code to use another filename.

---

## 💻 Usage

Run the main script:

```bash
python hash.py
```

Follow the program's prompts to provide the target hash and perform the comparison.

The program checks candidate strings against the supplied hash and reports a match if one is found in the wordlist.

---

## 🔐 Security & Responsible Use

This project is intended for educational purposes and authorized security testing.

- Test only hashes you own or have explicit permission to assess.
- Use the project to understand password strength and hashing security.
- Remember that hashing is generally one-way; recovery relies on finding a candidate that produces a matching hash.
- Use modern password-hashing algorithms with salts, such as Argon2id, for new password-storage systems.

---

## 🎓 Learning Objectives

- Understand the difference between hashing and encryption.
- Explore common hash formats and their uses.
- Learn how wordlist-based recovery works.
- Understand why weak passwords are easier to guess.
- Recognize the importance of secure password storage.

---

<div align="center">

**Learn • Analyze • Secure**

*Making cybersecurity concepts practical through Python.*

</div>
