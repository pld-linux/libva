Summary:	VAAPI (Video Acceleration API)
Summary(pl.UTF-8):	VAAPI (Video Acceleration API) - API akceleracji filmów
Name:		libva
Version:	1.0.12
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: http://cgit.freedesktop.org/libva/
Source0:	http://cgit.freedesktop.org/libva/snapshot/%{name}-%{version}.tar.bz2
# Source0-md5:	84408a0746a63b8cf308dc7b9f2451cf
URL:		http://www.freedesktop.org/wiki/Software/vaapi
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4.23
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
Requires:	libdrm >= 2.4.23
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The main motivation for VAAPI (Video Acceleration API) is to enable
hardware accelerated video decode/encode at various entry-points (VLD,
IDCT, Motion Compensation etc.) for the prevailing coding standards
today (MPEG-2, MPEG-4 ASP/H.263, MPEG-4 AVC/H.264, and VC-1/VMW3).

%description -l pl.UTF-8
Głównym celem API akceleracji filmów VAAPI (Video Acceleration API)
jest umożliwienie sprzętowej akceleracji dekodowania/kodowania filmów
na różnych etapach (VLD, IDCT, kompensacja ruchu itp.) dla obecnie
przeważających standardów kodowania (MPEG-2, MPEG-4 ASP/H.263, MPEG-4
AVC/H.264, VC-1/VMW3).

%package devel
Summary:	Header files for libva libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek libva
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libva libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek libva.

%package static
Summary:	Static libva libraries
Summary(pl.UTF-8):	Statyczne biblioteki libva
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libva libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libva.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-static \
	--enable-i965-driver \
	--with-drivers-path=%{_libdir}/%{name}/dri

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/dri/*.{a,la}
%{__rm} $RPM_BUILD_ROOT%{_bindir}/test_*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/h264encode
%attr(755,root,root) %{_bindir}/mpeg2vldemo
%attr(755,root,root) %{_bindir}/putsurface
%attr(755,root,root) %{_bindir}/vainfo
%attr(755,root,root) %{_libdir}/libva.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva.so.1
%attr(755,root,root) %{_libdir}/libva-egl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva-egl.so.1
%attr(755,root,root) %{_libdir}/libva-glx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva-glx.so.1
%attr(755,root,root) %{_libdir}/libva-tpi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva-tpi.so.1
%attr(755,root,root) %{_libdir}/libva-x11.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva-x11.so.1
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/dri
%attr(755,root,root) %{_libdir}/%{name}/dri/dummy_drv_video.so
%attr(755,root,root) %{_libdir}/%{name}/dri/i965_drv_video.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva.so
%attr(755,root,root) %{_libdir}/libva-egl.so
%attr(755,root,root) %{_libdir}/libva-glx.so
%attr(755,root,root) %{_libdir}/libva-tpi.so
%attr(755,root,root) %{_libdir}/libva-x11.so
%{_libdir}/libva.la
%{_libdir}/libva-egl.la
%{_libdir}/libva-glx.la
%{_libdir}/libva-tpi.la
%{_libdir}/libva-x11.la
%{_includedir}/va
%{_pkgconfigdir}/libva.pc
%{_pkgconfigdir}/libva-egl.pc
%{_pkgconfigdir}/libva-glx.pc
%{_pkgconfigdir}/libva-tpi.pc
%{_pkgconfigdir}/libva-x11.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libva.a
%{_libdir}/libva-egl.a
%{_libdir}/libva-glx.a
%{_libdir}/libva-tpi.a
%{_libdir}/libva-x11.a
