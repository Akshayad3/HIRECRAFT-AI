
from flask import Flask, request, jsonify, session, send_from_directory
from flask_cors import CORS
from flask_mail import Mail, Message
import sqlite3
import os
import json
import re
import hashlib
import pdfplumber
import docx2txt
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
app.secret_key = 'hirecraft_secret_2024'
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE']   = False
CORS(app, supports_credentials=True, origins=["http://localhost:5000", "http://127.0.0.1:5000"])

# ── Mail Config ───────────────────────────────────────────
app.config['MAIL_SERVER']         = 'smtp.gmail.com'
app.config['MAIL_PORT']           = 587
app.config['MAIL_USE_TLS']        = True
app.config['MAIL_USERNAME']       = 'your_email@gmail.com'
app.config['MAIL_PASSWORD']       = 'your_app_password'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'
mail = Mail(app)

# ── Upload Config ─────────────────────────────────────────
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc', 'txt'}

# ── Skills Database ───────────────────────────────────────
SKILLS_DB = {
    "Infosys": {
        "Software Engineer":  ["python", "java", "sql", "git", "communication"],
        "Data Scientist":     ["python", "machine learning", "sql", "statistics", "excel"],
        "Frontend Developer": ["html", "css", "javascript", "react", "figma"],
        "DevOps Engineer":    ["docker", "linux", "aws", "git", "networking"],
        "Business Analyst":   ["excel", "sql", "communication", "powerpoint", "reporting"],
    },
    "Wipro": {
        "Software Engineer":     ["java", "python", "sql", "git", "problem solving"],
        "Cloud Engineer":        ["aws", "linux", "docker", "networking", "python"],
        "QA Engineer":           ["manual testing", "selenium", "sql", "jira", "excel"],
        "Data Analyst":          ["sql", "excel", "python", "tableau", "reporting"],
        "Cybersecurity Analyst": ["networking", "linux", "python", "firewalls", "compliance"],
    },
    "TCS": {
        "Software Developer": ["java", "sql", "git", "python", "communication"],
        "Data Engineer":      ["python", "sql", "excel", "aws", "reporting"],
        "SAP Consultant":     ["sap", "excel", "sql", "communication", "reporting"],
        "AI Engineer":        ["python", "machine learning", "sql", "tensorflow", "git"],
        "Project Manager":    ["communication", "excel", "jira", "leadership", "reporting"],
    },
    "Accenture": {
        "Software Engineer":  ["python", "javascript", "sql", "git", "communication"],
        "Consulting Analyst": ["excel", "powerpoint", "communication", "sql", "reporting"],
        "Cloud Architect":    ["aws", "docker", "linux", "networking", "python"],
        "Data Scientist":     ["python", "machine learning", "sql", "excel", "statistics"],
        "UX Designer":        ["figma", "html", "css", "communication", "user research"],
    },
    "Mahindra": {
        "Software Engineer":         ["java", "python", "sql", "git", "communication"],
        "Embedded Systems Engineer": ["c", "c++", "linux", "microcontrollers", "debugging"],
        "Data Analyst":              ["sql", "excel", "python", "reporting", "powerpoint"],
        "Mechanical Engineer":       ["autocad", "matlab", "solidworks", "excel", "communication"],
        "HR Analyst":                ["excel", "communication", "recruitment", "powerpoint", "reporting"],
    },
    "HCL": {
        "Software Engineer": ["java", "python", "sql", "git", "communication"],
        "Network Engineer":  ["networking", "cisco", "linux", "firewalls", "communication"],
        "Data Scientist":    ["python", "machine learning", "sql", "excel", "statistics"],
        "ERP Consultant":    ["sap", "sql", "excel", "communication", "reporting"],
        "DevOps Engineer":   ["docker", "linux", "aws", "git", "python"],
    },
    "Tech Mahindra": {
        "Software Developer":     ["java", "python", "sql", "git", "communication"],
        "Telecom Engineer":       ["networking", "linux", "python", "communication", "documentation"],
        "QA Engineer":            ["manual testing", "selenium", "sql", "jira", "communication"],
        "Business Analyst":       ["excel", "sql", "communication", "powerpoint", "reporting"],
        "Cybersecurity Engineer": ["networking", "linux", "python", "firewalls", "communication"],
    },
    "Cognizant": {
        "Software Engineer":  ["java", "python", "sql", "git", "communication"],
        "Data Engineer":      ["python", "sql", "aws", "excel", "reporting"],
        "Frontend Developer": ["html", "css", "javascript", "react", "git"],
        "Cloud Engineer":     ["aws", "docker", "linux", "python", "networking"],
        "Business Analyst":   ["excel", "sql", "communication", "powerpoint", "reporting"],
    },
    "Amazon": {
        "Software Development Engineer": ["python", "java", "sql", "algorithms", "aws"],
        "Data Scientist":                ["python", "machine learning", "sql", "statistics", "excel"],
        "Cloud Solutions Architect":     ["aws", "docker", "linux", "networking", "python"],
        "Product Manager":               ["communication", "excel", "sql", "powerpoint", "leadership"],
        "ML Engineer":                   ["python", "machine learning", "tensorflow", "sql", "git"],
    },
    "Google": {
        "Software Engineer": ["python", "java", "algorithms", "sql", "git"],
        "Data Scientist":    ["python", "machine learning", "sql", "statistics", "excel"],
        "UX Researcher":     ["communication", "figma", "excel", "user research", "reporting"],
        "DevOps Engineer":   ["docker", "linux", "python", "git", "networking"],
        "Product Manager":   ["communication", "excel", "sql", "leadership", "powerpoint"],
    },
    "Microsoft": {
        "Software Engineer":  ["python", "java", "sql", "git", "communication"],
        "Cloud Engineer":     ["azure", "docker", "linux", "networking", "python"],
        "Data Engineer":      ["python", "sql", "excel", "azure", "reporting"],
        "AI Engineer":        ["python", "machine learning", "tensorflow", "sql", "git"],
        "Business Analyst":   ["excel", "powerpoint", "sql", "communication", "reporting"],
    },
    "IBM": {
        "Software Engineer":    ["java", "python", "sql", "git", "communication"],
        "AI Consultant":        ["python", "machine learning", "communication", "sql", "excel"],
        "Blockchain Developer": ["python", "javascript", "sql", "git", "communication"],
        "Data Analyst":         ["sql", "excel", "python", "tableau", "reporting"],
        "Cloud Architect":      ["aws", "docker", "linux", "networking", "python"],
    },
    "Deloitte": {
        "Consulting Analyst":    ["excel", "powerpoint", "communication", "sql", "reporting"],
        "Data Analyst":          ["sql", "excel", "python", "tableau", "reporting"],
        "Cybersecurity Analyst": ["networking", "linux", "python", "firewalls", "compliance"],
        "SAP Consultant":        ["sap", "sql", "excel", "communication", "reporting"],
        "Risk Analyst":          ["excel", "sql", "statistics", "communication", "reporting"],
    },
    "Capgemini": {
        "Software Engineer":  ["java", "python", "sql", "git", "communication"],
        "Data Scientist":     ["python", "machine learning", "sql", "excel", "statistics"],
        "Cloud Engineer":     ["aws", "docker", "linux", "python", "networking"],
        "Business Analyst":   ["excel", "sql", "communication", "powerpoint", "reporting"],
        "ERP Consultant":     ["sap", "sql", "excel", "communication", "reporting"],
    },
    "Oracle": {
        "Software Engineer":      ["java", "sql", "python", "git", "communication"],
        "Database Administrator": ["sql", "oracle db", "linux", "excel", "reporting"],
        "Cloud Engineer":         ["aws", "docker", "linux", "python", "networking"],
        "ERP Consultant":         ["sql", "excel", "communication", "reporting", "powerpoint"],
        "Data Analyst":           ["sql", "excel", "python", "tableau", "reporting"],
    },
}
# ── Database ──────────────────────────────────────────────
def get_db():
    db_path = os.path.join(os.path.dirname(__file__), 'hirecraft.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS companies (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        name       TEXT UNIQUE NOT NULL,
        email      TEXT UNIQUE NOT NULL,
        password   TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        email      TEXT UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS applications (
        id               INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email       TEXT NOT NULL,
        company_name     TEXT NOT NULL,
        job_role         TEXT NOT NULL,
        resume_path      TEXT NOT NULL,
        resume_text      TEXT,
        match_percentage REAL,
        status           TEXT DEFAULT 'pending',
        matched_skills   TEXT,
        missing_skills   TEXT,
        submitted_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    companies = [
        ("Infosys",       "infosys@hirecraft.com",      hashlib.sha256("infosys123".encode()).hexdigest()),
        ("Wipro",         "wipro@hirecraft.com",        hashlib.sha256("wipro123".encode()).hexdigest()),
        ("TCS",           "tcs@hirecraft.com",          hashlib.sha256("tcs123".encode()).hexdigest()),
        ("Accenture",     "accenture@hirecraft.com",    hashlib.sha256("accenture123".encode()).hexdigest()),
        ("Mahindra",      "mahindra@hirecraft.com",     hashlib.sha256("mahindra123".encode()).hexdigest()),
        ("HCL",           "hcl@hirecraft.com",          hashlib.sha256("hcl123".encode()).hexdigest()),
        ("Tech Mahindra", "techmahindra@hirecraft.com", hashlib.sha256("techmahindra123".encode()).hexdigest()),
        ("Cognizant",     "cognizant@hirecraft.com",    hashlib.sha256("cognizant123".encode()).hexdigest()),
        ("Amazon",        "amazon@hirecraft.com",       hashlib.sha256("amazon123".encode()).hexdigest()),
        ("Google",        "google@hirecraft.com",       hashlib.sha256("google123".encode()).hexdigest()),
        ("Microsoft",     "microsoft@hirecraft.com",    hashlib.sha256("microsoft123".encode()).hexdigest()),
        ("IBM",           "ibm@hirecraft.com",          hashlib.sha256("ibm123".encode()).hexdigest()),
        ("Deloitte",      "deloitte@hirecraft.com",     hashlib.sha256("deloitte123".encode()).hexdigest()),
        ("Capgemini",     "capgemini@hirecraft.com",    hashlib.sha256("capgemini123".encode()).hexdigest()),
        ("Oracle",        "oracle@hirecraft.com",       hashlib.sha256("oracle123".encode()).hexdigest()),
    ]
    for name, email, pwd in companies:
        try:
            c.execute(
                "INSERT INTO companies (name, email, password) VALUES (?,?,?)",
                (name, email, pwd)
            )
        except:
            pass
    conn.commit()
    conn.close()

# ── NLP Helpers ───────────────────────────────────────────
def extract_text_from_file(filepath):
    ext  = filepath.rsplit('.', 1)[-1].lower()
    text = ""
    try:
        if ext == 'pdf':
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    t = page.extract_text()
                    if t:
                        text += t + "\n"
        elif ext in ['docx', 'doc']:
            text = docx2txt.process(filepath)
        elif ext == 'txt':
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read()
    except Exception as e:
        print(f"Text extraction error: {e}")
    return text.lower()

def calculate_match(resume_text, company, job_role):
    required_skills = SKILLS_DB.get(company, {}).get(job_role, [])
    if not required_skills:
        return 0, [], []
    matched = []
    missing = []
    for skill in required_skills:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, resume_text):
            matched.append(skill)
        else:
            missing.append(skill)
    percentage = (len(matched) / len(required_skills)) * 100
    return round(percentage, 2), matched, missing

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ── Page Routes ───────────────────────────────────────────
TEMPLATES = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'templates')

