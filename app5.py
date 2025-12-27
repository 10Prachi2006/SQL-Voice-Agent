import streamlit as st
import requests
import uuid
import pyaudio
import wave
import speech_recognition as sr
from io import BytesIO
import pandas as pd
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="Enterprise AI Voice-SQL Platform",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with modern design
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        padding: 1rem 2rem;
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    }
    
    /* Card styling */
    .custom-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin: 1rem 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .custom-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #2d3561 0%, #1a1a2e 100%);
        color: white;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        border-radius: 10px;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin-bottom: 2rem;
    }
    
    .header-title {
        font-size: 3rem;
        font-weight: 800;
        color: white;
        margin-bottom: 0.5rem;
    }
    
    .header-subtitle {
        font-size: 1.2rem;
        color: rgba(255,255,255,0.9);
        font-weight: 500;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
    
    [data-testid="stSidebar"] .element-container {
        color: white;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background-color: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 1rem 2rem;
        font-weight: 600;
        color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2d3561 0%, #1a1a2e 100%);
        color: white;
        transform: scale(1.05);
    }
    
    /* Success/Error boxes */
    .success-message {
        background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        color: #0f5132;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #0f5132;
        font-weight: 600;
        margin: 1rem 0;
        animation: slideIn 0.5s ease;
    }
    
    .error-message {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: #842029;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #842029;
        font-weight: 600;
        margin: 1rem 0;
        animation: slideIn 0.5s ease;
    }
    
    /* Query history styling */
    .query-item {
        background: rgba(255,255,255,0.1);
        padding: 0.75rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        color: white;
        font-size: 0.9rem;
        border-left: 3px solid white;
        transition: all 0.3s ease;
    }
    
    .query-item:hover {
        background: rgba(255,255,255,0.2);
        transform: translateX(5px);
    }
    
    /* Stats box */
    .stat-box {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .stat-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        color: white;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #666;
        font-weight: 600;
        margin-top: 0.5rem;
    }
    
    /* Animation */
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background: linear-gradient(135deg, #2d3561 0%, #1a1a2e 100%);
    }
    
    /* Recording indicator */
    .recording-pulse {
        width: 15px;
        height: 15px;
        background-color: #ff4444;
        border-radius: 50%;
        display: inline-block;
        margin-right: 10px;
        animation: pulse 1.5s infinite;
    }
    
    @keyframes pulse {
        0% {
            transform: scale(1);
            opacity: 1;
        }
        50% {
            transform: scale(1.2);
            opacity: 0.7;
        }
        100% {
            transform: scale(1);
            opacity: 1;
        }
    }
    
    /* Example query buttons */
    .example-btn {
        background: rgba(255,255,255,0.1);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        border: 1px solid rgba(255,255,255,0.3);
        margin: 0.25rem;
        transition: all 0.3s ease;
        cursor: pointer;
        font-size: 0.85rem;
    }
    
    .example-btn:hover {
        background: rgba(255,255,255,0.2);
        color: white;
        transform: scale(1.05);
    }
    
    /* Text area styling */
    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    
    .stTextArea textarea:focus {
        border-color: #2d3561;
        box-shadow: 0 0 0 2px rgba(45, 53, 97, 0.3);
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: rgba(255,255,255,0.1);
        border-radius: 8px;
        color: white;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if 'query_history' not in st.session_state:
    st.session_state.query_history = []
if 'recorded_text' not in st.session_state:
    st.session_state.recorded_text = ""
if 'excel_uploaded' not in st.session_state:
    st.session_state.excel_uploaded = False
if 'total_queries' not in st.session_state:
    st.session_state.total_queries = 0
if 'successful_queries' not in st.session_state:
    st.session_state.successful_queries = 0
if 'is_recording' not in st.session_state:
    st.session_state.is_recording = False

# API Configuration
FLOW_ID = "f2eec69f-32f1-4a60-b8c0-f63eda95296a"
LANGFLOW_API_URL = f"http://localhost:8000/api/v1/run/{FLOW_ID}"

def record_audio(duration=5, sample_rate=16000):
    """Record audio from microphone"""
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    p = pyaudio.PyAudio()
    
    try:
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=sample_rate,
                       input=True, frames_per_buffer=CHUNK)
        frames = []
        progress_bar = st.progress(0)
        status_text = st.empty()
        total_chunks = int(sample_rate / CHUNK * duration)
        
        for i in range(total_chunks):
            data = stream.read(CHUNK)
            frames.append(data)
            progress = (i + 1) / total_chunks
            progress_bar.progress(progress)
            remaining = duration - int(i * CHUNK / sample_rate)
            status_text.markdown(f'<div class="recording-pulse"></div> **Recording... {remaining}s remaining**', unsafe_allow_html=True)
        
        progress_bar.empty()
        status_text.empty()
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        audio_buffer = BytesIO()
        wf = wave.open(audio_buffer, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        return audio_buffer.getvalue()
    except Exception as e:
        st.error(f"🎤 Recording error: {str(e)}")
        return None

def transcribe_audio(audio_data, language="en-US"):
    """Transcribe audio to text"""
    try:
        recognizer = sr.Recognizer()
        audio_file = BytesIO(audio_data)
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio, language=language)
    except sr.UnknownValueError:
        return "❌ Could not understand audio"
    except sr.RequestError as e:
        return f"❌ Speech recognition error: {str(e)}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

def call_langflow_api(user_input, tweaks=None):
    """Call Langflow API"""
    payload = {
        "input_value": user_input,
        "output_type": "chat",
        "input_type": "chat",
    }
    
    if tweaks:
        payload["tweaks"] = tweaks
    
    try:
        response = requests.post(
            LANGFLOW_API_URL, 
            json=payload,
            headers={"Content-Type": "application/json"}, 
            timeout=120
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        st.error("⏱️ Request timed out. The query might be too complex.")
        return None
    except requests.exceptions.ConnectionError:
        st.error("🔌 Cannot connect to Langflow. Is it running on http://localhost:8000?")
        return None
    except requests.exceptions.HTTPError as e:
        st.error(f"❌ HTTP Error: {e.response.status_code}")
        return None
    except Exception as e:
        st.error(f"❌ API Error: {str(e)}")
        return None

def format_result(response_data):
    """Extract and format results from Langflow response"""
    if not response_data:
        return None, "No data returned from API"
    
    try:
        if isinstance(response_data, dict):
            if 'outputs' in response_data:
                outputs = response_data['outputs']
                if outputs and len(outputs) > 0:
                    first_output = outputs[0]
                    
                    if 'outputs' in first_output and first_output['outputs']:
                        result = first_output['outputs'][0]
                        
                        if 'results' in result:
                            message = result['results'].get('message', {})
                            text = message.get('text', '')
                            
                            if any(err in text.lower() for err in ['error', 'timeout', 'failed']):
                                return None, text
                            
                            return text, None
                        
                        if 'artifacts' in result:
                            return str(result['artifacts']), None
            
            return str(response_data), None
        
        return str(response_data), None
        
    except Exception as e:
        return None, f"Parse error: {str(e)}"

# Header
st.markdown("""
    <div class="header-container">
        <h1 class="header-title">🎤 Enterprise AI Voice-SQL Platform</h1>
        <p class="header-subtitle">Transform Natural Language into Powerful SQL Queries | AI-Powered Business Intelligence</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 🎯 Session Dashboard")
    
    # Session info card
    st.markdown(f"""
        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
            <p style="color: white; margin: 0; font-size: 0.85rem;">Session ID</p>
            <p style="color: white; margin: 0; font-weight: 600; font-family: monospace;">{st.session_state.session_id[:16]}...</p>
            <p style="color: rgba(255,255,255,0.7); margin-top: 0.5rem; margin-bottom: 0; font-size: 0.75rem;">
                Started: {datetime.now().strftime('%I:%M %p')}
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Action buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Reset", use_container_width=True):
            st.session_state.session_id = str(uuid.uuid4())
            st.session_state.query_history = []
            st.session_state.recorded_text = ""
            st.session_state.total_queries = 0
            st.session_state.successful_queries = 0
            st.rerun()
    
    with col2:
        if st.button("🧪 Test", use_container_width=True):
            with st.spinner("Testing..."):
                test_response = call_langflow_api("test")
                if test_response:
                    st.success("✅ OK")
                    time.sleep(1)
                    st.rerun()
    
    st.markdown("---")
    
    # Statistics
    success_rate = (st.session_state.successful_queries / st.session_state.total_queries * 100) if st.session_state.total_queries > 0 else 0
    
    st.markdown("## 📊 Statistics")
    st.markdown(f"""
        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span style="color: white;">Total Queries</span>
                <span style="color: white; font-weight: 700;">{st.session_state.total_queries}</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span style="color: white;">Successful</span>
                <span style="color: #84fab0; font-weight: 700;">{st.session_state.successful_queries}</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: white;">Success Rate</span>
                <span style="color: #8fd3f4; font-weight: 700;">{success_rate:.1f}%</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Query History
    st.markdown("## 📜 Recent Queries")
    if st.session_state.query_history:
        for i, q in enumerate(reversed(st.session_state.query_history[-8:])):
            st.markdown(f"""
                <div class="query-item">
                    <strong>#{len(st.session_state.query_history)-i}</strong>: {q[:50]}{"..." if len(q) > 50 else ""}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 8px; text-align: center; color: rgba(255,255,255,0.7);">
                No queries yet
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Example queries
    st.markdown("## 💡 Quick Examples")
    
    example_queries = {
        "📊 Simple": ["Show all departments", "List all employees"],
        "🔍 Filtering": ["Employees in HR", "Show Neha's salary"],
        "📈 Aggregation": ["Total salary by dept", "Count employees"],
        "⚡ Complex": ["Top 3 highest paid", "Salary > 60000"]
    }
    
    for category, queries in example_queries.items():
        with st.expander(category):
            for query in queries:
                if st.button(query, key=f"ex_{query}", use_container_width=True):
                    st.session_state.example_query = query
                    st.rerun()

# Main content area
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("### 🔍 Your Query")
with col2:
    language_options = {
        "🇺🇸 English": "en-US",
        "🇮🇳 हिंदी": "hi-IN",
        "🇪🇸 Español": "es-ES",
        "🇫🇷 Français": "fr-FR",
        "🇩🇪 Deutsch": "de-DE"
    }
    language = st.selectbox("Language", list(language_options.keys()), label_visibility="collapsed")
    selected_lang_code = language_options[language]

# Query Input Tabs
tab1, tab2 = st.tabs(["💬 Text Input", "🎤 Voice Input"])

user_query = None

with tab1:
    default_text = st.session_state.get('example_query', '')
    if default_text:
        st.session_state.pop('example_query')
    
    text_query = st.text_area(
        "Type your natural language query",
        value=default_text,
        placeholder="💡 Try: Show me all employees in HR department\n💡 Or: What's the average salary by department?",
        height=120,
        label_visibility="collapsed"
    )
    
    col1, col2 = st.columns([3, 1])
    with col1:
        text_button = st.button("🚀 Execute Query", type="primary", use_container_width=True)
    with col2:
        if st.button("🗑️ Clear", use_container_width=True):
            st.rerun()

with tab2:
    col_a, col_b = st.columns([3, 1])
    
    with col_a:
        duration = st.slider("⏱️ Duration (seconds)", 3, 10, 5)
        if st.button("🔴 Start Recording", type="primary", use_container_width=True):
            st.session_state.is_recording = True
            with st.spinner("🎤 Listening..."):
                audio_data = record_audio(duration)
                if audio_data:
                    st.success("✅ Recording captured!")
                    with st.spinner("🔄 Converting speech to text..."):
                        transcribed = transcribe_audio(audio_data, selected_lang_code)
                        st.session_state.recorded_text = transcribed
                        st.session_state.is_recording = False
                    st.rerun()
    
    with col_b:
        if st.button("🗑️ Clear", key="clear_voice", use_container_width=True):
            st.session_state.recorded_text = ""
            st.rerun()
    
    # Display transcribed text
    if st.session_state.recorded_text:
        if st.session_state.recorded_text.startswith("❌"):
            st.markdown(f'<div class="error-message">{st.session_state.recorded_text}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="success-message">📝 Transcribed: <strong>{st.session_state.recorded_text}</strong></div>', unsafe_allow_html=True)
    
    voice_query = st.text_input(
        "Edit transcription if needed",
        value=st.session_state.recorded_text if not st.session_state.recorded_text.startswith("❌") else "",
        placeholder="Your transcribed voice query will appear here...",
        label_visibility="collapsed"
    )
    
    voice_button = st.button(
        "🎙️ Execute Voice Query",
        type="primary",
        disabled=not voice_query or voice_query.startswith("❌"),
        use_container_width=True
    )

# Execute Query
if text_button and text_query:
    user_query = text_query
elif voice_button and voice_query:
    user_query = voice_query

if user_query:
    st.session_state.query_history.append(user_query)
    st.session_state.total_queries += 1
    
    st.markdown("---")
    st.markdown(f'<div class="custom-card"><strong>🔄 Processing:</strong> {user_query}</div>', unsafe_allow_html=True)
    
    with st.spinner("⚡ Executing through Langflow pipeline..."):
        response = call_langflow_api(user_query)
        
        if response:
            result_text, error = format_result(response)
            
            if error:
                st.markdown(f'<div class="error-message"><strong>❌ Error:</strong> {error}</div>', unsafe_allow_html=True)
                
                with st.expander("🔧 Troubleshooting Tips"):
                    st.markdown("""
                    1. ✅ Verify Excel file is uploaded in Langflow UI
                    2. ✅ Test the same query directly in Langflow
                    3. ✅ Check database connection in Langflow
                    4. ✅ Ensure all components are properly connected
                    5. ✅ Check Langflow logs for detailed errors
                    """)
            elif result_text:
                st.session_state.successful_queries += 1
                
                st.markdown("### 📊 Query Results")
                
                if "Found" in result_text and "rows:" in result_text:
                    st.markdown('<div class="success-message">✅ Query executed successfully!</div>', unsafe_allow_html=True)
                    st.code(result_text, language="text")
                elif "ERROR" in result_text.upper():
                    st.markdown(f'<div class="error-message">{result_text}</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="success-message">✅ Success!</div>', unsafe_allow_html=True)
                    st.code(result_text, language="text")
            
            with st.expander("🔍 Raw API Response"):
                st.json(response)
        else:
            st.markdown("""
                <div class="error-message">
                    <strong>❌ No response from Langflow</strong><br>
                    Please verify: Langflow is running | Flow ID is correct | No console errors
                </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='background: black; border-radius: 15px; padding: 2rem; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
        <p style='font-size: 1.8rem; color: white; font-weight: 600; margin-bottom: 0.5rem;'>
            🚀 Powered by <strong>Langflow</strong> + <strong>Streamlit</strong>
        </p>
        <p style='font-size: 1.2rem; color: white;'>
            🎤 Voice-Enabled | 🌐 Multilingual | 📊 Business Intelligence | ⚡ Real-time Processing
        </p>
    </div>
""", unsafe_allow_html=True)