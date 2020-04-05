%{!?tcp_wrappers:%define tcp_wrappers 1}
#%define _generatorsdir %{_prefix}/lib/systemd/system-generators
%define _unpackaged_files_terminate_build 0

Name: vsftpd
Version: 3.0.2
Release: 25%{?dist}
Summary: Very Secure Ftp Daemon

Group: System Environment/Daemons
# OpenSSL link exception
License: GPLv2 with exceptions
URL: https://security.appspot.com/vsftpd.html
Source0: https://security.appspot.com/downloads/%{name}-%{version}.tar.gz
#Source1: vsftpd.xinetd
#Source2: vsftpd.pam
#Source3: vsftpd.ftpusers
#Source4: vsftpd.user_list
#Source5: vsftpd.init
#Source6: vsftpd_conf_migrate.sh
#Source7: vsftpd.service
#Source8: vsftpd@.service
#Source9: vsftpd.target
#Source10: vsftpd-generator

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: pam-devel
BuildRequires: libcap-devel
BuildRequires: openssl-devel
BuildRequires: systemd
%if %{tcp_wrappers}
BuildRequires: tcp_wrappers-devel
%endif

Requires: logrotate

# Build patches
#Patch1: vsftpd-2.1.0-libs.patch
#Patch2: vsftpd-2.1.0-build_ssl.patch
#Patch3: vsftpd-2.1.0-tcp_wrappers.patch

# Use /etc/vsftpd/ instead of /etc/
#Patch4: vsftpd-2.1.0-configuration.patch

# These need review
#Patch5: vsftpd-2.1.0-pam_hostname.patch
#Patch6: vsftpd-close-std-fds.patch
#Patch7: vsftpd-2.1.0-filter.patch
#Patch9: vsftpd-2.1.0-userlist_log.patch

#Patch10: vsftpd-2.1.0-trim.patch
#Patch12: vsftpd-2.1.1-daemonize_plus.patch
#Patch14: vsftpd-2.2.0-wildchar.patch

#Patch16: vsftpd-2.2.2-clone.patch
#Patch19: vsftpd-2.3.4-sd.patch
#Patch20: vsftpd-2.3.4-sqb.patch
#Patch21: vsftpd-2.3.4-listen_ipv6.patch
#Patch22: vsftpd-2.3.5-aslim.patch
#Patch23: vsftpd-3.0.0-tz.patch
#Patch24: vsftpd-3.0.0-xferlog.patch
#Patch25: vsftpd-3.0.0-logrotate.patch
#Patch26: vsftpd-3.0.2-seccomp.patch
#Patch27: vsftpd-3.0.2-mrate.patch
#Patch28: vsftpd-3.0.2-wnohang.patch
#Patch29: vsftpd-3.0.2-dh.patch
#Patch30: vsftpd-3.0.2-ecdh.patch
#Patch31: vsftpd-2.0.5-fix_qm.patch
#Patch32: vsftpd-3.0.2-reverse-lookup.patch
#Patch33: vsftpd-3.0.2-del-upl.patch
#Patch34: vsftpd-2.2.2-nfs-fail.patch
#Patch35: vsftpd-2.2.2-man-pages.patch
#Patch36: vsftpd-3.0.2-uint-uidgid.patch
#Patch37: vsftpd-2.2.2-blank-chars-overflow.patch
#Patch38: vsftpd-2.2.2-syslog.patch
#Patch39: vsftpd-3.0.2-docupd.patch
#Patch40: vsftpd-2.2.2-tlsv1_2.patch
#Patch41: vsftpd-3.0.2-defaulttls.patch
#Patch42: 0001-Redefine-VSFTP_COMMAND_FD-to-1.patch
#Patch43: 0001-Document-the-relationship-of-text_userdb_names-and-c.patch
#Patch44: 0001-Document-allow_writeable_chroot-in-the-man-page.patch
#Patch45: 0001-Improve-documentation-of-ascii_-options.patch
#Patch46: 0001-Add-new-filename-generation-algorithm-for-STOU-comma.patch
#Patch47: 0001-Fix-rDNS-with-IPv6.patch
#Patch48: 0001-Log-die-calls-to-syslog.patch
#Patch49: 0002-Improve-error-message-when-max-number-of-bind-attemp.patch
#Patch50: 0003-Make-the-max-number-of-bind-retries-tunable.patch

%description
vsftpd is a Very Secure FTP daemon. It was written completely from
scratch.

