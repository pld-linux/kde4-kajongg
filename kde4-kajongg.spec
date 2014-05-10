%define		_state		stable
%define		orgname		kajongg
%define		qtver		4.8.0

Summary:	kajongg
Name:		kde4-kajongg
Version:	4.13.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	e9646b05b068b0c21da99b1d318a8228
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	phonon-devel >= 4.3.80
BuildRequires:	python-PyKDE4
BuildRequires:	python-TwistedCore
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	python-TwistedCore
Obsoletes:	kde4-kdegames-kajongg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kajongg.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kajongg
%attr(755,root,root) %{_bindir}/kajonggserver
#%attr(755,root,root) %{_libdir}/libkcardgame.so
%{_desktopdir}/kde4/kajongg.desktop
%{_datadir}/apps/kajongg
%{_kdedocdir}/en/kajongg
%{_iconsdir}/hicolor/*x*/apps/kajongg.png
%{_iconsdir}/hicolor/scalable/apps/kajongg.svgz
%{_iconsdir}/hicolor/scalable/actions/games-kajongg-law.svgz
