const SKILLS_DB = {
  "Infosys": {
    "Software Engineer": ["python","java","javascript","sql","git","algorithms","data structures","oop","rest api","agile"],
    "Data Scientist": ["python","machine learning","deep learning","tensorflow","pandas","numpy","statistics","sql","data visualization","nlp"],
    "Frontend Developer": ["html","css","javascript","react","angular","typescript","responsive design","git","figma","rest api"],
    "DevOps Engineer": ["docker","kubernetes","aws","ci/cd","linux","jenkins","terraform","git","python","monitoring"],
    "Business Analyst": ["business analysis","sql","excel","requirements gathering","uml","agile","jira","powerpoint","stakeholder management","reporting"]
  },
  "Wipro": {
    "Software Engineer": ["java","python","c++","sql","git","oop","data structures","algorithms","rest api","junit"],
    "Cloud Engineer": ["aws","azure","gcp","docker","kubernetes","terraform","linux","python","networking","ci/cd"],
    "QA Engineer": ["manual testing","selenium","java","sql","agile","jira","test cases","api testing","regression testing","bug tracking"],
    "Data Analyst": ["sql","python","excel","tableau","power bi","statistics","data visualization","reporting","etl","pandas"],
    "Cybersecurity Analyst": ["network security","firewalls","siem","python","linux","vulnerability assessment","ethical hacking","compliance","encryption","incident response"]
  },
  "TCS": {
    "Software Developer": ["java","python","javascript","sql","git","spring boot","microservices","rest api","maven","agile"],
    "Data Engineer": ["python","sql","spark","hadoop","etl","aws","azure","kafka","airflow","data warehousing"],
    "SAP Consultant": ["sap","sap fico","sap mm","sap sd","abap","business analysis","sql","erp","project management","reporting"],
    "AI Engineer": ["python","machine learning","deep learning","nlp","tensorflow","pytorch","sql","docker","rest api","git"],
    "Project Manager": ["project management","agile","scrum","jira","risk management","stakeholder management","ms project","pmp","budgeting","reporting"]
  },
  "Accenture": {
    "Software Engineer": ["python","java","javascript","react","node.js","sql","git","rest api","docker","agile"],
    "Consulting Analyst": ["business analysis","powerpoint","excel","sql","data visualization","stakeholder management","problem solving","reporting","agile","communication"],
    "Cloud Architect": ["aws","azure","gcp","docker","kubernetes","terraform","microservices","python","networking","security"],
    "Data Scientist": ["python","machine learning","statistics","sql","tableau","tensorflow","pandas","numpy","data visualization","nlp"],
    "UX Designer": ["figma","adobe xd","user research","wireframing","prototyping","html","css","usability testing","design thinking","responsive design"]
  },
  "Mahindra": {
    "Software Engineer": ["java","python","c++","sql","git","oop","rest api","spring boot","agile","maven"],
    "Embedded Systems Engineer": ["c","c++","embedded systems","rtos","microcontrollers","arm","can bus","linux","debugging","matlab"],
    "Data Analyst": ["sql","python","excel","power bi","tableau","statistics","reporting","data visualization","etl","pandas"],
    "Mechanical Engineer": ["autocad","solidworks","catia","matlab","fea","manufacturing","project management","python","ms office","quality control"],
    "HR Analyst": ["excel","sql","powerpoint","hrms","data analysis","reporting","communication","recruitment","payroll","compliance"]
  },
  "HCL": {
    "Software Engineer": ["java","python","javascript","sql","git","rest api","microservices","agile","docker","spring boot"],
    "Network Engineer": ["networking","cisco","routing","switching","firewalls","linux","tcp/ip","vpn","network security","monitoring"],
    "Data Scientist": ["python","machine learning","deep learning","sql","tensorflow","pandas","statistics","nlp","data visualization","git"],
    "ERP Consultant": ["sap","oracle erp","sql","business analysis","erp","project management","reporting","excel","stakeholder management","documentation"],
    "DevOps Engineer": ["docker","kubernetes","aws","jenkins","terraform","linux","ci/cd","python","git","monitoring"]
  },
  "Tech Mahindra": {
    "Software Developer": ["java","python","javascript","sql","git","rest api","agile","spring boot","microservices","docker"],
    "Telecom Engineer": ["telecom","4g","5g","networking","python","linux","sql","testing","monitoring","documentation"],
    "QA Engineer": ["selenium","java","manual testing","api testing","sql","jira","agile","test automation","regression testing","bug tracking"],
    "Business Analyst": ["business analysis","sql","excel","requirements gathering","agile","jira","uml","powerpoint","stakeholder management","reporting"],
    "Cybersecurity Engineer": ["network security","python","linux","ethical hacking","siem","firewalls","vulnerability assessment","encryption","compliance","incident response"]
  },
  "Cognizant": {
    "Software Engineer": ["java","python","javascript","sql","git","rest api","spring boot","agile","microservices","junit"],
    "Data Engineer": ["python","sql","spark","hadoop","aws","etl","kafka","airflow","data warehousing","scala"],
    "Frontend Developer": ["html","css","javascript","react","angular","typescript","git","figma","rest api","responsive design"],
    "Cloud Engineer": ["aws","azure","docker","kubernetes","terraform","python","linux","ci/cd","networking","monitoring"],
    "Business Analyst": ["business analysis","sql","excel","agile","jira","requirements gathering","uml","powerpoint","stakeholder management","reporting"]
  },
  "Amazon": {
    "Software Development Engineer": ["java","python","algorithms","data structures","sql","distributed systems","rest api","git","aws","system design"],
    "Data Scientist": ["python","machine learning","deep learning","sql","statistics","tensorflow","pytorch","nlp","data visualization","aws"],
    "Cloud Solutions Architect": ["aws","docker","kubernetes","terraform","microservices","python","networking","security","system design","ci/cd"],
    "Product Manager": ["product management","agile","sql","data analysis","user research","roadmap","stakeholder management","excel","communication","jira"],
    "ML Engineer": ["python","machine learning","deep learning","tensorflow","pytorch","aws","docker","sql","mlops","git"]
  },
  "Google": {
    "Software Engineer": ["python","java","c++","algorithms","data structures","distributed systems","system design","sql","git","rest api"],
    "Data Scientist": ["python","machine learning","statistics","tensorflow","sql","big data","data visualization","nlp","deep learning","research"],
    "UX Researcher": ["user research","usability testing","qualitative research","quantitative research","figma","data analysis","communication","surveys","a/b testing","reporting"],
    "DevOps Engineer": ["kubernetes","docker","gcp","terraform","linux","python","ci/cd","monitoring","git","networking"],
    "Product Manager": ["product management","agile","data analysis","sql","user research","roadmap","communication","stakeholder management","a/b testing","go-to-market"]
  },
  "Microsoft": {
    "Software Engineer": ["c#","python","java","azure","sql","git","rest api",".net","agile","system design"],
    "Cloud Engineer": ["azure","aws","docker","kubernetes","terraform","python","powershell","networking","ci/cd","monitoring"],
    "Data Engineer": ["python","sql","azure","spark","etl","data warehousing","power bi","kafka","airflow","scala"],
    "AI Engineer": ["python","machine learning","deep learning","azure","tensorflow","pytorch","nlp","mlops","docker","git"],
    "Business Analyst": ["excel","power bi","sql","business analysis","azure","powerpoint","stakeholder management","reporting","agile","requirements gathering"]
  },
  "IBM": {
    "Software Engineer": ["java","python","javascript","sql","git","rest api","microservices","docker","agile","spring boot"],
    "AI Consultant": ["python","machine learning","deep learning","nlp","watson","sql","data visualization","communication","stakeholder management","reporting"],
    "Blockchain Developer": ["blockchain","hyperledger","smart contracts","python","javascript","cryptography","sql","rest api","git","docker"],
    "Data Analyst": ["sql","python","excel","tableau","power bi","statistics","reporting","etl","data visualization","cognos"],
    "Cloud Architect": ["ibm cloud","aws","azure","docker","kubernetes","terraform","microservices","python","networking","security"]
  },
  "Deloitte": {
    "Consulting Analyst": ["business analysis","excel","powerpoint","sql","data visualization","stakeholder management","problem solving","communication","agile","reporting"],
    "Data Analyst": ["sql","python","excel","tableau","power bi","statistics","reporting","data visualization","etl","communication"],
    "Cybersecurity Analyst": ["network security","siem","firewalls","python","compliance","vulnerability assessment","incident response","risk analysis","encryption","linux"],
    "SAP Consultant": ["sap","sap fico","sap mm","abap","sql","business analysis","erp","project management","reporting","excel"],
    "Risk Analyst": ["risk analysis","excel","sql","statistics","compliance","financial modeling","reporting","powerpoint","python","audit"]
  },
  "Capgemini": {
    "Software Engineer": ["java","python","javascript","sql","git","rest api","agile","spring boot","docker","microservices"],
    "Data Scientist": ["python","machine learning","sql","tensorflow","pandas","statistics","data visualization","nlp","deep learning","git"],
    "Cloud Engineer": ["aws","azure","docker","kubernetes","terraform","python","linux","ci/cd","networking","monitoring"],
    "Business Analyst": ["business analysis","sql","excel","agile","jira","requirements gathering","uml","powerpoint","stakeholder management","reporting"],
    "ERP Consultant": ["sap","oracle erp","sql","business analysis","project management","reporting","excel","documentation","stakeholder management","erp"]
  },
  "Oracle": {
    "Software Engineer": ["java","sql","python","oracle db","rest api","git","microservices","spring boot","agile","pl/sql"],
    "Database Administrator": ["oracle db","sql","pl/sql","database tuning","backup recovery","linux","python","monitoring","data warehousing","documentation"],
    "Cloud Engineer": ["oracle cloud","aws","docker","kubernetes","terraform","python","linux","networking","ci/cd","monitoring"],
    "ERP Consultant": ["oracle erp","oracle fusion","sql","business analysis","erp","project management","reporting","excel","stakeholder management","pl/sql"],
    "Data Analyst": ["sql","oracle db","python","excel","tableau","statistics","reporting","data visualization","etl","pl/sql"]
  }
};

