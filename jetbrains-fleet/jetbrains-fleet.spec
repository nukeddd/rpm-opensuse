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
# do not automatically detect and export provides and dependencies on bundled libraries and executables
%global _exclude_from %{_datadir}/%{name}/lib/.*
%global __provides_exclude_from %{_exclude_from}
%global __requires_exclude_from %{_exclude_from}

Name:    jetbrains-fleet
Version: 1.48.261
Release: 2%{?dist}
Summary: Next-generation IDE by JetBrains
License: Commercial
URL:     https://www.jetbrains.com/%{appname}/

Source0: %{name}.desktop
Source1: %{name}.metainfo.xml
Source2: https://download-cf.jetbrains.com/fleet/installers/linux_x64/Fleet-%{version}.tar.gz
Source3: jetbrains-fleet.rpmlintrc


BuildRequires: desktop-file-utils
BuildRequires: appstream-glib
BuildRequires: hicolor-icon-theme
BuildRequires: javapackages-filesystem
BuildRequires: wget
BuildRequires: tar
BuildRequires: fdupes

Requires:       gtk3
Requires:       libgtk-3-0
Requires:       libgthread-2_0-0
Requires:      hicolor-icon-theme
Requires:      javapackages-filesystem

%description
Fleet is a code editor designed for simplicity, combining a clean UI, AI capabilities, and an essential set of built-in features for most major languages.

%prep
%ifarch x86_64
download_file="%{SOURCE2}"
download_arch="x64"
%else
download_file="Fleet-%{version}-aarch64.tar.gz"
download_arch="aarch64"
%endif

mkdir "${download_file}.out"
tar xf "$download_file" -C "${download_file}.out"
mv "${download_file}.out"/*/* .

%install
# Installing application...
install -d %{buildroot}/usr/share/%{name}
cp -arf ./{bin,lib} %{buildroot}/usr/share/%{name}/
chmod -R 775 "%{buildroot}%{_datadir}/%{name}/lib/app/code-cache"

# Installing icons...
install -d %{buildroot}%{_datadir}/pixmaps
install -m 0644 -p lib/Fleet.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Installing launcher...
install -d %{buildroot}%{_bindir}
ln -s /usr/share/%{name}/bin/Fleet %{buildroot}%{_bindir}/%{name}

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
%{_datadir}/metainfo/%{name}.metainfo.xml