%package sysvinit
Group: System Environment/Daemons
Summary: SysV initscript for vsftpd daemon
Requires: %{name} = %{version}-%{release}
Requires(preun): /sbin/service
Requires(postun): /sbin/service

%description sysvinit
The vsftpd-sysvinit contains SysV initscritps support.

%prep
%setup -q -n %{name}-%{version}
#cp %{SOURCE1} .

#%patch1 -p1 -b .libs
#%patch2 -p1 -b .build_ssl
#%if %{tcp_wrappers}
#%patch3 -p1 -b .tcp_wrappers
#%endif
#%patch4 -p1 -b .configuration
#%patch5 -p1 -b .pam_hostname
#%patch6 -p1 -b .close_fds
#%patch7 -p1 -b .filter
#%patch9 -p1 -b .userlist_log
#%patch10 -p1 -b .trim
#%patch12 -p1 -b .daemonize_plus
#%patch14 -p1 -b .wildchar
#%patch16 -p1 -b .clone
#%patch19 -p1 -b .sd
#%patch20 -p1 -b .sqb
#%patch21 -p1 -b .listen_ipv6
#%patch22 -p1 -b .aslim
#%patch23 -p1 -b .tz
#%patch24 -p1 -b .xferlog
#%patch25 -p1 -b .logrotate
#%patch26 -p1 -b .seccomp
#%patch27 -p1 -b .mrate
#%patch28 -p1 -b .wnohang
#%patch29 -p1 -b .dh
#%patch30 -p1 -b .ecdh
#%patch31 -p1 -b .fix_qm
#%patch32 -p1 -b .reverse-lookup
#%patch33 -p1 -b .del-upl
#%patch34 -p1 -b .nfs-fail
#%patch35 -p1 -b .man_pages
#%patch36 -p1 -b .uint-uidgid
#%patch37 -p1 -b .blank-char-overflow
#%patch38 -p1 -b .syslog
#%patch39 -p1 -b .docup
#%patch40 -p1 -b .tls_version
#%patch41 -p1 -b .defaulttls
#%patch42 -p1 -b .command-fd
#%patch43 -p1 -b .text-userdb-names
#%patch44 -p1 -b .allow-writeable-chroot
#%patch45 -p1 -b .ascii
#%patch46 -p1 -b .better-stou
#%patch47 -p1 -b .ipv6-rdns
#%patch48 -p1 -b .errors-to-syslog
#%patch49 -p1 -b .improve-error-message
#%patch50 -p1 -b .bind-retries-configurable

%build
%ifarch s390x sparcv9 sparc64
make CFLAGS="$RPM_OPT_FLAGS -fPIE -pipe -Wextra -Werror" \
%else
make CFLAGS="$RPM_OPT_FLAGS -fpie -pipe -Wextra -Werror" \
%endif
        LINK="-pie -lssl" %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/{vsftpd,pam.d,logrotate.d,rc.d/init.d}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{5,8}
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
#mkdir -p $RPM_BUILD_ROOT%{_generatorsdir}
install -m 755 vsftpd  $RPM_BUILD_ROOT%{_sbindir}/vsftpd
install -m 600 vsftpd.conf $RPM_BUILD_ROOT%{_sysconfdir}/vsftpd/vsftpd.conf
install -m 644 vsftpd.conf.5 $RPM_BUILD_ROOT/%{_mandir}/man5/
install -m 644 vsftpd.8 $RPM_BUILD_ROOT/%{_mandir}/man8/
#install -m 644 RedHat/vsftpd.log $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/vsftpd
#install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/vsftpd
#install -m 600 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/vsftpd/ftpusers
#install -m 600 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/vsftpd/user_list
#install -m 755 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/vsftpd
#install -m 744 %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/vsftpd/vsftpd_conf_migrate.sh
#install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_unitdir}
#install -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_unitdir}
#install -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_unitdir}
#install -m 755 %{SOURCE10} $RPM_BUILD_ROOT%{_generatorsdir}
                  
mkdir -p $RPM_BUILD_ROOT/%{_var}/ftp/pub

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_post vsftpd.service

%preun
%systemd_preun vsftpd.service
%systemd_preun vsftpd.target

%postun
%systemd_postun_with_restart vsftpd.service 

