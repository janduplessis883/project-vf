from setuptools import setup, find_packages

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(
    name='vf',
    version="0.0.1",
    description="Description",
    packages=find_packages(),
    install_requires=requirements,
    author='Jan du Plessis',
    author_email='drjanduplessis@icloud.com',
    url='https://github.com/janduplessis883/project-inforcast/',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    # entry_points={
    #     'console_scripts': [
    #         'inforecast=inforecast.main:main',  # This line assumes that your package is named `inforecast` and `main.py` has a `main` function.
    #     ],
    # },
    include_package_data=True,
    package_data={
        'sampledata': ['*.csv'],  # This is an example, adjust if your non-Python files are located elsewhere.
    },
    # If you are using version control system, it's good to sync your version with it
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
)
