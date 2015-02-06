Name:		blowfish-j
Version:	2.15
Release:	0.0.5
Epoch:		0
Summary:	A Blowfish implementation in Java
License:	Apache License
Url: 		http://www.lassekolb.info/bfacs.htm
Source0:	http://www.lassekolb.info/bfj215.zip
Source1:	%{name}-build.xml
BuildRequires:	ant
BuildRequires:  jpackage-utils >= 0:1.5
BuildRequires:  java-rpmbuild
Group: 		Development/Java
Buildarch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The Blowfish implementation in Java, very fast ECB and CBC 
encryption. Comes with the BlowfishEasy class for simple string 
encryption, plus a solution for streaming.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java

%description javadoc
Javadoc for %{name}

%prep
%setup -c -n %{name}-%{version}
[ ! -f build.xml ] && cp -a %{SOURCE1} build.xml

%build
%{ant} clean dist javadoc

%install
# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 dist/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

# javadoc
install -p -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
(cd $RPM_BUILD_ROOT%{_javadocdir} && ln -sf %{name}-%{version} %{name})

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,755)
%doc license.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%files javadoc
%defattr(0644,root,root,0755)
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/*
%dir %{_javadocdir}/%{name}


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0:2.15-0.0.4mdv2011.0
+ Revision: 616779
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0:2.15-0.0.3mdv2010.0
+ Revision: 424662
- rebuild

* Sat Feb 23 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0:2.15-0.0.2mdv2008.1
+ Revision: 174087
- import blowfish-j


