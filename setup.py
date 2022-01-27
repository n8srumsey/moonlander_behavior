import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

description = "A modular system to handle behavior logic for UAV drones."

setuptools.setup(
    name="Moonlander Behavior Core",
    version="0.0.2",
    author="Nathan Rumsey",
    author_email="rumseyn@oregonstate.edu",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/n8srumsey/moonlander_behavior_core",
    project_urls= {
        "Issues": "https://github.com/n8srumsey/moonlander_behavior_core/issues"
    },
    packages=['moonlander_behavior_core'],
    install_requires=['git+https://github.com/InquisitivePenguin/moonlander.git', 
                    'git+https://github.com/OSURoboticsClub/Aerial_2021_ArucoMarkerTracking.git'],
)