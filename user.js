// Tab switching functionality
const tabBtns = document.querySelectorAll('.tab-btn');
const formContainers = document.querySelectorAll('.form-container');

tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        // Remove active class from all buttons and forms
        tabBtns.forEach(b => b.classList.remove('active'));
        formContainers.forEach(f => f.classList.remove('active'));

        // Add active class to clicked button and corresponding form
        btn.classList.add('active');
        document.querySelector(`.${btn.dataset.tab}-form`).classList.add('active');
    });
});

// Form submission handling
const forms = document.querySelectorAll('.user-form');

forms.forEach(form => {
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Get all form data
        const formData = new FormData(form);
        const data = Object.fromEntries(formData);
        
        // Here you would typically send this data to a server
        console.log('Form submitted:', data);
        
        // Show success message
        alert('Form submitted successfully!');
        
        // Reset form
        form.reset();
    });
});

// Password visibility toggle
const passwordInputs = document.querySelectorAll('input[type="password"]');

passwordInputs.forEach(input => {
    const toggleBtn = document.createElement('i');
    toggleBtn.className = 'fas fa-eye password-toggle';
    toggleBtn.style.cssText = `
        position: absolute;
        right: 1.5rem;
        top: 50%;
        transform: translateY(-50%);
        cursor: pointer;
        color: #666;
        padding: 0.5rem;
        z-index: 10;
        background: transparent;
        border-radius: 50%;
        transition: all 0.3s ease;
    `;
    
    // Add hover effect
    toggleBtn.addEventListener('mouseover', () => {
        toggleBtn.style.color = '#ff5733';
    });
    
    toggleBtn.addEventListener('mouseout', () => {
        toggleBtn.style.color = '#666';
    });
    
    input.parentElement.appendChild(toggleBtn);
    
    // Adjust input padding to prevent text overlap with icon
    input.style.paddingRight = '4rem';
    
    toggleBtn.addEventListener('click', () => {
        const type = input.getAttribute('type');
        input.setAttribute('type', type === 'password' ? 'text' : 'password');
        toggleBtn.className = `fas ${type === 'password' ? 'fa-eye-slash' : 'fa-eye'} password-toggle`;
    });
}); 