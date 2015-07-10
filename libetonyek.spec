%define api 0.1
%define major 1
%define libname %mklibname etonyek %{api} %{major}
%define devname %mklibname etonyek -d

Name: libetonyek
Version: 0.1.3
Release: 1
Source0: http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
Summary: Library for interpreting and importing Apple Keynote presentiations
URL: http://freedesktop.org/wiki/Software/libetonyek
License: MPL 2.0
Group: System/Libraries
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: boost-devel >= 1.55.0
BuildRequires: glm-devel
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
CFLAGS="%{optflags} -Qunused-arguments" \
CXXFLAGS="%{optflags} -Qunused-arguments" \
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
