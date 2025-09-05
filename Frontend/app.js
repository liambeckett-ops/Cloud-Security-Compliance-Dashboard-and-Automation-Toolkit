// Basic frontend script for Cloud Security Compliance Dashboard
// Fetches compliance data from backend and displays it

async function fetchComplianceData() {
	try {
		const response = await fetch('http://localhost:8000/compliance');
		if (!response.ok) {
			throw new Error('Network response was not ok');
		}
		const data = await response.json();
		displayComplianceData(data);
	} catch (error) {
		console.error('Error fetching compliance data:', error);
	}
}

function displayComplianceData(data) {
	const container = document.getElementById('compliance-container');
	if (!container) return;
	container.innerHTML = '';
	data.forEach(check => {
		const div = document.createElement('div');
		div.textContent = `${check.name}: ${check.passed ? 'Passed' : 'Failed'}`;
		container.appendChild(div);
	});
}

// Call fetch on page load
window.onload = fetchComplianceData;
