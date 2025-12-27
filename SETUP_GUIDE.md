# 🚀 Complete Setup Guide

## Step-by-Step Installation

### 1️⃣ System Prerequisites

**Operating System:**
- Windows 10/11
- macOS 10.14+
- Linux (Ubuntu 20.04+)

**Software Requirements:**
- Python 3.8 or higher
- pip (Python package manager)
- Git

**Hardware:**
- Microphone (for voice input)
- Minimum 4GB RAM
- 500MB free disk space

### 2️⃣ Python Installation

**Windows:**
```bash
# Download from python.org and install
# Make sure to check "Add Python to PATH"
python --version
```

**macOS:**
```bash
# Using Homebrew
brew install python@3.11
python3 --version
```

**Linux:**
```bash
sudo apt update
sudo apt install python3.11 python3-pip
python3 --version
```

### 3️⃣ Clone the Repository

```bash
# Clone the repo
git clone https://github.com/yourusername/voice-sql-assistant.git

# Navigate to directory
cd voice-sql-assistant

# Verify files
ls -la
# Should see: app5.py, Voice-SQL.json, README.md, requirements.txt
```

### 4️⃣ Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 5️⃣ Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install all requirements
pip install -r requirements.txt

# For macOS users (if pyaudio fails):
brew install portaudio
pip install pyaudio

# For Linux users (if pyaudio fails):
sudo apt-get install python3-pyaudio
# or
sudo apt-get install portaudio19-dev
pip install pyaudio
```

### 6️⃣ Install Langflow

```bash
# Install Langflow
pip install langflow

# Verify installation
langflow --version
```

### 7️⃣ Start Langflow

```bash
# Start Langflow server
langflow run --host 0.0.0.0 --port 8000

# You should see:
# ✓ Langflow is running at http://localhost:8000
```

**Keep this terminal window open!**

### 8️⃣ Import Flow to Langflow

1. Open browser: `http://localhost:8000`
2. Click **"New Project"** or **"Import"**
3. Select `Voice-SQL.json` from your project folder
4. Wait for the flow to load
5. You should see all components connected

### 9️⃣ Configure Database

**Option A: Use Sample Excel File**

Create a sample Excel file named `employees.xlsx`:

| employee_id | name  | department_id | salary | join_date  |
|-------------|-------|---------------|--------|------------|
| 1           | Rahul | 2             | 80000  | 2022-01-01 |
| 2           | Neha  | 2             | 75000  | 2022-03-01 |
| 3           | Karan | 3             | 60000  | 2023-02-01 |
| 4           | Priya | 1             | 50000  | 2021-06-01 |

Create another sheet named `departments`:

| department_id | name        |
|---------------|-------------|
| 1             | IT          |
| 2             | HR          |
| 3             | Engineering |

**Option B: Use Your Own Excel File**

Prepare your Excel file with:
- Clear column headers
- No merged cells
- Data starting from row 1
- No empty rows

**Upload to Langflow:**
1. In Langflow UI, click **"Excel to Database"** component
2. Click **"Upload File"**
3. Select your Excel file
4. Wait for green checkmark ✅
5. Database is now ready!

### 🔟 Get Your Flow ID

1. In Langflow, look at the URL
2. Copy the Flow ID: `http://localhost:8000/flow/YOUR_FLOW_ID`
3. Update `app5.py` line 42:
   ```python
   FLOW_ID = "YOUR_FLOW_ID"  # Replace with your actual Flow ID
   ```

### 1️⃣1️⃣ Test in Langflow First

Before using Streamlit:
1. Click **"Playground"** in Langflow
2. Type a simple query: "Show all employees"
3. Click **"Run"**
4. Verify you get results

If this works, you're ready for Streamlit!

### 1️⃣2️⃣ Run Streamlit App

**Open a NEW terminal window:**

```bash
# Navigate to project folder
cd voice-sql-assistant

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Run Streamlit
streamlit run app5.py
```

### 1️⃣3️⃣ Access the Application

1. Browser should open automatically
2. Or manually open: `http://localhost:8501`
3. You should see the beautiful dashboard!

### 1️⃣4️⃣ Test the Application

**Test Text Input:**
1. Go to "Text Input" tab
2. Type: "Show all employees"
3. Click "Execute Query"
4. Verify results appear

**Test Voice Input:**
1. Go to "Voice Input" tab
2. Click "Start Recording"
3. Say: "Show all departments"
4. Click "Execute Voice Query"
5. Verify results appear

---

## 🎯 Quick Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution:**
```bash
pip install streamlit
```

### Issue: "Cannot connect to Langflow"
**Solution:**
1. Check Langflow is running: `http://localhost:8000`
2. Verify FLOW_ID in app5.py
3. Check firewall settings

### Issue: "PyAudio error"
**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**macOS:**
```bash
brew install portaudio
pip install pyaudio
```

**Linux:**
```bash
sudo apt-get install python3-pyaudio
```

### Issue: "Could not understand audio"
**Solution:**
1. Check microphone permissions
2. Test microphone in system settings
3. Reduce background noise
4. Speak clearly and slowly
5. Increase recording duration

### Issue: "Excel file not loading"
**Solution:**
1. Ensure file has .xlsx extension
2. No merged cells
3. Clear column headers
4. Data starts from row 1
5. No empty rows in between

---

## 📊 Expected Results

When everything is working:
- ✅ Langflow running on port 8000
- ✅ Streamlit running on port 8501
- ✅ Excel file uploaded with green checkmark
- ✅ Test query returns results
- ✅ Voice recording works
- ✅ Statistics update in sidebar

---

## 🎬 Recording Your Demo

**Tips for a great demo video:**
1. Use OBS Studio or Loom for recording
2. Show the complete workflow
3. Demonstrate both text and voice input
4. Show different query types
5. Highlight the statistics panel
6. Show multilingual support
7. Keep it under 3 minutes

**Suggested Demo Flow:**
1. Open Langflow → Show flow
2. Upload Excel file
3. Switch to Streamlit
4. Text query example
5. Voice query example (in different language)
6. Show query history
7. Show statistics

---

## 📤 Pushing to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Voice-SQL Assistant"

# Add remote
git remote add origin https://github.com/yourusername/voice-sql-assistant.git

# Push
git push -u origin main
```

**Files to include:**
- ✅ app5.py
- ✅ Voice-SQL.json
- ✅ README.md
- ✅ requirements.txt
- ✅ SETUP_GUIDE.md
- ✅ .gitignore (create one)
- ✅ LICENSE
- ✅ screenshots/ folder

**Files to exclude (.gitignore):**
```txt
# Python
__pycache__/
*.py[cod]
*$py.class
venv/
env/

# Streamlit
.streamlit/

# Data files
*.db
*.sqlite
*.xlsx
*.csv

# OS
.DS_Store
Thumbs.db
```

---

## 🎉 You're All Set!

If you followed all steps, you should have:
- ✅ Working Langflow instance
- ✅ Streamlit dashboard running
- ✅ Voice input functional
- ✅ Database queries working
- ✅ Project on GitHub

**Next Steps:**
1. Record your demo video
2. Add screenshots to README
3. Share on LinkedIn
4. Get feedback and improve!

---

## 💬 Need Help?

If you're stuck:
1. Check the troubleshooting section
2. Review Langflow logs
3. Check Streamlit terminal output
4. Open an issue on GitHub
5. Connect on LinkedIn

**Happy Coding! 🚀**