let allApplications = [];
let companyName = '';

document.addEventListener('DOMContentLoaded', function () {

  fetch('/api/company/session', { credentials: 'include' })
    .then(r => r.json())
    .then(d => {
      if (!d.company_name) {
        window.location.href = 'company-login.html';
        return;
      }
      companyName = d.company_name;
      document.getElementById('companyNameNav').textContent = companyName;
      document.getElementById('companyTagline').textContent = `${companyName} — Recruitment Dashboard`;
      loadStats();
      loadApplications();
      populateRoleFilter();
      renderSkillsRef();
    })
    .catch(() => {
      window.location.href = 'company-login.html';
    });

});

function populateRoleFilter() {
  const roles = Object.keys(SKILLS_DB[companyName] || {});
  const sel = document.getElementById('filterRole');
  sel.innerHTML = '<option value="">All Roles</option>';
  roles.forEach(r => {
    const opt = document.createElement('option');
    opt.value = r;
    opt.textContent = r;
    sel.appendChild(opt);
  });
}

function renderSkillsRef() {
  const roles = SKILLS_DB[companyName] || {};
  document.getElementById('skillsRefContent').innerHTML = Object.entries(roles)
    .map(([role, skills]) => `
      <div class="skills-ref-role">
        <div class="skills-ref-role-name">
          <i class="fas fa-briefcase" style="margin-right:6px;color:#a78bfa"></i>${role}
        </div>
        <div class="skills-tags">
          ${skills.map(s => `<span class="skill-tag">${s}</span>`).join('')}
        </div>
      </div>
    `).join('');
}

