async function fetchComplianceReports() {
    const response = await fetch('http://127.0.0.1:8000/api/compliance');
    const data = await response.json();
    return data;
}

function renderReports(reports) {
    const container = document.getElementById('reports');
    container.innerHTML = '';
    reports.forEach(report => {
        const div = document.createElement('div');
        div.className = 'report';
        div.innerHTML = `
            <h2>${report.cloud_provider} - ${report.service}</h2>
            <div>Status: <span class="${report.compliance_status === 'Compliant' ? 'compliant' : 'non-compliant'}">${report.compliance_status}</span></div>
            <div>Last Checked: ${report.last_checked}</div>
            <div class="issues">
                <strong>Issues:</strong>
                <ul>
                    ${report.issues.length === 0 ? '<li>None</li>' : report.issues.map(issue => `<li>${issue}</li>`).join('')}
                </ul>
            </div>
        `;
        container.appendChild(div);
    });
}

fetchComplianceReports().then(renderReports).catch(err => {
    document.getElementById('reports').innerHTML = '<p style="color:red;">Failed to load reports. Is the backend running?</p>';
});
