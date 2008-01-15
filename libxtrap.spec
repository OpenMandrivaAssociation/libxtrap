%define major		6
%define libname		%mklibname xtrap %{major}
%define develname	%mklibname xtrap -d
%define staticname	%mklibname xtrap -d -s

Name:		libxtrap
Summary:	X Trap Library
Version:	1.0.0
Release:	%mkrel 7
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXTrap-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	x11-util-macros		>= 1.1.5
BuildRequires:	libxt-devel		>= 1.0.5
BuildRequires:	libx11-devel		>= 1.1.3
BuildRequires:	libxext-devel		>= 1.0.3
BuildRequires:	x11-proto-devel		>= 7.3

%description
X Trap Library.

#-----------------------------------------------------------

%package -n %{libname}
Summary:  X Trap Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
X Trap Library

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libname} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{mklibname xtrap 6 -d}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXTrap.so
%{_libdir}/libXTrap.la
%{_libdir}/pkgconfig/xtrap.pc

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}
Provides: %{name}-static-devel = %{version}-%{release}
Obsoletes: %{mklibname xtrap 6 -s -d}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
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

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXTrap.so.%{major}*

