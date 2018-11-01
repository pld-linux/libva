#
# Conditional build:
%bcond_without	static_libs	# static libraries

Summary:	VAAPI (Video Acceleration API)
Summary(pl.UTF-8):	VAAPI (Video Acceleration API) - API akceleracji filmów
Name:		libva
Version:	2.3.0
Release:	2
License:	MIT
Group:		Libraries
Source0:	https://github.com/intel/libva/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	2555c46075ab2f6128f39902ba1c6183
URL:		https://github.com/intel/libva
BuildRequires:	Mesa-libEGL-devel
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4
BuildRequires:	libtool
BuildRequires:	pkgconfig
# wayland-client
BuildRequires:	wayland-devel >= 1.0.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
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

%package drm
Summary:	VAAPI - DRM interface library
Summary(pl.UTF-8):	VAAPI - biblioteka interfejsu DRM
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libdrm >= 2.4

%description drm
VAAPI - DRM interface library.

%description drm -l pl.UTF-8
VAAPI - biblioteka interfejsu DRM.

%package drm-devel
Summary:	Header files for VAAPI DRM interface library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki interfejsu DRM VAAPI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-drm = %{version}-%{release}
Requires:	libdrm-devel >= 2.4

%description drm-devel
Header files for VAAPI DRM interface library.

%description drm-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki interfejsu DRM VAAPI.

%package drm-static
Summary:	VAAPI - DRM interface static library
Summary(pl.UTF-8):	VAAPI - statyczna biblioteka interfejsu DRM
Group:		Development/Libraries
Requires:	%{name}-drm-devel = %{version}-%{release}

%description drm-static
VAAPI - DRM interface static library.

%description drm-static -l pl.UTF-8
VAAPI - statyczna biblioteka interfejsu DRM.

%package glx
Summary:	VAAPI - GLX interface library
Summary(pl.UTF-8):	VAAPI - biblioteka interfejsu GLX
Group:		Libraries
Requires:	%{name}-x11 = %{version}-%{release}

%description glx
VAAPI - GLX interface library.

%description glx -l pl.UTF-8
VAAPI - biblioteka interfejsu GLX.

%package glx-devel
Summary:	Header files for VAAPI GLX interface library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki interfejsu GLX VAAPI
Group:		Development/Libraries
Requires:	%{name}-glx = %{version}-%{release}
Requires:	%{name}-x11-devel = %{version}-%{release}
Requires:	OpenGL-GLX-devel

%description glx-devel
Header files for VAAPI GLX interface library.

%description glx-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki interfejsu GLX VAAPI.

%package glx-static
Summary:	VAAPI - GLX interface static library
Summary(pl.UTF-8):	VAAPI - statyczna biblioteka interfejsu GLX
Group:		Development/Libraries
Requires:	%{name}-glx-devel = %{version}-%{release}

%description glx-static
VAAPI - GLX interface static library.

%description glx-static -l pl.UTF-8
VAAPI - statyczna biblioteka interfejsu GLX.

%package wayland
Summary:	VAAPI - Wayland interface library
Summary(pl.UTF-8):	VAAPI - biblioteka interfejsu Wayland
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	wayland >= 1.0.0

%description wayland
VAAPI - Wayland interface library.

%description wayland -l pl.UTF-8
VAAPI - biblioteka interfejsu Wayland.

%package wayland-devel
Summary:	Header files for VAAPI Wayland interface library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki interfejsu Wayland VAAPI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-wayland = %{version}-%{release}
Requires:	wayland-devel >= 1.0.0

%description wayland-devel
Header files for VAAPI Wayland interface library.

%description wayland-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki interfejsu Wayland VAAPI.

%package wayland-static
Summary:	VAAPI - Wayland interface static library
Summary(pl.UTF-8):	VAAPI - statyczna biblioteka interfejsu Wayland
Group:		Development/Libraries
Requires:	%{name}-wayland-devel = %{version}-%{release}

%description wayland-static
VAAPI - Wayland interface static library.

%description wayland-static -l pl.UTF-8
VAAPI - statyczna biblioteka interfejsu Wayland.

%package x11
Summary:	VAAPI - X11 interface library
Summary(pl.UTF-8):	VAAPI - biblioteka interfejsu X11
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libdrm >= 2.4

%description x11
VAAPI - X11 interface library.

%description x11 -l pl.UTF-8
VAAPI - biblioteka interfejsu X11.

%package x11-devel
Summary:	Header files for VAAPI X11 interface library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki interfejsu X11 VAAPI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-x11 = %{version}-%{release}
Requires:	libdrm-devel >= 2.4
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel

