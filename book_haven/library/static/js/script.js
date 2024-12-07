function changeImage(feature) {
  const featureImage = document.getElementById('feature-img');
  const featureDescription = document.getElementById('feature-description');

  // Reset all button active states
  const buttons = document.querySelectorAll('.sidebar-btn');
  buttons.forEach(button => button.classList.remove('active'));

  // Set the active button
  event.target.classList.add('active');

  // Change image and description based on the selected feature
  if (feature === 'admin') {
    featureImage.src = 'https://via.placeholder.com/400x250?text=Admin+Power';
    featureDescription.textContent = 'Admins can add, edit, and delete books like a boss. Manage your library with ease!';
  } else if (feature === 'user') {
    featureImage.src = 'https://via.placeholder.com/400x250?text=User+Fun';
    featureDescription.textContent = 'Let users enjoy reading with personalized recommendations, reviews, and more!';
  } else if (feature === 'ebook') {
    featureImage.src = 'https://via.placeholder.com/400x250?text=eBook+Reader';
    featureDescription.textContent = 'A seamless and interactive eBook reader for your library!';
  } else if (feature === 'reviews') {
    featureImage.src = 'https://via.placeholder.com/400x250?text=Reviews+%26+Ratings';
    featureDescription.textContent = 'Allow users to leave ratings and reviews on their favorite books!';
  } else if (feature === 'freeBooks') {
    featureImage.src = 'https://via.placeholder.com/400x250?text=Free+Books';
    featureDescription.textContent = 'Explore a vast collection of free books available to read!';
  } else if (feature === 'api') {
    featureImage.src = 'https://via.placeholder.com/400x250?text=API+Integration';
    featureDescription.textContent = 'Integrate your library with external APIs for enhanced functionality!';
  }
}
