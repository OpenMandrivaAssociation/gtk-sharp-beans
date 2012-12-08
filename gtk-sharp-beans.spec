Name:		gtk-sharp-beans
Version:	2.13.92
Release:	1
License:	LGPLv2+
Group:		Development/Other
Summary:	Extra Gtk# bindings
Url:		http://gitorious.org/gtk-sharp-beans
Source:		%{name}-%{version}.tar.bz2

BuildRequires:	gtk-sharp2
BuildRequires:	gtk-sharp2-devel
BuildRequires:	gio-sharp-devel
BuildRequires:	mono-devel
BuildRequires:	monodoc-core
BuildArch:	noarch

%description
Gtk# Beans aims to fill the gap between the current Gtk# packages
state and all the blings and desktop integration stuffs anyone
would want to use.

It builds on top of Gtk# and extend it by adding new classes and
extension methods.

%package devel
Group:		Development/Other
Summary:	Extra Gtk# bindings
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


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.13.92-0.2mdv2011.0
+ Revision: 664947
- mass rebuild

* Sat Aug 07 2010 Götz Waschk <waschk@mandriva.org> 2.13.92-0.1mdv2011.0
+ Revision: 567394
- import gtk-sharp-beans


