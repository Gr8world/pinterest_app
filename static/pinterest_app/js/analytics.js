document.addEventListener("DOMContentLoaded", function() {
    loadBoards();

    function loadBoards() {
        fetch("/api/boards/")
          .then(response => response.json())
          .then(data => {
            const container = document.getElementById("boards-container");
            container.innerHTML = "";
            data.items.forEach(board => {
                const col = document.createElement("div");
                col.className = "col-md-3 mb-3";
                col.innerHTML = `
                    <div class="card h-100" data-board-id="${board.id}">
                      <div class="card-body">
                        <h5 class="card-title">${board.name}</h5>
                        <p class="card-text">${board.description || ""}</p>
                      </div>
                    </div>
                `;
                col.querySelector('.card').addEventListener('click', function() {
                    document.getElementById("selected-board-name").textContent = board.name;
                    loadPins(board.id);
                    document.getElementById("pins-section").style.display = "block";
                    updateExportButton(board.id);
                });
                container.appendChild(col);
            });
          });
    }

    function loadPins(boardId) {
        fetch(`/api/boards/${boardId}/pins/`)
          .then(response => response.json())
          .then(data => {
            const container = document.getElementById("pins-container");
            container.innerHTML = "";
            data.items.forEach(pin => {
                const col = document.createElement("div");
                col.className = "col-md-3 mb-3";
                col.innerHTML = `
                    <div class="card h-100" data-pin-id="${pin.id}">
                      <img src="${pin.media.images.originals.url}" class="card-img-top" alt="pin">
                      <div class="card-body">
                        <p class="card-text">${pin.title || ""}</p>
                      </div>
                    </div>
                `;
                col.querySelector('.card').addEventListener('click', function() {
                    loadAnalytics(pin.id);
                });
                container.appendChild(col);
            });
          });
    }

    function loadAnalytics(pinId) {
        fetch(`/api/pins/${pinId}/analytics/`)
          .then(response => response.json())
          .then(data => {
            document.getElementById("analytics-section").style.display = "block";
            const ctx = document.getElementById("analyticsChart").getContext("2d");
            new Chart(ctx, {
              type: "bar",
              data: {
                labels: ["Impressions", "Saves", "Outbound Clicks", "Engagements"],
                datasets: [{                
                  label: "Engagement Metrics",
                  data: [
                    data.metrics.impression?.value || 0,
                    data.metrics.save?.value || 0,
                    data.metrics.outbound_click?.value || 0,
                    data.metrics.engagement?.value || 0
                  ],
                  backgroundColor: ["#007bff", "#ffc107", "#28a745", "#dc3545"]
                }]
              }
            });
          });
    }

    function loadAudienceInsights() {
        fetch('/api/audience-insights/')
          .then(response => response.json())
          .then(data => {
            // Age distribution
            const ageCtx = document.getElementById('ageChart').getContext('2d');
            new Chart(ageCtx, {
                type: 'pie',
                data: {                   
                    labels: Object.keys(data.age_distribution),                    
                    datasets: [{                      
                        data: Object.values(data.age_distribution),                      
                        backgroundColor: ['#f87171', '#60a5fa', '#34d399', '#fbbf24', '#a78bfa']                    
                    }]                
                }
            });
            // Gender distribution
            const genderCtx = document.getElementById('genderChart').getContext('2d');
            new Chart(genderCtx, {
                type: 'doughnut',
                data: {
                    labels: Object.keys(data.gender_distribution),
                    datasets: [{
                        data: Object.values(data.gender_distribution),
                        backgroundColor: ['#FF6384', '#36A2EB']
                    }]
                }
            });
            // Location distribution
            const locationCtx = document.getElementById('locationChart').getContext('2d');
            new Chart(locationCtx, {
                type: 'bar',
                data: {
                    labels: Object.keys(data.location_distribution),
                    datasets: [{
                        data: Object.values(data.location_distribution),
                        label: 'Location',
                        backgroundColor: '#60a5fa'
                    }]
                }
            });
          });
    }

    function updateExportButton(boardId) {
        document.getElementById("export-btn").href = `/api/export/csv/?board_id=${boardId}`;
    }

    // Load audience insights on page load
    loadAudienceInsights();
});
