%def_disable check
Name: vpncloud
Version: 2.3.0
Release: alt1

Summary: VpnCloud is a high performance peer-to-peer mesh VPN over UDP
License: GPL-3
Group: Networking/Remote access

Url: https://vpncloud.ddswd.de/
Packager: Ivan Grigorev <lordvivec@mail.ru>
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
mkdir -p %buildroot%_man1dir/
mkdir -p %buildroot%_unitdir/
mkdir -p %buildroot%_sysconfdir/%name/

cp -a target/vpncloud.1.gz %buildroot%_man1dir/
cp -a assets/vpncloud@.service %buildroot%_unitdir/
cp -a assets/vpncloud.target %buildroot%_unitdir/
cp -a assets/vpncloud-wsproxy.service %buildroot%_unitdir/
cp -a assets/example.net.disabled %buildroot%_sysconfdir/%name/

%check
%rust_test

%files
%_bindir/%name
%doc *.md README.ALT
%_man1dir/*
%_unitdir/*
%_sysconfdir/*


%changelog
* Wed Oct 19 2022 Ivan G <lordvivec@mail.ru> 2.3.0-alt0.1
- initial build for ALT Linux Sisyphus
