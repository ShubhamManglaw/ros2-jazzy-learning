from setuptools import find_packages, setup
from glob import glob

package_name = 'my_first_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (
        'share/' + package_name + '/config',
        glob('config/*.yaml')
    )
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shubham',
    maintainer_email='shubhammanglaw@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publisher_node = my_first_pkg.publisher_node:main',
'subscriber_node = my_first_pkg.subscriber_node:main',
'distance_publisher = my_first_pkg.distance_publisher:main',
'distance_subscriber = my_first_pkg.distance_subscriber:main',
'number_publisher = my_first_pkg.number_publisher:main',
'number_doubler = my_first_pkg.number_doubler:main',
'number_printer = my_first_pkg.number_printer:main',
'velocity_source = my_first_pkg.velocity_source:main',
'velocity_limiter = my_first_pkg.velocity_limiter:main',
'velocity_monitor = my_first_pkg.velocity_monitor:main',
'robot_status_publisher = my_first_pkg.robot_status_publisher:main',
'add_server = my_first_pkg.add_server:main',
'add_client = my_first_pkg.add_client:main',
'velocity_limiter_v3 = my_first_pkg.velocity_limiter_v3:main',
'velocity_watchdog = my_first_pkg.velocity_watchdog:main'

        ],
    },
)
