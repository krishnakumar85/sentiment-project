document.getElementById('scrape-btn').addEventListener('click', async () => {
  // Get the active tab
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  // Execute the content script in the active tab
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    files: ["content.js"]
  }, async () => {
    // Listen for scraped data
    chrome.tabs.sendMessage(tab.id, { action: "getReviews" }, (response) => {
      if (response && response.reviews) {
        const reviewsContainer = document.getElementById('reviews');
        reviewsContainer.innerHTML = ''; // Clear existing content

        // Display reviews
        response.reviews.forEach(review => {
          const reviewElement = document.createElement('div');
          reviewElement.classList.add('review');
          reviewElement.innerHTML = `
            <strong>User:</strong> ${review.user} <br>
            <strong>Rating:</strong> ${review.rating} <br>
            <strong>Comment:</strong> ${review.text}
          `;
          reviewsContainer.appendChild(reviewElement);
        });
        // Show download buttons
        document.getElementById('download-csv').style.display = 'block';
        document.getElementById('download-json').style.display = 'block';

        // Download reviews as CSV
        document.getElementById('download-csv').addEventListener('click', function() {
        let csvData = convertToCSV(response.reviews);
        downloadFile(csvData, 'reviews.csv', 'text/csv');
         });
          // Download reviews as JSON
          document.getElementById('download-json').addEventListener('click', function() {
          let jsonData = JSON.stringify(response.reviews, null, 2);
          downloadFile(jsonData, 'reviews.json', 'application/json');
          });
      } else {
        alert('No reviews found or an error occurred!');
      }
    });
  });
});

// Function to convert review data into CSV format
function convertToCSV(reviews) {
    const header = ['Reviewer', 'Rating', 'Review Text'];
    const rows = reviews.map(review => [
        review.user,
        review.rating,
        review.text.replace(/\n/g, ' ').replace(/,/g, ' ')  // Clean up newlines and commas in the text
    ]);

    const csvContent = [header, ...rows].map(row => row.join(',')).join('\n');
    return csvContent;
}

// Function to trigger the download of the file
function downloadFile(data, filename, mimeType) {
    const blob = new Blob([data], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
}
