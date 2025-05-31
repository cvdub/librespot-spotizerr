import setuptools

setuptools.setup(name="librespot",
                 version="0.1.0",
                 description="Spotizerr's python librespot implementation",
                 long_description=open("README.md").read(),
                 long_description_content_type="text/markdown",
                 author="Xoconoch",
                 url="https://github.com/Xoconoch/librespot-spotizerr",
                 license="Apache-2.0",
                 packages=setuptools.find_packages("."),
                 install_requires=open("requirements.txt").read().splitlines(),
                 classifiers=[
                     "Development Status :: 1 - Planning",
                     "License :: OSI Approved :: Apache Software License",
                     "Topic :: Multimedia :: Sound/Audio"
                 ])
