%global appname dataspell
%global build_ver 252.27397.129

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

Name:    dataspell
Version: 2025.2.2
Release: 1%{?dist}
Summary: Python IDE for data scientists
License: Commercial
URL:     https://www.jetbrains.com/%{appname}/

Source0: %{name}.desktop
Source1: %{name}.metainfo.xml
Source2: https://download-cf.jetbrains.com/python/%{name}-%{version}.tar.gz
Source3: dataspell.rpmlintrc


BuildRequires: desktop-file-utils
BuildRequires: hicolor-icon-theme
BuildRequires: appstream-glib
BuildRequires: python3-devel
BuildRequires: javapackages-filesystem
BuildRequires: wget
BuildRequires: fdupes
BuildRequires: tar
BuildRequires: patchelf

Requires:      hicolor-icon-theme
Requires:      javapackages-filesystem
Requires:      %{name}-jbr = %{version}-%{release}

%description
DataSpell is an Integrated Development Environment (IDE) that is dedicated to specific tasks for exploratory data analysis and prototyping ML (machine learning) models. 

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
download_file="%{name}-%{version}-aarch64.tar.gz"
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
cp -arf ./{bin,jbr,lib,plugins,build.txt,product-info.json} %{buildroot}/usr/share/%{name}/

patchelf --set-rpath '' %{buildroot}/usr/share/%{name}/jbr/lib/jcef_helper
patchelf --set-rpath '' %{buildroot}/usr/share/%{name}/plugins/r-plugin/rwrapper-x64-linux
patchelf --set-rpath '' %{buildroot}/usr/share/%{name}/plugins/r-plugin/rwrapper-arm64-linux

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

%changelog
* Thu May 15 2025 M3DZIK <me@medzik.dev> - 2025.1.1-1
- Update to 2025.1.1 (251.25410.158)

* Wed Apr 16 2025 M3DZIK <me@medzik.dev> - 2025.1-1
- Update to 2025.1 (251.23774.439)

* Fri Feb 28 2025 M3DZIK <me@medzik.dev> - 2024.3.2-1
- Update to 2024.3.2 (243.25659.44)

* Fri Dec 20 2024 M3DZIK <me@medzik.dev> - 2024.3.1.1-1
- Update to 2024.3.1.1 (243.22562.236)

* Thu Dec 12 2024 M3DZIK <me@medzik.dev> - 2024.3.1-1
- Update to 2024.3.1 (243.22562.185)

* Fri Nov 22 2024 M3DZIK <me@medzik.dev> - 2024.3-1
- Update to 2024.3 (243.21565.247)

* Thu Sep 19 2024 M3DZIK <me@medzik.dev> - 2024.2.2-1
- Update to 2024.2.2 (242.22855.78)

* Thu Aug 29 2024 M3DZIK <me@medzik.dev> - 2024.2.1-1
- Update to 2024.2.1 (242.21829.112)

* Mon Aug 12 2024 M3DZIK <me@medzik.dev> - 2024.2-1
- Update to 2024.2 (242.20224.354)

* Sat Aug 10 2024 M3DZIK <me@medzik.dev> - 2024.1.4-1
- Update to 2024.1.4 (241.19072.25)

* Mon Jul 22 2024 M3DZIK <me@medzik.dev> - 2024.1.3-1
- Initial release
