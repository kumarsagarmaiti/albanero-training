# You can have multiple environments, with multiple sets of packages, without conflicts among them. This way, different projects’ requirements can be satisfied at the same time.
# You can easily release your project with its own dependent modules.
# The short answer is that Python isn’t great at dependency management. If you’re not specific, then pip will place all the external packages that you install in a folder called site-packages/ in your base Python installation.
# Several issues can come up if all of your external packages land in the same folder. In this section, you’ll learn more about them, as well as other problems that virtual environments mitigate.
# If all your packages live in one location, then it’ll be difficult to only pin dependencies that are relevant for a single project.
# Include\ is an initially empty folder that Python uses to include C header files for packages you might install that depend on C extensions.

# Lib\ contains the site-packages\ folder, which is one of the main reasons for creating your virtual environment. This folder is where you’ll install external packages that you want to use within your virtual environment. By default, your virtual environment comes preinstalled with two dependencies, pip and setuptools. You’ll learn more about them in a bit.

# Scripts\ contains the executable files of your virtual environment. Most notable are the Python interpreter (python.exe), the pip executable (pip.exe), and the activation script for your virtual environment, which comes in a couple of different flavors to allow you to work with different shells. In this tutorial, you’ve used activate, which handles the activation of your virtual environment for Windows across most shells.

# pyvenv.cfg is a crucial file for your virtual environment. It contains only a couple of key-value pairs that Python uses to set variables in the sys module that determine which Python interpreter and which site-packages directory the current Python session will use.

# A Python virtual environment consists of two essential components: the Python interpreter that the virtual environment runs on and a folder containing third-party libraries installed in the virtual environment. These virtual environments are isolated from the other virtual environments, which means any changes on dependencies installed in a virtual environment don’t affect the dependencies of the other virtual environments or the system-wide libraries. Thus, we can create multiple virtual environments with different Python versions, plus different libraries or the same libraries in different versions.

#  For projects with complex requirements, you should keep in the root of the project a requirements.txt file that lists the requirements for the project. This way, if you need to recreate the virtual environment, you can reinstall all of the needed packages with the command pip install -r requirements.txt.