%description x11-devel
Header files for VAAPI X11 interface library.

%description x11-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki interfejsu X11 VAAPI.

%package x11-static
Summary:	VAAPI - X11 interface static library
Summary(pl.UTF-8):	VAAPI - statyczna biblioteka interfejsu X11
Group:		Development/Libraries
Requires:	%{name}-x11-devel = %{version}-%{release}

%description x11-static
VAAPI - X11 interface static library.

%description x11-static -l pl.UTF-8
VAAPI - statyczna biblioteka interfejsu X11.

%package tools
Summary:	VAAPI test and example programs
Summary(pl.UTF-8):	Programy testowe i przykładowe do VAAPI
Group:		Applications/Graphics
Requires:	%{name}-drm = %{version}-%{release}
Requires:	%{name}-wayland = %{version}-%{release}
Requires:	%{name}-x11 = %{version}-%{release}

%description tools
VAAPI test and example programs.

%description tools -l pl.UTF-8
Programy testowe i przykładowe do VAAPI.

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
	%{?with_static_libs:--enable-static} \
	--with-drivers-path=%{_libdir}/%{name}/dri

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/dri

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo "#LIBVA_DRIVER_NAME=vdpau" > $RPM_BUILD_ROOT/etc/libva.conf

#%{__rm} $RPM_BUILD_ROOT%{_libdir}/{%{name}/dri/*.{a,la},libva*.la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	drm -p /sbin/ldconfig
%postun	drm -p /sbin/ldconfig

%post	glx -p /sbin/ldconfig
%postun	glx -p /sbin/ldconfig

%post	wayland -p /sbin/ldconfig
%postun	wayland -p /sbin/ldconfig

%post	x11 -p /sbin/ldconfig
%postun	x11 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS
%attr(755,root,root) %{_libdir}/libva.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva.so.2
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/dri
#%attr(755,root,root) %{_libdir}/%{name}/dri/dummy_drv_video.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libva.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva.so
%dir %{_includedir}/va
%{_includedir}/va/va.h
%{_includedir}/va/va_backend.h
#%{_includedir}/va/va_backend_tpi.h
%{_includedir}/va/va_backend_vpp.h
%{_includedir}/va/va_compat.h
%{_includedir}/va/va_dec_hevc.h
%{_includedir}/va/va_dec_jpeg.h
%{_includedir}/va/va_dec_vp8.h
%{_includedir}/va/va_dec_vp9.h
%{_includedir}/va/va_drmcommon.h
%{_includedir}/va/va_egl.h
%{_includedir}/va/va_enc_hevc.h
%{_includedir}/va/va_enc_h264.h
%{_includedir}/va/va_enc_jpeg.h
%{_includedir}/va/va_enc_mpeg2.h
%{_includedir}/va/va_enc_vp8.h
%{_includedir}/va/va_enc_vp9.h
%{_includedir}/va/va_fei*.h
%{_includedir}/va/va_str.h
%{_includedir}/va/va_tpi.h
%{_includedir}/va/va_version.h
%{_includedir}/va/va_vpp.h
%{_pkgconfigdir}/libva.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libva.a
%endif

%files drm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva-drm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva-drm.so.2

%files drm-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva-drm.so
%{_includedir}/va/va_drm.h
%{_pkgconfigdir}/libva-drm.pc

%if %{with static_libs}
%files drm-static
%defattr(644,root,root,755)
%{_libdir}/libva-drm.a
%endif

%files glx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva-glx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva-glx.so.2

%files glx-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva-glx.so
%{_includedir}/va/va_backend_glx.h
%{_includedir}/va/va_glx.h
%{_pkgconfigdir}/libva-glx.pc

%if %{with static_libs}
%files glx-static
%defattr(644,root,root,755)
%{_libdir}/libva-glx.a
%endif

%files wayland
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva-wayland.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva-wayland.so.2

%files wayland-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva-wayland.so
%{_includedir}/va/va_backend_wayland.h
%{_includedir}/va/va_wayland.h
%{_pkgconfigdir}/libva-wayland.pc

%if %{with static_libs}
%files wayland-static
%defattr(644,root,root,755)
%{_libdir}/libva-wayland.a
%endif

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva-x11.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva-x11.so.2

%files x11-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva-x11.so
%{_includedir}/va/va_dri2.h
%{_includedir}/va/va_dricommon.h
%{_includedir}/va/va_x11.h
%{_pkgconfigdir}/libva-x11.pc

%if %{with static_libs}
%files x11-static
%defattr(644,root,root,755)
%{_libdir}/libva-x11.a
%endif
