# vim: syntax=spec

%global tag 0.3

Name:           scenefx
Version:        %{tag}
Release:        4%{?dist}
Summary:        A drop-in replacement for the wlroots scene API that allows wayland compositors to render surfaces with eye-candy effects
License:        MIT
URL:            https://github.com/wlrfx/scenefx
Source0:        %{url}/archive/refs/tags/%{tag}.tar.gz


BuildRequires:  gcc
BuildRequires:  glslang
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.59.0

BuildRequires:  pkgconfig(wlroots-0.18)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(libdrm) >= 2.4.122
BuildRequires:  pkgconfig(pixman-1) >= 0.42.0
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.35
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.23

%description
%{summary}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} == %{version}-%{release}
# for examples
Suggests:       gcc
Suggests:       meson >= 0.58.0
Suggests:       pkgconfig(wayland-egl)

%description    devel
Development files for %{name}.


%prep
%autosetup -N

%build
MESON_OPTIONS=(
    # Disable options requiring extra/unpackaged dependencies
    -Dexamples=false
    -Dwerror=false
)

%{meson} "${MESON_OPTIONS[@]}"
%{meson_build}


%install
%{meson_install}


%check
%{meson_test}


%files
%license LICENSE
%doc README.md
%{_libdir}/libscenefx-%{tag}.so


%files  devel
%{_includedir}/scenefx-%{tag}/scenefx
%{_libdir}/libscenefx-%{tag}.so
%{_libdir}/pkgconfig/scenefx-%{tag}.pc


# Changelog will be empty until you make first annotated Git tag.
# %changelog
