%define debug_package %{nil}

Name:		openstack-neutron-bgpvpn
Version:	2015.2
Release:	1%{?dist}
Summary:	BGPVPN Support for OpenStack Neutron

Group:		Applications/Internet
License:	Apache 2.0
URL:		https://github.com/openstack/networking-bgpvpn/blob/master/devstack/plugin.sh
Source0:	openstack-neutron-bgpvpn.tar.gz

BuildArch:	noarch
BuildRequires:	python-setuptools
Requires:	openstack-neutron

%description
BGPVPN Support for OpenStack Neutron

%prep
%setup -q

%build

%install
PBR_VERSION=1.8.1 /usr/bin/python setup.py install --prefix=%{buildroot} --install-lib=%{buildroot}/usr/lib/python2.7/site-packages
cp networking_bgpvpn/neutron/db/migration/alembic_migrations/versions/HEADS %{buildroot}/usr/lib/python2.7/site-packages/networking_bgpvpn/neutron/db/migration/alembic_migrations/versions/HEADS
rm -rf %{buildroot}/usr/lib/python2.7/site-packages/networking_bgpvpn_tempest

%files
%config(noreplace) %attr(-, root, root) %{_sysconfdir}/neutron/networking_bgpvpn.conf
%config(noreplace) %attr(-, root, root) %{_sysconfdir}/neutron/policy.d/bgpvpn.conf
/bin/neutron-bagpipe-openvswitch-agent
/usr/lib/python2.7/site-packages/networking_bgpvpn/*
/usr/lib/python2.7/site-packages/networking_bgpvpn-*.egg-info

%changelog

