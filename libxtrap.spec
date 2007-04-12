%define libxtrap %mklibname xtrap 6
Name: libxtrap
Summary:  X Trap Library
Version: 1.0.0
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXTrap-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X Trap Library

#-----------------------------------------------------------

%package -n %{libxtrap}
Summary:  X Trap Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxtrap}
X Trap Library

#-----------------------------------------------------------

%package -n %{libxtrap}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxtrap} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxtrap-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxtrap}-devel
Development files for %{name}

%files -n %{libxtrap}-devel
%defattr(-,root,root)
%{_libdir}/libXTrap.so
%{_libdir}/libXTrap.la
%{_libdir}/pkgconfig/xtrap.pc

#-----------------------------------------------------------

%package -n %{libxtrap}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxtrap}-devel = %{version}
Provides: libxtrap-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxtrap}-static-devel
Static development files for %{name}

%files -n %{libxtrap}-static-devel
%defattr(-,root,root)
%{_libdir}/libXTrap.a

#-----------------------------------------------------------

%prep
%setup -q -n libXTrap-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxtrap}
%defattr(-,root,root)
%{_libdir}/libXTrap.so.6
%{_libdir}/libXTrap.so.6.4.0


