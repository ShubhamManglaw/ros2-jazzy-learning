from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'motion_safety_stack'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',['resource/' + package_name]),
        ('share/' + package_name,['package.xml']),
        (os.path.join('share', package_name, 'launch'),glob('launch/*.py')),
        (os.path.join('share', package_name, 'config', 'robots'),glob('config/robots/*.yaml')),
        (os.path.join('share', package_name, 'config', 'environments'),glob('config/environments/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='parallels',
    maintainer_email='Shubhammanglaw@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'robot_info = motion_safety_stack.robot_info:main',
            'velocity_source = motion_safety_stack.velocity_source:main',
            'velocity_limiter = motion_safety_stack.velocity_limiter:main',
            'velocity_monitor = motion_safety_stack.velocity_monitor:main',
            'velocity_watchdog = motion_safety_stack.velocity_watchdog:main',
        ],
    },
)