function toggleSkillsRef() {
  const content = document.getElementById('skillsRefContent');
  const icon = document.getElementById('skillsRefIcon');
  content.classList.toggle('hidden');
  icon.className = content.classList.contains('hidden')
    ? 'fas fa-chevron-down'
    : 'fas fa-chevron-up';
}

function loadStats() {
  fetch('/api/company/stats', { credentials: 'include' })
    .then(r => r.json())
    .then(d => {
      document.getElementById('statTotal').textContent = d.total;
      document.getElementById('statShortlisted').textContent = d.shortlisted;
      document.getElementById('statRejected').textContent = d.rejected;
      const rate = d.total > 0
        ? Math.round((d.shortlisted / d.total) * 100)
        : 0;
      document.getElementById('statRate').textContent = rate + '%';

      const breakdown = document.getElementById('roleBreakdown');
      if (d.by_role && d.by_role.length > 0) {
        breakdown.innerHTML = d.by_role.map(r => `
          <div class="role-stat-item">
            <span class="role-stat-name">
              <i class="fas fa-briefcase"></i> ${r.job_role}
            </span>
            <span class="role-stat-count">${r.count}</span>
          </div>
        `).join('');
      } else {
        breakdown.innerHTML = `
          <p style="color:var(--text-dim);font-size:13px;padding:8px 0">
            No applications yet
          </p>`;
      }
    });
}

function loadApplications() {
  const role = document.getElementById('filterRole').value;
  const status = document.getElementById('filterStatus').value;
  let url = '/api/company/applications?';
  if (role)   url += `job_role=${encodeURIComponent(role)}&`;
  if (status) url += `status=${encodeURIComponent(status)}`;

  fetch(url, { credentials: 'include' })
    .then(r => r.json())
    .then(d => {
      allApplications = d.applications || [];
      renderApplications(allApplications);
      loadStats();
    });
}

