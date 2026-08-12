# 📦 Pacify — Object & Contact Manager

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey?style=for-the-badge"/>
</p>

<p align="center">
  A lightweight Python CLI tool to <strong>store, manage, find, edit, and email</strong> your objects/contacts — all from the terminal.
</p>

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| 📝 **Store Data** | Save object records (Name, ID, Email) persistently in `Data.py` |
| 🔍 **Find by ID** | Search and display any object using its unique ID |
| ✏️ **Edit Details** | Update an object's Name, ID, or Email at any time |
| 📧 **Email All** | Send a bulk email to every object stored in your data |
| 💌 **Email Specific** | Target and email a single object by their ID |
| 🗑️ **Clear Data** | Wipe all stored records with a single command |

---
For more information : [`Pacify website`](https://pacify-cli.netlify.app/)

## 📁 Project Structure

```
📦 Pacify/
├── 📄 main.py           # Entry point — handles all menu logic & operations
├── 📄 Login_page.py     # Handles data input & persistent storage
├── 📄 Data.py           # Acts as a local database (auto-updated at runtime)
└── 📄 Background.py     # Contains ASCII art & branding visuals
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pacify.git
cd pacify
```

### 2. Install Dependencies

```bash
pip install prettytable
```

> All other modules (`smtplib`, `email`, `pprint`) are part of Python's standard library.

---

## ▶️ Usage

```bash
python main.py
```

On first launch, you'll be prompted to enter your objects/contacts. After that, the main menu will appear:

```
+------+------------------------------------------+
| No.  | Options You Have                         |
+------+------------------------------------------+
|  1.  | Remove all data from your device         |
|  2.  | E-mail all objects                       |
|  3.  | E-mail a specific object by ID           |
|  4.  | Edit details of an object                |
|  5.  | Find an object by ID                     |
+------+------------------------------------------+
```

---

## Comands for pacify: -
```
show all data
```

Command for using the ai : -
```
ai --chat
```
Command for closing the model: -
```
exit --model
```
Shows the all data in table format stored in ``Data.py `` file.

````commandline
skip-api
````
Skips the API prompt in the login section and you can enter your API key later alternative command : ``sk-a``

---

## AI features in Pacify

Pacify includes a built-in AI assistant powered by a model configured in `model.py`. The assistant can help with coding, data analysis, and quick lookups of the local Pacify dataset. This section explains how to start the AI, how to write effective prompts, the special "data mode" trigger, and how to obtain and configure the NVIDIA API key required by the model.

How the AI is run in Pacify
- The AI runner is implemented in `model.py`. The program reads an API key from the file `API_KEY.txt` in the project root and uses NVIDIA's Integrate endpoint (base URL: `https://integrate.api.nvidia.com/v1`).
- To launch the AI from the Pacify CLI: run the main program and choose the AI option (or use the provided shortcut `ai --chat` if available in the menu). You can also run the model directly for quick testing with:


Basic usage
- When the AI starts it will display the Pacify logo and then prompt you with: `Enter your prompt:`
- Type your question or instruction and press Enter. The model streams responses to the console.
- To close the AI session, type:

```text
exit --model
```

How to write effective prompts
- Be concise and specific. For example:
  - "Help me write a function to validate email addresses in Python."
  - "Explain how to refactor this small loop into a list comprehension."

**Special "data mode" behavior (important)**
- If your prompt ends with either of the following (case-insensitive):
  - "from pacify data"
  - "pd"

  then the AI runner is programmed to trigger a two-step behavior:
  1. The model will first respond with the two-character token `DX` only. The program detects this and switches into data mode.
  2. In data mode, the program sends the original prompt again with access to `Data.User_data_1` and instructs the model to answer using only that data. The model's follow-up response is streamed to the console and will include an explicit statement that the information came from the Pacify dataset.

Use this mode when you explicitly want answers that are drawn from the local Pacify dataset. Be careful: any sensitive data stored in `Data.py` could be exposed when using this mode. Only use it with datasets you are comfortable revealing.

Where to get the NVIDIA API key and how to configure it
- The AI runner uses NVIDIA's Integrate API (the code sets `base_url` to `https://integrate.api.nvidia.com/v1`) and expects a valid API key stored in `API_KEY.txt` in the project root.
- To obtain an API key:
  1. Sign in or create an account on NVIDIA's developer/AI portal (search for "NVIDIA Integrate" or "NVIDIA API" if you're unsure).
  2. Create or navigate to an API credentials or API key section and generate a new key for the Integrate/Inference API.
  3. Copy the generated key.
  4. Here is the model link: https://build.nvidia.com/meta/llama-3_1-8b-instruct

- To configure the key for Pacify:
  1. Open `API_KEY.txt` in the project root. Initially it may contain the string `none`.
  2. Replace its contents with your API key and save the file. The AI runner reads this file on startup.


- If the file contains `none`, the program will prompt you for a key at runtime and then overwrite `API_KEY.txt` with the value you provide.

Security & privacy notes
- The special data mode explicitly reads from `Data.py` (local dataset). Only use data mode if you understand what is stored there and are comfortable with the data being used to produce responses.
- If you need to temporarily disable the AI or skip the API prompt, see the existing `skip-api` and `sk-a` in login section options referenced elsewhere in the README.
- And you can add API when you use Pacify ai.

**Examples**
- Normal query: "Explain how to validate an email address in Python." → AI responds normally.
- Data-mode query: "List the names of all users from pacify data" → Append `from pacify data` (or `pd`) to trigger the data mode behavior described above.

**An Important note**
Some features of AI don't come on the **exe version of the app**; this will update after sometimes⚠️
## 📧 Email Feature Setup

The email functionality uses **Gmail SMTP**. Before using it:

1. Go to your [Google Account Security Settings](https://myaccount.google.com/security)
2. Enable **2-Step Verification**
3. Generate an **App Password** under *App Passwords*
4. Use that App Password when prompted by Pacify

> ⚠️ Only **Gmail** accounts are currently supported. More providers coming in a future update.

---

## ⚠️ Important Notes

- 🌐 **Internet is required** for all email features
- 🔄 After adding or clearing data, **restart the program** for changes to take effect
- 🔑 Never share your **App Password** publicly or commit it to version control
- 📂 `Data.py` is your local database — don't manually edit it unless you know what you're doing

---

## 🛠️ Requirements

- Python **3.10+**
- [`prettytable`](https://pypi.org/project/prettytable/) — for table formatting in the terminal
- A **Gmail account** with App Password enabled (for email features)
- For more details visit at this link : [`Pacify website`](https://pacify-cli.netlify.app/)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **Apache 2.0** — see the [LICENSE](LICENSE) file for details.
- For more details visit at this link : [`Pacify website`](https://pacify-cli.netlify.app/)

---

## 👨‍💻 Author

Made with ❤️ by Lakshit

> *"Pacify your data chaos — one object at a time."*
