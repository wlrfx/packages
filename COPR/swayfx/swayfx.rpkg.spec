# vim: syntax=spec

### CHANGE THESE VARIABLES BEFORE RELEASE:
# Change to current Sway base version!
%global SwayBaseVersion 1.9.0
# Change to current SwayFX tag!
%global tag 0.4

Name:           swayfx
Version:        %{tag}
Release:        1%{?dist}
Summary:        SwayFX: Sway, but with eye candy!
License:        MIT
URL:            https://github.com/WillPower3309/swayfx
Source0:        %{url}/archive/refs/tags/%{tag}.tar.gz
Source101:      sway-portals.conf

# Upstream patches

# Fedora patches

# Conditional patches

BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.60.0
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(json-c) >= 0.13
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput) >= 1.21.0
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libsystemd) >= 239
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server) >= 1.21.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  (pkgconfig(wlroots) >= 0.17.0 with pkgconfig(wlroots) < 0.18)
BuildRequires:  (pkgconfig(scenefx) >= 0.1 with pkgconfig(scenefx) < 0.2)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xkbcommon) >= 1.5.0

# Require any of the available configuration packages;
# Prefer the -upstream one if none are directly specified in the package manager transaction
Requires:       %{name}-config
Suggests:       %{name}-config-upstream


Conflicts:      sway
Provides:       sway = %{SwayBaseVersion}

%description
SwayFX: Sway, but with eye candy!

# The artwork is heavy and we don't use it with our default config
%package        wallpapers
Summary:        Wallpapers for Sway
BuildArch:      noarch
License:        CC0

%description    wallpapers
Wallpaper collection provided with Sway


%prep
%autosetup -N -n %{name}-%{tag}

# apply unconditional patches
%autopatch -p1 -M99
# apply conditional patches

%build
%meson \
    -Dsd-bus-provider=libsystemd \
    -Dwerror=false
%meson_build

%install
%meson_install
# Install portals.conf for xdg-desktop-portal
install -D -m644 -pv %{SOURCE101} %{buildroot}%{_datadir}/xdg-desktop-portal/sway-portals.conf
# Create directory for extra config snippets
install -d -m755 -pv %{buildroot}%{_sysconfdir}/sway/config.d


%files
%license LICENSE
%dir %{_sysconfdir}/sway
%dir %{_sysconfdir}/sway/config.d
%{_mandir}/man1/sway*
%{_mandir}/man5/*
%{_mandir}/man7/*
%caps(cap_sys_nice=ep) %{_bindir}/sway
%{_bindir}/swaybar
%{_bindir}/swaymsg
%{_bindir}/swaynag

%config(noreplace) %{_sysconfdir}/sway/config
%{_datadir}/wayland-sessions/sway.desktop

%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/sway-portals.conf

%{bash_completions_dir}/sway*
%{fish_completions_dir}/sway*.fish
%{zsh_completions_dir}/_sway*


%files wallpapers
%license assets/LICENSE
%{_datadir}/backgrounds/sway

# Changelog will be empty until you make first annotated Git tag.
# %changelog
