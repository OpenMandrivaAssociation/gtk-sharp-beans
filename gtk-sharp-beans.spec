%define git 19023b6
Name:           gtk-sharp-beans
Version:        2.14.0
Release:        %mkrel 1
License:        LGPLv2+
Group:          Development/Other
Summary:        Extra Gtk# bindings
Url:            https://github.com/mono/gtk-sharp-beans/
# https://github.com/mono/gtk-sharp-beans/tarball/2.14.0
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  gtk-sharp2
BuildRequires:  gtk-sharp2-devel
BuildRequires:  gio-sharp-devel
BuildRequires:  mono-devel
BuildRequires:  monodoc-core
BuildArch: noarch
%define _requires_exceptions ^lib.*

%description

Gtk# Beans aims to fill the gap between the current Gtk# packages
state and all the blings and desktop integration stuffs anyone
would want to use.

It builds on top of Gtk# and extend it by adding new classes and
extension methods.

%package devel
Group:          Development/Other
Summary:        Extra Gtk# bindings
Requires:       %{name} = %{version}

%description devel
Files for developing programs that use gtk-sharp-beans

%prep
%setup -q -n mono-gtk-sharp-beans-%git
./autogen.sh

%build
%configure2_5x
#gw parallel make fails in 2.14.0
make

%install
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

%clean
rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%doc NEWS AUTHORS README
%_prefix/lib/%name

%files devel
%defattr(-,root,root)
%doc ChangeLog 
%{_datadir}/pkgconfig/gtk-sharp-beans-2.0.pc
