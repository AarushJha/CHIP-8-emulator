# Security Policy

## ⚠️ Development Status & Disclaimer
This CHIP-8 emulator is currently an **educational project in active development**. 

* **Experimental Codebase:** Features and instruction opcodes are being actively written, modified, and tested. The software is provided "as is" without warranty of any kind.
* **Untrusted ROM Files:** CHIP-8 ROMs are binary files loaded directly into memory. While the emulator runs inside a restricted Python environment and does not execute native system code, you should only load ROM files from known, trusted sources.

---

## 🔒 Supported Versions

Only the latest commit on the `main` branch receives active security consideration and bug fixes.

| Version | Supported |
| ------- | --------- |
| Main Branch | yes |
| Draft/Dev Branches | no |

---

## 🐛 Reporting a Vulnerability

If you discover a potential security flaw or unintended behavior with severe impact (e.g., memory leak, unhandled file parsing issue):

1. **Do not create a public issue** on GitHub.
2. Reach out directly by opening a **Private Vulnerability Report** via the **Security** tab of this repository, or contact the maintainer via email.
3. Provide a clear description of the issue, including steps to reproduce and sample ROM files if applicable.

We appreciate your assistance in keeping this open-source project safe and reliable!
