%def_disable check

Name: vpncloud
Version: 2.3.0
Release: alt0.1

Summary: VpnCloud is a high performance peer-to-peer mesh VPN over UDP
License: GPL-3
Group: Networking/Remote access

Url: https://vpncloud.ddswd.de/
Packager: Ivan Grigorev <lordvivec@mail.ru>
#only tested on x86_64
ExclusiveArch: x86_64
Source: %name-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: asciidoctor

%description
VpnCloud is a high performance peer-to-peer mesh VPN over UDP

%prep
%setup

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/%name
%doc *.md README.ALT

%changelog
* Wed Oct 19 2022 Ivan G <lordvivec@mail.ru> 2.3.0-alt0.1
- initial build for ALT Linux Sisyphus