function filterCards() {
  const q = document.getElementById('searchInput').value.toLowerCase();
  renderApplications(
    allApplications.filter(a => a.user_email.toLowerCase().includes(q))
  );
}

function renderApplications(apps) {
  const grid = document.getElementById('applicationsGrid');
  document.getElementById('applicationsCount').textContent =
    `${apps.length} candidate${apps.length !== 1 ? 's' : ''}`;

  if (!apps.length) {
    grid.innerHTML = `
      <div class="empty-state" style="grid-column:1/-1">
        <i class="fas fa-inbox"></i>
        <p>No applications found</p>
        <span style="font-size:12px;color:var(--text-dim)">
          Applications will appear here once candidates submit resumes
        </span>
      </div>`;
    return;
  }

  grid.innerHTML = apps.map(a => `
    <div class="candidate-card-item" onclick="openModal(${a.id})">
      <div style="display:flex;justify-content:space-between;
                  align-items:flex-start;margin-bottom:8px">
        <div class="candidate-email">${a.user_email}</div>
        <span class="status-badge status-${a.status}">${a.status}</span>
      </div>
      <div class="candidate-role">${a.job_role}</div>
      <div class="candidate-meta">
        <div class="match-pct-big ${a.status === 'shortlisted' ? 'high' : 'low'}">
          ${a.match_percentage}%
        </div>
        <div style="flex:1;margin-left:16px">
          <div class="app-match-bar" style="height:6px">
            <div class="app-match-fill ${a.status === 'shortlisted' ? 'high' : 'low'}"
                 style="width:${a.match_percentage}%"></div>
          </div>
          <div style="font-size:11px;color:var(--text-dim);margin-top:4px">
            ${new Date(a.submitted_at).toLocaleDateString()}
          </div>
        </div>
      </div>
    </div>
  `).join('');
}

function openModal(id) {
  const a = allApplications.find(x => x.id === id);
  if (!a) return;
  const matched = JSON.parse(a.matched_skills || '[]');
  const missing = JSON.parse(a.missing_skills || '[]');
  const isShortlisted = a.status === 'shortlisted';

  document.getElementById('modalContent').innerHTML = `
    <div class="modal-candidate-name">${a.user_email}</div>
    <div class="modal-role">${a.job_role} at ${a.company_name}</div>
    <div class="modal-match-big">
      <div class="modal-match-pct"
           style="color:${isShortlisted ? 'var(--success)' : 'var(--danger)'}">
        ${a.match_percentage}%
      </div>
      <div>
        <div style="font-size:16px;font-weight:600">
          ${isShortlisted ? 'Shortlisted' : 'Not Shortlisted'}
        </div>
        <div class="modal-match-label">Minimum required: 70%</div>
        <span class="status-badge status-${a.status}"
              style="margin-top:6px;display:inline-block">
          ${a.status}
        </span>
      </div>
    </div>
    <div class="match-bar-bg" style="margin-bottom:20px">
      <div class="match-bar-fill ${isShortlisted ? 'high' : 'low'}"
           style="width:${a.match_percentage}%"></div>
    </div>
    <div class="modal-skills-section">
      <div class="modal-skills-title">
        <i class="fas fa-check" style="color:var(--success);margin-right:6px"></i>
        Matched Skills (${matched.length})
      </div>
      <div class="skills-tags">
        ${matched.map(s => `<span class="skill-tag matched">${s}</span>`).join('')
          || '<span style="color:var(--text-dim);font-size:13px">None matched</span>'}
      </div>
    </div>
    <div class="modal-skills-section" style="margin-top:16px">
      <div class="modal-skills-title">
        <i class="fas fa-xmark" style="color:var(--danger);margin-right:6px"></i>
        Missing Skills (${missing.length})
      </div>
      <div class="skills-tags">
        ${missing.map(s => `<span class="skill-tag missing">${s}</span>`).join('')
          || '<span style="color:var(--success);font-size:13px">No skill gaps!</span>'}
      </div>
    </div>
    <div class="modal-date">
      <i class="fas fa-calendar" style="margin-right:6px"></i>
      Applied: ${new Date(a.submitted_at).toLocaleString()}
    </div>
  `;
  document.getElementById('modalOverlay').classList.remove('hidden');
}

function closeModal() {
  document.getElementById('modalOverlay').classList.add('hidden');
}

document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeModal();
});
