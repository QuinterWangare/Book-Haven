document.addEventListener('DOMContentLoaded', function () {
    const contactForm = document.querySelector('.contact-form');

    contactForm.addEventListener('submit', function (e) {
        e.preventDefault(); // Prevent default form submission

        // Collect form data
        const formData = new FormData(contactForm);

        // Optional: Show loading state
        const submitButton = contactForm.querySelector('button[type="submit"]');
        submitButton.disabled = true;
        submitButton.textContent = 'Submitting...';

        // Send form data to server
        fetch('/submit-contact', {
            method: 'POST',
            body: formData,
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then((data) => {
                if (data.success) {
                    // Show success message
                    alert('Message sent successfully!');
                    contactForm.reset(); // Clear the form
                } else {
                    // Show error message
                    alert('Error: ' + data.error);
                }
            })
            .catch((error) => {
                console.error('Error:', error);
                alert('An error occurred while submitting the form.');
            })
            .finally(() => {
                // Restore submit button state
                submitButton.disabled = false;
                submitButton.textContent = 'Submit';
            });
    });
});