@app.route('/')
def home():
    return send_from_directory(TEMPLATES, 'index.html')

@app.route('/<path:filename>')
def serve_page(filename):
    if filename.endswith('.html'):
        return send_from_directory(TEMPLATES, filename)
    return "Not Found", 404

# ── API — General ─────────────────────────────────────────
@app.route('/api/companies', methods=['GET'])
def get_companies():
    return jsonify({"companies": list(SKILLS_DB.keys())})

@app.route('/api/jobs/<company>', methods=['GET'])
def get_jobs(company):
    jobs = list(SKILLS_DB.get(company, {}).keys())
    return jsonify({"jobs": jobs})

@app.route('/api/skills/<company>/<job_role>', methods=['GET'])
def get_skills(company, job_role):
    skills = SKILLS_DB.get(company, {}).get(job_role, [])
    return jsonify({"skills": skills})

@app.route('/api/stats', methods=['GET'])
def global_stats():
    conn = get_db()
    c    = conn.cursor()
    c.execute("SELECT COUNT(*) as count FROM applications")
    total_apps  = c.fetchone()['count']
    c.execute("SELECT COUNT(*) as count FROM users")
    total_users = c.fetchone()['count']
    c.execute("SELECT COUNT(*) as count FROM applications WHERE status='shortlisted'")
    shortlisted = c.fetchone()['count']
    conn.close()
    return jsonify({
        "total_applications": total_apps,
        "total_users":        total_users,
        "shortlisted":        shortlisted,
        "companies":          len(SKILLS_DB)
    })

