document.addEventListener('DOMContentLoaded', function () {
    const fullData = [
      { seller: 'Prasad Babu', quantity: 79 },
      { seller: 'Lakshmi Reddy', quantity: 78 },
      { seller: 'Rameshwar Rao', quantity: 71 },
      { seller: 'Venkateshwarlu', quantity: 70 },
      { seller: 'Sai Kumar', quantity: 65 },
      { seller: 'Srilatha Reddy', quantity: 62 },
      { seller: 'Ravi Shankar', quantity: 60 },
      { seller: 'Padmaja Rao', quantity: 55 },
      { seller: 'Rajeshwari Naidu', quantity: 50 }
    ];
  
    const userProfile = {
      name: 'Lakshmi Reddy', // Replace with actual user's name
      quantityScore: 78 // Replace with actual user's quantity score
    };
  
    fullData.sort((a, b) => b.quantity - a.quantity);
    const userRank = fullData.findIndex(data => data.quantity <= userProfile.quantityScore) + 1;
    const userRankBox = document.getElementById('userRankInfo');
    userRankBox.textContent = `${userProfile.name}'s rank: ${userRank}`;
  
    // Retrieve data from table for top 5
    const table = document.getElementById('rankingTable');
    const rows = Array.from(table.querySelectorAll('tr')).slice(1); // Skip header row
  
    // Sort rows by quantity score (descending order)
    rows.sort((a, b) => {
      const quantityA = parseInt(a.cells[2].textContent);
      const quantityB = parseInt(b.cells[2].textContent);
      return quantityB - quantityA; // Compare quantities for sorting (descending)
    });
  
    // Update rank column for top 5
    rows.forEach((row, index) => {
      row.cells[0].textContent = index + 1;
      if (index === 0) {
        row.cells[3].innerHTML = '<span class="winner-award">Gold</span>';
      } else if (index === 1) {
        row.cells[3].innerHTML = '<span class="winner-award">Silver</span>';
      } else {
        row.cells[3].innerHTML = '';
      }
    });
  
    // Extract seller names and quantities from full data
    const sellers = fullData.map(item => item.seller);
    const quantities = fullData.map(item => item.quantity);
  
    // Draw chart using Chart.js
    const ctx = document.getElementById('quantityChart').getContext('2d');
    const quantityChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: sellers,
        datasets: [{
          label: 'Quantity Score',
          data: quantities,
          borderColor: '#fdcb6e', /* Line color */
          backgroundColor: 'rgba(253, 203, 110, 0.2)', /* Fill color */
          borderWidth: 2,
          pointBackgroundColor: '#fdcb6e', /* Point color */
          pointRadius: 5, /* Point radius */
          pointHoverRadius: 8 /* Point radius on hover */
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            display: false
          },
          tooltip: {
            callbacks: {
              label: function(tooltipItem) {
                return `Rank: ${tooltipItem.dataIndex + 1} - ${tooltipItem.label}: ${tooltipItem.formattedValue}`;
              }
            }
          }
        },
        scales: {
          x: {
            grid: {
              display: false /* Remove x-axis grid lines */
            },
            ticks: {
              font: {
                size: 14 /* X-axis tick font size */
              }
            }
          },
          y: {
            grid: {
              display: false /* Remove y-axis grid lines */
            },
            ticks: {
              beginAtZero: true,
              stepSize: 10,
              font: {
                size: 14 /* Y-axis tick font size */
              }
            }
          }
        }
      }
    });
  
    // Add hover effect to table rows
    rows.forEach(row => {
      row.addEventListener('mouseover', () => {
        row.style.backgroundColor = '#f2f2f2';
      });
  
      row.addEventListener('mouseout', () => {
        row.style.backgroundColor = '';
      });
    });
  });
  
  // Functionality for past months competition
  document.addEventListener('DOMContentLoaded', function () {
    const pastMonthsData = {
      January: [
        { seller: 'Prasad Babu', quantity: 50 },
        { seller: 'Lakshmi Reddy', quantity: 78 },
        { seller: 'Rameshwar Rao', quantity: 71 },
        { seller: 'Venkateshwarlu', quantity: 70 },
        { seller: 'Sai Kumar', quantity: 65 }
      ],
      February: [
        { seller: 'Prasad Babu', quantity: 85 },
        { seller: 'Lakshmi Reddy', quantity: 88 },
        { seller: 'Rameshwar Rao', quantity: 75 },
        { seller: 'Venkateshwarlu', quantity: 72 },
        { seller: 'Sai Kumar', quantity: 68 }
      ],
      March: [
        { seller: 'Prasad Babu', quantity: 92 },
        { seller: 'Lakshmi Reddy', quantity: 88 },
        { seller: 'Rameshwar Rao', quantity: 81 },
        { seller: 'Venkateshwarlu', quantity: 78 },
        { seller: 'Sai Kumar', quantity: 97}
      ]
    };
  
    const initialMonth = 'January';
    updateTop5Table(initialMonth);
  
    // Function to update top 5 table based on selected month
    function updateTop5Table(month) {
      const data = pastMonthsData[month];
  
      // Sort data by quantity score (descending order)
      data.sort((a, b) => b.quantity - a.quantity);
  
      // Generate HTML for top 5 table
      const tableHTML = `
        <div class="winner-table">
          <table>
            <tr>
              <th><i class="fas fa-user"></i> Rank</th>
              <th><i class="fas fa-user"></i> Seller</th>
              <th><i class="fas fa-recycle"></i> Quantity Score</th>
              <th><i class="fas fa-trophy"></i> Award</th>
            </tr>
            ${data.slice(0, 5).map((item, index) => `
              <tr>
                <td>${index + 1}</td>
                <td>${item.seller}</td>
                <td>${item.quantity}</td>
                <td>${index === 0 ? '<span class="winner-award">Gold</span>' : (index === 1 ? '<span class="winner-award">Silver</span>' : '')}</td>
              </tr>
            `).join('')}
          </table>
        </div>
      `;
  
      // Update HTML of top 5 tables container
      document.getElementById('top5Tables').innerHTML = tableHTML;
    }
  
    // Event listeners for month buttons
    const monthButtons = document.querySelectorAll('.month-button');
    monthButtons.forEach(button => {
      button.addEventListener('click', () => {
        const selectedMonth = button.getAttribute('data-month');
        updateTop5Table(selectedMonth);
      });
    });
  });
  