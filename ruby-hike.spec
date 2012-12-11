%define rname	hike

Name:		ruby-%{rname}
Summary:	A Ruby library for finding files in a set of paths
Version:	1.2.1
Release:	1
License:	MIT
Group:		Development/Ruby
URL:		https://github.com/sstephenson/hike
Source0:	http://rubygems.org/downloads/%{rname}-%{version}.gem
BuildRequires:	ruby-RubyGems
BuildArch:	noarch

%description
Hike is a Ruby library for finding files in a set of paths. Use it to implement
search paths, load paths, and the like.

%prep

%build

%install
gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}
rm -rf %{buildroot}%{ruby_gemdir}/cache

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{rname}-%{version}
%{ruby_gemdir}/gems/%{rname}-%{version}
%{ruby_gemdir}/specifications/%{rname}-%{version}.gemspec


%changelog
* Thu May 03 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.2.1-1
+ Revision: 795375
- imported package ruby-hike