# ── API — User ────────────────────────────────────────────
@app.route('/api/user/login', methods=['POST'])
def user_login():
    data  = request.json
    email = data.get('email', '').strip().lower()
    if not email or '@' not in email:
        return jsonify({"error": "Enter a valid email"}), 400
    conn = get_db()
    c    = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (email) VALUES (?)", (email,))
    conn.commit()
    conn.close()
    session['user_email'] = email
    session['role']       = 'user'
    return jsonify({"success": True, "email": email})

@app.route('/api/user/logout', methods=['POST'])
def user_logout():
    session.clear()
    return jsonify({"success": True})

@app.route('/api/user/session', methods=['GET'])
def user_session():
    return jsonify({
        "user_email": session.get('user_email'),
        "role":       session.get('role')
    })

@app.route('/api/user/applications', methods=['GET'])
def user_applications():
    email = session.get('user_email')
    if not email:
        return jsonify({"error": "Not logged in"}), 401
    conn = get_db()
    c    = conn.cursor()
    c.execute(
        "SELECT * FROM applications WHERE user_email=? ORDER BY submitted_at DESC",
        (email,)
    )
    rows = [dict(r) for r in c.fetchall()]
    conn.close()
    return jsonify({"applications": rows})

@app.route('/api/submit-resume', methods=['POST'])
def submit_resume():
    user_email = session.get('user_email')
    if not user_email:
        return jsonify({"error": "Please login first"}), 401
    if 'resume' not in request.files:
        return jsonify({"error": "No resume file uploaded"}), 400

    file     = request.files['resume']
    company  = request.form.get('company')
    job_role = request.form.get('job_role')

    if not file or not allowed_file(file.filename):
        return jsonify({"error": "Invalid file. Use PDF, DOCX, or TXT"}), 400
    if not company or not job_role:
        return jsonify({"error": "Select company and job role"}), 400

    filename = secure_filename(
        f"{user_email}_{company}_{job_role}_"
        f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"
    )
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    resume_text              = extract_text_from_file(filepath)
    match_pct, matched, missing = calculate_match(resume_text, company, job_role)
    status                   = 'shortlisted' if match_pct >= 70 else 'rejected'

    conn = get_db()
    c    = conn.cursor()
    c.execute(
        '''INSERT INTO applications
           (user_email, company_name, job_role, resume_path, resume_text,
            match_percentage, status, matched_skills, missing_skills)
           VALUES (?,?,?,?,?,?,?,?,?)''',
        (user_email, company, job_role, filename, resume_text[:2000],
         match_pct, status, json.dumps(matched), json.dumps(missing))
    )
    conn.commit()
    conn.close()

    try:
        if status == 'shortlisted':
            msg = Message(
                subject=f"Congratulations! You are Shortlisted at {company}",
                recipients=[user_email],
                html=f"""
                <div style="font-family:Arial;padding:20px;background:#0f0f1a;
                            color:#fff;border-radius:12px;">
                  <h2 style="color:#00d4ff;">HireCraft AI — You are Shortlisted!</h2>
                  <p>Dear Candidate,</p>
                  <p>You have been <strong>shortlisted</strong> for
                     <strong>{job_role}</strong> at <strong>{company}</strong>.</p>
                  <p>Your resume matched <strong>{match_pct}%</strong>
                     of required skills.</p>
                  <p><strong>Matched Skills:</strong> {', '.join(matched)}</p>
                  <p>The HR team will contact you shortly for next steps.</p>
                  <p style="color:#00d4ff;">Best of luck!<br>Team HireCraft AI</p>
                </div>"""
            )
        else:
            msg = Message(
                subject=f"HireCraft AI — Application Update for {job_role} at {company}",
                recipients=[user_email],
                html=f"""
                <div style="font-family:Arial;padding:20px;background:#0f0f1a;
                            color:#fff;border-radius:12px;">
                  <h2 style="color:#ff6b6b;">HireCraft AI — Application Status</h2>
                  <p>Dear Candidate,</p>
                  <p>Thank you for applying for <strong>{job_role}</strong>
                     at <strong>{company}</strong>.</p>
                  <p>Your resume matched <strong>{match_pct}%</strong>
                     (minimum 70% required).</p>
                  <p><strong>Skills to improve:</strong> {', '.join(missing)}</p>
                  <p>Upskill and apply again!</p>
                  <p style="color:#00d4ff;">Best Regards,<br>Team HireCraft AI</p>
                </div>"""
            )
        mail.send(msg)
    except Exception as e:
        print(f"Email error: {e}")

    return jsonify({
        "success":        True,
        "match_percentage": match_pct,
        "status":         status,
        "matched_skills": matched,
        "missing_skills": missing
    })

