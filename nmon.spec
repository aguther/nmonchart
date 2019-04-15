Name:		nmonchart
Version:	35
Release:	1%{?dist}
Summary:	Nigel's .nmon to .html transformer for Linux
License:	GPLv3
Group:		Development/Tools
URL:		http://nmon.sourceforge.net
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Requires:	ksh

%description
The Korn shell script file nmonchart transforms .nmon performance capture files in to .html files for a webserver site.

%prep
%setup -q

%install
install -D -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc nmonchart_license
%doc nmon_upload.html
%doc nmon_upload.php
%doc README
%doc sampleC.html
%doc sampleC.nmon
%{_bindir}/%{name}

%changelog
* Sat Apr 15 2019 Andreas Guther <github@guther.net> - 35-1
- Update to version 35

* Sat Aug 12 2017 Andreas Guther <github@guther.net> - 31-1
- Update to version 31

* Sun Jan 10 2016 Andreas Guther <github@guther.net> - 23-1
- Initial package based on version 23
