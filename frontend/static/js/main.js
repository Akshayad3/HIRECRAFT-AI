
function showAlert(el, msg) {
  el.textContent = msg;
  el.classList.remove('hidden');
}

function logout() {
  const isCompany = window.location.href.includes('company');
  const endpoint = isCompany ? '/api/company/logout' : '/api/user/logout';
  fetch(endpoint, { method: 'POST', credentials: 'include' })
    .then(() => window.location.href = 'index.html');
}

document.addEventListener('DOMContentLoaded', () => {
  const zone = document.getElementById('uploadZone');
  if (!zone) return;
  zone.addEventListener('dragover', e => { e.preventDefault(); zone.classList.add('dragover'); });
  zone.addEventListener('dragleave', () => zone.classList.remove('dragover'));
  zone.addEventListener('drop', e => {
    e.preventDefault();
    zone.classList.remove('dragover');
    const file = e.dataTransfer.files[0];
    if (file) {
      const input = document.getElementById('resumeFile');
      const dt = new DataTransfer();
      dt.items.add(file);
      input.files = dt.files;
      fileSelected(input);
    }
  });
});

