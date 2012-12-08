%define name		libxtrap
%define version		1.0.0
%define release		13

%define major		6
%define libname		%mklibname xtrap %{major}
%define develname	%mklibname xtrap -d
%define staticname	%mklibname xtrap -d -s

Name:		%{name}
Summary:	X Trap Library
Version:	%{version}
Release:	%{release}
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXTrap-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

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


%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXTrap.so.%{major}*

%changelog
* Thu Aug 07 2012 Akdengi <akdengi>
- drop .la files

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-12mdv2011.0
+ Revision: 661561
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-11mdv2011.0
+ Revision: 602624
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-10mdv2010.1
+ Revision: 520973
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.0-9mdv2010.0
+ Revision: 425937
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-8mdv2009.0
+ Revision: 223087
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Tue Jan 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.0-7mdv2008.1
+ Revision: 153304
- Update BuildRequires and rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-6mdv2008.1
+ Revision: 150875
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 30 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.0-5mdv2008.0
+ Revision: 75080
- obsolete old -static-devel package

* Fri Aug 17 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.0-4mdv2008.0
+ Revision: 64689
- rebuild for 2008
- new devel policy
- spec clean


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