%files
%defattr(-,root,root,-)
#%{_unitdir}/*
#%{_generatorsdir}/*
%{_sbindir}/vsftpd
%dir %{_sysconfdir}/vsftpd
#%{_sysconfdir}/vsftpd/vsftpd_conf_migrate.sh
#%config(noreplace) %{_sysconfdir}/vsftpd/ftpusers
#%config(noreplace) %{_sysconfdir}/vsftpd/user_list
%config(noreplace) %{_sysconfdir}/vsftpd/vsftpd.conf
#%config(noreplace) %{_sysconfdir}/pam.d/vsftpd
#%config(noreplace) %{_sysconfdir}/logrotate.d/vsftpd
%doc FAQ INSTALL BUGS AUDIT Changelog LICENSE README README.security REWARD
#%doc SPEED TODO BENCHMARKS COPYING SECURITY/ EXAMPLE/ TUNING SIZE vsftpd.xinetd
#%OCOC{_mandir}/man5/vsftpd.conf.*
%{_mandir}/man8/vsftpd.*
%{_var}/ftp

%files sysvinit
#%{_sysconfdir}/rc.d/init.d/vsftpd

%changelog
* Thu Jun 21 2018 Ondřej Lysoněk <olysonek@redhat.com> - 3.0.2-25
- Add config option log_die allowing to pass error messages to syslog
- Add config option bind_retries allowing to change the max number
- of attempts to find a listening port for the PASV/EPSV command
- Resolves: rhbz#1318198

* Wed May 16 2018 Ondřej Lysoněk <olysonek@redhat.com> - 3.0.2-24
- Fix reverse hostname lookup with IPv6
- Resolves: rhbz#1576705

* Thu Apr 05 2018 Ondřej Lysoněk <olysonek@redhat.com> - 3.0.2-23
- Redefine VSFTP_COMMAND_FD to 1
- Resolves: rhbz#1443055
- Document the relationship of text_userdb_names and chroot_local_user
- Resolves: rhbz#1508021
- Document allow_writeable_chroot in the man page
- Resolves: rhbz#1508022
- Improve documentation of ascii_* options
- Resolves: rhbz#1517227
- Add new filename generation algorithm for STOU command
- Resolves: rhbz#1479237

* Thu Mar 23 2017 Zdenek Dohnal <zdohnal@redhat.com> - 3.0.2-22
- Resolves: #1432054 - secure ftp stopped working with default TLS settings in the new vsftpd package

* Thu Jun 02 2016 Martin Sehnoutka <msehnout@redhat.com> - 3.0.2-21
- Resolves: #1318947 vsftpd should permit specified TLS versions only

* Thu Apr 07 2016 Martin Sehnoutka <msehnout@redhat.com> - 3.0.2-20
- Resolves: #1147551 - Missing isolate_* options, incorrect default values of
  max_clients, max_per_ip in man vsftpd.conf

* Tue Apr 05 2016 Martin Sehnoutka <msehnout@redhat.com> - 3.0.2-19
- Resolves: #1311562 - Message is not logged to syslog when syslog_enable=yes in
  vsftpd.conf

* Tue Apr 05 2016 Martin Sehnoutka <msehnout@redhat.com> - 3.0.2-18
- Resolves: #1311600 - vsftpd segfaults in vsf_sysutil_strndup

* Fri Apr 01 2016 Martin Sehnoutka <msehnout@redhat.com> - 3.0.2-17
- Resolves: #1116385 - deny_file, hide_file

* Tue Mar 29 2016 Martin Sehnoutka <msehnout@redhat.com> - 3.0.2-16
- Resolves: #1087868 - uid and gid is not correctly shown

* Tue Mar 29 2016 Martin Sehnoutka <msehnout@redhat.com> - 3.0.2-15
- Resolves: #1147550 ssl_request_cert paragraph in the vsftpd.conf man page gets
  rendered incorrectly

* Tue Mar 29 2016 Martin Sehnoutka <msehnout@redhat.com> - 3.0.2-14
- Resolves: #1317891 Handle errors when calling close()

* Thu Mar 24 2016 Martin Sehnoutka <msehnout@redhat.com> - 3.0.2-13
- Resolves: #1148872 - The vsftpd doesn't remove failed upload when the
  delete_failed_uploads is enabled and the network cable is unplagged

* Tue Mar 22 2016 Martin Sehnoutka <msehnout@redhat.com> - 3.0.2-12
- Resolves: #1087834 - missing reverse_lookup_enable option

