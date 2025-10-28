# Automatically Updated RPM Repositories

This repository provides configuration files to automatically update RPM packages hosted on the OBS project using GitHub Actions. 

By leveraging GitHub Actions, these configurations enable you to keep your development environment up-to-date with the latest versions of the packages you rely on. 

**The auto-update task is scheduled to run every 6 hours, ensuring that all packages remains up-to-date.**

## Installing Packages

Once a repository is enabled, you can install packages using the dnf install command:

```bash
sudo opi <package name>
```

**Example**: To install Clion from the JetBrains repository:

```bash
sudo opi clion
```

## JetBrains Repository Packages

https://build.opensuse.org/project/show/home:nukeddd:JetbrainsIDE

The JetBrains repository offers the following development tools:

* `clion`: C and C++ IDE
* `dategrip`: Python IDE for data scientists
* `dataspell`: Data science IDE for Python
* `goland`: Go programming IDE
* `intellij-idea-community`: Free and open-source Java IDE
* `intellij-idea-ultimate`: Paid, feature-rich Java IDE
* `jetbrains-fleet`: Unified IDE for multiple languages
* `pycharm-professional`: Paid, feature-rich Python IDE
* `rider`: .NET development IDE
* `rubymine`: Ruby and Rails IDE
* `rustrover`: Rust IDE
* `webstorm`: JavaScript and web development IDE
