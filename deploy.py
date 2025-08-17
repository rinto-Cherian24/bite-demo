#!/usr/bin/env python3
"""
Simple deployment script for bite-demo
"""

import os
import sys
import subprocess

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'requirements.txt',
        'backend/app.py',
        'frontend/index.html',
        'frontend/style.css',
        'frontend/script.js',
        'Procfile',
        'runtime.txt'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("✅ All required files found")
    return True

def test_local():
    """Test the application locally"""
    print("\n🧪 Testing application locally...")
    try:
        # Change to backend directory
        os.chdir('backend')
        
        # Install requirements
        print("📦 Installing requirements...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', '../requirements.txt'], check=True)
        
        # Run the app
        print("🚀 Starting local server...")
        print("   Visit: http://localhost:5000")
        print("   Press Ctrl+C to stop")
        
        subprocess.run([sys.executable, 'app.py'])
        
    except KeyboardInterrupt:
        print("\n⏹️  Server stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    return True

def main():
    print("🚀 Bite-Demo Deployment Helper")
    print("=" * 40)
    
    if not check_requirements():
        sys.exit(1)
    
    print("\n📋 Deployment Options:")
    print("1. Test locally")
    print("2. Deploy to Render (Recommended)")
    print("3. Deploy to Railway")
    print("4. Deploy to Heroku")
    
    choice = input("\nSelect option (1-4): ").strip()
    
    if choice == '1':
        test_local()
    elif choice == '2':
        print("\n🌐 Deploy to Render:")
        print("1. Go to https://render.com")
        print("2. Sign up/Login")
        print("3. Click 'New Web Service'")
        print("4. Connect your GitHub repository")
        print("5. Configure:")
        print("   - Name: bite-demo")
        print("   - Environment: Python")
        print("   - Build Command: pip install -r requirements.txt")
        print("   - Start Command: gunicorn backend.app:app")
        print("6. Click 'Create Web Service'")
    elif choice == '3':
        print("\n🚂 Deploy to Railway:")
        print("1. Go to https://railway.app")
        print("2. Sign up/Login")
        print("3. Click 'New Project'")
        print("4. Select 'Deploy from GitHub repo'")
        print("5. Select your bite-demo repository")
        print("6. Railway will auto-deploy!")
    elif choice == '4':
        print("\n⚡ Deploy to Heroku:")
        print("1. Install Heroku CLI")
        print("2. Run: heroku login")
        print("3. Run: heroku create your-app-name")
        print("4. Run: git push heroku main")
    else:
        print("❌ Invalid option")

if __name__ == '__main__':
    main()
