Name:           scam
Version:        0.1
Release:        1%{?dist}
Summary:        System Configuration Abstraction Manager
License:        GPL2
URL:            https://gitlab.cee.redhat.com/vdo/open-sourcing/tools/third/scam
Source0:        %{url}/-/archive/master/scam-master.tar.gz
BuildArch:      noarch


%description
System Configuration Abstraction Manager provides a simple way to drive
configuration by using key:value data in text files stored on the local
machine.

%prep
#XXX: This should be fixed when we post publicly.
%setup -q -n %{name}-master

%install
%{__install} -d $RPM_BUILD_ROOT/%{_sbindir}
%{__install} -m 0755 scam $RPM_BUILD_ROOT/%{_sbindir}/scam
%{__install} -d $RPM_BUILD_ROOT/%{_sysconfdir}/scam

%files
#defattr(-,root,root)
%{_sbindir}/scam
%dir %{_sysconfdir}/scam

%changelog
* Thu Dec 09 2021 Andy Walsh <awalsh@redhat.com> - 0.1-1
- Initial build
