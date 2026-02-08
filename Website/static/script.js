console.log("JS is running");

const passwordInput = document.getElementById('password');
const strengthMessage = document.getElementById('strength-message');

passwordInput.addEventListener('input', () => {
    const val = passwordInput.value;

    // Immediately mark as weak if contains spaces
    if (/\s/.test(val)) {
        strengthMessage.textContent = "No spaces allowed";
        strengthMessage.style.color = "red";
        return;
    }

    let score = 0;

    if(val.length >= 8) score++;
    if(/[A-Z]/.test(val)) score++;
    if(/[0-9]/.test(val)) score++;
    if(/[^A-Za-z0-9]/.test(val)) score++; // special characters

    let strength = '';
    let color = '';

    switch(score){
        case 0:
        case 1:
            strength = 'Weak';
            color = 'red';
            break;
        case 2:
            strength = 'Medium';
            color = 'orange';
            break;
        case 3:
            strength = 'Strong';
            color = 'blue';
            break;
        case 4:
            strength = 'Very Strong';
            color = 'green';
            break;
    }

    strengthMessage.textContent = strength;
    strengthMessage.style.color = color;
});