from setuptools import setup, find_packages

p = {}
with open("snidynatrace/version.py","r") as f :
    exec( f.read(), p )
    V = p['__version__']

setup(
    name="snidynatrace",
    version=V,
    packages=find_packages(),
    package_data={"snidynatrace": ["wrappers/*"]},
    install_requires=["wrapt>=1.11.2", "oneagent-sdk>=1.3.0", "six>=1.13.0"],
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
    author="David Lopes",
    author_email="david.lopes@dynatrace.com",
    description="Auto instrumentation for the OneAgent SDK",
    long_description="The snidynatrace package will auto instrument your python apps",
    url="https://github.com/krb70/snidynatrace",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "License :: OSI Approved :: Apache Software License",  # 2.0
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        # 'Programming Language :: Python :: Implementation :: PyPy',
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Topic :: System :: Monitoring",
    ],
    project_urls={"Issue Tracker": "https://github.com/krb70/snidynatrace/issues"},
)
