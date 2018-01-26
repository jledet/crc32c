from distutils.core import setup

setup(name='CRC32C',
      version='0.1.0',
      description='Simple CRC32C file utility.',
      author='Jeppe Ledet-Pedersen',
      author_email='jlp@satlab.org',
      url='https://www.github.com/jledet/crc32c/',
      license='MIT',
      requires=['crcmod'],
      scripts=['crc32c'])
