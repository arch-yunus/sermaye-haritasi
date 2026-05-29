const quotes = [
    { text: "Kapitalizm bir uygarlık meselesidir; yüzyılların birikimini, toplumların ruhunu ve coğrafyanın kaderini tek bir bilançoda eritir.", author: "Fernand Braudel" },
    { text: "Sermaye, ölü emektir; ancak vampir gibi, yalnızca canlı emeği emerek yaşar.", author: "Karl Marx" },
    { text: "Geçmiş, geleceği yutuyor. Mirasla devralınan servetler, üretilen servetlerden daha hızlı büyüdüğünde, kapitalizm kendi liyakat efsanesini yok eder.", author: "Thomas Piketty" },
    { text: "Kapitalizm ölmedi, daha kötü bir şeye dönüştü: Tekno-Feodalizm.", author: "Yanis Varoufakis" },
    { text: "Kazanmayı bilenler, koşullar henüz şekillenmeden zaferi tasarlayanlardır.", author: "Sun Tzu" },
    { text: "Servet, güçtür.", author: "Thomas Hobbes" }
];

// Display random quote
function displayRandomQuote() {
    const quote = quotes[Math.floor(Math.random() * quotes.length)];
    document.getElementById('quoteText').textContent = `"${quote.text}"`;
    document.getElementById('quoteAuthor').textContent = `— ${quote.author}`;
}

// Global data object
let capitalData = [];

// Helper function to get sector from company string
function getSector(company) {
    const c = company.toLowerCase();
    if (['google', 'microsoft', 'amazon', 'meta', 'oracle', 'yazılım', 'tiktok', 'tencent', 'apple', 'nvidia'].some(kw => c.includes(kw))) return 'Technology/Software';
    if (['finans', 'bank', 'fon', 'hedge', 'capital', 'yatırım', 'bloomberg', 'bitcoin', 'binance', 'tether'].some(kw => c.includes(kw))) return 'Finance/Crypto';
    if (['tesla', 'çelik', 'maden', 'enerji', 'otomotiv', 'sanayi', 'demir', 'kömür', 'spacex'].some(kw => c.includes(kw))) return 'Heavy Industry/Energy';
    if (['lvmh', 'chanel', 'perakende', 'zara', 'walmart', 'gıda', 'nutella', "l'oréal", 'amazon'].some(kw => c.includes(kw))) return 'Retail/Consumer';
    return 'Other/Diversified';
}

// Fetch data
async function loadData() {
    try {
        const response = await fetch('../data/capital_registry.json');
        if (!response.ok) throw new Error('Data fetch failed');
        capitalData = await response.json();
        
        initDashboard();
    } catch (error) {
        console.error("Error loading data:", error);
        document.getElementById('tableBody').innerHTML = `<tr><td colspan="5" style="color:var(--accent); text-align:center;">Veri yüklenemedi. Lütfen web sunucusu (http.server) üzerinden çalıştırdığınızdan emin olun.</td></tr>`;
    }
}

function initDashboard() {
    populateTable();
    initSectorChart();
    initCitizenshipChart();
}

function populateTable() {
    const tbody = document.getElementById('tableBody');
    tbody.innerHTML = '';
    
    capitalData.forEach(row => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${row.rank}</td>
            <td style="color: var(--text-secondary); font-weight: bold;">${row.name}</td>
            <td>$${row.net_worth_billions.toFixed(1)} B</td>
            <td>${row.company_source}</td>
            <td>${row.ethnicity_background}</td>
        `;
        tbody.appendChild(tr);
    });
}

function initSectorChart() {
    const ctx = document.getElementById('sectorChart').getContext('2d');
    
    // Count sectors
    const sectorCounts = {};
    capitalData.forEach(row => {
        const sector = getSector(row.company_source);
        sectorCounts[sector] = (sectorCounts[sector] || 0) + 1;
    });

    const labels = Object.keys(sectorCounts);
    const data = Object.values(sectorCounts);

    Chart.defaults.color = '#e0e0e0';
    Chart.defaults.font.family = "'Rajdhani', sans-serif";

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: [
                    '#00ffaa', '#ff0055', '#00ccff', '#ffcc00', '#aa00ff'
                ],
                borderWidth: 0,
                hoverOffset: 10
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'right',
                    labels: { color: '#e0e0e0' }
                }
            }
        }
    });
}

function initCitizenshipChart() {
    const ctx = document.getElementById('citizenshipChart').getContext('2d');
    
    // Count citizenships
    const citCounts = {};
    capitalData.forEach(row => {
        // Just take the first country if multiple
        const cit = row.citizenship.split('/')[0].trim();
        citCounts[cit] = (citCounts[cit] || 0) + 1;
    });

    // Sort and get top 7
    const sortedCits = Object.entries(citCounts).sort((a,b) => b[1] - a[1]).slice(0, 7);
    
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: sortedCits.map(x => x[0]),
            datasets: [{
                label: 'Kişi Sayısı',
                data: sortedCits.map(x => x[1]),
                backgroundColor: 'rgba(0, 255, 170, 0.7)',
                borderColor: '#00ffaa',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    grid: { color: 'rgba(255,255,255,0.1)' }
                },
                x: {
                    grid: { display: false }
                }
            }
        }
    });
}

// Bootstrap
window.addEventListener('DOMContentLoaded', () => {
    displayRandomQuote();
    loadData();
});
