Name:           scenefx
Version:        0.5
Release:        1%{?dist}
Summary:        A drop-in replacement for the wlroots scene API with eye-candy effects

License:        MIT
URL:            https://github.com/wlrfx/scenefx
Source0:        %{url}/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-server) >= 1.24.0
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wlroots-0.20) >= 0.20.0
BuildRequires:  pkgconfig(libdrm) >= 2.4.129
BuildRequires:  pkgconfig(xkbcommon) >= 1.8.0
BuildRequires:  pkgconfig(pixman-1) >= 0.43.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(lcms2)

%description
scenefx is a drop-in replacement for the wlroots scene API that allows
Wayland compositors to render surfaces with eye-candy effects -- including
blur, drop shadows, and rounded corners -- while keeping the simplicity of
the standard wlroots scene API. It is used by compositors such as SwayFX,
MangoWC, and mwc.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(wlroots-0.20)

%description devel
Header files and pkgconfig data needed to build Wayland compositors
against scenefx.

%prep
%autosetup -p1 -n %{name}-%{version}
# tinywl example is CC0-1.0 licensed; Fedora no longer permits CC0 for
# code (only content). It is unused since -Dexamples=false disables it.
rm -rf tinywl

%build
%meson -Dexamples=false
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
# FIXME: library does not follow standard soname versioning
# (libscenefx.so.X + libscenefx.so symlink in -devel). Tracked upstream:
# https://github.com/wlrfx/scenefx/issues/219
%{_libdir}/libscenefx-%{version}.so

%files devel
%{_libdir}/pkgconfig/scenefx-%{version}.pc
%{_includedir}/scenefx-%{version}/

%changelog
* Mon Sep 07 2026 Damian Daniel <damian@danielovci.net> - 0.5-1
- Initial packaging
