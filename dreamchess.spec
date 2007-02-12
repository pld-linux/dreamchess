Summary:	3D chess game for X-Window
Summary(pl.UTF-8):   Trójwymiarowe szachy dla X-Window
Name:		dreamchess
Version:	0.1.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://download.berlios.de/dreamchess/%{name}-%{version}.tar.gz
# Source0-md5:	0c265cbd95c003d478f7825581742765
Source1:	%{name}.desktop
URL:		http://www.dreamchess.org/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DreamChess is an open source chess game. It features 3D OpenGL
graphics and provides various chess board sets, ranging from classic
wooden to flat figurines.

%description -l pl.UTF-8
DreamChess jest darmową grą posiadającą otwarte źródła. Gra posiada
grafikę 3D OpenGL i dostarcza zróżnicowane zestawy szachowe, począwszy
od klasycznej drewnianej planszy i standardowych figur.

%prep
%setup -q

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
install desktop/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_mandir}/man6/*
