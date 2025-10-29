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
[![build result](https://build.opensuse.org/projects/home:nukeddd:JetbrainsIDE/packages/clion/badge.svg?type=default)](https://build.opensuse.org/package/show/home:nukeddd:JetbrainsIDE/clion)
* `dategrip`: Python IDE for data scientists
[![build result](https://build.opensuse.org/projects/home:nukeddd:JetbrainsIDE/packages/datagrip/badge.svg?type=default)](https://build.opensuse.org/package/show/home:nukeddd:JetbrainsIDE/datagrip)
* `dataspell`: Data science IDE for Python
[![build result](https://build.opensuse.org/projects/home:nukeddd:JetbrainsIDE/packages/dataspell/badge.svg?type=default)](https://build.opensuse.org/package/show/home:nukeddd:JetbrainsIDE/dataspell)
* `goland`: Go programming IDE
[![build result](https://build.opensuse.org/projects/home:nukeddd:JetbrainsIDE/packages/goland/badge.svg?type=default)](https://build.opensuse.org/package/show/home:nukeddd:JetbrainsIDE/goland)
* `intellij-idea-community`: Free and open-source Java IDE
[![build result](https://build.opensuse.org/projects/home:nukeddd:JetbrainsIDE/packages/intellij-idea-community/badge.svg?type=default)](https://build.opensuse.org/package/show/home:nukeddd:JetbrainsIDE/intellij-idea-community)
* `intellij-idea-ultimate`: Paid, feature-rich Java IDE
[![build result](https://build.opensuse.org/projects/home:nukeddd:JetbrainsIDE/packages/intellij-idea-ultimate/badge.svg?type=default)](https://build.opensuse.org/package/show/home:nukeddd:JetbrainsIDE/intellij-idea-ultimate)
* `jetbrains-fleet`: Unified IDE for multiple languages
[![build result](https://build.opensuse.org/projects/home:nukeddd:JetbrainsIDE/packages/jetbrains-fleet/badge.svg?type=default)](https://build.opensuse.org/package/show/home:nukeddd:JetbrainsIDE/jetbrains-fleet)
* `phpstorm`: Empowering PHP Developers
[![build result](https://build.opensuse.org/projects/home:nukeddd:JetbrainsIDE/packages/phpstorm/badge.svg?type=default)](https://build.opensuse.org/package/show/home:nukeddd:JetbrainsIDE/phpstorm)
* `pycharm-professional`: Paid, feature-rich Python IDE
[![build result](https://build.opensuse.org/projects/home:nukeddd:JetbrainsIDE/packages/pycharm-professional/badge.svg?type=default)](https://build.opensuse.org/package/show/home:nukeddd:JetbrainsIDE/pycharm-professional)
* `rider`: .NET development IDE
[![build result](https://build.opensuse.org/projects/home:nukeddd:JetbrainsIDE/packages/rider/badge.svg?type=default)](https://build.opensuse.org/package/show/home:nukeddd:JetbrainsIDE/rider)
* `rubymine`: Ruby and Rails IDE
[![build result](https://build.opensuse.org/projects/home:nukeddd:JetbrainsIDE/packages/rubymine/badge.svg?type=default)](https://build.opensuse.org/package/show/home:nukeddd:JetbrainsIDE/rubymine)
* `rustrover`: Rust IDE
[![build result](https://build.opensuse.org/projects/home:nukeddd:JetbrainsIDE/packages/rustrover/badge.svg?type=default)](https://build.opensuse.org/package/show/home:nukeddd:JetbrainsIDE/rustrover)
* `webstorm`: JavaScript and web development IDE
[![build result](https://build.opensuse.org/projects/home:nukeddd:JetbrainsIDE/packages/webstorm/badge.svg?type=default)](https://build.opensuse.org/package/show/home:nukeddd:JetbrainsIDE/webstorm)
