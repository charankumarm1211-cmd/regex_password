# 🔐 Password Validator

A simple and elegant **Streamlit** web application that validates passwords against common security requirements — with a styled gradient UI.

---

## 🖥️ Demo

> Enter a password → Click **Check Password** → Get instant feedback.

---

## 📁 Project Structure

```
password-validator/
│
├── app.py          # Main Streamlit application
└── README.md       # Project documentation
```

---

## ⚙️ How It Works

### 1. Custom Styling

```python
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, red, blue);
    }
    </style>
    """,
    unsafe_allow_html=True
)
```

This injects custom CSS directly into the Streamlit app using `st.markdown()` with `unsafe_allow_html=True`. It applies a **red-to-blue gradient background** across the entire app using the `.stApp` selector.

---

### 2. Regex Pattern Compilation

```python
pattern = re.compile(
    r'(?=.*[A-Z])'        # At least one uppercase letter
    r'(?=.*[a-z])'        # At least one lowercase letter
    r'(?=.*\d)'           # At least one digit
    r'(?=.*[!@#$%^&*])'   # At least one special character
    r'[A-Za-z\d!@#$%^&*]{8,}'  # Minimum 8 characters
)
```

A **regular expression** is compiled once using `re.compile()` for efficiency. It uses **lookaheads** — zero-width assertions that check for the presence of a character type without consuming characters — to enforce all rules simultaneously:

| Component | Meaning |
|---|---|
| `(?=.*[A-Z])` | Must contain at least one uppercase letter |
| `(?=.*[a-z])` | Must contain at least one lowercase letter |
| `(?=.*\d)` | Must contain at least one digit (`0–9`) |
| `(?=.*[!@#$%^&*])` | Must contain at least one special character |
| `[A-Za-z\d!@#$%^&*]{8,}` | Must be at least 8 characters long, using only allowed characters |

> ⚠️ **Note:** The final character class `[A-Za-z\d!@#$%^&*]{8,}` restricts which characters are valid. Passwords with characters outside this set (e.g. spaces, `@`, `_`) will be rejected even if they're long and complex.

---

### 3. Streamlit UI

```python
st.title("Password Validator")

password = st.text_input("Enter your password", type="password")
```

- `st.title()` renders the app heading.
- `st.text_input()` with `type="password"` renders a masked input field so the password isn't visible while typing.

---

### 4. Validation Logic

```python
if st.button("Check Password"):
    if pattern.fullmatch(password):
        st.success("Password is valid.")
    else:
        st.error("Invalid password.")
        st.write("Your password must:")
        ...
```

- `st.button()` triggers validation only when clicked.
- `pattern.fullmatch(password)` checks that the **entire string** matches the pattern (not just a substring).
- `st.success()` shows a green banner on valid passwords.
- `st.error()` shows a red banner and lists requirements when the password fails.

---

## ✅ Password Requirements

A valid password must:

- Be **at least 8 characters** long
- Contain at least one **uppercase letter** (A–Z)
- Contain at least one **lowercase letter** (a–z)
- Contain at least one **digit** (0–9)
- Contain at least one **special character**: `! @ # $ % ^ & *`

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/password-validator.git
cd password-validator

# Install dependencies
pip install streamlit

# Run the app
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 🛠️ Built With

- [Python](https://www.python.org/) — Core language
- [Streamlit](https://streamlit.io/) — Web UI framework
- [re](https://docs.python.org/3/library/re.html) — Python standard library for regular expressions

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
