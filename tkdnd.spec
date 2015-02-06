%define oname	tkdnd
%define dirname %{oname}%{version}

Name:		tcl-%{oname}
Version:	2.6
Release:	2
Summary:	Tk extension that adds native drag & drop capabilities
Group:		Development/Other
License:	BSD
URL:		http://tkdnd.sourceforge.net/
Source0:	http://dl.sourceforge.net/%{oname}/%{oname}%{version}-src.tar.gz
BuildRequires:	tcl-devel >= 8.4
BuildRequires:	tk-devel >= 8.4
Requires:	tcl >= 8.4
Provides:	tkdnd = %{version}-%{release}

%description
Tk Drag & Drop: tkdnd is an extension that adds native drag & drop capabilities
to the tk toolkit. It can be used with any tk version equal or greater to 8.4.
Under Unix the drag & drop protocol in use is the XDND protocol version 4
(also used by the QT toolkit, KDE & GNOME Desktops).

%prep
%setup -q -n %{oname}%{version}

# fix file rights
chmod 644 doc/tkDND.htm

%build
%configure2_5x --libdir=%{tcl_sitearch} \
%ifarch x86_64
	--enable-64bit \
%endif
	--enable-symbols
%make

%install
%makeinstall_std

%files
%doc doc/tkDND.htm
%{tcl_sitearch}/%{dirname}
%{_mandir}/mann/tkDND.*
