document.getElementById('reportForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;

    if (!startDate || !endDate) {
        alert('Please fill in both dates.');
        return;
    }

    // Add logic to generate report
    alert(`Generating report from ${startDate} to ${endDate}`);
});
