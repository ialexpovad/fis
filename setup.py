from setuptools import setup, find_packages

setup(name='fis-api',
      version='0.1.13',
      description='Fuzzy Interface System API',
      author='Alex Povod',
      url='https://github.com/ialexpovod/fis/tree/main',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'numpy',
          'matplotlib',
      ],
      zip_safe=False) 
