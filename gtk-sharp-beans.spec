Summary:	Extra Gtk sharp bindings
Name:		gtk-sharp-beans
Version:	2.13.92
Release:	6
License:	LGPLv2+
Group:		Development/Other
Url:		http://gitorious.org/gtk-sharp-beans
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch

BuildRequires:	monodoc-core
BuildRequires:	pkgconfig(gapi-2.0)
BuildRequires:	pkgconfig(gio-sharp-2.0)
BuildRequires:	pkgconfig(gtk-sharp-2.0)
BuildRequires:	pkgconfig(mono)

%description
Gtk# Beans aims to fill the gap between the current Gtk# packages
state and all the blings and desktop integration stuffs anyone
would want to use.

It builds on top of Gtk sharp and extend it by adding new classes and
extension methods.

%package devel
Group:		Development/Other
Summary:	Extra Gtk sharp bindings
Requires:	%{name} = %{version}

%description devel
Files for developing programs that use gtk-sharp-beans

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

%files
%doc NEWS AUTHORS README
%dir %{_prefix}/lib/mono/gac/gtk-sharp-beans
%dir %{_prefix}/lib/mono/gac/gtk-sharp-beans/2.14.0.0__97a95fb57b03c03a
%{_prefix}/lib/mono/gac/gtk-sharp-beans/*/*.dll*

%dir %{_prefix}/lib/mono/gtk-sharp-beans-2.0
%{_prefix}/lib/mono/gtk-sharp-beans-2.0/gtk-sharp-beans.dll

%files devel
%doc ChangeLog 
%{_datadir}/pkgconfig/gtk-sharp-beans-2.0.pc

