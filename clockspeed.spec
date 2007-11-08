# TODO:
# - makefile for human, not for DJB
# - check the license
Summary:	clockspeed - compensate for a system clock
Name:		clockspeed
Version:	0.62
Release:	0.1
License:	unknown?
Group:		Daemons
Source0:	http://cr.yp.to/clockspeed/%{name}-%{version}.tar.gz
# Source0-md5:	425614174fcfe2ad42d22d3d02e2d567
URL:		http://cr.yp.to/clockspeed.html
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clockspeed uses a hardware tick counter to compensate for a persistently
fast or slow system clock. Given a few time measurements from a reliable
source, it computes and then eliminates the clock skew.

sntpclock checks another system's NTP clock, and prints the results in a
format suitable for input to clockspeed. sntpclock is the simplest available
NTP/SNTP client.

taiclock and taiclockd form an even simpler alternative to SNTP. They are
suitable for precise time synchronization over a local area network, without
the hassles and potential security problems of an NTP server.

This version of clockspeed can use the Pentium RDTSC tick counter or the
Solaris gethrtime() nanosecond counter. 

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	LD="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \

#	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BLURB CHANGES INSTALL README THANKS TODO
%attr(754,root,root) %{_sbindir}/*
