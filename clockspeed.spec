# TODO:
# - makefile for human, not for DJB
# - check the license
Summary:	clockspeed - compensate for a system clock
Summary(pl.UTF-8):	clockspeed - kompensacja zegara systemowego
Name:		clockspeed
Version:	0.62
Release:	0.1
License:	unknown?
Group:		Daemons
Source0:	http://cr.yp.to/clockspeed/%{name}-%{version}.tar.gz
# Source0-md5:	425614174fcfe2ad42d22d3d02e2d567
Patch0:		%{name}-fix.patch
URL:		http://cr.yp.to/clockspeed.html
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clockspeed uses a hardware tick counter to compensate for a
persistently fast or slow system clock. Given a few time measurements
from a reliable source, it computes and then eliminates the clock
skew.

sntpclock checks another system's NTP clock, and prints the results in
a format suitable for input to clockspeed. sntpclock is the simplest
available NTP/SNTP client.

taiclock and taiclockd form an even simpler alternative to SNTP. They
are suitable for precise time synchronization over a local area
network, without the hassles and potential security problems of an NTP
server.

This version of clockspeed can use the Pentium TSC tick counter or the
Solaris gethrtime() nanosecond counter. 

%description -l pl.UTF-8
clockspeed wykorzystuje sprzętowy licznik taktów do kompensacji stale
zbyt szybkiego lub zbyt wolnego zegara systemowego. Po podaniu kilku
pomiarów czasu z wiarygodnego źródła oblicza i eliminuje niedokładność
zegara.

sntpclock sprawdza zegar NTP innego systemu i wypisuje wynik w
formacie pasującym do wejścia clockspeed. sntpclock to najprostszy
dostępny klient NTP/SNTP.

taiclock i taiclockd tworzą nawet jeszcze prostszą alternatywę dla
SNTP. Nadają się do synchronizacji czasu w sieci lokalnej, bez
potencjalnych problemów z bezpieczeństwem związanych z serwerem NTP.

Ta wersja programu clockspeed potrafi wykorzystywać licznik taktów
TSC procesora Pentium lub nanosekundowy licznik gethrtime() systemu
Solaris.

%prep
%setup -q
%patch -P0 -p1

%build
echo '%{__cc} %{rpmcflags}' > conf-cc
echo '%{__cc} %{rpmldflags}' > conf-ld
echo "$RPM_BUILD_ROOT%{_prefix}" > conf-home

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# bleh, doesn't honour home for /etc
./install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BLURB CHANGES INSTALL README THANKS TODO
%attr(754,root,root) %{_sbindir}/*
