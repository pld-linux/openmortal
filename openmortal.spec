Summary:	Parody of the popular game, Mortal Kombat
Summary(pl):	Parodia popularnej gry, Mortal Kombat
Name:		openmortal
Version:	0.5
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	441e3b8fc81ba9260a91692d0ca9458d
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-freetype-includes.patch
URL:		http://openmortal.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	libstdc++-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	SDL_net-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parody of the popular game, Mortal Kombat.

%description -l pl
Parodia popularnej gry, Mortal Kombat.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
