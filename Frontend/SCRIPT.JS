function submitForm(event) {
    event.preventDefault(); 

    // Get form values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const crimeType = document.getElementById('crimeType').value;
    const description = document.getElementById('description').value;

    // Check if all fields are filled (optional, extra validation)
    if (!name || !email || !crimeType || !description) {
        alert("Please fill out all fields.");
        return;
    }

    // Show confirmation message
    alert("Report submitted successfully!\n\nName: ${name}\nEmail: ${email}\nCrime: ${crimeType}\nDescription: ${description}");

    // Clear form after submission
    document.getElementById('cyberCrimeForm').reset();
}