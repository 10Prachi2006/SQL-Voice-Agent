# 🎤 Enterprise AI Voice-SQL Platform

> Transform your voice into powerful SQL queries using AI! A cutting-edge voice-enabled natural language to SQL converter powered by Langflow and Streamlit.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg)](https://streamlit.io/)
[![Langflow](https://img.shields.io/badge/Langflow-Latest-purple.svg)](https://langflow.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🌟 Features

- **🎙️ Voice Input Support** - Speak your queries naturally in multiple languages
- **💬 Text Input** - Type queries in plain natural language
- **🌐 Multilingual** - Supports English, Hindi, Spanish, French, and German
- **📊 Real-time Statistics** - Track query success rates and history
- **⚡ Fast Processing** - Instant SQL generation and execution
- **🎯 Smart Query Examples** - Pre-built examples for quick testing
- **📈 Session Management** - Maintain query history across sessions
- **🔒 Secure** - Local processing with API-based architecture

## 🎥 Demo

https://vimeo.com/1149629769?share=copy&fl=sv&fe=ci


## 📸 Screenshots


Voice Input Interface
<img width="1365" height="624" alt="Screenshot 2025-12-27 at 16-02-49 Enterprise AI Voice-SQL Platform" src="https://github.com/user-attachments/assets/ede8efbb-f417-453a-a4dc-25d1ac6de855" />

### Query Results
<img width="1365" height="636" alt="Screenshot 2025-12-27 at 16-03-42 Enterprise AI Voice-SQL Platform" src="https://github.com/user-attachments/assets/723fda6f-760e-4701-ad39-e854398df5b4" />

### Statistics Panel
<img width="1365" height="634" alt="Screenshot 2025-12-27 at 16-03-19 Enterprise AI Voice-SQL Platform" src="https://github.com/user-attachments/assets/7770242c-8b1f-489b-b466-ecfc57d0d5cf" />

### Architecture
<img width="1365" height="639" alt="Screenshot 2025-12-27 at 16-02-18 Langflow" src="https://github.com/user-attachments/assets/a04a4bb7-8969-47f8-94a6-5b4e5745e2aa" />

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Langflow installed and running
- Microphone access (for voice input)
- Excel file with your data

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/voice-sql-assistant.git
   cd voice-sql-assistant
   ```

2. **Install required packages**
   ```bash
   pip install streamlit requests pyaudio wave SpeechRecognition pandas
   ```

3. **Install Langflow**
   ```bash
   pip install langflow
   ```

### Setup

1. **Start Langflow**
   ```bash
   langflow run --host 0.0.0.0 --port 8000
   ```

2. **Import the Flow**
   - Open Langflow UI at `http://localhost:8000`
   - Click on "Import Flow"
   - Select the `Voice-SQL.json` file from this repository
   - The flow will be automatically configured

3. **Upload Your Data**
   - In Langflow, click on the "Excel to Database" component
   - Upload your Excel file
   - Wait for the green checkmark ✅ confirmation

4. **Update Flow ID** (if needed)
   - Copy your Flow ID from Langflow URL
   - Update `FLOW_ID` in `app5.py` if different

5. **Run the Streamlit App**
   ```bash
   streamlit run app5.py
   ```

6. **Access the Application**
   - Open your browser at `http://localhost:8501`
   - Start querying!

## 📖 Usage Guide

### Text Queries
1. Navigate to the "Text Input" tab
2. Type your query in natural language
3. Click "Execute Query"

**Example Queries:**
- "Show all employees in HR department"
- "What is the total salary by department?"
- "Find employees with salary greater than 60000"
- "Top 3 highest paid employees"

### Voice Queries
1. Navigate to the "Voice Input" tab
2. Select your language
3. Click "Start Recording"
4. Speak your query clearly
5. Review the transcription and edit if needed
6. Click "Execute Voice Query"

### Supported Languages
- 🇺🇸 English (en-US)
- 🇮🇳 हिंदी (hi-IN)
- 🇪🇸 Español (es-ES)
- 🇫🇷 Français (fr-FR)
- 🇩🇪 Deutsch (de-DE)


## 🔧 Configuration

### Langflow Flow Components

The Langflow flow consists of:
- **Chat Input** - Entry point for queries
- **Excel to Database** - Converts Excel to SQLite database
- **Text to SQL** - Converts natural language to SQL
- **SQL Database** - Executes SQL queries
- **Chat Output** - Returns formatted results



## 🐛 Troubleshooting

### Common Issues

**1. "Cannot connect to Langflow"**
- Ensure Langflow is running on `http://localhost:8000`
- Check if the Flow ID is correct
- Verify firewall settings

**2. "Could not understand audio"**
- Speak clearly and closer to the microphone
- Reduce background noise
- Check microphone permissions
- Try increasing recording duration

**3. "No data returned"**
- Verify Excel file is uploaded in Langflow
- Check database connection in Langflow
- Test the query directly in Langflow first

**4. "Query execution failed"**
- Verify your query syntax
- Check if the table/column names exist
- Review the error message in the expander

## 🔐 Security Notes

- All processing happens locally
- No data is sent to external servers (except Google Speech API for transcription)
- Excel files are stored in your local Langflow instance
- Database queries are executed in a sandboxed environment

## 📦 Dependencies

```txt
streamlit>=1.28.0
requests>=2.31.0
pyaudio>=0.2.13
SpeechRecognition>=3.10.0
pandas>=2.0.0
langflow>=latest
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Langflow](https://langflow.org/) - For the amazing workflow builder
- [Streamlit](https://streamlit.io/) - For the beautiful UI framework
- [Google Speech Recognition](https://cloud.google.com/speech-to-text) - For voice transcription

## 📧 Contact & Connect

**Developer:** Prachi Yadav.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/prachi-yadav-60466b343)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/10Prachi2006)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:starletprachi@gmail.com)

---

## ⚠️ Important Note

**This project is for educational and demonstration purposes.** While it showcases the power of AI-driven natural language processing for database queries, please ensure you:

- **Review all generated SQL queries** before execution in production environments
- **Implement proper security measures** (authentication, authorization, input validation)
- **Test thoroughly** with your specific use case and data
- **Handle sensitive data** according to your organization's security policies
- **Add rate limiting** and error handling for production use

The voice recognition feature uses Google's Speech Recognition API, which requires an internet connection and is subject to Google's usage policies and quotas.

**Use at your own risk** - The developers are not responsible for any data loss, security breaches, or issues arising from the use of this software.

---

<div align="center">

### 💡 If this project helped you, consider giving it a ⭐!

**Made with ❤️ and AI**

*Transforming the way humans interact with databases, one voice command at a time.*

</div>

---


---

<div align="center">

### 🔗 Connect with Me

For questions, suggestions, or collaboration opportunities:

**LinkedIn: www.linkedin.com/in/prachi-yadav-60466b343** 

*Let's build the future of data interaction together!*

</div>

## Author
### Prachi Yadav.
