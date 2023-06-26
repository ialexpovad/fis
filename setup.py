from setuptools import setup, find_packages

setup(name='fis-api',
      version='0.1.12',
      description='Fuzzy Interface System API',
      author='Alex Povod',
      url='',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'numpy',
          'matplotlib',
      ],
      zip_safe=False) 
