%define major 6
%define libname	%mklibname xtrap %{major}
%define devname	%mklibname xtrap -d

Name:		libxtrap
Summary:	X Trap Library
Version:	1.0.1
Release:	13
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXTrap-%{version}.tar.bz2
Patch0:		0000-Drop-VMS-support-unifdef-Uvms.patch
Patch1:		0001-Require-ANSI-C89-pre-processor-drop-pre-C89-token-pa.patch
Patch2:		0002-Kill-VMS-harder-unifdef-UVMS.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xt)

%description
X Trap Library.

%package -n %{libname}
Summary:	X Trap Library
Group:		Development/X11
Provides:	%{name} = %{version}

%description -n %{libname}
X Trap Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%setup -qn libXTrap-%{version}
%apply_patches

%build
%configure \
	--disable-static \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXTrap.so.%{major}*

%files -n %{devname}
%{_libdir}/libXTrap.so
%{_libdir}/pkgconfig/xtrap.pc
