// Scrape Amazon reviews
let reviews = Array.from(document.querySelectorAll('.review')).map(review => ({
  //user: review.querySelector('.reviewer')?.textContent.trim() || 'N/A',
  user: review.querySelector('.a-profile-content')?.textContent.trim() || 'N/A',
  rating: review.querySelector('.review-rating')?.textContent.trim() || 'N/A',
  text: review.querySelector('.review-text')?.textContent.trim() || 'N/A'
}));

// Listen for a message from the popup and send the scraped data
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getReviews") {
    sendResponse({ reviews });
  }
});
