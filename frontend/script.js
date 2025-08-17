document.addEventListener('DOMContentLoaded', function() {
    const uploadArea = document.getElementById('uploadArea');
    const fileInput = document.getElementById('fileInput');
    const previewSection = document.getElementById('previewSection');
    const resultSection = document.getElementById('resultSection');
    const loading = document.getElementById('loading');
    const previewImage = document.getElementById('previewImage');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const newImageBtn = document.getElementById('newImageBtn');

    // Upload area click handler
    uploadArea.addEventListener('click', () => {
        fileInput.click();
    });

    // Drag and drop handlers
    uploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadArea.classList.add('dragover');
    });

    uploadArea.addEventListener('dragleave', () => {
        uploadArea.classList.remove('dragover');
    });

    uploadArea.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadArea.classList.remove('dragover');
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            handleFile(files[0]);
        }
    });

    // File input change handler
    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleFile(e.target.files[0]);
        }
    });

    // Analyze button handler
    analyzeBtn.addEventListener('click', analyzeImage);

    // New image button handler
    newImageBtn.addEventListener('click', resetApp);

    function handleFile(file) {
        if (!file.type.startsWith('image/')) {
            alert('Please select an image file.');
            return;
        }

        const reader = new FileReader();
        reader.onload = (e) => {
            previewImage.src = e.target.result;
            previewSection.style.display = 'block';
            resultSection.style.display = 'none';
            uploadArea.style.display = 'none';
        };
        reader.readAsDataURL(file);
    }

    async function analyzeImage() {
        const file = fileInput.files[0];
        if (!file) {
            alert('Please select an image first.');
            return;
        }

        // Show loading
        loading.style.display = 'block';
        previewSection.style.display = 'none';

        const formData = new FormData();
        formData.append('image', file);

        try {
            const response = await fetch('/api/predict', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();

            if (response.ok) {
                displayResult(result);
            } else {
                throw new Error(result.error || 'Analysis failed');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error analyzing image: ' + error.message);
            previewSection.style.display = 'block';
        } finally {
            loading.style.display = 'none';
        }
    }

    function displayResult(result) {
        const resultIcon = document.getElementById('resultIcon');
        const resultTitle = document.getElementById('resultTitle');
        const resultDescription = document.getElementById('resultDescription');
        const confidenceFill = document.getElementById('confidenceFill');
        const confidenceValue = document.getElementById('confidenceValue');

        // Set result content
        resultTitle.textContent = result.result;
        confidenceValue.textContent = result.confidence;

        // Set confidence bar
        confidenceFill.style.width = result.confidence + '%';

        // Set icon and description based on result
        if (result.result === 'Biting detected') {
            resultIcon.innerHTML = '⚠️';
            resultIcon.className = 'result-icon warning';
            resultDescription.textContent = 'Nail biting behavior detected in the image. Consider using stress management techniques or seeking professional help.';
        } else {
            resultIcon.innerHTML = '✅';
            resultIcon.className = 'result-icon success';
            resultDescription.textContent = 'No nail biting detected. Keep up the good habits!';
        }

        // Show result section
        resultSection.style.display = 'block';
    }

    function resetApp() {
        // Reset file input
        fileInput.value = '';
        
        // Hide sections
        previewSection.style.display = 'none';
        resultSection.style.display = 'none';
        loading.style.display = 'none';
        
        // Show upload area
        uploadArea.style.display = 'block';
    }

    // Health check on page load
    checkHealth();
});

async function checkHealth() {
    try {
        const response = await fetch('/api/health');
        const health = await response.json();
        
        if (!health.model_loaded) {
            console.warn('Model not loaded. Analysis may not work properly.');
        }
    } catch (error) {
        console.error('Health check failed:', error);
    }
}