* Tue Feb 23 2016 Pavel Šimerda <psimerda@redhat.com> - 3.0.2-11
- Resolves: #1166741 - Wildcard ? does not work correctly in vsftpd-3.0.2-9.el7

* Mon Aug 03 2015 Martin Osvald <mosvald@rehat.com> - 3.0.2-10
- Resolves: #1058704 - vsftpd does not support DHE cipher suites
- Resolves: #1058712 - vsftpd does not support ECDHE cipher suites
- Resolves: #1198259 - The vsftpd hangs in a SIGCHLD handler when the pam_exec.so is used in pam.d configuration

* Fri Mar 07 2014 Jiri Skala <jskala@redhat.com> - 3.0.2-9
- Resolves: #1063402 - vsftpd local_max_rate option doesn't work as expected

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.0.2-8
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.0.2-7
- Mass rebuild 2013-12-27

* Fri Sep 13 2013 Jiri Skala <jskala@redhat.com> - 3.0.2-6
- Resolves: #833093 - multiple instances - improved service, target unit files, man page

* Thu Aug 29 2013 Ondrej Vasik <ovasik@redhat.com> - 3.0.2-5
- Readd seccomp disabled by default (#860951)

* Thu Aug 15 2013 Jiri Skala <jskala@redhat.com> - 3.0.2-4
- Resolves: #833093 - vsftpd service does not start more than one daemon

* Mon Feb 25 2013 Jiri Skala <jskala@redhat.com> - 3.0.2-3
- fixes #913519 - login fails (increased AS_LIMIT)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 19 2012 Jiri Skala <jskala@redhat.com> - 3.0.2-2
- update to latest upstream 3.0.2

* Mon Sep 17 2012 Jiri Skala <jskala@redhat.com> - 3.0.1-1
- update to latest upstream 3.0.1
- fixes #851441 - Introduce new systemd-rpm macros in vsftpd spec file
- fixes #845980 - vsftpd seccomp filter is too strict

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Jiri Skala <jskala@redhat.com> - 3.0.0-3
- changed default value of xferlog_file to /var/log/xferlog
- added rotating xferlog

* Thu Apr 26 2012 Jiri Skala <jskala@redhat.com> - 3.0.0-2
- corrected time zone handling - especially DST flag
- fixed default value of option 'listen'

* Tue Apr 10 2012 Jiri Skala <jskala@redhat.com> - 3.0.0-1
- updated to latest upstream 3.0.0

* Thu Feb 09 2012 Jiri Skala <jskala@redhat.com> - 2.3.5-3
- fixes #788812 - authentication failure on x86_64 when using nss_pgsql

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Jiri Skala <jskala@redhat.com> - 2.3.5-1
- updated to latest upstream 2.3.5

* Mon Nov 28 2011 Jiri Skala <jskala@redhat.com> - 2.3.4-7
- added patch from BZ#450853#c23

* Tue Nov 15 2011 Jiri Skala <jskala@redhat.com> - 2.3.4-6
- fixes #753365 - multiple issues with vsftpd's systemd unit
- removes exclusivity between listen and listen_ipv6 BZ#450853
- ls wildchars supports square brackets

* Wed Aug 03 2011 Jiri Skala <jskala@redhat.com> - 2.3.4-5
- fixes #719434 - Provide native systemd unit file
- moving SysV initscript into subpackage

* Mon Aug 01 2011 Jiri Skala <jskala@redhat.com> - 2.3.4-4
- rebuild for libcap

* Mon Jul 04 2011 Nils Philippsen <nils@redhat.com> - 2.3.4-3
- update upstream and source URL

* Wed Feb 16 2011 Jiri Skala <jskala@redhat.com> - 2.3.4-2
- fixes #717412 - Connection failures - patched by Takayuki Nagata

* Wed Feb 16 2011 Jiri Skala <jskala@redhat.com> - 2.3.4-1
- updated to latest upstream 2.3.4

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 20 2010 Jiri Skala <jskala@redhat.com> - 2.3.2-1
- fixes #625404 - vsftpd-2.3.1 is available
- joined patches (libs+dso, wildchar+greedy)

* Fri Aug 06 2010 Jiri Skala <jskala@redhat.com> - 2.2.2-8
- fixes #472880 - Configuration can cause confusion because of selinux labels

* Mon May 17 2010 Jiri Skala <jskala@redhat.com> - 2.2.2-7
- when listen_ipv6=YES sets socket option to listen IPv6 only

* Fri May 14 2010 Jiri Skala <jskala@redhat.com> - 2.2.2-6
- syscall(__NR_clone) replaced by clone() to fix incorrect order of params on s390 arch

* Wed Apr 07 2010 Jiri Skala <jskala@redhat.com> - 2.2.2-5
- corrected daemonize_plus patch - don't try kill parent when vsftpd isn't daemonized

* Tue Mar 16 2010 Jiri Skala <jskala@redhat.com> - 2.2.2-4
- fixes #544251 - /etc/rc.d/init.d/vsftpd does not start more than one daemon

* Mon Feb 15 2010 Jiri Skala <jskala@redhat.com> - 2.2.2-3
- fixes #565067 - FTBFS: ImplicitDSOLinking

* Thu Dec 17 2009 Jiri Skala <jskala@redhat.com> - 2.2.2-2
- corrected two patches due to fuzz 0

* Thu Dec 17 2009 Jiri Skala <jskala@redhat.com> - 2.2.2-1
- update to latest upstream

* Mon Nov 23 2009 Jiri Skala <jskala@rehat.com> - 2.2.0-6
- added lost default values of vsftpd.conf (rh patch)

* Wed Sep 16 2009 Tomas Mraz <tmraz@redhat.com> - 2.2.0-5
- use password-auth common PAM configuration instead of system-auth

* Mon Sep 14 2009 Jiri Skala <jskala@rehat.com> - 2.2.0-4
- modified init script to be LSB compliant

* Tue Sep 08 2009 Jiri Skala <jskala@rehat.com> - 2.2.0-3
- fixed bug messaged in RHEL-4 #479774 - Wildcard failures with vsftpd

* Thu Aug 27 2009 Tomas Mraz <tmraz@redhat.com> - 2.2.0-2
- rebuilt with new openssl

* Tue Aug 04 2009 Martin Nagy <mnagy@redhat.com> - 2.2.0-0.1.pre4
- update to latest upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 02 2009 Jiri Skala <jskala@redhat.com> - 2.1.2-1
- updated to latest upstream version

* Thu May 21 2009 Jiri Skala <jskala@redhat.com> - 2.1.1-0.3
- fixed daemonize_plus patch
- fixed test in initscript [ -z "CONFS" ]

* Mon May 04 2009 Jiri Skala <jskala@redhat.com> - 2.1.1-0.2
- fixes daemonize patch

* Wed Apr 22 2009 Jiri Skala <jskala@redhat.com> - 2.1.0-3
- updated to latest upstream version
- improved daemonizing - init script gets correct return code if binding fails
- trim white spaces from option values
- fixed #483604 - vsftpd not honouring delay_failed_login when userlist active

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 24 2009 Martin Nagy <mnagy@redhat.com> - 2.1.0-1
- update to latest upstream release

* Fri Jan 23 2009 Martin Nagy <mnagy@redhat.com> - 2.1.0-0.3.pre4
- update to latest upstream release
- enable ptrace sandbox again
- don't mark vsftpd_conf_migrate.sh as a config file

* Fri Jan 16 2009 Martin Nagy <mnagy@redhat.com> - 2.1.0-0.2.pre3
- disable ptrace sandbox to fix build on i386

* Fri Jan 16 2009 Martin Nagy <mnagy@redhat.com> - 2.1.0-0.1.pre3
- update to latest upstream release
- cleanup the spec file
- drop patches fixed upstream:
    vsftpd-1.0.1-missingok.patch
    vsftpd-1.2.1-nonrootconf.patch
    vsftpd-2.0.1-tcp_wrappers.patch
    vsftpd-2.0.2-signal.patch
    vsftpd-2.0.3-daemonize_fds.patch
    vsftpd-2.0.5-correct_comments.patch
    vsftpd-2.0.5-pasv_dot.patch
    vsftpd-2.0.5-write_race.patch
    vsftpd-2.0.5-fix_unique.patch
    vsftpd-2.0.5-uname_size.patch
    vsftpd-2.0.5-bind_denied.patch
    vsftpd-2.0.5-pam_end.patch
    vsftpd-2.0.5-underscore_uname.patch
    vsftpd-2.0.6-listen.patch
- join all configuration patches into one:
    vsftpd-1.1.3-rh.patch
    vsftpd-1.2.1-conffile.patch
    vsftpd-2.0.1-dir.patch
    vsftpd-2.0.1-server_args.patch
    vsftpd-2.0.3-background.patch
    vsftpd-2.0.5-default_ipv6.patch
    vsftpd-2.0.5-add_ipv6_option.patch
    vsftpd-2.0.5-man.patch

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.7-1
- fix license tag
- update to 2.0.7

* Fri Jun 20 2008 Dennis Gilmore <dennis@ausil.us> - 2.0.6-5
- add sparc arches to -fPIE list

* Wed May 21 2008 Martin Nagy <mnagy@redhat.com> - 2.0.6-4
- fix a small memory leak (#397011)

* Mon Mar 31 2008 Martin Nagy <mnagy@redhat.com> - 2.0.6-3
- set option listen to default to YES

* Mon Feb 25 2008 Martin Nagy <mnagy@redhat.com> - 2.0.6-2
- fix init script (#431452)
- make the init script LSB compliant (#247093)

* Fri Feb 22 2008 Martin Nagy <mnagy@redhat.com> - 2.0.6-1
- rebase for new upstream version
- remove patches that were fixed in upstream: kickline, confspell, anon_umask

* Mon Feb 11 2008 Martin Nagy <mnagy@redhat.com> - 2.0.5-22
- rebuild for gcc-4.3

* Fri Nov 30 2007 Martin Nagy <mnagy@redhat.com> - 2.0.5-21
- Remove uniq_rename patch.
- Correct create/lock race condition, original patch by <mpoole@redhat.com>
  (#240550).
- Fix bad handling of unique files (#392231).
- Added userlist_log option.
- Allow usernames to begin with underscore or dot (#339911).
- Removed user_config patch.
- Fix nonrootconf patch (#400921).
- Increase maximum length of allowed username (#236326).
- Fix file listing issue with wildcard (#392181).
- Removed use_localtime patch (#243087).

* Thu Nov 08 2007 Martin Nagy <mnagy@redhat.com> - 2.0.5-20
- Correct calling of pam_end (#235843).

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2.0.5-19
- Rebuild for selinux ppc32 issue.

* Tue Jul 10 2007 Maros Barabas <mbarabas@redhat.com> - 2.0.5-18
- Add comment for xferlog_std_format
- Resolves #218260

* Fri Jun 29 2007 Maros Barabas <mbarabas@redhat.com> - 2.0.5-17
- Fix pasv dot after pasv response (RFC 959 page 40)

* Wed Apr 04 2007 Maros Barabas <mbarabas@redhat.com> - 2.0.5-16
- Merge review: - fix using %%{_var}, %%{_sbindir} and 
                  %%{_sysconfigdir} macros for files and install
                - fix BuildRoot
                - dropped usermod, openssl & pam requirement

* Tue Mar 20 2007 Florian La Roche <laroche@redhat.com> - 2.0.5-15
- fix BuildPrereq

* Tue Jan 30 2007 Maros Barabas <mbarabas@redhat.com> - 2.0.5-14
- remove file upload permission problem 
- change name of patch vsfptd-2.0.3-user_config
- Resolves #190193

* Fri Jan 19 2007 Maros Barabas <mbarabas@redhat.com> - 2.0.5-13
- add lost patch: don't die when no user config file is present 
- Resolves #166986

* Thu Jan 18 2007 Radek Vokal <rvokal@redhat.com> - 2.0.5-12
- add dist tag
- add buildrequires tcp_wrappers-devel

* Wed Jan 17 2007 Maros Barabas <mbarabas@redhat.com> - 2.0.5-11
- add errno EACCES to not die by vsf_sysutil_bind
- Resolves #198677

* Thu Dec 14 2006 Maros Barabas <mbarabas@redhat.com> - 2.0.5-10
- correct man (5) pages
- Resolves: #216765
- correct calling function stat 
- Resolves: bz200763

* Mon Dec 04 2006 Maros Barabas <mbarabas@redhat.com> - 2.0.5-9
- change BuildRequires tcp_wrappers to tcp_wrappers-devel

* Mon Aug 28 2006 Maros Barabas <mbarabas@redhat.com> - 2.0.5-8
- added forgotten patch to make filename filter (#174764)

* Tue Aug 22 2006 Maros Barabas <mbarabas@redhat.com> - 2.0.5-7
- correct paths of configuration files on man pages

* Tue Aug 15 2006 Maros Barabas <mbarabas@redhat.com> - 2.0.5-6
- correct comments

* Tue Aug 08 2006 Maros Barabas <mbarabas@redhat.com> - 2.0.5-5
- option to change listening to IPv6 protocol

* Mon Jul 17 2006 Radek Vokal <rvokal@redhat.com> - 2.0.5-3
- listen to IPv6 connections in default conf file

* Thu Jul 13 2006 Radek Vokal <rvokal@redhat.com> - 2.0.5-2
- add keyinit instructions to the vsftpd PAM script (#198637)

* Wed Jul 12 2006 Radek Vokal <rvokal@redhat.com> - 2.0.5-1
- upgrade to 2.0.5
- IE should now show the login dialog again (#191147)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.0.4-1.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.0.4-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.0.4-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Jan 12 2006 Radek Vokal <rvokal@redhat.com> 2.0.4-1
- upgrade to 2.0.4
- vsftpd now lock files for simultanous up/downloads (#162511)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 09 2005 Radek Vokal <rvokal@redhat.com> 2.0.3-12
- rebuilt against new openssl
- close std file descriptors

* Tue Oct 04 2005 Radek Vokal <rvokal@redhat.com> 2.0.3-11
- use include instead of pam_stack in pam config

* Fri Sep 09 2005 Radek Vokal <rvokal@redhat.com> 2.0.3-10
- vsfptd.log as a default log file has to be rotated (#167359)
- vsftpd does dns reverse before passing hosts to pam_access.so (#159745)

* Wed Aug 31 2005 Radek Vokal <rvokal@redhat.com> 2.0.3-9
- don't die when no user config file is present (#166986)

* Tue Aug 09 2005 Radek Vokal <rvokal@redhat.com> 2.0.3-8
- removed additional cmd line for ftp (#165083)

* Thu Aug 04 2005 Radek Vokal <rvokal@redhat.com> 2.0.3-7
- daemonize with file descriptors (#164998)

* Thu Jun 30 2005 Radek Vokal <rvokal@redhat.com> 2.0.3-6
- start in background as default, init script changed (#158714)

* Mon Jun 27 2005 Radek Vokal <rvokal@redhat.com> 2.0.3-5
- fixed requires for 64bit libs

* Thu Jun 23 2005 Radek Vokal <rvokal@redhat.com> 2.0.3-4
- fixed requires for pam_loginuid

* Wed Jun 01 2005 Radek Vokal <rvokal@redhat.com> 2.0.3-3
- vsftpd update for new audit system (#159223)

* Fri May 27 2005 Radek Vokal <rvokal@redhat.com> 2.0.3-2
- timezone fix, patch from suse.de (#158779)

* Wed Mar 23 2005 Radek Vokal <rvokal@redhat.com> 2.0.3-1
- new release, fixes #106416 and #134541 

* Mon Mar 14 2005 Radek Vokal <rvokal@redhat.com> 2.0.3-pre2
- prerelease, fixes IPv6 issues

* Mon Mar 14 2005 Radek Vokal <rvokal@redhat.com> 2.0.2-1
- update to new release, several bug fixes

* Wed Mar 02 2005 Radek Vokal <rvokal@redhat.com> 2.0.1-10
- rebuilt against gcc4 and new openssl

* Mon Feb 07 2005 Radek Vokal <rvokal@redhat.com> 2.0.1-9
- don't allow to read non-root config files (#145548)

* Mon Jan 10 2005 Radek Vokal <rvokal@redhat.com> 2.0.1-8
- use localtime also in logs (#143687)

* Tue Dec 14 2004 Radek Vokal <rvokal@redhat.com> 2.0.1-7
- fixing directory in vsftpd.pam file (#142805)

* Fri Oct 01 2004 Radek Vokal <rvokal@redhat.com> 2.0.1-5
- vsftpd under xinetd reads its config file (#134314)

* Thu Sep 16 2004 Radek Vokal <rvokal@redhat.com> 2.0.1-4
- spec file changed, ftp dir change commented (#130119)
- added doc files (#113056)

* Wed Sep 08 2004 Jan Kratochvil <project-vsftpd@jankratochvil.net>
- update for 2.0.1 for SSL

* Fri Aug 27 2004 Radek Vokal <rvokal@redhat.com> 2.0.1-2
- vsftpd.conf file changed, default IPv6 support

* Fri Aug 20 2004 Radek Vokal <rvokal@redhat.com> 2.0.1-1
- tcp_wrapper patch updated, signal patch updated
- upgrade to 2.0.1, fixes several bugs, RHEL and FC builds

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 19 2004 Bill Nottingham <notting@redhat.com> 1.2.1-6
- fix the logrotate config (#116253) 

* Mon May  3 2004 Bill Nottingham <notting@redhat.com> 1.2.1-5
- fix all references to vsftpd.conf to be /etc/vsftpd/vsftpd.conf,
  including in the binary (#121199, #104075)

* Thu Mar 25 2004 Bill Nottingham <notting@redhat.com> 1.2.1-4
- don't call malloc()/free() in signal handlers (#119136,
  <olivier.baudron@m4x.org>)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Nov 24 2003 Karsten Hopp <karsten@redhat.de> 1.2.1-1
- update to 1.2.1, which fixes #89765 and lot of other issues
- remove manpage patch, it isn't required anymore
- clean up init script
- don't use script to find libs to link with (lib64 issues)

* Sun Oct 12 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- allow compiling without tcp_wrappers support

* Mon Sep 15 2003 Bill Nottingham <notting@redhat.com> 1.2.0-4
- fix errant newline (#104443)

* Fri Aug  8 2003 Bill Nottingham <notting@redhat.com> 1.2.0-3
- tweak man page (#84584, #72798)
- buildprereqs for pie (#99336)
- free ride through the build system to fix (#101582)

* Thu Jun 26 2003 Bill Nottingham <notting@redhat.com> 1.2.0-2
- update to 1.2.0

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Apr 28 2003 Bill Nottingham <notting@redhat.com> 1.1.3-9
- fix tcp_wrappers usage (#89765, <dale@riyescott.com>)

* Fri Feb 28 2003 Nalin Dahyabhai <nalin@redhat.com> 1.1.3-8
- enable use of tcp_wrappers

* Tue Feb 11 2003 Bill Nottingham <notting@redhat.com> 1.1.3-7
- provide /var/ftp & /var/ftp/pub. obsolete anonftp.

* Mon Feb 10 2003 Bill Nottingham <notting@redhat.com> 1.1.3-6
- clean up comments in init script (#83962)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Dec 30 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- change to /etc/rc.d/init.d for better compatibility

* Mon Dec 16 2002 Bill Nottingham <notting@redhat.com> 1.1.3-3
- fix initscript perms
- fix typo in initscript (#76587)

* Fri Dec 13 2002 Bill Nottingham <notting@redhat.com> 1.1.3-2
- update to 1.1.3
- run standalone, don't run by default
- fix reqs
 
* Fri Nov 22 2002 Joe Orton <jorton@redhat.com> 1.1.0-3
- fix use with xinetd-ipv6; add flags=IPv4 in xinetd file (#78410)

* Tue Nov 12 2002 Nalin Dahyabhai <nalin@redhat.com> 1.0.1-9
- remove absolute paths from PAM configuration so that the right modules get
  used for whichever arch we're built for on multilib systems

* Thu Aug 15 2002 Elliot Lee <sopwith@redhat.com> 1.0.1-8
- -D_FILE_OFFSET_BITS=64
- smp make
- remove forced optflags=-g for lack of supporting documentation
 
* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Apr 10 2002 Bill Nottingham <notting@redhat.com> 1.0.1-5
- don't spit out ugly errors if anonftp isn't installed (#62987)
- fix horribly broken userlist setup (#62321)

* Thu Feb 28 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.0.1-4
- s/Copyright/License/
- add "missingok" to the logrotate script, so we don't get errors
  when nothing has happened

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Nov 28 2001 Bill Nottingham <notting@redhat.com>
- initial packaging for RHL, munge included specfile

* Thu Mar 22 2001 Seth Vidal <skvidal@phy.duke.edu>
- updated to 0.0.15
- added entry for vsftpd.8 man page
- added entry for vsftpd.log logrotate file
- added TUNING file to docs list

* Wed Mar 7 2001 Seth Vidal <skvidal@phy.duke.edu>
- Updated to 0.0.14
- made %%files entry for man page

* Wed Feb 21 2001 Seth Vidal <skvidal@phy.duke.edu>
- Updated to 0.0.13

* Mon Feb 12 2001 Seth Vidal <skvidal@phy.duke.edu>
- Updated to 0.0.12

* Wed Feb 7 2001 Seth Vidal <skvidal@phy.duke.edu>
- updated to 0.0.11

