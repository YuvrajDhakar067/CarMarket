// Custom JavaScript for Car Market

document.addEventListener('DOMContentLoaded', function() {
    // Auto-dismiss alerts after 5 seconds
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
        alerts.forEach(function(alert) {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Car image preview on file input change
    const imageInput = document.querySelector('input[type="file"][name="image"]');
    if (imageInput) {
        imageInput.addEventListener('change', function() {
            const previewContainer = document.getElementById('image-preview');
            if (previewContainer) {
                previewContainer.innerHTML = '';
                
                if (this.files && this.files.length > 0) {
                    for (let i = 0; i < this.files.length; i++) {
                        const file = this.files[i];
                        if (file.type.match('image.*')) {
                            const reader = new FileReader();
                            
                            reader.onload = function(e) {
                                const img = document.createElement('img');
                                img.src = e.target.result;
                                img.className = 'img-thumbnail me-2 mb-2';
                                img.style.width = '100px';
                                img.style.height = '100px';
                                img.style.objectFit = 'cover';
                                previewContainer.appendChild(img);
                            };
                            
                            reader.readAsDataURL(file);
                        }
                    }
                }
            }
        });
    }

    // Payment screenshot preview
    const paymentScreenshotInput = document.querySelector('input[type="file"][name="payment_screenshot"]');
    if (paymentScreenshotInput) {
        paymentScreenshotInput.addEventListener('change', function() {
            const previewContainer = document.getElementById('payment-preview');
            if (previewContainer) {
                previewContainer.innerHTML = '';
                
                if (this.files && this.files.length > 0) {
                    const file = this.files[0];
                    if (file.type.match('image.*')) {
                        const reader = new FileReader();
                        
                        reader.onload = function(e) {
                            const img = document.createElement('img');
                            img.src = e.target.result;
                            img.className = 'img-fluid rounded';
                            previewContainer.appendChild(img);
                        };
                        
                        reader.readAsDataURL(file);
                    }
                }
            }
        });
    }
}); 