Summary:	VAAPI (Video Acceleration API)
Name:		libva
# see configure.ac
Version:	1.0.3
Release:	1
License:	BSD
Group:		Libraries
# git clone git://anongit.freedesktop.org/git/libva
Source0:	http://cgit.freedesktop.org/libva/snapshot/%{name}-%{version}.tar.bz2
# Source0-md5:	5e92b34ec7047479993ac5b02a16491c
URL:		http://www.freedesktop.org/wiki/Software/vaapi
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4.21
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The main motivation for VAAPI (Video Acceleration API) is to enable
hardware accelerated video decode/encode at various entry-points (VLD,
IDCT, Motion Compensation etc.) for the prevailing coding standards
today (MPEG-2, MPEG-4 ASP/H.263, MPEG-4 AVC/H.264, and VC-1/VMW3).

%package devel
Summary:	Header files and develpment documentation for libva
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and documentation for libva.

%package static
Summary:	Static libva library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libva library.

%prep
%setup -q

%build
./autogen.sh
%configure \
	--enable-static \
	--enable-i965-driver \
	--with-drivers-path=%{_libdir}/%{name}/dri

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/%{name}/dri/*.{a,la}
rm $RPM_BUILD_ROOT%{_bindir}/test_*

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
%attr(755,root,root) %{_libdir}/libva*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libva*.so.1
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/dri
%attr(755,root,root) %{_libdir}/%{name}/dri/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva*.so
%{_includedir}/va
%{_libdir}/libva*.la
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libva*.a
