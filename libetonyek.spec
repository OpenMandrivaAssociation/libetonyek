%define api 0.0
%define major 0
%define libname %mklibname etonyek %{api} %{major}
%define devname %mklibname etonyek -d

Name: libetonyek
Version: 0.0.3
Release: 1
Source0: http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.bz2
Summary: Library for interpreting and importing Apple Keynote presentiations
URL: http://freedesktop.org/wiki/Software/libetonyek
License: MPL 2.0
Group: System/Libraries
BuildRequires: pkgconfig(libwpd-0.9)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(cppunit)
BuildRequires: boost-devel >= 1.55.0
BuildRequires: gperf
BuildRequires: doxygen

%description
Library for interpreting and importing Apple Keynote presentiations

%package -n %{libname}
Summary: Library for interpreting and importing Apple Keynote presentiations
Group: System/Libraries

%description -n %{libname}
Library for interpreting and importing Apple Keynote presentiations

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
aclocal
automake -a
autoheader
autoconf
%configure

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*-%{api}.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%doc %{_docdir}/libetonyek
