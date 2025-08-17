# Model Setup Instructions

## Important: Model File Setup

Due to GitHub's 25MB file size limit, the `nail_biter_model.h5` file (274MB) is not included in this repository.

### Option 1: Download from External Source
If you have the model file available elsewhere (Google Drive, Dropbox, etc.), download it and place it in the `backend/` directory.

### Option 2: Train Your Own Model
You can train a new model using the provided training script:

```bash
cd backend
python train_model.py
```

This will create a new `nail_biter_model.h5` file in the backend directory.

### Option 3: Use a Smaller Model
Consider using a smaller, pre-trained model or quantized version of your model.

## File Structure After Setup
```
backend/
├── nail_biter_model.h5  # Add this file manually
├── app.py
├── nail_detection.py
├── train_model.py
└── ...
```

## Running the Application
Once the model file is in place, you can run the application:

```bash
cd backend
python app.py
```

The application will be available at `http://localhost:5000`

## Deployment
For deployment platforms like Heroku, ensure the model file is included in your deployment package or use environment variables to specify the model location.
