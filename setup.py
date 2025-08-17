from setuptools import setup, find_packages

setup(
    name="bite-demo",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Flask==2.3.3",
        "opencv-python-headless==4.8.1.78",
        "tensorflow==2.20.0",
        "numpy==1.26.4",
        "Pillow==10.4.0",
        "gunicorn==21.2.0",
        "flask-cors==4.0.2",
    ],
)