# ── API — Company ─────────────────────────────────────────
@app.route('/api/company/login', methods=['POST'])
def company_login():
    data     = request.json
    email    = data.get('email', '').strip().lower()
    password = data.get('password', '')
    hashed   = hashlib.sha256(password.encode()).hexdigest()

    conn = get_db()
    c    = conn.cursor()
    c.execute(
        "SELECT * FROM companies WHERE email=? AND password=?",
        (email, hashed)
    )
    company = c.fetchone()
    conn.close()

    if not company:
        return jsonify({"error": "Invalid credentials"}), 401

    session['company_name']  = company['name']
    session['company_email'] = email
    session['role']          = 'company'
    return jsonify({"success": True, "company_name": company['name']})

@app.route('/api/company/logout', methods=['POST'])
def company_logout():
    session.clear()
    return jsonify({"success": True})

@app.route('/api/company/session', methods=['GET'])
def company_session():
    return jsonify({
        "company_name": session.get('company_name'),
        "role":         session.get('role')
    })

@app.route('/api/company/applications', methods=['GET'])
def company_applications():
    company_name = session.get('company_name')
    if not company_name:
        return jsonify({"error": "Not logged in"}), 401

    job_role      = request.args.get('job_role', '')
    status_filter = request.args.get('status', '')

    conn   = get_db()
    c      = conn.cursor()
    query  = "SELECT * FROM applications WHERE company_name=?"
    params = [company_name]

    if job_role:
        query += " AND job_role=?"
        params.append(job_role)
    if status_filter:
        query += " AND status=?"
        params.append(status_filter)

    query += " ORDER BY match_percentage DESC"
    c.execute(query, params)
    rows = [dict(r) for r in c.fetchall()]
    conn.close()
    return jsonify({"applications": rows, "company_name": company_name})

@app.route('/api/company/stats', methods=['GET'])
def company_stats():
    company_name = session.get('company_name')
    if not company_name:
        return jsonify({"error": "Not logged in"}), 401

    conn = get_db()
    c    = conn.cursor()

    c.execute(
        "SELECT COUNT(*) as total FROM applications WHERE company_name=?",
        (company_name,)
    )
    total = c.fetchone()['total']

    c.execute(
        "SELECT COUNT(*) as cnt FROM applications WHERE company_name=? AND status='shortlisted'",
        (company_name,)
    )
    shortlisted = c.fetchone()['cnt']

    c.execute(
        "SELECT COUNT(*) as cnt FROM applications WHERE company_name=? AND status='rejected'",
        (company_name,)
    )
    rejected = c.fetchone()['cnt']

    c.execute(
        "SELECT job_role, COUNT(*) as count FROM applications WHERE company_name=? GROUP BY job_role",
        (company_name,)
    )
    by_role = [dict(r) for r in c.fetchall()]
    conn.close()

    return jsonify({
        "total":       total,
        "shortlisted": shortlisted,
        "rejected":    rejected,
        "by_role":     by_role
    })

# ── Run ───────────────────────────────────────────────────
if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
