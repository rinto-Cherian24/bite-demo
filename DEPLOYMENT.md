# Deployment Guide

## Quick Deploy Options

### Option 1: Render (Recommended - Free)

1. **Sign up at [Render.com](https://render.com)**
2. **Connect your GitHub repository**
3. **Create a new Web Service**
4. **Configure the service:**
   - **Name:** bite-demo
   - **Environment:** Python
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn backend.app:app`
   - **Python Version:** 3.11.7

5. **Deploy!** Render will automatically deploy your app.

### Option 2: Railway

1. **Sign up at [Railway.app](https://railway.app)**
2. **Connect your GitHub repository**
3. **Railway will auto-detect Python and deploy**
4. **No additional configuration needed!**

### Option 3: Heroku

1. **Sign up at [Heroku.com](https://heroku.com)**
2. **Install Heroku CLI**
3. **Run these commands:**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

## Local Testing

Before deploying, test locally:

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Visit: http://localhost:5000

## Model File Setup

**Important:** The model file (`nail_biter_model.h5`) is not included in the repository due to size limits.

### For Local Development:
1. Copy your model file to `backend/` directory
2. The app will work immediately

### For Deployment:
1. **Option A:** Upload model to cloud storage (AWS S3, Google Drive)
2. **Option B:** Use a smaller model or quantized version
3. **Option C:** Train a new model on the deployment platform

## Environment Variables

For production, consider setting these environment variables:

```bash
FLASK_ENV=production
MODEL_PATH=/path/to/your/model.h5
```

## Troubleshooting

### Common Issues:

1. **Model not found error:**
   - Ensure model file is in the correct location
   - Check file permissions

2. **Import errors:**
   - Verify all dependencies are in requirements.txt
   - Check Python version compatibility

3. **Port issues:**
   - Most platforms set PORT environment variable
   - App automatically uses: `os.environ.get('PORT', 5000)`

## Support

If you encounter issues:
1. Check the platform's logs
2. Verify all files are committed to Git
3. Ensure requirements.txt is up to date
