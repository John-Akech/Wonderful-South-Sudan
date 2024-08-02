document.addEventListener('DOMContentLoaded', function () {
    console.log('Document Loaded');

    document.getElementById('register-form').addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission

        const form = event.target;
        const formData = new FormData(form);
        const action = form.getAttribute('action');
        const method = form.getAttribute('method').toUpperCase();

        fetch(action, {
            method: method,
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            const messages = document.getElementById('messages');
            if (data.success) {
                messages.innerHTML = `
                    <div class="alert alert-success">
                        ${data.message}
                        <div class="mt-3">
                            <button id="booking-button-yes" class="btn btn-success">Yes</button>
                            <button id="booking-button-no" class="btn btn-danger">No</button>
                        </div>
                    </div>
                `;
                document.getElementById('booking-button-yes').addEventListener('click', function () {
                    window.location.href = "{% url 'booking' %}";
                });
                document.getElementById('booking-button-no').addEventListener('click', function () {
                    window.location.href = "{% url 'home' %}";
                });
            } else {
                // Handle error messages
                messages.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            const messages = document.getElementById('messages');
            messages.innerHTML = '<div class="alert alert-danger">An error occurred. Please try again.</div>';
        });
    });
});