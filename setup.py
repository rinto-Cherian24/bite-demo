from setuptools import setup, find_packages

setup(
    name="bite-demo",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Flask==2.3.3",
        "opencv-python==4.8.1.78",
        "tensorflow==2.13.0",
        "numpy==1.24.3",
        "Pillow==10.0.0",
        "gunicorn==21.2.0",
        "flask-cors==4.0.0",
    ],
)
