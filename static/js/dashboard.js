const ctx = document.getElementById('chart');

new Chart(ctx, {
type: 'line',
data: {
labels: ['Jan','Feb','Mar','Apr','May','Jun'],
datasets: [{
label: 'Visitors',
data: [1200,1900,3000,2500,3200,4100],
borderWidth: 2
}]
}
});
