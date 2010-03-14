%define oname	tkdnd
%define dirname %{oname}%{version}

Name:		tcl-%{oname}
Version:	2.0
Release:	%mkrel 1
Summary:	Tk extension that adds native drag & drop capabilities
Group:		Development/Other
License:	BSD
URL:		http://tkdnd.sourceforge.net/
Source0:	http://dl.sourceforge.net/%{oname}/%{oname}%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	tcl-devel >= 8.4
BuildRequires:	tk-devel >= 8.4
Requires:	tcl >= 8.4
Provides:	tkdnd = %{version}-%{release}

%description
Tk Drag & Drop: tkdnd is an extension that adds native drag & drop capabilities
to the tk toolkit. It can be used with any tk version equal or greater to 8.4.
Under unix the drag & drop protocol in use is the XDND protocol version 4
(also used by the QT toolkit, KDE & GNOME Desktops).

%prep
%setup -q -n %{dirname}

# fix file rights
chmod 644 doc/tkDND.htm

%build
%configure2_5x --libdir=%{tcl_sitearch} \
	--enable-64bit \
	--enable-symbols
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc doc/tkDND.htm
%{tcl_sitearch}/%{dirname}
%{_mandir}/mann/tkDND.n.lzma
