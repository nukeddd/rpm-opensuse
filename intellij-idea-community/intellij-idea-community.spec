# setting some global constants
%global appname idea
%global build_ver 252.27397.103
%global idea_name ideaIC

# disable debuginfo subpackage
%global debug_package %{nil}
# Disable build-id symlinks to avoid conflicts
%global _build_id_links none
# don't strip bundled binaries because pycharm checks length (!!!) of binary fsnotif
# and if you strip debug stuff from it, it will complain
%global __strip /bin/true
# dont repack jars
%global __jar_repack %{nil}
# disable rpath checks
%define __brp_check_rpaths %{nil}
# there are some python 2 and python 3 scripts so there is no way out to bytecompile them ^_^
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
# do not automatically detect and export provides and dependencies on bundled libraries and executables
%global _exclude_from %{_datadir}/%{name}/bin/.*|%{_datadir}/%{name}/lib/.*|%{_datadir}/%{name}/plugins/.*|%{_datadir}/%{name}/jbr/.*
%global __provides_exclude_from %{_exclude_from}
%global __requires_exclude_from %{_exclude_from}

Name:    intellij-idea-community
Version: 2025.2.4
Release: 1%{?dist}
Summary: Capable and Ergonomic Java IDE - Community Edition
License: Apache-2.0
URL:     https://www.jetbrains.com/%{appname}/

Source0: %{name}.desktop
Source1: %{name}.metainfo.xml
Source2: https://download-cf.jetbrains.com/idea/%{idea_name}-%{version}.tar.gz
Source3: rpm.rpmlintrc
Source4: https://download-cf.jetbrains.com/idea/%{idea_name}-%{version}-aarch64.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: appstream-glib
BuildRequires: python3-devel
BuildRequires: hicolor-icon-theme
BuildRequires: javapackages-filesystem
BuildRequires: wget
BuildRequires: tar
BuildRequires: fdupes
BuildRequires: patchelf

Requires:      hicolor-icon-theme
Requires:      javapackages-filesystem
Requires:      %{name}-jbr = %{version}-%{release}

%description
IntelliJ IDEA Community is a free and open-source edition of IntelliJ IDEA, the commercial Java IDE by JetBrains.
IntelliJ IDEA Community provides all the tools you need for Java, Groovy, Kotlin, Scala, and Android.

%package jbr
Summary:  JetBrains Runtime
Requires: %{name} = %{version}-%{release}

%global __provides_exclude_from %{_exclude_from}
%global __requires_exclude_from %{_exclude_from}

%description jbr
JetBrains Runtime - a patched Java Runtime Environment (JRE).

%prep
%ifarch x86_64
download_file="%{SOURCE2}"
%else
download_file="%{SOURCE4}"
%endif

mkdir "${download_file}.out"
tar xf "$download_file" -C "${download_file}.out"
mv "${download_file}.out"/*/* .

# Patching shebangs...
%if 0%{?fedora}
%py3_shebang_fix .
%else
find . -type f -name "*.py" -exec sed -e 's@/usr/bin/env python.*@%{__python3}@g' -i "{}" \;
%endif

%install
# Installing application...
install -d %{buildroot}/usr/share/%{name}
cp -arf ./{bin,jbr,lib,plugins,modules,build.txt,product-info.json} %{buildroot}/usr/share/%{name}/

patchelf --set-rpath '' %{buildroot}/usr/share/%{name}/jbr/lib/jcef_helper

# Installing icons...
install -d %{buildroot}%{_datadir}/pixmaps
install -m 0644 -p bin/%{appname}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m 0644 -p bin/%{appname}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Installing launcher...
install -d %{buildroot}%{_bindir}
ln -s /usr/share/%{name}/bin/%{appname} %{buildroot}%{_bindir}/%{name}

# Installing desktop file...
install -d %{buildroot}%{_datadir}/applications
install -m 0644 -p %{SOURCE0} %{buildroot}%{_datadir}/applications/%{name}.desktop

# Installing metainfo...
install -d %{buildroot}/usr/share/metainfo
install -m 0644 -p %{SOURCE1} %{buildroot}/usr/share/metainfo/%{name}.metainfo.xml

# Find and hardlink duplicate files to save space
%fdupes %{buildroot}/usr/share/%{name}
%fdupes %{buildroot}%{_licensedir}/%{name}

%check
appstream-util validate-relax --nonet %{buildroot}/usr/share/metainfo/%{name}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license license/*
%dir /usr/share/%{name}
/usr/share/%{name}/{bin,lib,plugins,modules,build.txt,product-info.json}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/%{name}.metainfo.xml

%files jbr
/usr/share/%{name}/jbr
